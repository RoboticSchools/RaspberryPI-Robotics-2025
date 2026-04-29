"""
Components Used:
1. Raspberry Pi
2. IR Sensor
3. Servo Motor
4. Jumper Wires
"""

import RPi.GPIO as gpio
from Raspi_PWM_Servo_Driver import PWM
import numpy as np
import time

# ---------------- GPIO Setup ----------------
ir_sensor_pin = 21   # IR sensor output

gpio.setmode(gpio.BCM)
gpio.setup(ir_sensor_pin, gpio.IN)

# ---------------- Servo Setup (PCA9685) ----------------
pwm_driver = PWM(0x6F)     # initialize driver
pwm_driver.setPWMFreq(60)  # servo frequency

servo_channel = 0          # servo channel

# move servo using angle → PWM mapping
def set_servo_angle(angle):
    pulse = int(np.interp(angle, [0, 180], [150, 600]))
    pwm_driver.setPWM(servo_channel, 0, pulse)

# ---------------- Main Logic ----------------
try:
    set_servo_angle(0)  # door closed

    while True:
        if gpio.input(ir_sensor_pin) == 0:   # object detected
            print("Person Detected - Opening Door")

            set_servo_angle(90)             # open door
            time.sleep(5)

            print("Closing Door")
            set_servo_angle(0)              # close door

        time.sleep(0.5)  # small delay

except KeyboardInterrupt:
    print("Exiting...")
    gpio.cleanup()