"""
Components Used:
1. Raspberry Pi
2. DC Motor HAT
3. Servo Motor
4. Blynk WebApp

Install Required Library:
pip install blynk-library-python numpy --break-system-packages
"""

from Raspi_PWM_Servo_Driver import PWM
from BlynkLib import Blynk
import numpy as np
import time

BLYNK_AUTH = "YOUR_BLYNK_AUTH_TOKEN"  # add your token

blynk = Blynk(BLYNK_AUTH, server="blynk.cloud", port=80)  # init Blynk

pwm = PWM(0x6F)     # init driver
pwm.setPWMFreq(60)  # servo frequency

channel = 0  # servo channel

# receive slider value from Blynk (V1)
def control_servo(value):
    angle = int(value[0])  # get slider value

    if 0 <= angle <= 180:
        angle_to_pwm = int(np.interp(angle, [0, 180], [150, 600]))
        pwm.setPWM(channel, 0, angle_to_pwm)  # move servo
        print(f"Servo: {angle}°")

# connection status
def connected():
    print("Blynk Connected")

# link handlers
blynk.on("V1", control_servo)
blynk.on("connected", connected)

try:
    while True:
        blynk.run()        # handle Blynk events
        time.sleep(0.05)

except KeyboardInterrupt:
    pass