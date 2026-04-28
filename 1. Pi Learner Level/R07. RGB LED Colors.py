import RPi.GPIO as gpio
import time

red_pin = 21    # GPIO pin for red LED
green_pin = 20  # GPIO pin for green LED
blue_pin = 16   # GPIO pin for blue LED

gpio.setmode(gpio.BCM)           # Use BCM pin numbering
gpio.setup(red_pin, gpio.OUT)    # Set red pin as output
gpio.setup(green_pin, gpio.OUT)  # Set green pin as output
gpio.setup(blue_pin, gpio.OUT)   # Set blue pin as output

try:
    while True:
        gpio.output(red_pin, gpio.HIGH)    # Red ON
        gpio.output(green_pin, gpio.LOW)
        gpio.output(blue_pin, gpio.LOW)
        print("Red")
        time.sleep(1)  # Wait 1 second

        gpio.output(red_pin, gpio.LOW)
        gpio.output(green_pin, gpio.HIGH)  # Green ON
        gpio.output(blue_pin, gpio.LOW)
        print("Green")
        time.sleep(1)

        gpio.output(red_pin, gpio.LOW)
        gpio.output(green_pin, gpio.LOW)
        gpio.output(blue_pin, gpio.HIGH)   # Blue ON
        print("Blue")
        time.sleep(1)

        gpio.output(red_pin, gpio.HIGH)    # Red + Green = Yellow
        gpio.output(green_pin, gpio.HIGH)
        gpio.output(blue_pin, gpio.LOW)
        print("Yellow")
        time.sleep(1)

        gpio.output(red_pin, gpio.HIGH)    # Red + Blue = Magenta
        gpio.output(green_pin, gpio.LOW)
        gpio.output(blue_pin, gpio.HIGH)
        print("Magenta")
        time.sleep(1)

        gpio.output(red_pin, gpio.LOW)
        gpio.output(green_pin, gpio.HIGH)  # Green + Blue = Cyan
        gpio.output(blue_pin, gpio.HIGH)
        print("Cyan")
        time.sleep(1)

        gpio.output(red_pin, gpio.HIGH)    # Red + Green + Blue = White
        gpio.output(green_pin, gpio.HIGH)
        gpio.output(blue_pin, gpio.HIGH)
        print("White")
        time.sleep(1)

except KeyboardInterrupt:
    gpio.cleanup()  # Reset GPIO on exit