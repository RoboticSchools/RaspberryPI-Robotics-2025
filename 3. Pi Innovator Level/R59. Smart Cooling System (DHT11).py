"""
Components Used:
1. Raspberry Pi
2. DHT11 Sensor (Temperature & Humidity)
3. DC Motor HAT
4. DC Motor (Fan)
5. Jumper Wires
6. Battery Holder with 18650 Batteries

Install Required Libraries:
pip3 install adafruit-circuitpython-dht adafruit-blinka --break-system-packages
"""

import adafruit_dht
import RPi.GPIO as gpio
from Raspi_MotorHAT import Raspi_MotorHAT
import time
import board

# ---------------- GPIO Setup ----------------
gpio.setmode(gpio.BCM)  # Use BCM pin numbering

# ---------------- Sensor Setup ----------------
dht_sensor = adafruit_dht.DHT11(board.D17)  # DHT11 connected to GPIO17

# ---------------- Motor Setup ----------------
motor_hat = Raspi_MotorHAT(addr=0x6f)  # Initialize Motor HAT (I2C)
fan_motor = motor_hat.getMotor(1)      # Use motor port 1 for fan

fan_motor.setSpeed(150)  # Set motor speed (0–255)

# ---------------- Main Loop ----------------
try:
    while True:
        try:
            # Read temperature from DHT11
            temperature = dht_sensor.temperature

            # If sensor reading fails, retry
            if temperature is None:
                print("Sensor error, retrying...")
                time.sleep(1)
                continue

            # Print temperature to terminal
            print(f"Temperature: {temperature} C")

            # If temperature is high → turn ON fan
            if temperature > 27:
                fan_motor.run(Raspi_MotorHAT.FORWARD)
                print("Fan ON - High Temperature")
            else:
                # If temperature is normal → turn OFF fan
                fan_motor.run(Raspi_MotorHAT.RELEASE)
                print("Fan OFF - Temperature Normal")

        except RuntimeError as error:
            # Handle common DHT sensor timing errors
            print("Read error:", error)

        time.sleep(1)  # Delay before next reading

except KeyboardInterrupt:
    # Clean exit when program is stopped
    print("Exiting...")
    fan_motor.run(Raspi_MotorHAT.RELEASE)  # Stop motor
    gpio.cleanup()  # Reset GPIO pins