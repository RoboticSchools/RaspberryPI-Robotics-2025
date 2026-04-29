"""
Components Used:
1. Raspberry Pi
2. Joystick (X-axis and Y-axis)
3. ADS1115 ADC Module
4. Jumper Wires
"""

import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# ---------------- ADS1115 Setup ----------------
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)

# joystick axes
x_axis = AnalogIn(ads, ADS.P0)  # X-axis → A0
y_axis = AnalogIn(ads, ADS.P1)  # Y-axis → A1

# ---------------- Main Loop ----------------
try:
    print("Reading joystick values...")

    while True:
        x_value = x_axis.value  # read X-axis
        y_value = y_axis.value  # read Y-axis

        print(f"X: {x_value} | Y: {y_value}")

        time.sleep(0.1)  # small delay

except KeyboardInterrupt:
    print("Exiting...")