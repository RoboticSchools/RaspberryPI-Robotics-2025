"""
Components Used:
1. Raspberry Pi
2. ADS1115 ADC Module
3. Potentiometer
4. Five LEDs
5. Breadboard
6. Jumper Wires

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

# 5 LED pins
led_pins = [17, 27, 22, 5, 6]

# Set all LED pins as output
for pin in led_pins:
    gpio.setup(pin, gpio.OUT)

# ---------------- ADS1115 Setup ----------------
i2c = busio.I2C(board.SCL, board.SDA)  # Initialize I2C
ads = ADS.ADS1115(i2c)                 # Create ADS1115 object

# Read potentiometer from A0
potentiometer = AnalogIn(ads, 0)

# ---------------- Main Loop ----------------
try:
    while True:
        # Read analog value from potentiometer
        pot_value = potentiometer.value

        # Map value (0–65535) → delay (50–500 ms)
        delay_ms = np.interp(pot_value, [0, 32676], [50, 500])

        # LED chaser sequence
        for pin in led_pins:
            gpio.output(pin, gpio.HIGH)        # Turn ON LED
            time.sleep(delay_ms / 1000.0)      # Delay
            gpio.output(pin, gpio.LOW)         # Turn OFF LED

        time.sleep(delay_ms / 1000.0)          # Small gap between cycles

except KeyboardInterrupt:
    print("Exiting...")
    gpio.cleanup()  # Reset GPIO pins