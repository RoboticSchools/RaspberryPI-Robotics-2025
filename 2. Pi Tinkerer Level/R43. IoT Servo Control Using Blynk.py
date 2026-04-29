"""
Components Used:
1. Raspberry Pi
2. Servo Motor (SG90 / MG995)
3. Blynk App
4. Jumper Wires

Install Required Library:
pip install blynklib --break-system-packages
"""

import time
import RPi.GPIO as gpio
from BlynkLib import Blynk

BLYNK_AUTH = "YOUR_BLYNK_AUTH_TOKEN"  # Add your token

blynk = Blynk(BLYNK_AUTH)  # Initialize Blynk

servo_pin = 18  # GPIO pin for servo

gpio.setmode(gpio.BCM)        # Use BCM numbering
gpio.setup(servo_pin, gpio.OUT)

servo = gpio.PWM(servo_pin, 50)  # 50Hz PWM
servo.start(0)

def set_servo_angle(angle):
    duty_cycle = 2 + (angle / 18)  # Convert angle
    servo.ChangeDutyCycle(duty_cycle)
    print(f"Servo: {angle}°")
    time.sleep(0.5)
    servo.ChangeDutyCycle(0)  # Stop signal (reduce jitter)

# Receive angle from Blynk (V1 slider)
@blynk.on("V1")
def control_servo(value):
    angle = int(value[0])

    if 0 <= angle <= 180:  # Safety check
        set_servo_angle(angle)

# Blynk connection status
@blynk.on("connected")
def blynk_connected():
    print("Blynk Connected")

try:
    while True:
        blynk.run()        # Handle Blynk events
        time.sleep(0.05)

except KeyboardInterrupt:
    print("Exiting...")
    servo.stop()
    gpio.cleanup()