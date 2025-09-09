import RPi.GPIO as gpio   # Library to control Raspberry Pi GPIO pins (input/output)
import time               # Library to manage delays and time-based functions

# --- Pin configuration ---
led_pin = 21  # The GPIO pin number (BCM mode) where the LED is connected

# --- GPIO setup ---
gpio.setmode(gpio.BCM)        # Set pin numbering system to BCM (Broadcom SOC channel)
gpio.setup(led_pin, gpio.OUT) # Configure the LED pin to work as an output

print("LED Blink Program Started (Press CTRL+C to stop)")

try:
    while True:
        # --- Turn LED ON ---
        gpio.output(led_pin, gpio.HIGH)  # Send HIGH signal to turn the LED on
        print("LED is ON")
        time.sleep(1)  # Keep LED on for 1 second

        # --- Turn LED OFF ---
        gpio.output(led_pin, gpio.LOW)   # Send LOW signal to turn the LED off
        print("LED is OFF")
        time.sleep(1)  # Keep LED off for 1 second

except KeyboardInterrupt:
    # --- Cleanup on exit ---
    print("\nProgram stopped by user. Cleaning up GPIO...")  
    gpio.cleanup()  # Reset all GPIO settings to safe state
