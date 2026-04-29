"""
Components Used:
1. Raspberry Pi
2. Ultrasonic Sensor (HC-SR04)
3. Servo Motor
4. Jumper Wires
"""

import numpy as np
from Raspi_PWM_Servo_Driver import PWM
import RPi.GPIO as gpio
import time

trig = 21       # trigger pin
echo = 20       # echo pin

gpio.setmode(gpio.BCM)        # use BCM numbering
gpio.setup(trig, gpio.OUT)
gpio.setup(echo, gpio.IN)

pwm = PWM(0x6F)               # init servo driver
pwm.setPWMFreq(60)            # servo frequency
channel = 0                   # servo channel

def set_servo_angle(angle):
    pulse = int(np.interp(angle, [0, 180], [150, 600]))  # angle → PWM
    pwm.setPWM(channel, 0, pulse)                        # move servo

def get_distance():
    gpio.output(trig, False)
    time.sleep(0.05)  # sensor settle

    gpio.output(trig, True)     # trigger pulse
    time.sleep(0.00001)
    gpio.output(trig, False)

    start_time = time.time()
    end_time = time.time()

    while gpio.input(echo) == 0:   # wait for HIGH
        start_time = time.time()

    while gpio.input(echo) == 1:   # wait for LOW
        end_time = time.time()

    duration = end_time - start_time
    distance = (duration * 34300) / 2  # distance in cm

    return round(distance, 2)

try:
    set_servo_angle(0)  # lid closed

    while True:
        distance = get_distance()        # read distance
        print(f"Distance: {distance} cm")

        if distance < 20:                # object detected
            set_servo_angle(90)          # open lid
            time.sleep(3)
            set_servo_angle(0)           # close lid

        time.sleep(0.5)                  # delay

except KeyboardInterrupt:
    gpio.cleanup()  # reset GPIO