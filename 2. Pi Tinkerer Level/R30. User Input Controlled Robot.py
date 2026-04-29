"""
Components Used:
1. Raspberry Pi
2. DC Motor HAT
3. Robot Car
4. 4 DC Motors
"""

import time
from Raspi_MotorHAT import Raspi_MotorHAT

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
    print("Moving Forward")
    rightFront.run(Raspi_MotorHAT.FORWARD)
    rightBack.run(Raspi_MotorHAT.FORWARD)
    leftFront.run(Raspi_MotorHAT.FORWARD)
    leftBack.run(Raspi_MotorHAT.FORWARD)

def move_backward():
    print("Moving Backward")
    rightFront.run(Raspi_MotorHAT.BACKWARD)
    rightBack.run(Raspi_MotorHAT.BACKWARD)
    leftFront.run(Raspi_MotorHAT.BACKWARD)
    leftBack.run(Raspi_MotorHAT.BACKWARD)

def turn_left():
    print("Turning Left")
    rightFront.run(Raspi_MotorHAT.BACKWARD)
    rightBack.run(Raspi_MotorHAT.BACKWARD)
    leftFront.run(Raspi_MotorHAT.FORWARD)
    leftBack.run(Raspi_MotorHAT.FORWARD)

def turn_right():
    print("Turning Right")
    rightFront.run(Raspi_MotorHAT.FORWARD)
    rightBack.run(Raspi_MotorHAT.FORWARD)
    leftFront.run(Raspi_MotorHAT.BACKWARD)
    leftBack.run(Raspi_MotorHAT.BACKWARD)

def stop_robot():
    print("Stopping Robot")
    rightFront.run(Raspi_MotorHAT.RELEASE)
    rightBack.run(Raspi_MotorHAT.RELEASE)
    leftFront.run(Raspi_MotorHAT.RELEASE)
    leftBack.run(Raspi_MotorHAT.RELEASE)

try:
    while True:
        command = input("Enter command (w=forward, s=backward, a=left, d=right, x=stop): ").lower()  # Get input

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
            print("Invalid command")

        time.sleep(0.1)  # Small delay

except KeyboardInterrupt:
    print("Exiting...")
    stop_robot()  # Stop all motors