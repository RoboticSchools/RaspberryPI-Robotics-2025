"""
Components Used:
1. Raspberry Pi
2. ADS1115 Module
3. Potentiometer
4. LED
5. Jumper Wires
"""

import time
import board
import busio
import numpy as np
import RPi.GPIO as GPIO
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# ---------------- GPIO Setup ----------------
led_pin = 21  # LED pin (PWM)

GPIO.setmode(GPIO.BCM)        # use BCM numbering
GPIO.setup(led_pin, GPIO.OUT)

pwm = GPIO.PWM(led_pin, 1000)  # 1kHz PWM
pwm.start(0)                   # start with 0% brightness

# ---------------- ADS1115 Setup ----------------
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)

potentiometer = AnalogIn(ads, ADS.P0)  # potentiometer on A0

# ---------------- Main Loop ----------------
try:
    print("Rotate potentiometer to control LED brightness")

    while True:
        pot_value = potentiometer.value  # read analog value

        # map 0–65535 → 0–100% using numpy
        brightness = np.interp(pot_value, [0, 65535], [0, 100])

        pwm.ChangeDutyCycle(brightness)  # update LED brightness

        print(f"Pot: {pot_value} | Brightness: {brightness:.2f}%")

        time.sleep(0.1)

except KeyboardInterrupt:
    print("Exiting...")
    pwm.stop()        # stop PWM
    GPIO.cleanup()    # reset GPIO