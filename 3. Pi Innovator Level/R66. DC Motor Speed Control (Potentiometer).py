"""
Components Used:
1. Raspberry Pi
2. DC Motor HAT
3. DC Motor
4. Potentiometer
5. ADS1115 ADC
6. Jumper Wires
"""

import time
import board
import busio
import numpy as np
from Raspi_MotorHAT import Raspi_MotorHAT
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# ---------------- ADS1115 Setup ----------------
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)

potentiometer = AnalogIn(ads, ADS.P0)  # potentiometer on A0

# ---------------- Motor Setup ----------------
motor_hat = Raspi_MotorHAT(addr=0x6f)
dc_motor = motor_hat.getMotor(1)

# ---------------- Main Loop ----------------
try:
    print("DC Motor Speed Control Started...")

    while True:
        pot_value = potentiometer.value  # read analog value

        # map 0–65535 → 0–255 using numpy
        motor_speed = int(np.interp(pot_value, [0, 65535], [0, 255]))

        dc_motor.setSpeed(motor_speed)                 # set speed
        dc_motor.run(Raspi_MotorHAT.FORWARD)           # run motor

        print(f"Motor Speed: {motor_speed}")

        time.sleep(0.1)

except KeyboardInterrupt:
    print("Exiting...")
    dc_motor.run(Raspi_MotorHAT.RELEASE)  # stop motor