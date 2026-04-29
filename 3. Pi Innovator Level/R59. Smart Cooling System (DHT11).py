"""
Components Used:
1. Raspberry Pi
2. DHT11 Sensor (Temperature & Humidity)
3. DC Motor HAT
4. DC Motor (Fan)
5. Jumper Wires
"""

import time
import adafruit_dht
import RPi.GPIO as GPIO
from Raspi_MotorHAT import Raspi_MotorHAT

# ---------------- GPIO Setup ----------------
GPIO.setmode(GPIO.BCM)

dht_pin = 17  # DHT11 data pin

# ---------------- Sensor Setup ----------------
dht_sensor = adafruit_dht.DHT11(dht_pin)

# ---------------- Motor Setup ----------------
motor_hat = Raspi_MotorHAT(addr=0x6f)
fan_motor = motor_hat.getMotor(1)  # fan motor

fan_motor.setSpeed(150)  # set speed

# ---------------- Main Loop ----------------
try:
    while True:
        temperature = dht_sensor.temperature  # read temperature

        if temperature is None:
            print("Sensor error, retrying...")
            time.sleep(1)
            continue

        print(f"Temperature: {temperature}°C")

        if temperature > 27:   # high temperature
            fan_motor.run(Raspi_MotorHAT.FORWARD)
            print("Fan ON - High Temperature")
        else:
            fan_motor.run(Raspi_MotorHAT.RELEASE)
            print("Fan OFF - Temperature Normal")

        time.sleep(1)

except KeyboardInterrupt:
    print("Exiting...")
    fan_motor.run(Raspi_MotorHAT.RELEASE)
    GPIO.cleanup()