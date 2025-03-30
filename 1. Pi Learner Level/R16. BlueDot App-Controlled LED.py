"""
Components Used:
- Raspberry Pi
- LED
- BlueDot App
- Jumper Wires
- Breadboard
"""

import RPi.GPIO as gpio
from bluedot import BlueDot

# Pin configuration
led_pin = 21  # GPIO21 connected to LED

# GPIO setup
gpio.setmode(gpio.BCM)  # Set pin numbering system to BCM
gpio.setup(led_pin, gpio.OUT)  # Set LED pin as output

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
    bd.wait_for_press()
except KeyboardInterrupt:
    pass

gpio.cleanup()  # Reset GPIO settings before exiting
