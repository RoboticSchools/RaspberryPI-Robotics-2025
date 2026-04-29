"""
Components Used:
1. Raspberry Pi
2. DC Motor HAT
3. 2 LDR Sensors (Left & Right)
4. Robot Car (4 DC Motors)
5. Battery Holder with 18650 Batteries
6. Jumper Wires
"""

import RPi.GPIO as gpio
from Raspi_MotorHAT import Raspi_MotorHAT
import time

mh = Raspi_MotorHAT(addr=0x6f)  # Initialize Motor HAT

# Motor connections
right_front_motor = mh.getMotor(1)
right_back_motor = mh.getMotor(2)
left_front_motor = mh.getMotor(3)
left_back_motor = mh.getMotor(4)

speed = 150  # Motor speed

# Set speed
right_front_motor.setSpeed(speed)
right_back_motor.setSpeed(speed)
left_front_motor.setSpeed(speed)
left_back_motor.setSpeed(speed)

gpio.setmode(gpio.BCM)  # Use BCM numbering

left_sensor_pin = 17   # Left LDR pin
right_sensor_pin = 18  # Right LDR pin

gpio.setup(left_sensor_pin, gpio.IN)   # Set left sensor
gpio.setup(right_sensor_pin, gpio.IN)  # Set right sensor

def move_forward():
    right_front_motor.run(Raspi_MotorHAT.FORWARD)
    right_back_motor.run(Raspi_MotorHAT.FORWARD)
    left_front_motor.run(Raspi_MotorHAT.FORWARD)
    left_back_motor.run(Raspi_MotorHAT.FORWARD)
    print("Forward")

def turn_left():
    right_front_motor.run(Raspi_MotorHAT.FORWARD)
    right_back_motor.run(Raspi_MotorHAT.FORWARD)
    left_front_motor.run(Raspi_MotorHAT.BACKWARD)
    left_back_motor.run(Raspi_MotorHAT.BACKWARD)
    print("Left")

def turn_right():
    right_front_motor.run(Raspi_MotorHAT.BACKWARD)
    right_back_motor.run(Raspi_MotorHAT.BACKWARD)
    left_front_motor.run(Raspi_MotorHAT.FORWARD)
    left_back_motor.run(Raspi_MotorHAT.FORWARD)
    print("Right")

def stop_motors():
    right_front_motor.run(Raspi_MotorHAT.RELEASE)
    right_back_motor.run(Raspi_MotorHAT.RELEASE)
    left_front_motor.run(Raspi_MotorHAT.RELEASE)
    left_back_motor.run(Raspi_MotorHAT.RELEASE)
    print("Stop")

try:
    while True:
        left_sensor = gpio.input(left_sensor_pin)    # Read left sensor
        right_sensor = gpio.input(right_sensor_pin)  # Read right sensor

        if left_sensor == 0 and right_sensor == 0:
            move_forward()

        elif left_sensor == 0 and right_sensor == 1:
            turn_left()

        elif left_sensor == 1 and right_sensor == 0:
            turn_right()

        else:
            stop_motors()

        time.sleep(0.1)

except KeyboardInterrupt:
    print("Exiting...")
    stop_motors()
    gpio.cleanup()  # Reset GPIO