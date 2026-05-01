"""
Components Used:
1. Raspberry Pi
2. DC Motor HAT
3. Two IR Sensors (Left and Right)
4. Robot Car (4 DC Motors)
5. Jumper Wires
"""

import RPi.GPIO as gpio
from Raspi_MotorHAT import Raspi_MotorHAT
import time

# ---------------- GPIO Setup ----------------
gpio.setmode(gpio.BCM)  # Use BCM pin numbering

left_sensor_pin = 21   # GPIO pin connected to LEFT IR sensor
right_sensor_pin = 20  # GPIO pin connected to RIGHT IR sensor

# ---------------- Motor Setup ----------------
mh = Raspi_MotorHAT(addr=0x6f)  # Initialize Motor HAT (I2C address)

# Assign motors (based on Motor HAT ports)
right_front_motor = mh.getMotor(1)
right_back_motor  = mh.getMotor(2)
left_front_motor  = mh.getMotor(3)
left_back_motor   = mh.getMotor(4)

speed = 150  # Motor speed (0–255)

# Set same speed for all motors
for motor in (right_front_motor, right_back_motor, left_front_motor, left_back_motor):
    motor.setSpeed(speed)

# ---------------- Sensor Setup ----------------
gpio.setup(left_sensor_pin, gpio.IN)   # Set left sensor as input
gpio.setup(right_sensor_pin, gpio.IN)  # Set right sensor as input

# ---------------- Movement Functions ----------------
def move_forward():
    """Move robot straight forward"""
    print("Moving Forward")
    right_front_motor.run(Raspi_MotorHAT.FORWARD)
    right_back_motor.run(Raspi_MotorHAT.FORWARD)
    left_front_motor.run(Raspi_MotorHAT.FORWARD)
    left_back_motor.run(Raspi_MotorHAT.FORWARD)

def move_backward():
    """Move robot backward"""
    print("Moving Backward")
    right_front_motor.run(Raspi_MotorHAT.BACKWARD)
    right_back_motor.run(Raspi_MotorHAT.BACKWARD)
    left_front_motor.run(Raspi_MotorHAT.BACKWARD)
    left_back_motor.run(Raspi_MotorHAT.BACKWARD)

def turn_left():
    """Turn robot left (right wheels forward, left wheels backward)"""
    print("Turning Left")
    right_front_motor.run(Raspi_MotorHAT.FORWARD)
    right_back_motor.run(Raspi_MotorHAT.FORWARD)
    left_front_motor.run(Raspi_MotorHAT.BACKWARD)
    left_back_motor.run(Raspi_MotorHAT.BACKWARD)

def turn_right():
    """Turn robot right (left wheels forward, right wheels backward)"""
    print("Turning Right")
    right_front_motor.run(Raspi_MotorHAT.BACKWARD)
    right_back_motor.run(Raspi_MotorHAT.BACKWARD)
    left_front_motor.run(Raspi_MotorHAT.FORWARD)
    left_back_motor.run(Raspi_MotorHAT.FORWARD)

def stop_motors():
    """Stop all motors"""
    print("Stopping Motors")
    right_front_motor.run(Raspi_MotorHAT.RELEASE)
    right_back_motor.run(Raspi_MotorHAT.RELEASE)
    left_front_motor.run(Raspi_MotorHAT.RELEASE)
    left_back_motor.run(Raspi_MotorHAT.RELEASE)

# ---------------- Main Loop ----------------
try:
    while True:
        # Read sensor values
        left_sensor = gpio.input(left_sensor_pin)
        right_sensor = gpio.input(right_sensor_pin)

        # Logic for line following:
        # LOW  = line detected
        # HIGH = no line

        if left_sensor == gpio.HIGH and right_sensor == gpio.LOW:
            # Left sensor off line → turn right
            turn_right()

        elif left_sensor == gpio.LOW and right_sensor == gpio.HIGH:
            # Right sensor off line → turn left
            turn_left()

        elif left_sensor == gpio.LOW and right_sensor == gpio.LOW:
            # Both sensors on line → move forward
            move_forward()

        else:
            # Both sensors off line → stop
            stop_motors()

        time.sleep(0.1)  # Small delay for stability

except KeyboardInterrupt:
    # Clean exit when program is stopped
    print("Exiting...")
    stop_motors()
    gpio.cleanup()