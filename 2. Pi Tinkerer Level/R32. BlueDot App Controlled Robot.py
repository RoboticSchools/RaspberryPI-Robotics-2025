"""
Components Used:
1. Raspberry Pi
2. DC Motor HAT
3. Robot Car (4 DC Motors)
4. Battery Holder with 18650 Batteries
5. BlueDot App (Bluetooth Control)

Install Required Library:
pip install bluedot --break-system-packages
"""

from bluedot import BlueDot
from time import sleep
from Raspi_MotorHAT import Raspi_MotorHAT

mh = Raspi_MotorHAT(addr=0x6f)  # Initialize Motor HAT

rightFront = mh.getMotor(1)  # Motor 1
rightBack = mh.getMotor(2)   # Motor 2
leftFront = mh.getMotor(3)   # Motor 3
leftBack = mh.getMotor(4)    # Motor 4

speed = 150  # Motor speed (0–255)

rightFront.setSpeed(speed)
rightBack.setSpeed(speed)
leftFront.setSpeed(speed)
leftBack.setSpeed(speed)

bd = BlueDot()  # Create BlueDot controller

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

# Called when BlueDot is pressed
def on_press(pos):
    if pos.top:
        move_forward()
    elif pos.bottom:
        move_backward()
    elif pos.left:
        turn_left()
    elif pos.right:
        turn_right()

# Called when BlueDot is released
def on_release(pos):
    stop_motors()

bd.when_pressed = on_press
bd.when_released = on_release

try:
    print("Waiting for BlueDot input...")
    while True:
        sleep(0.1)  # Keep program running

except KeyboardInterrupt:
    print("Exiting...")
    stop_motors()  # Stop all motors