"""
Components Used:
1. Raspberry Pi
2. MQ7 Gas Sensor (Digital Output)
3. Buzzer
4. Blynk App
5. Jumper Wires
"""

import time
import RPi.GPIO as GPIO
from BlynkLib import Blynk

# Blynk setup
BLYNK_AUTH = "YOUR_BLYNK_AUTH_TOKEN"  # auth token
blynk = Blynk(BLYNK_AUTH)  # init Blynk

# GPIO setup
GPIO.setmode(GPIO.BCM)  # BCM mode

mq7_pin = 17      # MQ7 pin
buzzer_pin = 18   # buzzer pin

GPIO.setup(mq7_pin, GPIO.IN)        # sensor input
GPIO.setup(buzzer_pin, GPIO.OUT)    # buzzer output

# main loop
try:
    print("IoT Fire Detection Started...")

    while True:
        smoke = GPIO.input(mq7_pin)  # read sensor

        if smoke == 1:
            GPIO.output(buzzer_pin, GPIO.HIGH)  # buzzer ON
            print("Fire/Smoke Detected")

            blynk.virtual_write(1, 1)  # alert ON
            blynk.virtual_write(2, "FIRE ALERT")  # message

        else:
            GPIO.output(buzzer_pin, GPIO.LOW)  # buzzer OFF
            print("Safe Environment")

            blynk.virtual_write(1, 0)  # alert OFF
            blynk.virtual_write(2, "Safe")  # message

        blynk.run()  # handle Blynk
        time.sleep(1)  # delay

except KeyboardInterrupt:
    GPIO.output(buzzer_pin, GPIO.LOW)  # buzzer OFF
    GPIO.cleanup()  # reset GPIO
    print("Exiting...")