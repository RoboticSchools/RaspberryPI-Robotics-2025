"""
Components Used:
1. Raspberry Pi
2. 2 LDR Sensors (Left & Right)
3. DC Motor Hat
4. Servo Motor
5. Breadboard
6. Jumper Wires
"""

import RPi.GPIO as gpio
import numpy as np
import time
from Raspi_PWM_Servo_Driver import PWM

right_sensor = 16     # right LDR
left_sensor = 12      # left LDR

gpio.setmode(gpio.BCM)
gpio.setup(right_sensor, gpio.IN)
gpio.setup(left_sensor, gpio.IN)

pwm = PWM(0x6F)       # init driver
pwm.setPWMFreq(60)    # servo frequency

channel = 0           # servo channel
servo_angle = 90      # start center

def move_servo(angle):
    pulse = int(np.interp(angle, [0, 180], [150, 600]))  # angle → PWM
    pwm.setPWM(channel, 0, pulse)

move_servo(servo_angle)  # initial position

try:
    while True:
        right_ldr = gpio.input(right_sensor)  # read right
        left_ldr = gpio.input(left_sensor)    # read left

        # move towards brighter side
        if left_ldr == 1 and right_ldr == 0 and servo_angle < 180:
            servo_angle += 1

        elif left_ldr == 0 and right_ldr == 1 and servo_angle > 0:
            servo_angle -= 1

        move_servo(servo_angle)  # update position
        time.sleep(0.02)

except KeyboardInterrupt:
    gpio.cleanup()