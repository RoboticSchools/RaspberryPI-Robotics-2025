"""
Components Used:
- Raspberry Pi
- DHT11 Temperature Sensor
- Motor Driver (L298N / Motor HAT)
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
DHT_PIN = 17   # DHT11 sensor data pin
RED_LED = 6    # Red LED for high temperature warning
GREEN_LED = 5  # Green LED for normal temperature

# Setup LEDs
GPIO.setup(RED_LED, GPIO.OUT)
GPIO.setup(GREEN_LED, GPIO.OUT)

# Initialize DHT11 sensor
dht_device = adafruit_dht.DHT11(DHT_PIN)

# Initialize Motor HAT
mh = Raspi_MotorHAT(addr=0x6f)
fan = mh.getMotor(1)  # Fan connected to Motor Port 1

# Set fan speed
fan.setSpeed(150)

try:
    while True:
        try:
            # Read temperature from DHT11 sensor
            temperature = dht_device.temperature

            if temperature is None:
                print("Sensor error, retrying...")
                continue

            print(f"Temperature: {temperature}°C")

            if temperature > 27:
                fan.run(Raspi_MotorHAT.FORWARD)  # Turn ON fan
                GPIO.output(RED_LED, GPIO.HIGH)  # Turn ON red LED
                GPIO.output(GREEN_LED, GPIO.LOW) # Turn OFF green LED
                print("Fan ON - High Temperature!")
            else:
                fan.run(Raspi_MotorHAT.RELEASE)  # Turn OFF fan
                GPIO.output(RED_LED, GPIO.LOW)   # Turn OFF red LED
                GPIO.output(GREEN_LED, GPIO.HIGH) # Turn ON green LED
                print("Fan OFF - Temperature Normal.")

        except Exception as e:
            print(f"Error: {e}")

        time.sleep(1)  # Delay before next reading

except KeyboardInterrupt:
    print("Exiting...")
    fan.run(Raspi_MotorHAT.RELEASE)  # Stop the fan
    GPIO.cleanup()  # Clean up GPIO settings
