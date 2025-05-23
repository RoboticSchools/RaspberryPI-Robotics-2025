"""
Components Used:
- Raspberry Pi
- RGB LED (Common Cathode)
- Breadboard
- Jumper Wires
"""

import RPi.GPIO as gpio
import time

# Pin configuration
red_pin = 21   
green_pin = 20 
blue_pin = 16  

# GPIO setup
gpio.setmode(gpio.BCM)  # Set pin numbering system to BCM
gpio.setup(red_pin, gpio.OUT)  
gpio.setup(green_pin, gpio.OUT) 
gpio.setup(blue_pin, gpio.OUT)

try:
    while True:
        # Red color
        gpio.output(red_pin, gpio.HIGH)
        gpio.output(green_pin, gpio.LOW)
        gpio.output(blue_pin, gpio.LOW)
        print("Red")
        time.sleep(1)

        # Green color
        gpio.output(red_pin, gpio.LOW)
        gpio.output(green_pin, gpio.HIGH)
        gpio.output(blue_pin, gpio.LOW)
        print("Green")
        time.sleep(1)

        # Blue color
        gpio.output(red_pin, gpio.LOW)
        gpio.output(green_pin, gpio.LOW)
        gpio.output(blue_pin, gpio.HIGH)
        print("Blue")
        time.sleep(1)

        # Yellow color (Red + Green)
        gpio.output(red_pin, gpio.HIGH)
        gpio.output(green_pin, gpio.HIGH)
        gpio.output(blue_pin, gpio.LOW)
        print("Yellow")
        time.sleep(1)

        # Magenta color (Red + Blue)
        gpio.output(red_pin, gpio.HIGH)
        gpio.output(green_pin, gpio.LOW)
        gpio.output(blue_pin, gpio.HIGH)
        print("Magenta")
        time.sleep(1)

        # Cyan color (Green + Blue)
        gpio.output(red_pin, gpio.LOW)
        gpio.output(green_pin, gpio.HIGH)
        gpio.output(blue_pin, gpio.HIGH)
        print("Cyan")
        time.sleep(1)

        # White color (Red + Green + Blue)
        gpio.output(red_pin, gpio.HIGH)
        gpio.output(green_pin, gpio.HIGH)
        gpio.output(blue_pin, gpio.HIGH)
        print("White")
        time.sleep(1)

except KeyboardInterrupt:
    gpio.cleanup()  # Reset GPIO settings on exit
