"""
Components Used:
- Raspberry Pi
- IR Sensor (Obstacle Sensor)
- Servo Motor (SG90)
- Breadboard
- Jumper Wires
"""

import time
import RPi.GPIO as gpio

# GPIO Pin configuration
ir_sensor = 17   # IR Sensor output pin
servo_pin = 18   # Servo motor pin

# GPIO setup
gpio.setmode(gpio.BCM)
gpio.setup(ir_sensor, gpio.IN)  # IR sensor as input
gpio.setup(servo_pin, gpio.OUT) # Servo motor as output

# Initialize PWM for the servo
servo = gpio.PWM(servo_pin, 50)  # 50Hz frequency
servo.start(0)

def set_servo_angle(angle):
    """Move servo to a specific angle."""
    duty_cycle = (angle / 18) + 2.5  # Convert angle to PWM duty cycle
    servo.ChangeDutyCycle(duty_cycle)
    time.sleep(0.5)  # Allow time to move

try:
    # Set initial position of servo (door closed)
    set_servo_angle(0)

    while True:
        if gpio.input(ir_sensor) == 0:  # Object detected (IR sensor LOW)
            print("Person Detected - Opening Door")
            set_servo_angle(90)  # Open door
            time.sleep(5)  # Keep door open for 5 seconds
            print("Closing Door")
            set_servo_angle(0)  # Close door
        
        time.sleep(0.5)  # Update every 500ms

except KeyboardInterrupt:
    print("Exiting...")
    servo.stop()
    gpio.cleanup()
