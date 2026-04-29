"""
Components Used:
1. Raspberry Pi
2. DC Motor HAT
3. Servo Motor
4. Jumper Wires
"""

from Raspi_PWM_Servo_Driver import PWM
import numpy as np

pwm = PWM(0x6F)     # init driver
pwm.setPWMFreq(60)  # servo frequency

channel = 0

def angle_to_pwm(angle):
    return int(np.interp(angle, [0, 180], [150, 600]))  # map angle

try:
    while True:
        angle = int(input("Enter angle (0-180): "))

        if 0 <= angle <= 180:
            pwm.setPWM(channel, 0, angle_to_pwm(angle))  # move servo
        else:
            print("Invalid angle")

except KeyboardInterrupt:
    pass