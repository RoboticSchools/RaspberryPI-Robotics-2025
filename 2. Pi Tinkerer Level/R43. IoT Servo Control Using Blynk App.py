"""
Components Used:
- Raspberry Pi
- Servo Motor (SG90/MG995)
- Blynk App
- Jumper Wires
"""

import time
import RPi.GPIO as gpio
from BlynkLib import Blynk, VIRTUAL_WRITE

# Blynk authentication token (replace with your actual token)
BLYNK_AUTH = "YOUR_BLYNK_AUTH_TOKEN"

# GPIO setup
SERVO_PIN = 18  # GPIO18 for PWM control
gpio.setmode(gpio.BCM)
gpio.setup(SERVO_PIN, gpio.OUT)

# Start PWM on the servo pin at 50Hz
servo = gpio.PWM(SERVO_PIN, 50)
servo.start(0)

# Initialize Blynk
blynk = Blynk(BLYNK_AUTH)

# Function to convert angle (0-180) to duty cycle
def set_servo_angle(angle):
    duty_cycle = (angle / 18) + 2.5  # Convert angle to PWM duty cycle
    servo.ChangeDutyCycle(duty_cycle)
    print(f"Servo Moved: {angle}°")
    time.sleep(0.5)  # Allow servo to move

# Function to receive servo angle from Blynk (V1)
@blynk.on("V1")
def control_servo(value):
    angle = int(value[0])
    set_servo_angle(angle)

# Function to handle Blynk connection
@blynk.on("connected")
def blynk_connected():
    print("✅ Blynk Connected - Ready to control Servo")

# Run Blynk
try:
    while True:
        blynk.run()
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Exiting...")
    servo.stop()
    gpio.cleanup()
