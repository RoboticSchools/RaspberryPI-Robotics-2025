"""
Components Used:
- Raspberry Pi
- Pi DC Motor HAT
- Robot Car Setup
- 4 DC Motors (Right Front, Right Back, Left Front, Left Back)
"""

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

# Define the movement functions
def move_forward():
    print("Moving forward")
    rightFront.run(Raspi_MotorHAT.FORWARD)
    rightBack.run(Raspi_MotorHAT.FORWARD)
    leftFront.run(Raspi_MotorHAT.FORWARD)
    leftBack.run(Raspi_MotorHAT.FORWARD)
    time.sleep(2)

def move_backward():
    print("Moving backward")
    rightFront.run(Raspi_MotorHAT.BACKWARD)
    rightBack.run(Raspi_MotorHAT.BACKWARD)
    leftFront.run(Raspi_MotorHAT.BACKWARD)
    leftBack.run(Raspi_MotorHAT.BACKWARD)
    time.sleep(2)

def turn_left():
    print("Turning left")
    rightFront.run(Raspi_MotorHAT.BACKWARD)
    rightBack.run(Raspi_MotorHAT.BACKWARD)
    leftFront.run(Raspi_MotorHAT.FORWARD)
    leftBack.run(Raspi_MotorHAT.FORWARD)
    time.sleep(2)

def turn_right():
    print("Turning right")
    rightFront.run(Raspi_MotorHAT.FORWARD)
    rightBack.run(Raspi_MotorHAT.FORWARD)
    leftFront.run(Raspi_MotorHAT.BACKWARD)
    leftBack.run(Raspi_MotorHAT.BACKWARD)
    time.sleep(2)

def stop_motors():
    print("Stopping motors")
    rightFront.run(Raspi_MotorHAT.RELEASE)
    rightBack.run(Raspi_MotorHAT.RELEASE)
    leftFront.run(Raspi_MotorHAT.RELEASE)
    leftBack.run(Raspi_MotorHAT.RELEASE)
    time.sleep(2)

# Run the movements in a loop
try:
    while True:
        move_forward()    
        move_backward()   
        stop_motors()    
        turn_left()      
        turn_right()   
        stop_motors()  

except KeyboardInterrupt:
    print("Exiting program...")
    stop_motors()  # Ensure motors stop when the program is interrupted
