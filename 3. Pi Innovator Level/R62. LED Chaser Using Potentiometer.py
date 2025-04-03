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
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import RPi.GPIO as GPIO

# Setup
GPIO.setmode(GPIO.BCM)

# Set up the LED pins (GPIO pins 17, 27, 22, 5, 6, 13 for 6 LEDs)
led_pins = [17, 27, 22, 5, 6, 13]
for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT)

# Initialize I2C and ADS1115 ADC
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
potentiometer_channel = AnalogIn(ads, ADS.P0)

def read_potentiometer():
    """Reads the potentiometer value and maps it to a time range (50ms - 500ms)."""
    pot_value = potentiometer_channel.value  # Read the raw potentiometer value (0-65535)
    mapped_time = (pot_value * (500 - 50)) // 65535 + 50  # Map the value to 50ms - 500ms
    return mapped_time

def chaser_effect():
    """Runs the LED chaser effect."""
    while True:
        time_delay = read_potentiometer()  # Get the delay from potentiometer
        for pin in led_pins:
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(time_delay / 1000.0)  # Convert milliseconds to seconds
            GPIO.output(pin, GPIO.LOW)
        time.sleep(time_delay / 1000.0)

# Run the chaser effect
try:
    chaser_effect()

except KeyboardInterrupt:
    print("Program Interrupted. Cleaning up...")
    GPIO.cleanup()  # Clean up GPIO settings when exiting the program
