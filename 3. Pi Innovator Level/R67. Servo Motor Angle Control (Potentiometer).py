"""
Components Used:
1. Raspberry Pi
2. Servo Motor (PCA9685)
3. Potentiometer
4. ADS1115 ADC
5. Jumper Wires
6. Breadboard

Install Required Libraries:
pip3 install adafruit-circuitpython-ads1x15 adafruit-blinka numpy --break-system-packages
"""

import time
import board
import busio
import numpy as np
from Raspi_PWM_Servo_Driver import PWM
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# ---------------- ADS1115 Setup ----------------
i2c = busio.I2C(board.SCL, board.SDA)   # Initialize I2C
ads = ADS.ADS1115(i2c)                  # Create ADS1115 object

# Read potentiometer from A0
potentiometer = AnalogIn(ads, 0)

# ---------------- Servo Setup (PCA9685) ----------------
pwm_driver = PWM(0x6F)     # Initialize PCA9685 driver (I2C address)
pwm_driver.setPWMFreq(60)  # Set frequency for servo (60Hz)

servo_channel = 0          # Servo connected to channel 0

# ---------------- Main Loop ----------------
try:
    while True:
        # Read analog value from potentiometer
        pot_value = potentiometer.value

        # Map raw value (0–32767) → angle (0–180 degrees)
        angle = int(np.interp(pot_value, [0, 32767], [0, 180]))

        # Convert angle → PWM pulse (150–600 range for servo)
        pulse = int(np.interp(angle, [0, 180], [150, 600]))

        # Move servo
        pwm_driver.setPWM(servo_channel, 0, pulse)

        print(f"Servo Angle: {angle} degrees")

        time.sleep(0.1)

except KeyboardInterrupt:
    print("Exiting...")