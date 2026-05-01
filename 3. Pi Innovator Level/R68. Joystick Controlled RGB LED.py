"""
Components Used:
1. Raspberry Pi
2. Joystick (X-axis and Y-axis)
3. ADS1115 ADC Module
4. RGB LED (Red, Green, Blue pins)
5. Jumper Wires
6. Breadboard

Install Required Libraries:
pip3 install adafruit-circuitpython-ads1x15 adafruit-blinka numpy --break-system-packages
"""

import time
import board
import busio
import numpy as np
import RPi.GPIO as gpio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# ---------------- GPIO Setup ----------------
gpio.setmode(gpio.BCM)  # Use BCM numbering

# Define RGB LED pins
RED = 21
GREEN = 20
BLUE = 16

# Set pins as output
gpio.setup(RED, gpio.OUT)
gpio.setup(GREEN, gpio.OUT)
gpio.setup(BLUE, gpio.OUT)

# ---------------- ADS1115 Setup ----------------
i2c = busio.I2C(board.SCL, board.SDA)  # Initialize I2C communication
ads = ADS.ADS1115(i2c)                 # Create ADS1115 object

# Joystick axes connected to ADS channels
x_axis = AnalogIn(ads, 0)  # X-axis (left-right)
y_axis = AnalogIn(ads, 1)  # Y-axis (up-down)

# ---------------- Helper Function ----------------
def turn_off_all():
    """Turn OFF all RGB LED colors"""
    gpio.output(RED, gpio.LOW)
    gpio.output(GREEN, gpio.LOW)
    gpio.output(BLUE, gpio.LOW)

# ---------------- Main Loop ----------------
try:
    while True:
        # Read raw joystick values (0–32767)
        x_raw = x_axis.value
        y_raw = y_axis.value

        # Convert raw values to percentage (0–100)
        x_value = int(np.interp(x_raw, [0, 32767], [0, 100]))
        y_value = int(np.interp(y_raw, [0, 32767], [0, 100]))

        # Print mapped values
        print(f"X: {x_value}% | Y: {y_value}%")

        # Direction control based on joystick position

        if x_value < 30:
            # LEFT → turn ON RED
            turn_off_all()
            gpio.output(RED, gpio.HIGH)
            print("LEFT → RED")

        elif x_value > 70:
            # RIGHT → turn ON GREEN
            turn_off_all()
            gpio.output(GREEN, gpio.HIGH)
            print("RIGHT → GREEN")

        elif y_value < 30:
            # DOWN → turn ON BLUE
            turn_off_all()
            gpio.output(BLUE, gpio.HIGH)
            print("DOWN → BLUE")

        elif y_value > 70:
            # UP → turn ON RED + GREEN (YELLOW)
            turn_off_all()
            gpio.output(RED, gpio.HIGH)
            gpio.output(GREEN, gpio.HIGH)
            print("UP → YELLOW")

        else:
            # CENTER → turn OFF all LEDs
            turn_off_all()
            print("CENTER → ALL OFF")

        time.sleep(0.1)  # Small delay for smooth operation

except KeyboardInterrupt:
    # Clean exit when program is stopped
    print("Exiting...")
    gpio.cleanup()