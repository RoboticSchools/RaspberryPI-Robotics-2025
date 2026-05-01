"""
Components Used:
1. Raspberry Pi
2. MQ7 Gas Sensor
3. Buzzer
4. Jumper Wires
"""

import time
import RPi.GPIO as gpio

# ---------------- GPIO Setup ----------------
gpio.setmode(gpio.BCM)  # Use BCM pin numbering

mq7_pin = 21      # GPIO pin connected to MQ7 sensor
buzzer_pin = 16   # GPIO pin connected to buzzer

# Set pin modes
gpio.setup(mq7_pin, gpio.IN)      # MQ7 as input
gpio.setup(buzzer_pin, gpio.OUT)  # Buzzer as output

# ---------------- Main Loop ----------------
try:
    print("Smoke Detection System Started...")

    while True:
        # Read sensor value (1 = smoke detected, 0 = clean air)
        smoke_detected = gpio.input(mq7_pin)

        if smoke_detected == 1:
            # If smoke is detected → turn ON buzzer
            gpio.output(buzzer_pin, gpio.HIGH)
            print("Smoke Detected!")
        else:
            # If no smoke → turn OFF buzzer
            gpio.output(buzzer_pin, gpio.LOW)
            print("Air Clean")

        time.sleep(0.5)  # Small delay for stability

except KeyboardInterrupt:
    # Turn OFF buzzer and clean GPIO on exit
    gpio.output(buzzer_pin, gpio.LOW)
    gpio.cleanup()
    print("Exiting...")