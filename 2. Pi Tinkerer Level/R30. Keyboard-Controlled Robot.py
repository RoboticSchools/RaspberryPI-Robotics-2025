"""
Components Used:
- Raspberry Pi
- Pi DC Motor HAT
- Robot Car Setup
- 4 DC Motors (Right Front, Right Back, Left Front, Left Back)
- Keyboard (for controlling the robot)
"""

from pynput import keyboard
from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor
import time

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

# Function to handle key press
def on_press(key):
    if key == keyboard.Key.up:
        move_forward()
    elif key == keyboard.Key.down:
        move_backward()
    elif key == keyboard.Key.left:
        turn_left()
    elif key == keyboard.Key.right:
        turn_right()

# Function to handle key release
def on_release(key):
    # Stop motors when any key is released
    stop_motors()

    # Exit when escape key is pressed
    if key == keyboard.Key.esc:
        return False  # Stop listener

# Listener for keyboard inputs
try:
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
except KeyboardInterrupt:
    print("Exiting...")
    stop_motors()  # Ensure motors are stopped on exit
