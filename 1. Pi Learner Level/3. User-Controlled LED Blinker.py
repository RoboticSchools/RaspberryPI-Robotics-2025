import RPi.GPIO as gpio   # Library to control Raspberry Pi GPIO pins (input/output)
import time               # Library to manage delays and time-based functions

# --- Pin configuration ---
led_pin = 21  # The GPIO pin number (BCM mode) where the LED is connected

# --- GPIO setup ---
gpio.setmode(gpio.BCM)        # Set pin numbering system to BCM (Broadcom SOC channel)
gpio.setup(led_pin, gpio.OUT) # Configure the LED pin to work as an output

print("LED Blink Program Started (User Defined Number of Blinks)")

try:
    # --- Ask the user how many times the LED should blink ---
    blinks = int(input("Enter the number of times to blink the LED: "))

    # --- Blink the LED for the given number of times ---
    for i in range(blinks):
        gpio.output(led_pin, gpio.HIGH)  # Send HIGH signal to turn the LED on
        print(f"Blink {i+1}: LED is ON")
        time.sleep(1)  # Keep LED on for 1 second

        gpio.output(led_pin, gpio.LOW)   # Send LOW signal to turn the LED off
        print(f"Blink {i+1}: LED is OFF")
        time.sleep(1)  # Keep LED off for 1 second

except KeyboardInterrupt:
    # --- Cleanup on exit ---
    print("\nProgram stopped by user. Cleaning up GPIO...")  
    gpio.cleanup()  # Reset all GPIO settings to safe state
