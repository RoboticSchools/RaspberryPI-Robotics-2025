"""
Components Used:
- Raspberry Pi
- Joystick (2 analog axes: X-axis and Y-axis)
- ADS1115 ADC (to read joystick analog values)
- Jumper Wires
"""

import time
import busio
import board
from adafruit_ads1x15.ads1115 import ADS1115
from adafruit_ads1x15.analog_in import AnalogIn

# setup i2c for ads1115 to read analog values from joystick
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS1115(i2c)

# assign ads channels for x-axis and y-axis of joystick
x_axis = AnalogIn(ads, ADS1115.P0)  # X-axis to A0
y_axis = AnalogIn(ads, ADS1115.P1)  # Y-axis to A1

try:
    print("Reading joystick values...")

    # main loop to read and display joystick position
    while True:
        x_val = x_axis.value
        y_val = y_axis.value

        print(f"X: {x_val} | Y: {y_val}")

        time.sleep(0.1)

except KeyboardInterrupt:
    print("Joystick reading stopped.")
