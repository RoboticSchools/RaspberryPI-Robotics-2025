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
green_led = 21   
yellow_led = 16 
red_led = 12 

# GPIO setup
gpio.setmode(gpio.BCM)  # Use BCM pin numbering
gpio.setup(red_led, gpio.OUT)
gpio.setup(yellow_led, gpio.OUT)
gpio.setup(green_led, gpio.OUT)

try:
    while True:
        gpio.output(green_led, gpio.HIGH)  # Green LED ON (Go)
        gpio.output(yellow_led, gpio.LOW)
        gpio.output(red_led, gpio.LOW)
        print("Green Light - GO")
        time.sleep(5)

        gpio.output(green_led, gpio.LOW)
        gpio.output(yellow_led, gpio.HIGH)  # Yellow LED ON (Slow Down)
        gpio.output(red_led, gpio.LOW)
        print("Yellow Light - SLOW DOWN")
        time.sleep(2)

        gpio.output(green_led, gpio.LOW)
        gpio.output(yellow_led, gpio.LOW)
        gpio.output(red_led, gpio.HIGH)  # Red LED ON (Stop)
        print("Red Light - STOP")
        time.sleep(5)

except KeyboardInterrupt:
    gpio.cleanup()  # Reset GPIO settings on exit
