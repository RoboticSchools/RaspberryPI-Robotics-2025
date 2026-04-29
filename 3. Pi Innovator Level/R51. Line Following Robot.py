"""
Components Used:
1. Raspberry Pi
2. DC Motor HAT
3. 2 IR Sensors (Left and Right)
4. Robot Car (4 DC Motors)
5. Breadboard
6. Jumper Wires
"""

import RPi.GPIO as GPIO
from Raspi_MotorHAT import Raspi_MotorHAT
import time

# ---------------- GPIO Setup ----------------
GPIO.setmode(GPIO.BCM)

left_sensor_pin = 21   # left IR sensor
right_sensor_pin = 20  # right IR sensor

# ---------------- Motor Setup ----------------
mh = Raspi_MotorHAT(addr=0x6f)

right_front_motor = mh.getMotor(1)
right_back_motor  = mh.getMotor(2)
left_front_motor  = mh.getMotor(3)
left_back_motor   = mh.getMotor(4)

speed = 150  # motor speed

for motor in (right_front_motor, right_back_motor, left_front_motor, left_back_motor):
    motor.setSpeed(speed)

# ---------------- Sensor Setup ----------------
GPIO.setup(left_sensor_pin, GPIO.IN)
GPIO.setup(right_sensor_pin, GPIO.IN)

# ---------------- Movement Functions ----------------
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

# ---------------- Main Loop ----------------
try:
    while True:
        left_sensor = GPIO.input(left_sensor_pin)    # read left sensor
        right_sensor = GPIO.input(right_sensor_pin)  # read right sensor

        if left_sensor == GPIO.HIGH and right_sensor == GPIO.LOW:
            turn_right()      # left off line → turn right

        elif left_sensor == GPIO.LOW and right_sensor == GPIO.HIGH:
            turn_left()       # right off line → turn left

        elif left_sensor == GPIO.LOW and right_sensor == GPIO.LOW:
            move_forward()    # both on line → forward

        else:
            stop_motors()     # both off line → stop

        time.sleep(0.1)

except KeyboardInterrupt:
    print("Exiting...")
    stop_motors()
    GPIO.cleanup()