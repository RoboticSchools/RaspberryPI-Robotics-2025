"""
Components Used:
- Raspberry Pi
- LDR (Light Dependent Resistor)
- Buzzer
- Push Button
- Breadboard
- Jumper Wires
"""

import RPi.GPIO as gpio
import time

# Pin configuration
ldr_pin = 21
buzzer_pin = 16
button_pin = 12

# GPIO setup
gpio.setmode(gpio.BCM)  # Set pin numbering system to BCM
gpio.setup(ldr_pin, gpio.IN)  # Set LDR pin as input
gpio.setup(buzzer_pin, gpio.OUT)  # Set Buzzer pin as output
gpio.setup(button_pin, gpio.IN, pull_up_down=gpio.PUD_UP)  # Set Button pin as input with internal pull-up resistor

try:
    while True:
        ldr_state = gpio.input(ldr_pin)  # Read LDR value
        button_state = gpio.input(button_pin)  # Read Button state

        if ldr_state == 0:  # If light is detected (Morning)
            gpio.output(buzzer_pin, gpio.HIGH)  # Turn ON Buzzer (Alarm)
            print("Morning Detected - Buzzer ON")

        if button_state == 0:  # If button is pressed
            gpio.output(buzzer_pin, gpio.LOW)  # Turn OFF Buzzer (Stop Alarm)
            print("Button Pressed - Buzzer OFF")
            while True:  # Stop execution until reset
                pass

        time.sleep(0.1)  # Small delay for stable readings

except KeyboardInterrupt:
    gpio.cleanup()  # Reset GPIO settings before exiting
