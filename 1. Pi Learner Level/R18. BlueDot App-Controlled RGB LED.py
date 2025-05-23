"""
Components Used:
- Raspberry Pi
- RGB LED (Common Cathode)
- BlueDot App
- Jumper Wires
- Breadboard
"""

import RPi.GPIO as gpio
from bluedot import BlueDot
from signal import pause

# Pin configuration
red_pin = 21
green_pin = 20 
blue_pin = 16

# GPIO setup
gpio.setmode(gpio.BCM)  # Set pin numbering system to BCM
gpio.setup(red_pin, gpio.OUT)   
gpio.setup(green_pin, gpio.OUT)
gpio.setup(blue_pin, gpio.OUT) 

# BlueDot setup with 8 buttons (7 colors + 1 OFF)
bd = BlueDot(cols=4, rows=2)

# Set button colors
bd[0,0].color = "red"
bd[1,0].color = "green"
bd[2,0].color = "blue"
bd[3,0].color = "yellow"
bd[0,1].color = "cyan"
bd[1,1].color = "magenta"
bd[2,1].color = "white"
bd[3,1].color = "gray"  # OFF button

# Functions to set colors
def button_red():
    gpio.output(red_pin, gpio.HIGH)
    gpio.output(green_pin, gpio.LOW)
    gpio.output(blue_pin, gpio.LOW)
    print("Red LED ON")

def button_green():
    gpio.output(red_pin, gpio.LOW)
    gpio.output(green_pin, gpio.HIGH)
    gpio.output(blue_pin, gpio.LOW)
    print("Green LED ON")

def button_blue():
    gpio.output(red_pin, gpio.LOW)
    gpio.output(green_pin, gpio.LOW)
    gpio.output(blue_pin, gpio.HIGH)
    print("Blue LED ON")

def button_yellow():
    gpio.output(red_pin, gpio.HIGH)
    gpio.output(green_pin, gpio.HIGH)
    gpio.output(blue_pin, gpio.LOW)
    print("Yellow LED ON")

def button_cyan():
    gpio.output(red_pin, gpio.LOW)
    gpio.output(green_pin, gpio.HIGH)
    gpio.output(blue_pin, gpio.HIGH)
    print("Cyan LED ON")

def button_magenta():
    gpio.output(red_pin, gpio.HIGH)
    gpio.output(green_pin, gpio.LOW)
    gpio.output(blue_pin, gpio.HIGH)
    print("Magenta LED ON")

def button_white():
    gpio.output(red_pin, gpio.HIGH)
    gpio.output(green_pin, gpio.HIGH)
    gpio.output(blue_pin, gpio.HIGH)
    print("White LED ON")

def button_off():
    gpio.output(red_pin, gpio.LOW)
    gpio.output(green_pin, gpio.LOW)
    gpio.output(blue_pin, gpio.LOW)
    print("LED OFF")

# Assign buttons to colors
bd[0,0].when_pressed = button_red      # Red
bd[1,0].when_pressed = button_green    # Green
bd[2,0].when_pressed = button_blue     # Blue
bd[3,0].when_pressed = button_yellow   # Yellow
bd[0,1].when_pressed = button_cyan     # Cyan
bd[1,1].when_pressed = button_magenta  # Magenta
bd[2,1].when_pressed = button_white    # White
bd[3,1].when_pressed = button_off      # OFF

# Keep the script running
try:
    pause()
except KeyboardInterrupt:
    gpio.cleanup()  # Reset GPIO settings before exiting
