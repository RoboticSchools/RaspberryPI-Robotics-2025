"""
Components Used:
- Raspberry Pi
- RGB LED (Common Cathode)
- Push Button
- Breadboard
- Jumper Wires
"""

import RPi.GPIO as gpio
import time
import random

# Pin configuration
red_pin = 21      # GPIO21 connected to Red pin of RGB LED
green_pin = 20    # GPIO20 connected to Green pin of RGB LED
blue_pin = 16     # GPIO16 connected to Blue pin of RGB LED
button_pin = 12   # GPIO12 connected to Push Button

# GPIO setup
gpio.setmode(gpio.BCM)  # Set pin numbering system to BCM
gpio.setup(button_pin, gpio.IN, pull_up_down=gpio.PUD_UP)  # Set button pin as input with pull-up resistor
gpio.setup(red_pin, gpio.OUT)  # Set Red pin as output
gpio.setup(green_pin, gpio.OUT)  # Set Green pin as output
gpio.setup(blue_pin, gpio.OUT)  # Set Blue pin as output

try:
    while True:
        if gpio.input(button_pin) == gpio.LOW:  # If button is pressed
            time.sleep(0.1)  # Simple debounce
            while gpio.input(button_pin) == gpio.LOW:  # Wait for button release
                pass
            
            # Generate random states (0 or 1) for each LED color
            red_state = random.randint(0, 1)
            green_state = random.randint(0, 1)
            blue_state = random.randint(0, 1)

            # Set the RGB LED to the new random color
            gpio.output(red_pin, red_state)
            gpio.output(green_pin, green_state)
            gpio.output(blue_pin, blue_state)

except KeyboardInterrupt:
    pass  # Handle keyboard interrupt (Ctrl+C) safely

gpio.cleanup()  # Reset GPIO settings before exiting
