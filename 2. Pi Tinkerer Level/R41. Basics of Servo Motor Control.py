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

servo = gpio.PWM(servo_pin, 50)  # 50Hz PWM for servo
servo.start(0)  # Start PWM

def set_angle(angle):
    duty_cycle = 2 + (angle / 18)  # Convert angle to duty cycle
    servo.ChangeDutyCycle(duty_cycle)  # Move servo
    time.sleep(1)  # Wait to reach position
    servo.ChangeDutyCycle(0)  # Stop signal (reduce jitter)

try:
    while True:
        set_angle(0)    # Move to 0°
        set_angle(90)   # Move to 90°
        set_angle(180)  # Move to 180°

except KeyboardInterrupt:
    servo.stop()     # Stop PWM
    gpio.cleanup()   # Reset GPIO