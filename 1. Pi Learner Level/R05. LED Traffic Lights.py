import RPi.GPIO as gpio
import time

green_led = 21   # GPIO pin for green LED
yellow_led = 16  # GPIO pin for yellow LED
red_led = 12     # GPIO pin for red LED

gpio.setmode(gpio.BCM)            # Use BCM pin numbering
gpio.setup(red_led, gpio.OUT)     # Set red LED as output
gpio.setup(yellow_led, gpio.OUT)  # Set yellow LED as output
gpio.setup(green_led, gpio.OUT)   # Set green LED as output

try:
    while True:
        gpio.output(green_led, gpio.HIGH)  # Turn green LED ON
        gpio.output(yellow_led, gpio.LOW)
        gpio.output(red_led, gpio.LOW)
        print("Green Light - GO")
        time.sleep(5)  # Wait 5 seconds

        gpio.output(green_led, gpio.LOW)
        gpio.output(yellow_led, gpio.HIGH)  # Turn yellow LED ON
        gpio.output(red_led, gpio.LOW)
        print("Yellow Light - SLOW DOWN")
        time.sleep(2)  # Wait 2 seconds

        gpio.output(green_led, gpio.LOW)
        gpio.output(yellow_led, gpio.LOW)
        gpio.output(red_led, gpio.HIGH)  # Turn red LED ON
        print("Red Light - STOP")
        time.sleep(5)  # Wait 5 seconds

except KeyboardInterrupt:
    gpio.cleanup()  # Reset GPIO on exit