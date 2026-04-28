import RPi.GPIO as gpio
import time

led_pin = 21     # GPIO pin for LED
button_pin = 16  # GPIO pin for button

gpio.setmode(gpio.BCM)  # Use BCM pin numbering
gpio.setup(button_pin, gpio.IN, pull_up_down=gpio.PUD_UP)  # Set button as input
gpio.setup(led_pin, gpio.OUT)  # Set LED as output

led_state = False  # Store LED state

try:
    while True:
        if gpio.input(button_pin) == 0:  # Check button press
            time.sleep(0.1)  # Small delay

            while gpio.input(button_pin) == 0:  # Wait until release
                pass

            led_state = not led_state  # Toggle LED state
            gpio.output(led_pin, led_state)  # Update LED

            print("LED ON" if led_state else "LED OFF")  # Show status

except KeyboardInterrupt:
    gpio.cleanup()  # Reset GPIO on exit