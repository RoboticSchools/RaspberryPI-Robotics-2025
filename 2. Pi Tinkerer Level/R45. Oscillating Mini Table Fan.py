"""
Components Used:
1. Raspberry Pi
2. DC Motor HAT
3. DC Motor
4. Servo Motor
5. Push Button
6. Breadboard
7. Jumper Wires
"""

import RPi.GPIO as gpio
from Raspi_MotorHAT import Raspi_MotorHAT
from Raspi_PWM_Servo_Driver import PWM
import numpy as np
import time

# Motor setup
motor_hat = Raspi_MotorHAT(addr=0x6f)
dc_motor = motor_hat.getMotor(1)

# Servo setup (PCA9685)
pwm_driver = PWM(0x6F)
pwm_driver.setPWMFreq(60)
servo_channel = 0

# Button setup
button_pin = 12
gpio.setmode(gpio.BCM)
gpio.setup(button_pin, gpio.IN, pull_up_down=gpio.PUD_UP)

# State variables
system_on = False
last_button_state = 1
servo_angle = 0
servo_direction = 1

# Move servo using angle → PWM mapping
def move_servo(angle):
    pulse = int(np.interp(angle, [0, 180], [150, 600]))
    pwm_driver.setPWM(servo_channel, 0, pulse)

try:
    while True:
        button_state = gpio.input(button_pin)

        # Toggle system on button press
        if last_button_state == 1 and button_state == 0:
            system_on = not system_on

            if system_on:
                dc_motor.setSpeed(255)
                dc_motor.run(Raspi_MotorHAT.FORWARD)
                print("System ON")
            else:
                dc_motor.run(Raspi_MotorHAT.RELEASE)
                print("System OFF")

            time.sleep(0.3)  # debounce

        last_button_state = button_state

        # Servo oscillation
        if system_on:
            servo_angle += servo_direction * 2

            if servo_angle >= 180 or servo_angle <= 0:
                servo_direction *= -1

            move_servo(servo_angle)

        time.sleep(0.02)

except KeyboardInterrupt:
    dc_motor.run(Raspi_MotorHAT.RELEASE)
    gpio.cleanup()