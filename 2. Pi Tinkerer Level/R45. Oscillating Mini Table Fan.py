"""
Components Used:
1. Raspberry Pi
2. DC Motor HAT
3. DC Motor
4. Servo Motor
5. 3 Push Buttons
6. Breadboard
7. Jumper Wires
"""

import RPi.GPIO as gpio
import time
from Raspi_MotorHAT import Raspi_MotorHAT

mh = Raspi_MotorHAT(addr=0x6f)  # Motor HAT

fanMotor = mh.getMotor(1)  # DC motor

buttonOn = 12
buttonOff = 16
servoButton = 21

gpio.setmode(gpio.BCM)
gpio.setup(buttonOn, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(buttonOff, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(servoButton, gpio.IN, pull_up_down=gpio.PUD_UP)

servoPin = 18
gpio.setup(servoPin, gpio.OUT)

servo = gpio.PWM(servoPin, 50)
servo.start(0)

servoRunning = False
servoAngle = 0
direction = 1  # 1 = forward, -1 = backward

def update_servo():
    global servoAngle, direction

    servoAngle += direction * 2

    if servoAngle >= 180:
        servoAngle = 180
        direction = -1

    elif servoAngle <= 0:
        servoAngle = 0
        direction = 1

    duty = 2 + (servoAngle / 18)
    servo.ChangeDutyCycle(duty)
    time.sleep(0.02)
    servo.ChangeDutyCycle(0)

try:
    while True:
        if gpio.input(buttonOn) == 0:
            fanMotor.setSpeed(255)
            fanMotor.run(Raspi_MotorHAT.FORWARD)
            servoRunning = True
            print("Motor ON + Servo Start")
            time.sleep(0.3)

        if gpio.input(buttonOff) == 0:
            fanMotor.run(Raspi_MotorHAT.RELEASE)
            servoRunning = False
            print("Motor OFF + Servo Stop")
            time.sleep(0.3)

        if gpio.input(servoButton) == 0:
            servoRunning = not servoRunning
            print("Servo Toggle:", "ON" if servoRunning else "OFF")
            time.sleep(0.3)

        if servoRunning:
            update_servo()

        time.sleep(0.02)

except KeyboardInterrupt:
    print("Exiting...")
    servo.stop()
    fanMotor.run(Raspi_MotorHAT.RELEASE)
    gpio.cleanup()