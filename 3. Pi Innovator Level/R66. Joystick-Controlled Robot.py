"""
Components Used:
- Raspberry Pi
- UGeek DC Motor HAT
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

# Setup I2C for ADS1115 (to read joystick analog values)
i2c = busio.I2C(board.SCL, board.SDA)  # Initialize I2C interface
ads = ADS1115(i2c)  # Initialize ADS1115

# Define the analog input channels for X-axis and Y-axis
x_axis_channel = AnalogIn(ads, ADS1115.P0)  # Joystick X-axis connected to A0
y_axis_channel = AnalogIn(ads, ADS1115.P1)  # Joystick Y-axis connected to A1

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

def read_joystick():
    """Reads the joystick values from X and Y axes."""
    x_value = x_axis_channel.value  # Read the X-axis analog value (0-65535)
    y_value = y_axis_channel.value  # Read the Y-axis analog value (0-65535)
    
    # Print the joystick values
    print(f"X-axis Value: {x_value}")
    print(f"Y-axis Value: {y_value}")
    
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

# Run the robot based on joystick input
try:
    while True:
        x_value, y_value = read_joystick()  # Get joystick input

        if y_value < 3000:  # Move forward if joystick pushed forward (Y value low)
            move_forward()
        elif y_value > 30000:  # Move backward if joystick pushed backward (Y value high)
            move_backward()
        elif x_value < 3000:  # Turn left if joystick pushed left (X value low)
            turn_left()
        elif x_value > 30000:  # Turn right if joystick pushed right (X value high)
            turn_right()
        else:  # Stop motors if joystick is centered
            stop_motors()

        time.sleep(0.1)  # Small delay for smoother operation

except KeyboardInterrupt:
    print("Exiting program...")
    stop_motors()  # Ensure motors stop when the program is interrupted
