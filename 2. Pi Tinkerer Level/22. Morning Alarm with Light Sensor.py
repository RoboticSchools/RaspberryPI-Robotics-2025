"""
Components Used:
- Raspberry Pi
- LDR (Light Dependent Resistor)
- Buzzer
- Push Button
- Resistors
- Breadboard
- Jumper Wires
"""

import RPi.GPIO as gpio
import time

# Pin configuration
ldr_pin = 21      # GPIO21 connected to LDR (Digital Output)
buzzer_pin = 20   # GPIO20 connected to Buzzer
button_pin = 16   # GPIO16 connected to Push Button

# GPIO setup
gpio.setmode(gpio.BCM)  # Set pin numbering system to BCM
gpio.setup(ldr_pin, gpio.IN)  # Set LDR pin as input
gpio.setup(buzzer_pin, gpio.OUT)  # Set Buzzer pin as output
gpio.setup(button_pin, gpio.IN, pull_up_down=gpio.PUD_UP)  # Set Button pin as input with pull-up resistor

try:
    while True:
        ldr_state = gpio.input(ldr_pin)  # Read LDR value
        button_state = gpio.input(button_pin)  # Read Button state

        if ldr_state == gpio.LOW:  # If light is detected (Morning)
            gpio.output(buzzer_pin, gpio.HIGH)  # Turn ON Buzzer (Alarm)
            print("Morning Detected - Buzzer ON")

        if button_state == gpio.LOW:  # If button is pressed
            gpio.output(buzzer_pin, gpio.LOW)  # Turn OFF Buzzer (Stop Alarm)
            print("Button Pressed - Buzzer OFF")
            while True:  # Stop execution until reset
                pass

        time.sleep(0.1)  # Small delay for stable readings

except KeyboardInterrupt:
    pass

gpio.cleanup()  # Reset GPIO settings before exiting
