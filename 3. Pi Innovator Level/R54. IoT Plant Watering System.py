"""
Components Used:
1. Raspberry Pi
2. DC Motor HAT
3. Soil Moisture Sensor
4. Water Pump
5. ADS1115 Module
6. Blynk Web App
7. Jumper Wires

Install Required Libraries:
pip install adafruit-circuitpython-ads1x15 --break-system-packages
pip install adafruit-blinka --break-system-packages
pip install blynk-library-python --break-system-packages
pip install numpy --break-system-packages
"""

import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from Raspi_MotorHAT import Raspi_MotorHAT
from BlynkLib import Blynk
import numpy as np
import time
import board
import busio

# ---------------- Blynk Setup ----------------
BLYNK_AUTH = 'your_blynk_auth_token'  # Replace with your Blynk auth token
blynk = Blynk(BLYNK_AUTH, server="blynk.cloud", port=80)  # Initialize Blynk

pump_state = 0  # Stores current pump state (0 = OFF, 1 = ON)

# ---------------- ADS1115 Setup ----------------
i2c = busio.I2C(board.SCL, board.SDA)  # Initialize I2C communication
ads = ADS.ADS1115(i2c)                 # Create ADS1115 object
soil_sensor = AnalogIn(ads, ADS.P0)    # Read from A0 pin (soil sensor)

# ---------------- Motor Setup ----------------
motor_hat = Raspi_MotorHAT(addr=0x6f)  # Initialize Motor HAT
water_pump = motor_hat.getMotor(1)     # Use motor channel 1 for pump
water_pump.setSpeed(150)               # Set pump speed (0–255)

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
        blynk.run()  # Handle communication with Blynk server

        # Read raw soil moisture value from ADS1115
        raw_value = soil_sensor.value

        # Convert raw value (0–32767) to percentage (0–100)
        moisture_value = int(np.interp(raw_value, [0, 32767], [0, 100]))

        print(f"Moisture: {moisture_value}%")

        # Send moisture percentage to Blynk (V0 widget)
        blynk.virtual_write(0, moisture_value)

        # Read button state from Blynk (V1 widget)
        button_value = blynk.virtual_read(1)

        # Update pump state if button data is received
        if button_value:
            pump_state = int(button_value[0])

        # Control pump based on button state
        if pump_state == 1:
            turn_on_water_pump()
        else:
            turn_off_water_pump()

        time.sleep(1)  # Delay for stability

except KeyboardInterrupt:
    # Safe shutdown on program exit
    print("Exiting...")
    turn_off_water_pump()