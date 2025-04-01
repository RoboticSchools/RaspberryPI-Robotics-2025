"""
Components Used:
- Raspberry Pi
- UGeek DC Motor HAT
- 4 DC Motors (Right Front, Right Back, Left Front, Left Back)
- Jumper Wires
"""

import time
from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor

# Initialize Motor HAT (Default I2C address 0x6F)
mh = Raspi_MotorHAT(addr=0x6f)

# Create motor objects for 4 motors
rightFront = mh.getMotor(1)   # Right Front Motor
rightBack = mh.getMotor(2)    # Right Back Motor
leftFront = mh.getMotor(3)    # Left Front Motor
leftBack = mh.getMotor(4)     # Left Back Motor

# Set initial motor speeds (can adjust based on need)
rightFront.setSpeed(150)
rightBack.setSpeed(150)
leftFront.setSpeed(150)
leftBack.setSpeed(150)

# Function to move the robot forward
def move_forward():
    print("Moving Forward")
    rightFront.run(Raspi_MotorHAT.FORWARD)
    rightBack.run(Raspi_MotorHAT.FORWARD)
    leftFront.run(Raspi_MotorHAT.FORWARD)
    leftBack.run(Raspi_MotorHAT.FORWARD)

# Function to move the robot backward
def move_backward():
    print("Moving Backward")
    rightFront.run(Raspi_MotorHAT.BACKWARD)
    rightBack.run(Raspi_MotorHAT.BACKWARD)
    leftFront.run(Raspi_MotorHAT.BACKWARD)
    leftBack.run(Raspi_MotorHAT.BACKWARD)

# Function to turn the robot left
def turn_left():
    print("Turning Left")
    rightFront.run(Raspi_MotorHAT.BACKWARD)
    rightBack.run(Raspi_MotorHAT.BACKWARD)
    leftFront.run(Raspi_MotorHAT.FORWARD)
    leftBack.run(Raspi_MotorHAT.FORWARD)

# Function to turn the robot right
def turn_right():
    print("Turning Right")
    rightFront.run(Raspi_MotorHAT.FORWARD)
    rightBack.run(Raspi_MotorHAT.FORWARD)
    leftFront.run(Raspi_MotorHAT.BACKWARD)
    leftBack.run(Raspi_MotorHAT.BACKWARD)

# Function to stop the robot
def stop_robot():
    print("Stopping Robot")
    rightFront.run(Raspi_MotorHAT.RELEASE)
    rightBack.run(Raspi_MotorHAT.RELEASE)
    leftFront.run(Raspi_MotorHAT.RELEASE)
    leftBack.run(Raspi_MotorHAT.RELEASE)

# Main code execution
try:
    while True:
        command = input("Enter command (w=forward, s=backward, a=left, d=right, x=stop): ").lower()
        
        if command == 'w':
            move_forward()
        elif command == 's':
            move_backward()
        elif command == 'a':
            turn_left()
        elif command == 'd':
            turn_right()
        elif command == 'x':
            stop_robot()
        else:
            print("Invalid command!")

        time.sleep(0.1)

except KeyboardInterrupt:
    print("Exiting...")
    stop_robot()
