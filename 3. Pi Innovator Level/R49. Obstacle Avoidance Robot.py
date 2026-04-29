"""
Components Used:
1. Raspberry Pi
2. Ultrasonic Sensor (HC-SR04)
3. DC Motor HAT
4. Robot Car (4 DC Motors)
"""

import time
import RPi.GPIO as gpio
from Raspi_MotorHAT import Raspi_MotorHAT

# ---------------- Ultrasonic Sensor Setup ----------------
trigger_pin = 21   # GPIO for trigger
echo_pin = 20      # GPIO for echo

gpio.setmode(gpio.BCM)          # use BCM pin numbering
gpio.setup(trigger_pin, gpio.OUT)
gpio.setup(echo_pin, gpio.IN)

# ---------------- Motor Setup ----------------
motor_hat = Raspi_MotorHAT(addr=0x6f)

right_front_motor = motor_hat.getMotor(1)
right_back_motor  = motor_hat.getMotor(2)
left_front_motor  = motor_hat.getMotor(3)
left_back_motor   = motor_hat.getMotor(4)

motor_speed = 140  # motor speed (0–255)

# set speed for all motors
for motor in (right_front_motor, right_back_motor, left_front_motor, left_back_motor):
    motor.setSpeed(motor_speed)

# ---------------- Distance Function ----------------
def get_distance():
    gpio.output(trigger_pin, False)
    time.sleep(0.02)  # allow sensor to settle

    # send 10µs pulse
    gpio.output(trigger_pin, True)
    time.sleep(0.00001)
    gpio.output(trigger_pin, False)

    # measure echo time
    while gpio.input(echo_pin) == 0:
        start_time = time.time()

    while gpio.input(echo_pin) == 1:
        end_time = time.time()

    # calculate distance (cm)
    duration = end_time - start_time
    distance = duration * 17150

    return round(distance, 2)

# ---------------- Motor Control Functions ----------------
def move_forward():
    right_front_motor.run(Raspi_MotorHAT.FORWARD)
    right_back_motor.run(Raspi_MotorHAT.FORWARD)
    left_front_motor.run(Raspi_MotorHAT.FORWARD)
    left_back_motor.run(Raspi_MotorHAT.FORWARD)

def move_backward():
    right_front_motor.run(Raspi_MotorHAT.BACKWARD)
    right_back_motor.run(Raspi_MotorHAT.BACKWARD)
    left_front_motor.run(Raspi_MotorHAT.BACKWARD)
    left_back_motor.run(Raspi_MotorHAT.BACKWARD)

def turn_left():
    right_front_motor.run(Raspi_MotorHAT.FORWARD)
    right_back_motor.run(Raspi_MotorHAT.FORWARD)
    left_front_motor.run(Raspi_MotorHAT.BACKWARD)
    left_back_motor.run(Raspi_MotorHAT.BACKWARD)

def stop_motors():
    right_front_motor.run(Raspi_MotorHAT.RELEASE)
    right_back_motor.run(Raspi_MotorHAT.RELEASE)
    left_front_motor.run(Raspi_MotorHAT.RELEASE)
    left_back_motor.run(Raspi_MotorHAT.RELEASE)

# ---------------- Main Loop ----------------
try:
    while True:
        distance = get_distance()   # read distance
        print(f"Distance: {distance} cm")

        if distance > 25:           # path is clear
            move_forward()

        else:                       # obstacle detected
            stop_motors()
            time.sleep(0.3)

            move_backward()
            time.sleep(0.5)

            turn_left()
            time.sleep(0.6)

            stop_motors()

        time.sleep(0.05)            # small delay

except KeyboardInterrupt:
    print("Exiting...")
    stop_motors()
    gpio.cleanup()                 # reset GPIO