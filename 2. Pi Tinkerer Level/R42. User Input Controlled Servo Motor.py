"""
Components Used:
1. Raspberry Pi
2. Servo Motor (SG90)
3. Jumper Wires
"""

import time
import RPi.GPIO as gpio

servo_pin = 18  # GPIO pin for servo

gpio.setmode(gpio.BCM)        # Use BCM numbering
gpio.setup(servo_pin, gpio.OUT)  # Set servo pin as output

pwm = gpio.PWM(servo_pin, 50)  # 50Hz PWM for servo
pwm.start(0)  # Start PWM

def set_angle(angle):
    duty_cycle = 2 + (angle / 18)  # Convert angle to duty cycle
    pwm.ChangeDutyCycle(duty_cycle)  # Move servo
    time.sleep(0.8)  # Wait for movement
    pwm.ChangeDutyCycle(0)  # Stop signal (reduce jitter)

try:
    while True:
        try:
            angle = int(input("Enter angle (0-180): "))  # Get input

            if 0 <= angle <= 180:
                set_angle(angle)
            else:
                print("Enter value between 0 and 180")

        except ValueError:
            print("Invalid input! Enter a number")

except KeyboardInterrupt:
    pwm.stop()
    gpio.cleanup()