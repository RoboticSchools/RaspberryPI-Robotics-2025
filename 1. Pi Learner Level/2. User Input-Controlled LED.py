"""
Components Used:
- Raspberry Pi
- LED  
- Breadboard
- Jumper Wires
"""

import RPi.GPIO as gpio
import time

# Pin configuration
led_pin = 21  # Use GPIO21

# GPIO setup
gpio.setmode(gpio.BCM)  # Set pin numbering system to BCM
gpio.setup(led_pin, gpio.OUT)  # Set LED pin as output

try:
    while True:
        user_input = input("Enter 'on' to turn on LED, 'off' to turn off, or 'exit' to quit: ").lower()
        
        if user_input == "on":
            gpio.output(led_pin, gpio.HIGH)  # Turn the LED on
        elif user_input == "off":
            gpio.output(led_pin, gpio.LOW)  # Turn the LED off
        elif user_input == "exit":
            break
        else:
            print("Invalid input! Please enter 'on', 'off', or 'exit'.")

except KeyboardInterrupt:
    gpio.cleanup()  # Reset GPIO settings on exit
