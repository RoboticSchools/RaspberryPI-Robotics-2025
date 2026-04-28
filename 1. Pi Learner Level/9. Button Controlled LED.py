import RPi.GPIO as gpio
import time

led_pin = 21     # GPIO pin for LED
button_pin = 16  # GPIO pin for button

gpio.setmode(gpio.BCM)  # Use BCM pin numbering
gpio.setup(led_pin, gpio.OUT)  # Set LED pin as output
gpio.setup(button_pin, gpio.IN, pull_up_down=gpio.PUD_UP)  # Set button as input with pull-up

try:
    while True:
        if gpio.input(button_pin) == 0:  # Check if button is pressed
            gpio.output(led_pin, gpio.HIGH)  # Turn LED ON
            print("Button Pressed - LED ON")
        else:
            gpio.output(led_pin, gpio.LOW)  # Turn LED OFF
            print("Button Released - LED OFF")

        time.sleep(0.1)  # Small delay

except KeyboardInterrupt:
    gpio.cleanup()  # Reset GPIO on exit