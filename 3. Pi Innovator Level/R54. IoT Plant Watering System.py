"""
Components Used:
1. Raspberry Pi
2. DC Motor HAT
3. Soil Moisture Sensor
4. Water Pump
5. ADS1115 Module
6. Blynk Web App
7. Jumper Wires
"""

import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from Raspi_MotorHAT import Raspi_MotorHAT
from BlynkLib import Blynk
import time
import board
import busio

# ---------------- Blynk Setup ----------------
BLYNK_AUTH_TOKEN = 'your_blynk_auth_token'  # add your token
blynk = Blynk(BLYNK_AUTH_TOKEN)

# ---------------- ADS1115 Setup ----------------
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
soil_sensor = AnalogIn(ads, ADS.P0)  # moisture channel

# ---------------- Motor Setup (Pump) ----------------
motor_hat = Raspi_MotorHAT(addr=0x6f)
water_pump = motor_hat.getMotor(1)
water_pump.setSpeed(150)

# ---------------- Pump Control ----------------
def turn_on_water_pump():
    print("Water Pump ON")
    water_pump.run(Raspi_MotorHAT.FORWARD)

def turn_off_water_pump():
    print("Water Pump OFF")
    water_pump.run(Raspi_MotorHAT.RELEASE)

# ---------------- Blynk Control ----------------
@blynk.on("V1")  # manual control from app
def control_pump(value):
    if int(value[0]) == 1:
        turn_on_water_pump()
    else:
        turn_off_water_pump()

# ---------------- Main Loop ----------------
try:
    while True:
        moisture_value = soil_sensor.value  # read soil moisture
        print(f"Soil Moisture Value: {moisture_value}")

        # automatic watering logic
        if moisture_value < 2000:
            print("Soil is dry → Watering")
            turn_on_water_pump()
            time.sleep(3)
            turn_off_water_pump()
        else:
            print("Soil is moist → No watering")

        blynk.run()   # handle Blynk events
        time.sleep(1) # delay

except KeyboardInterrupt:
    print("Exiting...")
    turn_off_water_pump()