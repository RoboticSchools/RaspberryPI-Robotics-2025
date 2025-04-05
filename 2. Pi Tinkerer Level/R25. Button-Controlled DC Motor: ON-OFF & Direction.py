"""
Components Used:
- Raspberry Pi
- Pi DC Motor HAT
- DC Motor
- 3 Push Buttons (Forward, Backward, Stop)
- Breadboard
- Jumper Wires
"""

import time
import RPi.GPIO as gpio
from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor

# Initialize Motor HAT (Default I2C address 0x6F)
mh = Raspi_MotorHAT(addr=0x6f)

# Select Motor 3
motor = mh.getMotor(3)
motor.setSpeed(150)  # Set speed

# GPIO pin configuration for buttons
forward_button = 21
backward_button = 16
stop_button = 12

# Set up GPIO
gpio.setmode(gpio.BCM)
gpio.setup(forward_button, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(backward_button, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(stop_button, gpio.IN, pull_up_down=gpio.PUD_UP)

try:
    while True:
        if gpio.input(forward_button) == 0: # Forward Button pressed
            print("Motor Forward")
            motor.run(Raspi_MotorHAT.FORWARD)

        elif gpio.input(backward_button) == 0: # Backward Button pressed
            print("Motor Backward")
            motor.run(Raspi_MotorHAT.BACKWARD)

        elif gpio.input(stop_button) == 0: # Stop Button pressed
            print("Motor Stopped")
            motor.run(Raspi_MotorHAT.RELEASE)

        time.sleep(0.1)  # Small delay to prevent button bounce

except KeyboardInterrupt:
    print("Exiting...")
    motor.run(Raspi_MotorHAT.RELEASE)
    gpio.cleanup()

