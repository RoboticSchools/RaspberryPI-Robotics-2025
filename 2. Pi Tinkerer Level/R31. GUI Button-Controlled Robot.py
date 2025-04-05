"""
Components Used:
- Raspberry Pi
- Pi DC Motor HAT
- Robot Car setup
- 4 DC Motors (Right Front, Right Back, Left Front, Left Back)
"""

import tkinter as tk
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

# Create main window
root = tk.Tk()
root.title("Robot Control")

# Define movement functions
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

# Define button commands
def on_press(key):
    if key == "Up":
        move_forward()
    elif key == "Down":
        move_backward()
    elif key == "Left":
        turn_left()
    elif key == "Right":
        turn_right()

def on_release(key):
    stop_motors()

# Create the diamond layout using 5 buttons
up_button = tk.Button(root, text="Up", command=lambda: on_press("Up"))
up_button.grid(row=0, column=1, padx=10, pady=10)

left_button = tk.Button(root, text="Left", command=lambda: on_press("Left"))
left_button.grid(row=1, column=0, padx=10, pady=10)

right_button = tk.Button(root, text="Right", command=lambda: on_press("Right"))
right_button.grid(row=1, column=2, padx=10, pady=10)

down_button = tk.Button(root, text="Down", command=lambda: on_press("Down"))
down_button.grid(row=2, column=1, padx=10, pady=10)

# Run the GUI in a loop
try:
    root.mainloop()
except KeyboardInterrupt:
    stop_motors()
    print("Exiting...")
