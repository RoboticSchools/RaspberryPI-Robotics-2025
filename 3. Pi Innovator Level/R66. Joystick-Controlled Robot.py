"""
Components Used:
- Raspberry Pi
- Pi DC Motor HAT
- 4 DC Motors (Right Front, Right Back, Left Front, Left Back)
- Joystick (X-axis and Y-axis)
- ADS1115 ADC (to read joystick analog values)
- Jumper Wires
"""

import time
import busio
import board
from adafruit_ads1x15.ads1115 import ADS1115
from adafruit_ads1x15.analog_in import AnalogIn
from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor

# setup i2c and ads1115 for reading joystick input
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS1115(i2c)

# assign ads channels for x and y joystick axes
x_axis_channel = AnalogIn(ads, ADS1115.P0)
y_axis_channel = AnalogIn(ads, ADS1115.P1)

# initialize motor hat and setup motors
mh = Raspi_MotorHAT(addr=0x6f)
rightFront = mh.getMotor(1)
rightBack = mh.getMotor(2)
leftFront = mh.getMotor(3)
leftBack = mh.getMotor(4)

# set motor speed
speed = 150
rightFront.setSpeed(speed)
rightBack.setSpeed(speed)
leftFront.setSpeed(speed)
leftBack.setSpeed(speed)

def read_joystick():
    x_value = x_axis_channel.value
    y_value = y_axis_channel.value
    print(f"X: {x_value} | Y: {y_value}")
    return x_value, y_value

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

# main loop to control robot using joystick
try:
    while True:
        x_value, y_value = read_joystick()

        if y_value < 3000:
            move_forward()
        elif y_value > 30000:
            move_backward()
        elif x_value < 3000:
            turn_left()
        elif x_value > 30000:
            turn_right()
        else:
            stop_motors()

        time.sleep(0.1)

except KeyboardInterrupt:
    print("Exiting program...")
    stop_motors()
