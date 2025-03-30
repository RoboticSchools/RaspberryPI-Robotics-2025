"""
Components Used:
- Raspberry Pi
- Servo Motor (SG90)
- External Power Supply (if required)
- Breadboard
- Jumper Wires
"""

import time
import RPi.GPIO as gpio

# Servo Pin Configuration
servo_pin = 21  # GPIO21 connected to Servo PWM

# GPIO Setup
gpio.setmode(gpio.BCM)
gpio.setup(servo_pin, gpio.OUT)

# Initialize PWM for Servo (50Hz frequency)
pwm = gpio.PWM(servo_pin, 50)
pwm.start(0)

def set_angle(angle):
    """Convert angle (0-180) to PWM duty cycle and rotate servo"""
    duty_cycle = 2 + (angle / 18)  # Convert angle to duty cycle
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(1)  # Wait for servo to reach position
    pwm.ChangeDutyCycle(2)  # Stop signal to avoid jitter

try:
    while True:
        angle = int(input("Enter angle (0-180): "))  # Directly convert input to integer
        if 0 <= angle <= 180:  # Ensure angle is within range
            set_angle(angle)
        else:
            print("Error: Please enter a number between 0 and 180.")

except KeyboardInterrupt:
    pwm.stop()
    gpio.cleanup()  # Reset GPIO settings before exit
