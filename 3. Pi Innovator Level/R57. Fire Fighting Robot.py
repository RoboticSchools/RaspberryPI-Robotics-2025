"""
Components Used:
1. Raspberry Pi
2. MQ7 Gas Sensor
3. DC Motor HAT (Robot Car)
4. Water Pump (Motor)
5. Buzzer
6. Jumper Wires
"""

import time
import RPi.GPIO as GPIO
from Raspi_MotorHAT import Raspi_MotorHAT

# ---------------- GPIO Setup ----------------
GPIO.setmode(GPIO.BCM)  # BCM mode

mq7_pin = 17        # gas sensor
buzzer_pin = 18     # buzzer

GPIO.setup(mq7_pin, GPIO.IN)        # sensor input
GPIO.setup(buzzer_pin, GPIO.OUT)    # buzzer output

# ---------------- Motor Setup ----------------
mh = Raspi_MotorHAT(addr=0x6f)

right_front = mh.getMotor(1)
right_back  = mh.getMotor(2)
left_front  = mh.getMotor(3)
left_back   = mh.getMotor(4)

pump = mh.getMotor(1)  # use another port if available

speed = 150

for m in (right_front, right_back, left_front, left_back, pump):
    m.setSpeed(speed)

# ---------------- Movement Functions ----------------
def move_forward():
    right_front.run(Raspi_MotorHAT.FORWARD)
    right_back.run(Raspi_MotorHAT.FORWARD)
    left_front.run(Raspi_MotorHAT.FORWARD)
    left_back.run(Raspi_MotorHAT.FORWARD)

def stop_robot():
    right_front.run(Raspi_MotorHAT.RELEASE)
    right_back.run(Raspi_MotorHAT.RELEASE)
    left_front.run(Raspi_MotorHAT.RELEASE)
    left_back.run(Raspi_MotorHAT.RELEASE)

def start_pump():
    pump.run(Raspi_MotorHAT.FORWARD)  # pump ON

def stop_pump():
    pump.run(Raspi_MotorHAT.RELEASE)  # pump OFF

# ---------------- Main Loop ----------------
try:
    print("Fire Fighting Robot Started...")

    while True:
        smoke = GPIO.input(mq7_pin)  # read sensor

        if smoke == 1:
            print("Fire Detected")

            GPIO.output(buzzer_pin, GPIO.HIGH)  # buzzer ON

            move_forward()  # move towards fire
            time.sleep(2)

            stop_robot()  # stop near fire

            start_pump()  # spray water
            time.sleep(5)

            stop_pump()  # stop spraying
            GPIO.output(buzzer_pin, GPIO.LOW)  # buzzer OFF

        else:
            print("Searching...")

            move_forward()  # keep moving
            GPIO.output(buzzer_pin, GPIO.LOW)

        time.sleep(1)

except KeyboardInterrupt:
    stop_robot()
    stop_pump()
    GPIO.output(buzzer_pin, GPIO.LOW)
    GPIO.cleanup()
    print("Exiting...")