import RPi.GPIO as gpio
import time

led_pin = 21  # GPIO pin connected to LED

gpio.setmode(gpio.BCM)         # Use BCM pin numbering
gpio.setup(led_pin, gpio.OUT)  # Set LED pin as output

try:
    blinks = int(input("Enter number of blinks: "))  # Get user input

    for i in range(blinks):
        gpio.output(led_pin, gpio.HIGH)  # Turn LED ON
        print(f"Blink {i+1}: LED is ON")
        time.sleep(1)  # Wait 1 second

        gpio.output(led_pin, gpio.LOW)   # Turn LED OFF
        print(f"Blink {i+1}: LED is OFF")
        time.sleep(1)  # Wait 1 second

except KeyboardInterrupt:
    gpio.cleanup()  # Reset GPIO on exit