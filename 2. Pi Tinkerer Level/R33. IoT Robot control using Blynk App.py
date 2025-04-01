"""
Components Used:
- Raspberry Pi
- Raspi Motor HAT
- 4 DC Motors (Right Front, Right Back, Left Front, Left Back)
- Blynk App (for controlling the robot via IoT)
"""

import time
from BlynkLib import Blynk
from Raspi_MotorHAT import Raspi_MotorHAT

# Replace with your Blynk authentication token
BLYNK_AUTH = 'YOUR_BLYNK_AUTH_TOKEN'

# Initialize Motor HAT (Default I2C address 0x6F)
mh = Raspi_MotorHAT(addr=0x6f)

# Create motor objects for the four wheels
rightFront = mh.getMotor(1)
rightBack = mh.getMotor(2)
leftFront = mh.getMotor(3)
leftBack = mh.getMotor(4)

# Set motors speed
speed = 150
rightFront.setSpeed(speed)
rightBack.setSpeed(speed)
leftFront.setSpeed(speed)
leftBack.setSpeed(speed)

# Initialize Blynk
blynk = Blynk(BLYNK_AUTH)

# Function to move forward
def move_forward():
    print("Moving forward")
    rightFront.run(Raspi_MotorHAT.FORWARD)
    rightBack.run(Raspi_MotorHAT.FORWARD)
    leftFront.run(Raspi_MotorHAT.FORWARD)
    leftBack.run(Raspi_MotorHAT.FORWARD)

# Function to move backward
def move_backward():
    print("Moving backward")
    rightFront.run(Raspi_MotorHAT.BACKWARD)
    rightBack.run(Raspi_MotorHAT.BACKWARD)
    leftFront.run(Raspi_MotorHAT.BACKWARD)
    leftBack.run(Raspi_MotorHAT.BACKWARD)

# Function to turn left
def turn_left():
    print("Turning left")
    rightFront.run(Raspi_MotorHAT.BACKWARD)
    rightBack.run(Raspi_MotorHAT.BACKWARD)
    leftFront.run(Raspi_MotorHAT.FORWARD)
    leftBack.run(Raspi_MotorHAT.FORWARD)

# Function to turn right
def turn_right():
    print("Turning right")
    rightFront.run(Raspi_MotorHAT.FORWARD)
    rightBack.run(Raspi_MotorHAT.FORWARD)
    leftFront.run(Raspi_MotorHAT.BACKWARD)
    leftBack.run(Raspi_MotorHAT.BACKWARD)

# Function to stop motors
def stop_motors():
    print("Stopping motors")
    rightFront.run(Raspi_MotorHAT.RELEASE)
    rightBack.run(Raspi_MotorHAT.RELEASE)
    leftFront.run(Raspi_MotorHAT.RELEASE)
    leftBack.run(Raspi_MotorHAT.RELEASE)

# Blynk Virtual Pin handlers
@blynk.on("V1")  # Forward Button
def move_forward_blynk(value):
    if value[0] == '1':  # Button pressed
        move_forward()

@blynk.on("V2")  # Backward Button
def move_backward_blynk(value):
    if value[0] == '1':  # Button pressed
        move_backward()

@blynk.on("V3")  # Left Button
def move_left_blynk(value):
    if value[0] == '1':  # Button pressed
        turn_left()

@blynk.on("V4")  # Right Button
def move_right_blynk(value):
    if value[0] == '1':  # Button pressed
        turn_right()

@blynk.on("V5")  # Stop Button
def stop_blynk(value):
    if value[0] == '1':  # Button pressed
        stop_motors()

# Run Blynk
try:
    while True:
        blynk.run()
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Exiting...")
    stop_motors()
