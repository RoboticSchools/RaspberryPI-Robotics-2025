"""
Components Used:
- Raspberry Pi
- Green LED (Go)
- Yellow LED (Slow Down)
- Red LED (Stop)
- Breadboard
- Jumper Wires
"""

import RPi.GPIO as gpio
import time

# Pin configuration
green_led = 21   # GPIO21 for Green LED (Go)
yellow_led = 20  # GPIO20 for Yellow LED (Ready)
red_led = 16     # GPIO16 for Red LED (Stop)

# GPIO setup
gpio.setmode(gpio.BCM)  # Use BCM pin numbering
gpio.setup(red_led, gpio.OUT)
gpio.setup(yellow_led, gpio.OUT)
gpio.setup(green_led, gpio.OUT)

try:
    while True:
        gpio.output(red_led, gpio.LOW)
        gpio.output(yellow_led, gpio.LOW)
        gpio.output(green_led, gpio.HIGH)  # Green LED ON (Go)
        print("Green Light - GO")
        time.sleep(5)

        gpio.output(green_led, gpio.LOW)
        gpio.output(yellow_led, gpio.HIGH)  # Yellow LED ON (Slow Down)
        gpio.output(red_led, gpio.LOW)
        print("Yellow Light - SLOW DOWN")
        time.sleep(2)

        gpio.output(yellow_led, gpio.LOW)
        gpio.output(red_led, gpio.HIGH)  # Red LED ON (Stop)
        gpio.output(green_led, gpio.LOW)
        print("Red Light - STOP")
        time.sleep(5)

except KeyboardInterrupt:
    pass

gpio.cleanup()  # Reset GPIO settings on exit
