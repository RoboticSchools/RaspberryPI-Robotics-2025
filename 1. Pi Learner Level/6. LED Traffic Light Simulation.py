"""
Components Used:
- Raspberry Pi
- Red LED (Stop)
- Yellow LED (Ready)
- Green LED (Go)
- Breadboard
- Jumper Wires
"""

import RPi.GPIO as gpio
import time

# Pin configuration
red_led = 21    # GPIO21 for Red LED (Stop)
yellow_led = 20  # GPIO20 for Yellow LED (Ready)
green_led = 16   # GPIO16 for Green LED (Go)

# GPIO setup
gpio.setmode(gpio.BCM)  # Set pin numbering system to BCM
gpio.setup(red_led, gpio.OUT)  # Set Red LED as output
gpio.setup(yellow_led, gpio.OUT)  # Set Yellow LED as output
gpio.setup(green_led, gpio.OUT)  # Set Green LED as output

try:
    while True:
        gpio.output(red_led, gpio.HIGH)  # Red LED ON (Stop)
        gpio.output(yellow_led, gpio.LOW)
        gpio.output(green_led, gpio.LOW)
        print("Red Light - STOP")
        time.sleep(5)

        gpio.output(red_led, gpio.LOW)
        gpio.output(yellow_led, gpio.HIGH)  # Yellow LED ON (Ready)
        gpio.output(green_led, gpio.LOW)
        print("Yellow Light - READY")
        time.sleep(2)

        gpio.output(red_led, gpio.LOW)
        gpio.output(yellow_led, gpio.LOW)
        gpio.output(green_led, gpio.HIGH)  # Green LED ON (Go)
        print("Green Light - GO")
        time.sleep(5)

except KeyboardInterrupt:
    pass

gpio.cleanup()  # Reset GPIO settings on exit
