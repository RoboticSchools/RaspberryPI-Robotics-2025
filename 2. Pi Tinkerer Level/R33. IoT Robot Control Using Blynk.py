"""
Components Used:
1. Raspberry Pi
2. DC Motor HAT
3. Robot Car (4 DC Motors)
4. Battery Holder with 18650 Batteries
5. Blynk WebApp

Install Required Library:
pip install blynk-library-python --break-system-packages
"""

from BlynkLib import Blynk
from Raspi_MotorHAT import Raspi_MotorHAT
import time

BLYNK_AUTH = "YOUR_BLYNK_AUTH_TOKEN"  # Enter your Blynk token

mh = Raspi_MotorHAT(addr=0x6f)  # Initialize Motor HAT

# Motor connections
rightFront = mh.getMotor(1)  # Right front motor
rightBack = mh.getMotor(2)   # Right back motor
leftFront = mh.getMotor(3)   # Left front motor
leftBack = mh.getMotor(4)    # Left back motor

speed = 150  # Speed (0–255)

# Set speed for all motors
rightFront.setSpeed(speed)
rightBack.setSpeed(speed)
leftFront.setSpeed(speed)
leftBack.setSpeed(speed)

blynk = Blynk(BLYNK_AUTH, server="blynk.cloud", port=80)  # Connect to Blynk server

# Movement functions
def move_forward():
    rightFront.run(Raspi_MotorHAT.FORWARD)   # Move all motors forward
    rightBack.run(Raspi_MotorHAT.FORWARD)
    leftFront.run(Raspi_MotorHAT.FORWARD)
    leftBack.run(Raspi_MotorHAT.FORWARD)
    print("Forward")

def move_backward():
    rightFront.run(Raspi_MotorHAT.BACKWARD)  # Move all motors backward
    rightBack.run(Raspi_MotorHAT.BACKWARD)
    leftFront.run(Raspi_MotorHAT.BACKWARD)
    leftBack.run(Raspi_MotorHAT.BACKWARD)
    print("Backward")

def turn_left():
    rightFront.run(Raspi_MotorHAT.BACKWARD)  # Right side backward
    rightBack.run(Raspi_MotorHAT.BACKWARD)
    leftFront.run(Raspi_MotorHAT.FORWARD)    # Left side forward
    leftBack.run(Raspi_MotorHAT.FORWARD)
    print("Left")

def turn_right():
    rightFront.run(Raspi_MotorHAT.FORWARD)   # Right side forward
    rightBack.run(Raspi_MotorHAT.FORWARD)
    leftFront.run(Raspi_MotorHAT.BACKWARD)   # Left side backward
    leftBack.run(Raspi_MotorHAT.BACKWARD)
    print("Right")

def stop_motors():
    rightFront.run(Raspi_MotorHAT.RELEASE)  # Stop all motors
    rightBack.run(Raspi_MotorHAT.RELEASE)
    leftFront.run(Raspi_MotorHAT.RELEASE)
    leftBack.run(Raspi_MotorHAT.RELEASE)
    print("Stop")

# Forward button handler (V1)
def forward_handler(value):
    if int(value[0]) == 1:  # Button pressed
        move_forward()
    else:                   # Button released
        stop_motors()

# Backward button handler (V2)
def backward_handler(value):
    if int(value[0]) == 1:
        move_backward()
    else:
        stop_motors()

# Left button handler (V3)
def left_handler(value):
    if int(value[0]) == 1:
        turn_left()
    else:
        stop_motors()

# Right button handler (V4)
def right_handler(value):
    if int(value[0]) == 1:
        turn_right()
    else:
        stop_motors()

# Called when Blynk connects
def blynk_connected():
    print("Blynk Connected")

# Link Blynk virtual pins to functions
blynk.on("V1", forward_handler)
blynk.on("V2", backward_handler)
blynk.on("V3", left_handler)
blynk.on("V4", right_handler)
blynk.on("connected", blynk_connected)

try:
    print("Waiting for Blynk control...")  # Status message
    while True:
        blynk.run()        # Handle Blynk communication
        time.sleep(0.05)   # Small delay for stability

except KeyboardInterrupt:
    print("Exiting...")
    stop_motors()  # Stop all motors safely