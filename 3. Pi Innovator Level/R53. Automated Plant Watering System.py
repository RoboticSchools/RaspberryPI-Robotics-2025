"""
Components Used:
- Raspberry Pi
- Pi DC Motor HAT
- Soil Moisture Sensor
- Water Pump
- ADS1115 ADC
- Breadboard
- Jumper Wires
"""

import board
import time
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from Raspi_MotorHAT import Raspi_MotorHAT

# Initialize the I2C interface for ADS1115
i2c = busio.I2C(board.SCL, board.SDA)

# Create an ADS1115 object to read analog values
ads = ADS.ADS1115(i2c)

# Define the analog input channel for the moisture sensor (connected to P0)
channel = AnalogIn(ads, ADS.P0)

# Initialize Motor HAT (Default I2C address 0x6F)
mh = Raspi_MotorHAT(addr=0x6f)

# Create motor object for the water pump
pump = mh.getMotor(1)

# Set pump speed (0-255)
pump.setSpeed(150)

def turn_on_water_pump():
    print("Water Pump ON")
    pump.run(Raspi_MotorHAT.FORWARD)  # Activate water pump

def turn_off_water_pump():
    print("Water Pump OFF")
    pump.run(Raspi_MotorHAT.RELEASE)  # Turn off water pump

try:
    while True:
        # Read the soil moisture value (analog value)
        moisture_value = channel.value

        # Print the soil moisture value
        print(f"Soil Moisture Value: {moisture_value}")

        # If soil moisture is below a threshold, turn on the water pump
        if moisture_value < 2000:  # Adjust this threshold based on your soil moisture sensor calibration
            turn_on_water_pump()
            time.sleep(3)  # Run the pump for 3 seconds
            turn_off_water_pump()

        # Wait for 1 second before the next reading
        time.sleep(1)

except KeyboardInterrupt:
    print("Exiting...")
    turn_off_water_pump()  # Ensure pump is turned off before exit
