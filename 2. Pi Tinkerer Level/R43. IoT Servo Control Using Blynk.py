"""
Components Used:
1. Raspberry Pi
2. DC Motor HAT
3. Servo Motor
4. Blynk Web App
5. Jumper Wires

Install Required Library:
pip install blynklib numpy --break-system-packages
"""

from Raspi_PWM_Servo_Driver import PWM
from BlynkLib import Blynk
import numpy as np
import time

BLYNK_AUTH = "YOUR_BLYNK_AUTH_TOKEN"  # add your token

blynk = Blynk(BLYNK_AUTH)  # init Blynk

pwm = PWM(0x6F)     # init driver
pwm.setPWMFreq(60)  # servo frequency

channel = 0  # servo channel

# map angle (0–180) → PWM (150–600)
def angle_to_pwm(angle):
    return int(np.interp(angle, [0, 180], [150, 600]))

# receive slider value from Blynk (V1)
@blynk.on("V1")
def control_servo(value):
    angle = int(value[0])  # get slider value

    if 0 <= angle <= 180:
        pwm.setPWM(channel, 0, angle_to_pwm(angle))  # move servo
        print(f"Servo: {angle}°")

@blynk.on("connected")
def connected():
    print("Blynk Connected")

try:
    while True:
        blynk.run()        # handle Blynk events
        time.sleep(0.05)

except KeyboardInterrupt:
    pass