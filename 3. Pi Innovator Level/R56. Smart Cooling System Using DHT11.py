"""
Components Used:
- Raspberry Pi
- DHT11 Temperature Sensor
- Pi DC Motor HAT
- DC Motor (Fan)
- Red LED (High Temperature Warning)
- Green LED (Normal Temperature Indicator)
- Jumper Wires
"""

import time
import adafruit_dht
import RPi.GPIO as GPIO
from Raspi_MotorHAT import Raspi_MotorHAT

# Setup GPIO mode
GPIO.setmode(GPIO.BCM)

# Define GPIO pins
dht_pin = 17       # DHT11 sensor data pin
red_led = 12       # Red LED for high temperature warning
green_led = 16     # Green LED for normal temperature

# Setup LEDs
GPIO.setup(red_led, GPIO.OUT)
GPIO.setup(green_led, GPIO.OUT)

# Initialize DHT11 sensor
dht_device = adafruit_dht.DHT11(dht_pin)

# Initialize Motor HAT
motor_hat = Raspi_MotorHAT(addr=0x6f)
fan = motor_hat.getMotor(1)  # Fan connected to Motor Port 1

# Set fan speed
fan.setSpeed(150)

try:
    while True:
        temperature = dht_device.temperature

        if temperature is None:
            print("Sensor error, retrying...")
            continue

        print(f"Temperature: {temperature}°C")

        if temperature > 27:
            fan.run(Raspi_MotorHAT.FORWARD)
            GPIO.output(red_led, GPIO.HIGH)
            GPIO.output(green_led, GPIO.LOW)
            print("Fan ON - High Temperature!")
        else:
            fan.run(Raspi_MotorHAT.RELEASE)
            GPIO.output(red_led, GPIO.LOW)
            GPIO.output(green_led, GPIO.HIGH)
            print("Fan OFF - Temperature Normal.")

        time.sleep(1)

except KeyboardInterrupt:
    print("Exiting...")
    fan.run(Raspi_MotorHAT.RELEASE)
    GPIO.cleanup()
