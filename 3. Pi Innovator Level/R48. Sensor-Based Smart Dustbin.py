"""
Components Used:
- Raspberry Pi
- Ultrasonic Sensor
- Servo Motor (SG90)
- Jumper Wires
"""

import time
import RPi.GPIO as gpio

# GPIO Pin configuration
trig = 23      # Trigger pin of HC-SR04
echo = 24      # Echo pin of HC-SR04
servo_pin = 18 # Servo motor pin

# GPIO setup
gpio.setmode(gpio.BCM)
gpio.setup(trig, gpio.OUT)
gpio.setup(echo, gpio.IN)
gpio.setup(servo_pin, gpio.OUT)

# Initialize PWM for the servo
servo = gpio.PWM(servo_pin, 50)  # 50Hz frequency
servo.start(0)

def set_servo_angle(angle):
    """Move servo to a specific angle."""
    duty_cycle = (angle / 18) + 2.5  # Convert angle to PWM duty cycle
    servo.ChangeDutyCycle(duty_cycle)
    time.sleep(0.5)  # Allow time to move

def get_distance():
    """Measure the distance using the ultrasonic sensor."""
    
    # Send a short pulse to trigger the sensor
    gpio.output(trig, True)
    time.sleep(0.00001)  # 10µs pulse
    gpio.output(trig, False)

    # Wait for the echo pin to go HIGH
    start_time = time.time()
    while gpio.input(echo) == 0:
        start_time = time.time()

    # Wait for the echo pin to go LOW
    end_time = time.time()
    while gpio.input(echo) == 1:
        end_time = time.time()

    # Calculate the distance in cm
    duration = end_time - start_time
    distance = (duration * 34300) / 2  # Speed of sound = 343m/s

    return round(distance, 2)  # Return the distance rounded to 2 decimal places

try:
    # Set initial position of servo (close lid)
    set_servo_angle(0)

    while True:
        distance = get_distance()
        print(f"Distance: {distance} cm")

        # If an object is detected within 20 cm, open the dustbin lid
        if distance < 20:
            set_servo_angle(90)  # Open lid
            time.sleep(3)  # Keep lid open for 3 seconds
            set_servo_angle(0)   # Close lid
        
        time.sleep(0.5)  # Update every 500ms

except KeyboardInterrupt:
    print("Exiting...")
    servo.stop()
    gpio.cleanup()
