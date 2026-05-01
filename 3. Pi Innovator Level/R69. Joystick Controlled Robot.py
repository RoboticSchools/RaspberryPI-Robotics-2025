"""
Components Used:
1. Raspberry Pi
2. Pi DC Motor HAT
3. Robot Car (4 DC Motors)
4. Joystick (X-axis and Y-axis)
5. ADS1115 ADC
6. Jumper Wires

Install Required Libraries:
pip3 install adafruit-circuitpython-ads1x15 adafruit-blinka numpy --break-system-packages
"""

import time
import board
import busio
import numpy as np
from Raspi_MotorHAT import Raspi_MotorHAT
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# ---------------- ADS1115 Setup ----------------
i2c = busio.I2C(board.SCL, board.SDA)  # Initialize I2C communication
ads = ADS.ADS1115(i2c)                 # Create ADS1115 object

# Joystick axes connected to ADS channels
x_axis = AnalogIn(ads, ADS.P0)  # X-axis (left-right)
y_axis = AnalogIn(ads, ADS.P1)  # Y-axis (forward-backward)

# ---------------- Motor Setup ----------------
motor_hat = Raspi_MotorHAT(addr=0x6f)  # Initialize Motor HAT

# Assign motors (based on Motor HAT ports)
right_front_motor = motor_hat.getMotor(1)
right_back_motor  = motor_hat.getMotor(2)
left_front_motor  = motor_hat.getMotor(3)
left_back_motor   = motor_hat.getMotor(4)

motor_speed = 150  # Speed value (0–255)

# Set same speed for all motors
for motor in (right_front_motor, right_back_motor, left_front_motor, left_back_motor):
    motor.setSpeed(motor_speed)

# ---------------- Movement Functions ----------------
def move_forward():
    """Move robot forward"""
    right_front_motor.run(Raspi_MotorHAT.FORWARD)
    right_back_motor.run(Raspi_MotorHAT.FORWARD)
    left_front_motor.run(Raspi_MotorHAT.FORWARD)
    left_back_motor.run(Raspi_MotorHAT.FORWARD)

def move_backward():
    """Move robot backward"""
    right_front_motor.run(Raspi_MotorHAT.BACKWARD)
    right_back_motor.run(Raspi_MotorHAT.BACKWARD)
    left_front_motor.run(Raspi_MotorHAT.BACKWARD)
    left_back_motor.run(Raspi_MotorHAT.BACKWARD)

def turn_left():
    """Turn robot left"""
    right_front_motor.run(Raspi_MotorHAT.BACKWARD)
    right_back_motor.run(Raspi_MotorHAT.BACKWARD)
    left_front_motor.run(Raspi_MotorHAT.FORWARD)
    left_back_motor.run(Raspi_MotorHAT.FORWARD)

def turn_right():
    """Turn robot right"""
    right_front_motor.run(Raspi_MotorHAT.FORWARD)
    right_back_motor.run(Raspi_MotorHAT.FORWARD)
    left_front_motor.run(Raspi_MotorHAT.BACKWARD)
    left_back_motor.run(Raspi_MotorHAT.BACKWARD)

def stop_motors():
    """Stop all motors"""
    right_front_motor.run(Raspi_MotorHAT.RELEASE)
    right_back_motor.run(Raspi_MotorHAT.RELEASE)
    left_front_motor.run(Raspi_MotorHAT.RELEASE)
    left_back_motor.run(Raspi_MotorHAT.RELEASE)

# ---------------- Main Loop ----------------
try:
    print("Joystick Control Started...")

    while True:
        # Read raw joystick values (0–32767)
        x_raw = x_axis.value
        y_raw = y_axis.value

        # Convert raw values to percentage (0–100)
        x_value = int(np.interp(x_raw, [0, 32767], [0, 100]))
        y_value = int(np.interp(y_raw, [0, 32767], [0, 100]))

        # Print joystick position
        print(f"X: {x_value}% | Y: {y_value}%")

        # Control robot movement based on joystick position

        if y_value < 30:
            # Joystick pushed forward → move forward
            move_forward()

        elif y_value > 70:
            # Joystick pulled backward → move backward
            move_backward()

        elif x_value < 30:
            # Joystick moved left → turn left
            turn_left()

        elif x_value > 70:
            # Joystick moved right → turn right
            turn_right()

        else:
            # Joystick in center → stop robot
            stop_motors()

        time.sleep(0.1)  # Small delay for smooth control

except KeyboardInterrupt:
    # Clean exit when program is stopped
    print("Exiting...")
    stop_motors()