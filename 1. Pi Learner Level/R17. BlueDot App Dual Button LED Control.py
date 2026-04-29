"""
Components Used:
1. Raspberry Pi
2. LED
3. Breadboard
4. Jumper Wires
5. Android Mobile (BlueDot App)

Install Required Library:
pip install bluedot --break-system-packages
"""

import RPi.GPIO as gpio
from bluedot import BlueDot
from signal import pause

led_pin = 21  # GPIO pin for LED

gpio.setmode(gpio.BCM)        # Use BCM pin numbering
gpio.setup(led_pin, gpio.OUT) # Set LED as output

bd = BlueDot(cols=2, rows=1)  # Create BlueDot with 2 buttons

bd[0,0].color = "green"  # ON button
bd[1,0].color = "red"    # OFF button

def button_on():
    gpio.output(led_pin, gpio.HIGH)  # Turn LED ON
    print("LED ON - Button ON Pressed")

def button_off():
    gpio.output(led_pin, gpio.LOW)   # Turn LED OFF
    print("LED OFF - Button OFF Pressed")

bd[0,0].when_pressed = button_on  # Assign ON button
bd[1,0].when_pressed = button_off # Assign OFF button

try:
    pause()  # Keep program running
except KeyboardInterrupt:
    gpio.cleanup()  # Reset GPIO on exit