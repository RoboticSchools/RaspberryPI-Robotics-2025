import RPi.GPIO as gpio   # Library to control Raspberry Pi GPIO pins
import time               # Library to add delays (sleep) and track time

# --- Pin configuration ---
led_pin = 21  # GPIO pin number connected to the LED (BCM numbering)

# --- GPIO setup ---
gpio.setmode(gpio.BCM)        # Use Broadcom (BCM) pin numbering
gpio.setup(led_pin, gpio.OUT) # Set the LED pin as an output pin

print("LED Blink Program Started (Press CTRL+C to stop)")

try:
    while True:
        # Turn LED ON
        gpio.output(led_pin, gpio.HIGH)
        print("LED is ON")
        time.sleep(1)  # Keep LED on for 1 second

        # Turn LED OFF
        gpio.output(led_pin, gpio.LOW)
        print("LED is OFF")
        time.sleep(1)  # Keep LED off for 1 second

except KeyboardInterrupt:
    # Clean up GPIO settings before exiting
    print("\nProgram stopped by user. Cleaning up GPIO...")
    gpio.cleanup()
    print("GPIO cleanup done. Goodbye!")
