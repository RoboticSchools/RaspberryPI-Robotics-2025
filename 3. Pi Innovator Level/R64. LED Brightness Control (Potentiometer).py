"""
Components Used:
1. Raspberry Pi
2. ADS1115 Module
3. Potentiometer
4. LED
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
led_pin = 21  # GPIO pin connected to LED

gpio.setmode(gpio.BCM)       # Use BCM numbering
gpio.setup(led_pin, gpio.OUT)

# Setup PWM on LED pin (1kHz frequency)
pwm = gpio.PWM(led_pin, 1000)
pwm.start(0)  # Start with 0% brightness (LED OFF)

# ---------------- ADS1115 Setup ----------------
i2c = busio.I2C(board.SCL, board.SDA)  # Initialize I2C
ads = ADS.ADS1115(i2c)                 # Create ADS1115 object

# Read potentiometer from A0 (P0)
potentiometer = AnalogIn(ads, 0)

# ---------------- Main Loop ----------------
try:
    while True:
        # Read analog value from potentiometer
        pot_value = potentiometer.value

        # Convert raw value (0–65535) to brightness percentage (0–100)
        brightness = np.interp(pot_value, [0, 32676], [0, 100])

        # Update LED brightness using PWM
        pwm.ChangeDutyCycle(brightness)

        # Print values for monitoring
        print(f"Pot: {pot_value} | Brightness: {brightness:.2f}%")

        time.sleep(0.1)  # Small delay for smooth control

except KeyboardInterrupt:
    # Clean exit when program is stopped
    print("Exiting...")
    pwm.stop()        # Stop PWM signal
    gpio.cleanup()    # Reset GPIO pins