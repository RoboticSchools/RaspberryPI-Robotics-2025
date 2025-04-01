"""
Components Used:
- Raspberry Pi
- Raspi Motor HAT
- 2 LDR Sensors (Left and Right)
- 4 DC Motors (Right Front, Right Back, Left Front, Left Back)
- Breadboard
- Jumper Wires
"""

import RPi.GPIO as GPIO
import time
from Raspi_MotorHAT import Raspi_MotorHAT

# Setup GPIO mode and pins
GPIO.setmode(GPIO.BCM)

left_sensor_pin = 17  # LDR sensor connected to GPIO 17
right_sensor_pin = 27  # LDR sensor connected to GPIO 27

# Initialize Motor HAT (Default I2C address 0x6F)
mh = Raspi_MotorHAT(addr=0x6f)

# Create motor objects for the four wheels
right_front_motor = mh.getMotor(1)
right_back_motor = mh.getMotor(2)
left_front_motor = mh.getMotor(3)
left_back_motor = mh.getMotor(4)

# Set motors speed
speed = 150
right_front_motor.setSpeed(speed)
right_back_motor.setSpeed(speed)
left_front_motor.setSpeed(speed)
left_back_motor.setSpeed(speed)

# Set up the LDR sensor pins
GPIO.setup(left_sensor_pin, GPIO.IN)
GPIO.setup(right_sensor_pin, GPIO.IN)

def move_forward():
    print("Moving Forward")
    right_front_motor.run(Raspi_MotorHAT.FORWARD)
    right_back_motor.run(Raspi_MotorHAT.FORWARD)
    left_front_motor.run(Raspi_MotorHAT.FORWARD)
    left_back_motor.run(Raspi_MotorHAT.FORWARD)

def move_backward():
    print("Moving Backward")
    right_front_motor.run(Raspi_MotorHAT.BACKWARD)
    right_back_motor.run(Raspi_MotorHAT.BACKWARD)
    left_front_motor.run(Raspi_MotorHAT.BACKWARD)
    left_back_motor.run(Raspi_MotorHAT.BACKWARD)

def turn_left():
    print("Turning Left")
    right_front_motor.run(Raspi_MotorHAT.FORWARD)
    right_back_motor.run(Raspi_MotorHAT.FORWARD)
    left_front_motor.run(Raspi_MotorHAT.BACKWARD)
    left_back_motor.run(Raspi_MotorHAT.BACKWARD)

def turn_right():
    print("Turning Right")
    right_front_motor.run(Raspi_MotorHAT.BACKWARD)
    right_back_motor.run(Raspi_MotorHAT.BACKWARD)
    left_front_motor.run(Raspi_MotorHAT.FORWARD)
    left_back_motor.run(Raspi_MotorHAT.FORWARD)

def stop_motors():
    print("Stopping Motors")
    right_front_motor.run(Raspi_MotorHAT.RELEASE)
    right_back_motor.run(Raspi_MotorHAT.RELEASE)
    left_front_motor.run(Raspi_MotorHAT.RELEASE)
    left_back_motor.run(Raspi_MotorHAT.RELEASE)

try:
    while True:
        # Read the sensor values
        left_sensor = GPIO.input(left_sensor_pin)
        right_sensor = GPIO.input(right_sensor_pin)

        if left_sensor == GPIO.HIGH and right_sensor == GPIO.LOW:
            # Move right if the left sensor detects more light
            turn_right()
        elif left_sensor == GPIO.LOW and right_sensor == GPIO.HIGH:
            # Move left if the right sensor detects more light
            turn_left()
        elif left_sensor == GPIO.HIGH and right_sensor == GPIO.HIGH:
            # Move forward if both sensors detect light
            move_forward()
        else:
            # Stop the motors if no light is detected
            stop_motors()

        time.sleep(0.1)  # Small delay for smooth operation

except KeyboardInterrupt:
    print("Exiting...")
    stop_motors()
    GPIO.cleanup()  # Clean up GPIO settings
