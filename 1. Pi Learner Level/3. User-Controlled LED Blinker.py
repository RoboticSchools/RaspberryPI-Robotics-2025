"""
Components Used:
- Raspberry Pi
- LED  
- Breadboard
- Jumper Wires
"""

import RPi.GPIO as gpio
import time

# Pin configuration
led_pin = 21  # Use GPIO21

# GPIO setup
gpio.setmode(gpio.BCM)  # Set pin numbering system to BCM
gpio.setup(led_pin, gpio.OUT)  # Set LED pin as output

try:
    blink_count = int(input("Enter the number of times to blink the LED: "))
    
    for _ in range(blink_count):
        print(f"Blink {blink_count}")
        gpio.output(led_pin, gpio.HIGH)  # Turn the LED on
        time.sleep(1)  # Wait for 1 second
        gpio.output(led_pin, gpio.LOW)  # Turn the LED off
        time.sleep(1)  # Wait for 1 second

except KeyboardInterrupt:
    gpio.cleanup()  # Reset GPIO settings on exit
