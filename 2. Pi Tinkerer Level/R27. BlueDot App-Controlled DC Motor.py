"""
Components Used:
- Raspberry Pi
- UGeek DC Motor HAT
- DC Motor
- BlueDot App
- Jumper Wires
"""

import time
from bluedot import BlueDot
from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor

# Initialize Motor HAT (Default I2C address 0x6F)
mh = Raspi_MotorHAT(addr=0x6f)

# Select Motor 3
motor = mh.getMotor(3)
motor.setSpeed(150)  # Set initial speed

# Initialize BlueDot
bd = BlueDot()

# Function to control motor direction
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

# Attach the functions to BlueDot events
bd.when_pressed = move
bd.when_released = stop_motor

try:
    print("Waiting for BlueDot input...")
    while True:
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Exiting...")
    motor.run(Raspi_MotorHAT.RELEASE)
