"""
Components Used:
- Raspberry Pi
- Raspi Motor HAT
- 4 DC Motors (Right Front, Right Back, Left Front, Left Back)
- Breadboard
- Jumper Wires
- BlueDot App (for controlling the robot via Bluetooth)
"""

from bluedot import BlueDot
from gpiozero import Motor
from time import sleep
from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor

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

# Define motor control functions
def move_forward():
    print("Moving forward")
    rightFront.run(Raspi_MotorHAT.FORWARD)
    rightBack.run(Raspi_MotorHAT.FORWARD)
    leftFront.run(Raspi_MotorHAT.FORWARD)
    leftBack.run(Raspi_MotorHAT.FORWARD)

def move_backward():
    print("Moving backward")
    rightFront.run(Raspi_MotorHAT.BACKWARD)
    rightBack.run(Raspi_MotorHAT.BACKWARD)
    leftFront.run(Raspi_MotorHAT.BACKWARD)
    leftBack.run(Raspi_MotorHAT.BACKWARD)

def turn_left():
    print("Turning left")
    rightFront.run(Raspi_MotorHAT.BACKWARD)
    rightBack.run(Raspi_MotorHAT.BACKWARD)
    leftFront.run(Raspi_MotorHAT.FORWARD)
    leftBack.run(Raspi_MotorHAT.FORWARD)

def turn_right():
    print("Turning right")
    rightFront.run(Raspi_MotorHAT.FORWARD)
    rightBack.run(Raspi_MotorHAT.FORWARD)
    leftFront.run(Raspi_MotorHAT.BACKWARD)
    leftBack.run(Raspi_MotorHAT.BACKWARD)

def stop_motors():
    print("Stopping motors")
    rightFront.run(Raspi_MotorHAT.RELEASE)
    rightBack.run(Raspi_MotorHAT.RELEASE)
    leftFront.run(Raspi_MotorHAT.RELEASE)
    leftBack.run(Raspi_MotorHAT.RELEASE)

# Create a BlueDot instance
bd = BlueDot()

# Define BlueDot button actions
def on_press(pos):
    if pos.top > 0.6:  # Up button
        move_forward()
    elif pos.bottom < 0.4:  # Down button
        move_backward()
    elif pos.left < 0.4:  # Left button
        turn_left()
    elif pos.right > 0.6:  # Right button
        turn_right()

def on_release(pos):
    stop_motors()

# Initialize BlueDot listener
bd.when_pressed = on_press
bd.when_released = on_release

# Keep the program running
bd.wait_for_press()
