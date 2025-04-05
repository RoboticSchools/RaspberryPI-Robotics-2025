"""
Components Used:
- Raspberry Pi
- Pi DC Motor Hat
- IR Sensor
- Water Pump
- Jumper Wires
"""

import RPi.GPIO as GPIO
import time
from Raspi_MotorHAT import Raspi_MotorHAT

# Initialize Motor HAT (Default I2C address 0x6F)
mh = Raspi_MotorHAT(addr=0x6f)

# Create motor object for the water pump
water_pump = mh.getMotor(1)

# Set motor speed (0-255)
water_pump.setSpeed(150)

# Setup GPIO mode and pins
GPIO.setmode(GPIO.BCM)
ir_sensor_pin = 17
# Set up the IR sensor pin
GPIO.setup(ir_sensor_pin, GPIO.IN)

def turn_on_water_pump():
    print("Water Pump ON")
    water_pump.run(Raspi_MotorHAT.FORWARD)  # Turn on water pump

def turn_off_water_pump():
    print("Water Pump OFF")
    water_pump.run(Raspi_MotorHAT.RELEASE)  # Turn off water pump

try:
    while True:
        # Read the value from the IR sensor
        ir_sensor_value = GPIO.input(ir_sensor_pin)

        if ir_sensor_value == 0:
            # If IR sensor detects an object
            turn_on_water_pump()
            time.sleep(3)  # Keep the pump on for 3 seconds
            turn_off_water_pump()
        else:
            # If no object is detected, ensure the pump is off
            turn_off_water_pump()

        time.sleep(0.1)  # Small delay to avoid rapid switching

except KeyboardInterrupt:
    print("Exiting...")
    turn_off_water_pump()
    GPIO.cleanup()  # Clean up GPIO settings
