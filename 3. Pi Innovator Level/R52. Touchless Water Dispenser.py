"""
Components Used:
1. Raspberry Pi
2. DC Motor Hat
3. IR Sensor
4. Water Pump
5. Jumper Wires
"""

import RPi.GPIO as gpio
import time
from Raspi_MotorHAT import Raspi_MotorHAT

# ---------------- Motor HAT Setup ----------------
mh = Raspi_MotorHAT(addr=0x6f)  # Initialize Motor HAT (I2C address)

# Assign motor channel for water pump
water_pump = mh.getMotor(1)

# Set pump speed (0–255)
water_pump.setSpeed(150)

# ---------------- GPIO Setup ----------------
gpio.setmode(gpio.BCM)  # Use BCM pin numbering

ir_sensor_pin = 21  # GPIO pin connected to IR sensor

# Set IR sensor pin as input
gpio.setup(ir_sensor_pin, gpio.IN)

# ---------------- Pump Control Functions ----------------
def turn_on_water_pump():
    """Turn ON the water pump"""
    print("Water Pump ON")
    water_pump.run(Raspi_MotorHAT.FORWARD)

def turn_off_water_pump():
    """Turn OFF the water pump"""
    print("Water Pump OFF")
    water_pump.run(Raspi_MotorHAT.RELEASE)

# ---------------- Main Loop ----------------
try:
    while True:
        # Read IR sensor value
        ir_sensor_value = gpio.input(ir_sensor_pin)

        # IR Sensor Logic:
        # 0 (LOW)  → Object detected
        # 1 (HIGH) → No object

        if ir_sensor_value == 0:
            # Object detected → activate pump
            turn_on_water_pump()
            time.sleep(3)  # Keep pump ON for 3 seconds
            turn_off_water_pump()
        else:
            # No object → keep pump OFF
            turn_off_water_pump()

        time.sleep(0.1)  # Small delay to prevent rapid switching

except KeyboardInterrupt:
    # Safe exit when program is stopped
    print("Exiting...")
    turn_off_water_pump()
    gpio.cleanup()