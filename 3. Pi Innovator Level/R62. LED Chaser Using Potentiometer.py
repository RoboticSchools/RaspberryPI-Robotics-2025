"""
Components Used:
- Raspberry Pi
- ADS1115 Analog-to-Digital Converter (ADC)
- Potentiometer (for controlling timing)
- 6 LEDs
- Breadboard
- Jumper Wires
"""

import time
import board
import busio
import adafruit_ads1x15.ads1115 as ads_module
from adafruit_ads1x15.analog_in import AnalogIn
import RPi.GPIO as GPIO

# Set GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define the GPIO pins connected to the 6 LEDs and set them as outputs
led_pins = [17, 27, 22, 5, 6, 13]
for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT)

# Set up I2C communication and initialize the ADS1115 ADC
i2c = busio.I2C(board.SCL, board.SDA)
ads = ads_module.ADS1115(i2c)
pot_channel = AnalogIn(ads, ads_module.P0)  # Read analog input from potentiometer on channel 0

try:
    print("LED chaser started...")

    # Main loop: run LED chaser based on potentiometer speed control
    while True:
        # Read potentiometer value and map it to a delay between 50ms to 500ms
        pot_value = pot_channel.value
        time_delay = (pot_value * (500 - 50)) // 65535 + 50

        # Turn LEDs on one by one with the mapped delay
        for pin in led_pins:
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(time_delay / 1000.0)
            GPIO.output(pin, GPIO.LOW)

        time.sleep(time_delay / 1000.0)

except KeyboardInterrupt:
    # Stop the program and clean up GPIO when Ctrl+C is pressed
    print("Program interrupted. Cleaning up...")
    GPIO.cleanup()
