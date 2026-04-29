"""
Components Used:
1. Raspberry Pi
2. DC Motor HAT
3. DC Motor
4. Battery Holder with 18650 Batteries
5. 2 Push Buttons (Toggle + Stop)
6. Breadboard
7. Jumper Wires
"""

import RPi.GPIO as gpio
from Raspi_MotorHAT import Raspi_MotorHAT
import time

mh = Raspi_MotorHAT(addr=0x6f)  # motor driver init

motor = mh.getMotor(3)
motor.setSpeed(150)  # speed (0–255)

direction_button = 21
stop_button = 12

gpio.setmode(gpio.BCM)
gpio.setup(direction_button, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(stop_button, gpio.IN, pull_up_down=gpio.PUD_UP)

current_direction = Raspi_MotorHAT.FORWARD
last_state = 1  # for detecting button press

try:
    while True:
        current_state = gpio.input(direction_button)

        if last_state == 1 and current_state == 0:  # press detect
            if current_direction == Raspi_MotorHAT.FORWARD:
                current_direction = Raspi_MotorHAT.BACKWARD
                print("Motor Backward")
            else:
                current_direction = Raspi_MotorHAT.FORWARD
                print("Motor Forward")

            motor.run(current_direction)
            time.sleep(0.2)  # debounce

        last_state = current_state

        if gpio.input(stop_button) == 0:  # stop anytime
            print("Motor Stopped")
            motor.run(Raspi_MotorHAT.RELEASE)
            time.sleep(0.2)

        time.sleep(0.05)

except KeyboardInterrupt:
    motor.run(Raspi_MotorHAT.RELEASE)
    gpio.cleanup()