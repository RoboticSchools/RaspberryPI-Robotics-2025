import RPi.GPIO as gpio
import time

led_pin = 21      # GPIO pin for LED
button_on = 16    # GPIO pin for ON button
button_off = 12   # GPIO pin for OFF button

gpio.setmode(gpio.BCM)  # Use BCM pin numbering
gpio.setup(led_pin, gpio.OUT)  # Set LED pin as output
gpio.setup(button_on, gpio.IN, pull_up_down=gpio.PUD_UP)   # Set ON button as input
gpio.setup(button_off, gpio.IN, pull_up_down=gpio.PUD_UP)  # Set OFF button as input

try:
    while True:
        if gpio.input(button_on) == gpio.LOW:  # Check ON button press
            gpio.output(led_pin, gpio.HIGH)  # Turn LED ON
            print("ON Button Pressed - LED ON")

        if gpio.input(button_off) == gpio.LOW:  # Check OFF button press
            gpio.output(led_pin, gpio.LOW)  # Turn LED OFF
            print("OFF Button Pressed - LED OFF")

        time.sleep(0.1)  # Small delay

except KeyboardInterrupt:
    gpio.cleanup()  # Reset GPIO on exit