"""
Components Used:
- Raspberry Pi
- Pi DC Motor HAT
- Soil Moisture Sensor
- Water Pump
- ADS1115 ADC
- Blynk App
- Jumper Wires
"""

import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from Raspi_MotorHAT import Raspi_MotorHAT
from BlynkLib import Blynk

# Blynk Authentication Token (Get this from your Blynk App)
BLYNK_AUTH_TOKEN = 'your_blynk_auth_token'

# Set up Blynk
blynk = Blynk(BLYNK_AUTH_TOKEN)

# Initialize the I2C interface for ADS1115 (Soil Moisture Sensor)
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
channel = AnalogIn(ads, ADS.P0)

# Initialize Motor HAT for controlling the pump
mh = Raspi_MotorHAT(addr=0x6f)
pump = mh.getMotor(1)
pump.setSpeed(150)  # Set the speed of the water pump

# Functions to control the water pump
def turn_on_water_pump():
    print("Water Pump ON")
    pump.run(Raspi_MotorHAT.FORWARD)

def turn_off_water_pump():
    print("Water Pump OFF")
    pump.run(Raspi_MotorHAT.RELEASE)

# Blynk Virtual Pin 1 to control pump manually from the Blynk app
@blynk.on("V1")
def vpin_write_handler(value):
    if int(value[0]) == 1: 
        turn_on_water_pump()
    else: 
        turn_off_water_pump()

# Main loop to check soil moisture and control watering automatically
try:
    while True:
        # Read soil moisture value from the sensor
        moisture_value = channel.value
        print(f"Soil Moisture Value: {moisture_value}")

        # Automatic watering based on soil moisture (below threshold means dry)
        if moisture_value < 2000:
            print("Soil is dry, activating water pump automatically.")
            turn_on_water_pump()
            time.sleep(3)
            turn_off_water_pump()
        else:
            print("Soil moisture is sufficient, no need to water.")

        # Run the Blynk loop (for remote control from app)
        blynk.run()

        # Wait before next reading
        time.sleep(1)

except KeyboardInterrupt:
    print("Exiting...")
    turn_off_water_pump()  # Ensure pump is turned off before exit
