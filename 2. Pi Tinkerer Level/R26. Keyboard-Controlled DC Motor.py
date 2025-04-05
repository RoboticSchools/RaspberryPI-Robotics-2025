"""
Components Used:
- Raspberry Pi
- Pi DC Motor HAT
- DC Motor
- Keyboard (Arrow Keys for Control)
"""

import time
from pynput import keyboard
from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor

# Initialize Motor HAT (Default I2C address 0x6F)
mh = Raspi_MotorHAT(addr=0x6f)

# Select Motor 3
motor = mh.getMotor(3)
motor.setSpeed(150)  # Set speed

def on_press(key):
    if key == keyboard.Key.up:
        print("Motor Forward")
        motor.run(Raspi_MotorHAT.FORWARD)
    elif key == keyboard.Key.down:
        print("Motor Backward")
        motor.run(Raspi_MotorHAT.BACKWARD)

def on_release(key):
    print("Motor Stopped")
    motor.run(Raspi_MotorHAT.RELEASE)
    if key == keyboard.Key.esc:
        return False  # Stop listener

# Listen for keyboard inputs
try:
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
except KeyboardInterrupt:
    print("Exiting...")
    motor.run(Raspi_MotorHAT.RELEASE)
