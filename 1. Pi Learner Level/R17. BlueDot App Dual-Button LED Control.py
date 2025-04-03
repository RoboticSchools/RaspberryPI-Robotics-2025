"""
Components Used:
- Raspberry Pi
- One LED
- BlueDot App
- Jumper Wires
- Breadboard
"""

import RPi.GPIO as gpio
from bluedot import BlueDot
from signal import pause

# Pin configuration
led_pin = 21  # GPIO21 connected to LED

# GPIO setup
gpio.setmode(gpio.BCM)  # Set pin numbering system to BCM
gpio.setup(led_pin, gpio.OUT)  # Set LED pin as output

# BlueDot setup with 2 buttons in a single row
bd = BlueDot(cols=2, rows=1)

# Set button colors
bd[0,0].color = "green"  # ON button (Green)
bd[1,0].color = "red"    # OFF button (Red)

# Function to turn LED ON
def button_on():
    gpio.output(led_pin, gpio.HIGH)
    print("LED ON - Button ON Pressed")

# Function to turn LED OFF
def button_off():
    gpio.output(led_pin, gpio.LOW)
    print("LED OFF - Button OFF Pressed")

bd[0,0].when_pressed = button_on  # Assign button 1 to turn LED ON
bd[1,0].when_pressed = button_off  # Assign button 2 to turn LED OFF

pause()  # Keep the script running
