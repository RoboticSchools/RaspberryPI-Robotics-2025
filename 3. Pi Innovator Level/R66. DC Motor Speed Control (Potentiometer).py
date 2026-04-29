"""
Components Used:
- Raspberry Pi
- Pi DC Motor HAT
- DC Motor
- Potentiometer
- ADS1115 ADC (to read potentiometer analog values)
- Jumper Wires
"""

import time
import busio
import board
from adafruit_ads1x15.ads1115 import ADS1115
from adafruit_ads1x15.analog_in import AnalogIn
from Raspi_MotorHAT import Raspi_MotorHAT

# initialize i2c for ads1115
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS1115(i2c)
pot_channel = AnalogIn(ads, ADS1115.P0)

# initialize motor HAT and motor on port 1
mh = Raspi_MotorHAT(addr=0x6f)
motor = mh.getMotor(1)

try:
    print("DC motor speed control started...")

    # main loop to control motor speed using potentiometer
    while True:
        pot_value = pot_channel.value
        motor_speed = int((pot_value * 255) / 65535)

        motor.setSpeed(motor_speed)
        motor.run(Raspi_MotorHAT.FORWARD)

        print(f"Motor Speed: {motor_speed}")
        time.sleep(0.1)

except KeyboardInterrupt:
    motor.run(Raspi_MotorHAT.RELEASE)
    print("Motor stopped.")
