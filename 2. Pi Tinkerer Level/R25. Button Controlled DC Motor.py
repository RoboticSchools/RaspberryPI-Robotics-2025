"""
Components Used:
1. Raspberry Pi
2. DC Motor HAT
3. DC Motor
4. 3 Push Buttons
5. Breadboard
6. Jumper Wires
"""

import time
import RPi.GPIO as gpio
from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor

mh = Raspi_MotorHAT(addr=0x6f)  # Initialize Motor HAT

motor = mh.getMotor(3)  # Select motor
motor.setSpeed(150)     # Set motor speed

forward_button = 21   # GPIO pin for forward button
backward_button = 16  # GPIO pin for backward button
stop_button = 12      # GPIO pin for stop button

gpio.setmode(gpio.BCM)  # Use BCM pin numbering
gpio.setup(forward_button, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(backward_button, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(stop_button, gpio.IN, pull_up_down=gpio.PUD_UP)

try:
    while True:
        if gpio.input(forward_button) == 0:
            print("Motor Forward")
            motor.run(Raspi_MotorHAT.FORWARD)
            time.sleep(0.2)  # Debounce

        elif gpio.input(backward_button) == 0:
            print("Motor Backward")
            motor.run(Raspi_MotorHAT.BACKWARD)
            time.sleep(0.2)

        elif gpio.input(stop_button) == 0:
            print("Motor Stopped")
            motor.run(Raspi_MotorHAT.RELEASE)
            time.sleep(0.2)

        time.sleep(0.1)

except KeyboardInterrupt:
    print("Exiting...")
    motor.run(Raspi_MotorHAT.RELEASE)
    gpio.cleanup()