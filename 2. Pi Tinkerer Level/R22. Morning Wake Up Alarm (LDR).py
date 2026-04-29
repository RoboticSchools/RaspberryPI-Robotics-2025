"""
Components Used:
1. Raspberry Pi
2. LDR (Light Sensor)
3. Buzzer
4. Push Button
5. Breadboard
6. Jumper Wires
"""

import RPi.GPIO as gpio
import time

ldr_pin = 21     # GPIO pin for LDR
buzzer_pin = 16  # GPIO pin for buzzer
button_pin = 12  # GPIO pin for button

gpio.setmode(gpio.BCM)            # Use BCM pin numbering
gpio.setup(ldr_pin, gpio.IN)      # Set LDR as input
gpio.setup(buzzer_pin, gpio.OUT)  # Set buzzer as output
gpio.setup(button_pin, gpio.IN, pull_up_down=gpio.PUD_UP)  # Set button as input

try:
    while True:
        ldr_state = gpio.input(ldr_pin)       # Read LDR
        button_state = gpio.input(button_pin) # Read button

        if ldr_state == 0:  # Check light condition
            gpio.output(buzzer_pin, gpio.HIGH)  # Turn buzzer ON
            print("Morning Detected - Buzzer ON")

        if button_state == 0:  # Check button press
            gpio.output(buzzer_pin, gpio.LOW)  # Turn buzzer OFF
            print("Button Pressed - Buzzer OFF")
            while True:  # Stop program
                pass

        time.sleep(0.1)  # Small delay

except KeyboardInterrupt:
    gpio.cleanup()  # Reset GPIO on exit