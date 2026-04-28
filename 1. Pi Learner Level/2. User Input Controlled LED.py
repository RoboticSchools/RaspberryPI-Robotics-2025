import RPi.GPIO as gpio
import time

led_pin = 21  # GPIO pin connected to LED

gpio.setmode(gpio.BCM)         # Use BCM pin numbering
gpio.setup(led_pin, gpio.OUT)  # Set LED pin as output

try:
    while True:
        command = input("Enter command: ").lower()  # Get user input

        if command == "on":
            gpio.output(led_pin, gpio.HIGH)  # Turn LED ON
            print("LED is ON")

        elif command == "off":
            gpio.output(led_pin, gpio.LOW)   # Turn LED OFF
            print("LED is OFF")

        elif command == "exit":
            print("Exiting program...")
            break  # Exit loop

        else:
            print("Invalid command. Please type 'on', 'off', or 'exit'.")

except KeyboardInterrupt:
    gpio.cleanup()  # Reset GPIO on exit