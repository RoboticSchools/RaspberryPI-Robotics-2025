"""
LED Brightness Control using Potentiometer (ADS1115) on Raspberry Pi
"""

import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import RPi.GPIO as GPIO

# Define GPIO pin for LED PWM
LED_PIN = 18  # Use hardware PWM pin

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# Initialize PWM on LED_PIN with 1000Hz frequency
pwm = GPIO.PWM(LED_PIN, 1000)
pwm.start(0)  # Start with 0% brightness

# Initialize I2C and ADS1115
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)

# Define potentiometer channel (connected to A0 on ADS1115)
potentiometer = AnalogIn(ads, ADS.P0)

try:
    print("Adjust potentiometer to control LED brightness...")

    while True:
        # Read potentiometer value (0-65535)
        pot_value = potentiometer.value

        # Map potentiometer value (0-65535) to PWM duty cycle (0-100)
        brightness = (pot_value / 65535) * 100

        # Set LED brightness
        pwm.ChangeDutyCycle(brightness)

        print(f"Potentiometer Value: {pot_value} | LED Brightness: {brightness:.2f}%")
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nExiting...")
    pwm.stop()
    GPIO.cleanup()
