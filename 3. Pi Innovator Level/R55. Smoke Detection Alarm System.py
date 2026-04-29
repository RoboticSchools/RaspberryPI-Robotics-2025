"""
Components Used:
1. Raspberry Pi
2. MQ7 Gas Sensor (Digital Output)
3. Buzzer
4. Jumper Wires
"""

import time
import RPi.GPIO as GPIO

# ---------------- GPIO Setup ----------------
GPIO.setmode(GPIO.BCM)  # use BCM numbering

mq7_pin = 17      # MQ7 digital output
buzzer_pin = 18   # buzzer pin

GPIO.setup(mq7_pin, GPIO.IN)        # sensor input
GPIO.setup(buzzer_pin, GPIO.OUT)    # buzzer output

# ---------------- Main Loop ----------------
try:
    print("Smoke Detection System Started...")

    while True:
        smoke_detected = GPIO.input(mq7_pin)  # read sensor

        if smoke_detected == 1:
            GPIO.output(buzzer_pin, GPIO.HIGH)  # buzzer ON
            print("Smoke Detected!")
        else:
            GPIO.output(buzzer_pin, GPIO.LOW)   # buzzer OFF
            print("Air Clean")

        time.sleep(0.5)  # delay

except KeyboardInterrupt:
    GPIO.output(buzzer_pin, GPIO.LOW)  # turn OFF buzzer
    GPIO.cleanup()  # reset GPIO
    print("Exiting...")