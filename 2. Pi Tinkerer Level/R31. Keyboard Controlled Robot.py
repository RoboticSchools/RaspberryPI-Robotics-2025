"""
Components Used:
1. Raspberry Pi
2. DC Motor HAT
3. Robot Car
4. 4 DC Motors
5. Keyboard

Install Required Library:
pip install pynput --break-system-packages
"""

from pynput import keyboard
from Raspi_MotorHAT import Raspi_MotorHAT
import time

mh = Raspi_MotorHAT(addr=0x6f)  # Initialize Motor HAT

rightFront = mh.getMotor(1)  # Motor 1
rightBack = mh.getMotor(2)   # Motor 2
leftFront = mh.getMotor(3)   # Motor 3
leftBack = mh.getMotor(4)    # Motor 4

speed = 150  # Motor speed

rightFront.setSpeed(speed)
rightBack.setSpeed(speed)
leftFront.setSpeed(speed)
leftBack.setSpeed(speed)

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

def on_press(key):
    if key == keyboard.Key.up:
        move_forward()
    elif key == keyboard.Key.down:
        move_backward()
    elif key == keyboard.Key.left:
        turn_left()
    elif key == keyboard.Key.right:
        turn_right()

def on_release(key):
    stop_motors()  # Stop on key release

    if key == keyboard.Key.esc:
        return False  # Exit program

try:
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()  # Start listening

except KeyboardInterrupt:
    print("Exiting...")
    stop_motors()  # Stop all motors