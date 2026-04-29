"""
Components Used:
1. Raspberry Pi
2. DC Motor HAT
3. Servo Motor
4. Jumper Wires
"""

from Raspi_PWM_Servo_Driver import PWM
import time
import numpy as np  # for mapping

pwm = PWM(0x6F)          # initialize PWM driver
pwm.setPWMFreq(60)       # set frequency for servo

channel = 0              # servo channel

def angle_to_pwm(angle):
    return int(np.interp(angle, [0, 180], [150, 600]))  # map using numpy

while True:
    pwm.setPWM(channel, 0, angle_to_pwm(0))    # 0°
    time.sleep(1)

    pwm.setPWM(channel, 0, angle_to_pwm(90))   # 90°
    time.sleep(1)

    pwm.setPWM(channel, 0, angle_to_pwm(180))  # 180°
    time.sleep(1)