"""
Components Used:
- Raspberry Pi
- LED
- Push Button
- Breadboard
- Jumper Wires
"""

import RPi.GPIO as gpio
import time

# Pin configuration
button_pin = 20  # GPIO20 connected to the push button
led_pin = 21     # GPIO21 connected to the LED

# GPIO setup
gpio.setmode(gpio.BCM)  # Set pin numbering system to BCM
gpio.setup(button_pin, gpio.IN, pull_up_down=gpio.PUD_UP)  # Set button pin as input with internal pull-up resistor
gpio.setup(led_pin, gpio.OUT)  # Set LED pin as output

led_state = False  # Variable to store LED state (ON/OFF)

try:
    while True:
        if gpio.input(button_pin) == gpio.LOW:  # Check if button is pressed
            time.sleep(0.1)  # Simple debounce delay
            while gpio.input(button_pin) == gpio.LOW:  # Wait for button to be released
                pass
            
            led_state = not led_state  # Toggle LED state
            gpio.output(led_pin, led_state)  # Update LED status
            
            # Print the current LED state
            print("LED ON" if led_state else "LED OFF")

except KeyboardInterrupt:
    pass  # Handle keyboard interrupt (Ctrl+C) safely

gpio.cleanup()  # Reset GPIO settings before exiting
