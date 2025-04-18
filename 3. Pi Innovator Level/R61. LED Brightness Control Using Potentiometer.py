"""
Components Used:
- Raspberry Pi
- ADS1115 Analog-to-Digital Converter
- Potentiometer
- LED
- Jumper Wires
"""

import time
import board
import busio
import adafruit_ads1x15.ads1115 as ads_module
from adafruit_ads1x15.analog_in import AnalogIn
import RPi.GPIO as GPIO

# Define GPIO pin for LED PWM
led_pin = 21  # Use hardware PWM pin

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

# Initialize PWM on led_pin with 1000Hz frequency
pwm = GPIO.PWM(led_pin, 1000)
pwm.start(0)  # Start with 0% brightness

# Initialize I2C and ADS1115
i2c = busio.I2C(board.SCL, board.SDA)
ads = ads_module.ADS1115(i2c)

# Define potentiometer channel (connected to A0 on ADS1115)
potentiometer = AnalogIn(ads, ads_module.P0)

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
    print("Exiting...")
    pwm.stop()
    GPIO.cleanup()
