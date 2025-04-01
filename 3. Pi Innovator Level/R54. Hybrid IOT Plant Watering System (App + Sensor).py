"""
Components Used:
- Raspberry Pi
- Motor Driver (e.g., Motor HAT or L298N)
- Soil Moisture Sensor
- Water Pump
- ADS1115 ADC
- Blynk App for mobile control
- Breadboard
- Jumper Wires
"""

import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from Raspi_MotorHAT import Raspi_MotorHAT
import BlynkLib

# Blynk Authentication Token (Get this from your Blynk App)
BLYNK_AUTH_TOKEN = 'your_blynk_auth_token'

# Set up Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH_TOKEN)

# Initialize the I2C interface for ADS1115 (Soil Moisture Sensor)
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
channel = AnalogIn(ads, ADS.P0)

# Initialize Motor HAT for controlling the pump
mh = Raspi_MotorHAT(addr=0x6f)
pump = mh.getMotor(1)
pump.setSpeed(150)  # Set the speed of the water pump

# Define a threshold for soil moisture (adjust according to your sensor)
MOISTURE_THRESHOLD = 2000  # You may need to calibrate this value

# Functions to control the water pump
def turn_on_water_pump():
    print("Water Pump ON")
    pump.run(Raspi_MotorHAT.FORWARD)  # Activate water pump

def turn_off_water_pump():
    print("Water Pump OFF")
    pump.run(Raspi_MotorHAT.RELEASE)  # Turn off water pump

# Blynk Virtual Pin 1 to control pump manually from the Blynk app
@blynk.VIRTUAL_WRITE(1)
def vpin_write_handler(value):
    if value[0] == '1':  # If button is pressed on the Blynk App
        turn_on_water_pump()
    else:  # If button is released on the Blynk App
        turn_off_water_pump()

# Main loop to check soil moisture and control watering automatically
try:
    while True:
        # Read soil moisture value from the sensor
        moisture_value = channel.value
        voltage = channel.voltage
        print(f"Soil Moisture Value: {moisture_value}, Voltage: {voltage:.2f}V")

        # Automatic watering based on soil moisture (below threshold means dry)
        if moisture_value < MOISTURE_THRESHOLD:
            print("Soil is dry, activating water pump automatically.")
            turn_on_water_pump()
            time.sleep(5)  # Run the pump for 5 seconds
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
