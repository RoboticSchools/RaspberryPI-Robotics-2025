"""
Components Used:
1. Raspberry Pi
2. Servo Motor (PCA9685)
3. Potentiometer
4. ADS1115 ADC
5. Jumper Wires
"""

import time
import board
import busio
import numpy as np
from Raspi_PWM_Servo_Driver import PWM
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# ---------------- ADS1115 Setup ----------------
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)

potentiometer = AnalogIn(ads, ADS.P0)  # potentiometer on A0

# ---------------- Servo Setup (PCA9685) ----------------
pwm_driver = PWM(0x6F)     # initialize driver
pwm_driver.setPWMFreq(60)  # servo frequency

servo_channel = 0          # servo channel

# ---------------- Main Loop ----------------
try:
    print("Servo control using potentiometer started...")

    while True:
        pot_value = potentiometer.value  # read analog value

        # map 0–65535 → 0–180 degrees
        angle = int(np.interp(pot_value, [0, 65535], [0, 180]))

        # map 0–180 → 150–600 (PWM pulse range)
        pulse = int(np.interp(angle, [0, 180], [150, 600]))

        pwm_driver.setPWM(servo_channel, 0, pulse)  # move servo

        print(f"Servo Angle: {angle}°")

        time.sleep(0.1)

except KeyboardInterrupt:
    print("Exiting...")