"""
Components Used:
- Raspberry Pi
- LED
- Two Push Buttons
- Breadboard
- Jumper Wires
"""

import RPi.GPIO as gpio
import time

# Pin configuration
led_pin = 21       # GPIO21 connected to LED
button_on = 20     # GPIO20 connected to ON Button
button_off = 16    # GPIO16 connected to OFF Button

# GPIO setup
gpio.setmode(gpio.BCM)  # Set pin numbering system to BCM
gpio.setup(led_pin, gpio.OUT)  # Set LED pin as output
gpio.setup(button_on, gpio.IN, pull_up_down=gpio.PUD_UP)  # Set ON button as input with pull-up resistor
gpio.setup(button_off, gpio.IN, pull_up_down=gpio.PUD_UP)  # Set OFF button as input with pull-up resistor

try:
    while True:
        if gpio.input(button_on) == gpio.LOW:  # Check if ON button is pressed
            gpio.output(led_pin, gpio.HIGH)  # Turn LED on
            print("ON Button Pressed - LED ON")

        if gpio.input(button_off) == gpio.LOW:  # Check if OFF button is pressed
            gpio.output(led_pin, gpio.LOW)  # Turn LED off
            print("OFF Button Pressed - LED OFF")

        time.sleep(0.1)  # Small delay to avoid bouncing issues

except KeyboardInterrupt:
    pass

gpio.cleanup()  # Reset GPIO settings on exit
