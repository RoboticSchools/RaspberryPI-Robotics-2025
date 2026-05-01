"""
Components Used:
1. Raspberry Pi
2. MQ7 Gas Sensor (Digital Output)
3. Buzzer
4. Blynk App
5. Jumper Wires
"""

import time
import RPi.GPIO as gpio
from BlynkLib import Blynk

# ---------------- Blynk Setup ----------------
BLYNK_AUTH = 'your_blynk_auth_token'  # Replace with your Blynk auth token
blynk = Blynk(BLYNK_AUTH, server="blynk.cloud", port=80)  # Initialize Blynk connection

# ---------------- GPIO Setup ----------------
gpio.setmode(gpio.BCM)  # Use BCM pin numbering

mq7_pin = 21      # GPIO pin connected to MQ7 sensor (digital output)
buzzer_pin = 16   # GPIO pin connected to buzzer

# Set pin modes
gpio.setup(mq7_pin, gpio.IN)      # MQ7 sensor as input
gpio.setup(buzzer_pin, gpio.OUT)  # Buzzer as output

# ---------------- Main Loop ----------------
try:
    print("IoT Fire Detection Started...")

    while True:
        # Read value from MQ7 sensor (1 = smoke detected, 0 = clean air)
        smoke = gpio.input(mq7_pin)

        if smoke == 1:
            # Smoke detected → turn ON buzzer and send alert
            gpio.output(buzzer_pin, gpio.HIGH)
            print("Fire/Smoke Detected")

            # Send alert status to Blynk
            blynk.virtual_write(1, 1)          # V1 → LED/Indicator ON
            blynk.virtual_write(2, "FIRE ALERT")  # V2 → Display message

        else:
            # No smoke → turn OFF buzzer and send safe status
            gpio.output(buzzer_pin, gpio.LOW)
            print("Safe Environment")

            # Update Blynk with safe status
            blynk.virtual_write(1, 0)       # V1 → LED OFF
            blynk.virtual_write(2, "Safe")  # V2 → Display message

        blynk.run()      # Handle Blynk communication
        time.sleep(1)    # Delay to avoid rapid updates

except KeyboardInterrupt:
    # Safe shutdown when program is stopped
    gpio.output(buzzer_pin, gpio.LOW)  # Turn OFF buzzer
    gpio.cleanup()                     # Reset GPIO pins
    print("Exiting...")