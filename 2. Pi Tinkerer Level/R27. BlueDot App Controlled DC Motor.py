"""
Components Used:
1. Raspberry Pi
2. DC Motor HAT
3. DC Motor
4. BlueDot App

Install Required Library:
pip install bluedot --break-system-packages
"""

import time
from bluedot import BlueDot
from Raspi_MotorHAT import Raspi_MotorHAT

mh = Raspi_MotorHAT(addr=0x6f)  # Initialize Motor HAT

motor = mh.getMotor(3)  # Select motor
motor.setSpeed(150)     # Set motor speed

bd = BlueDot()  # Create BlueDot object

def move(pos):
    if pos.top:
        print("Motor Forward")
        motor.run(Raspi_MotorHAT.FORWARD)

    elif pos.bottom:
        print("Motor Backward")
        motor.run(Raspi_MotorHAT.BACKWARD)

    else:
        print("Motor Stopped")
        motor.run(Raspi_MotorHAT.RELEASE)

def stop_motor(pos):
    print("Motor Stopped")
    motor.run(Raspi_MotorHAT.RELEASE)

bd.when_pressed = move    # Run when pressed
bd.when_released = stop_motor  # Run when released

try:
    print("Waiting for BlueDot input...")
    while True:
        time.sleep(0.1)  # Keep program running

except KeyboardInterrupt:
    print("Exiting...")
    motor.run(Raspi_MotorHAT.RELEASE)  # Stop motor