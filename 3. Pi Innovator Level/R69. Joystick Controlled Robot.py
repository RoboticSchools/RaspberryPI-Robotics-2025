"""
Components Used:
1. Raspberry Pi
2. Pi DC Motor HAT
3. Robot Car (4 DC Motors)
4. Joystick (X-axis and Y-axis)
5. ADS1115 ADC
6. Jumper Wires
"""

import time
import board
import busio
from Raspi_MotorHAT import Raspi_MotorHAT
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# ---------------- ADS1115 Setup ----------------
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)

x_axis = AnalogIn(ads, ADS.P0)  # X-axis
y_axis = AnalogIn(ads, ADS.P1)  # Y-axis

# ---------------- Motor Setup ----------------
motor_hat = Raspi_MotorHAT(addr=0x6f)

right_front_motor = motor_hat.getMotor(1)
right_back_motor  = motor_hat.getMotor(2)
left_front_motor  = motor_hat.getMotor(3)
left_back_motor   = motor_hat.getMotor(4)

motor_speed = 150

for motor in (right_front_motor, right_back_motor, left_front_motor, left_back_motor):
    motor.setSpeed(motor_speed)

# ---------------- Movement Functions ----------------
def move_forward():
    right_front_motor.run(Raspi_MotorHAT.FORWARD)
    right_back_motor.run(Raspi_MotorHAT.FORWARD)
    left_front_motor.run(Raspi_MotorHAT.FORWARD)
    left_back_motor.run(Raspi_MotorHAT.FORWARD)

def move_backward():
    right_front_motor.run(Raspi_MotorHAT.BACKWARD)
    right_back_motor.run(Raspi_MotorHAT.BACKWARD)
    left_front_motor.run(Raspi_MotorHAT.BACKWARD)
    left_back_motor.run(Raspi_MotorHAT.BACKWARD)

def turn_left():
    right_front_motor.run(Raspi_MotorHAT.BACKWARD)
    right_back_motor.run(Raspi_MotorHAT.BACKWARD)
    left_front_motor.run(Raspi_MotorHAT.FORWARD)
    left_back_motor.run(Raspi_MotorHAT.FORWARD)

def turn_right():
    right_front_motor.run(Raspi_MotorHAT.FORWARD)
    right_back_motor.run(Raspi_MotorHAT.FORWARD)
    left_front_motor.run(Raspi_MotorHAT.BACKWARD)
    left_back_motor.run(Raspi_MotorHAT.BACKWARD)

def stop_motors():
    right_front_motor.run(Raspi_MotorHAT.RELEASE)
    right_back_motor.run(Raspi_MotorHAT.RELEASE)
    left_front_motor.run(Raspi_MotorHAT.RELEASE)
    left_back_motor.run(Raspi_MotorHAT.RELEASE)

# ---------------- Main Loop ----------------
try:
    print("Joystick Control Started...")

    while True:
        x_value = x_axis.value  # read X-axis
        y_value = y_axis.value  # read Y-axis

        print(f"X: {x_value} | Y: {y_value}")

        # joystick control logic
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
    print("Exiting...")
    stop_motors()