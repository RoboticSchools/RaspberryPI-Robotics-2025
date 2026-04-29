"""
Components Used:
1. Raspberry Pi
2. ADS1115 ADC Module
3. Potentiometer
4. 6 LEDs
5. Breadboard
6. Jumper Wires
"""

import time
import board
import busio
import numpy as np
import RPi.GPIO as GPIO
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# ---------------- GPIO Setup ----------------
GPIO.setmode(GPIO.BCM)  # use BCM numbering

led_pins = [17, 27, 22, 5, 6, 13]  # LED pins

for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT)  # set LEDs as output

# ---------------- ADS1115 Setup ----------------
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)

potentiometer = AnalogIn(ads, ADS.P0)  # potentiometer on A0

# ---------------- Main Loop ----------------
try:
    print("LED Chaser Started...")

    while True:
        pot_value = potentiometer.value  # read analog value

        # map potentiometer (0–65535) → delay (50–500 ms)
        delay_ms = np.interp(pot_value, [0, 65535], [50, 500])

        # LED chaser sequence
        for pin in led_pins:
            GPIO.output(pin, GPIO.HIGH)         # LED ON
            time.sleep(delay_ms / 1000.0)       # delay
            GPIO.output(pin, GPIO.LOW)          # LED OFF

        time.sleep(delay_ms / 1000.0)           # small gap

except KeyboardInterrupt:
    print("Exiting...")
    GPIO.cleanup()  # reset GPIO