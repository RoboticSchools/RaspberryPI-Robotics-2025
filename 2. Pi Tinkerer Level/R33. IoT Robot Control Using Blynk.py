"""
Components Used:
1. Raspberry Pi
2. DC Motor HAT
3. Robot Car (4 DC Motors)
4. Battery Holder with 18650 Batteries
5. Blynk App (IoT Control)

Install Required Library:
pip install blynklib --break-system-packages
"""

from BlynkLib import Blynk
from Raspi_MotorHAT import Raspi_MotorHAT
import time

BLYNK_AUTH = "YOUR_BLYNK_AUTH_TOKEN"  # Enter your Blynk token

mh = Raspi_MotorHAT(addr=0x6f)  # Initialize Motor HAT

# Motor connections
rightFront = mh.getMotor(1)
rightBack = mh.getMotor(2)
leftFront = mh.getMotor(3)
leftBack = mh.getMotor(4)

speed = 150  # Speed (0–255)

# Set speed for all motors
rightFront.setSpeed(speed)
rightBack.setSpeed(speed)
leftFront.setSpeed(speed)
leftBack.setSpeed(speed)

blynk = Blynk(BLYNK_AUTH)  # Connect to Blynk

# Movement functions
def move_forward():
    rightFront.run(Raspi_MotorHAT.FORWARD)
    rightBack.run(Raspi_MotorHAT.FORWARD)
    leftFront.run(Raspi_MotorHAT.FORWARD)
    leftBack.run(Raspi_MotorHAT.FORWARD)
    print("Forward")

def move_backward():
    rightFront.run(Raspi_MotorHAT.BACKWARD)
    rightBack.run(Raspi_MotorHAT.BACKWARD)
    leftFront.run(Raspi_MotorHAT.BACKWARD)
    leftBack.run(Raspi_MotorHAT.BACKWARD)
    print("Backward")

def turn_left():
    rightFront.run(Raspi_MotorHAT.BACKWARD)
    rightBack.run(Raspi_MotorHAT.BACKWARD)
    leftFront.run(Raspi_MotorHAT.FORWARD)
    leftBack.run(Raspi_MotorHAT.FORWARD)
    print("Left")

def turn_right():
    rightFront.run(Raspi_MotorHAT.FORWARD)
    rightBack.run(Raspi_MotorHAT.FORWARD)
    leftFront.run(Raspi_MotorHAT.BACKWARD)
    leftBack.run(Raspi_MotorHAT.BACKWARD)
    print("Right")

def stop_motors():
    rightFront.run(Raspi_MotorHAT.RELEASE)
    rightBack.run(Raspi_MotorHAT.RELEASE)
    leftFront.run(Raspi_MotorHAT.RELEASE)
    leftBack.run(Raspi_MotorHAT.RELEASE)
    print("Stop")

# Forward button (V1)
@blynk.on("V1")
def forward_handler(value):
    if int(value[0]) == 1:  # Press
        move_forward()
    else:                   # Release
        stop_motors()

# Backward button (V2)
@blynk.on("V2")
def backward_handler(value):
    if int(value[0]) == 1:
        move_backward()
    else:
        stop_motors()

# Left button (V3)
@blynk.on("V3")
def left_handler(value):
    if int(value[0]) == 1:
        turn_left()
    else:
        stop_motors()

# Right button (V4)
@blynk.on("V4")
def right_handler(value):
    if int(value[0]) == 1:
        turn_right()
    else:
        stop_motors()

try:
    print("Waiting for Blynk control...")
    while True:
        blynk.run()        # Handle Blynk events
        time.sleep(0.05)   # Small delay

except KeyboardInterrupt:
    print("Exiting...")
    stop_motors()  # Stop all motors safely