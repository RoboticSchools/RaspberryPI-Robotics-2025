"""
Components Used:
- Raspberry Pi
- LED
- BlueDot App
- Breadboard
- Jumper Wires
"""

import RPi.GPIO as gpio
from bluedot import BlueDot
from signal import pause

# Pin configuration
led_pin = 21

# GPIO setup
gpio.setmode(gpio.BCM)  # Set pin numbering system to BCM
gpio.setup(led_pin, gpio.OUT)

# BlueDot setup
bd = BlueDot()

# Turn LED ON when pressed
def led_on():
    gpio.output(led_pin, gpio.HIGH)
    print("LED ON - Button Pressed")

# Turn LED OFF when released
def led_off():
    gpio.output(led_pin, gpio.LOW)
    print("LED OFF - Button Released")

bd.when_pressed = led_on  # LED ON when button is pressed
bd.when_released = led_off  # LED OFF when button is released

# Keep the script running
try:
    pause()
except KeyboardInterrupt:
    gpio.cleanup()  # Reset GPIO settings before exiting
