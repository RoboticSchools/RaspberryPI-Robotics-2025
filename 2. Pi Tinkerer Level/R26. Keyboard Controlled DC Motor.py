"""
Components Used:
1. Raspberry Pi
2. DC Motor HAT
3. DC Motor
4. Battery Holder with 18650 Batteries
5. Keyboard (Arrow Keys)

Install Required Library:
pip install pynput --break-system-packages
"""

from pynput import keyboard
from Raspi_MotorHAT import Raspi_MotorHAT
import time

mh = Raspi_MotorHAT(addr=0x6f)  # Initialize Motor HAT

motor = mh.getMotor(3)  # Select motor
motor.setSpeed(150)     # Set motor speed

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
        return False  # Exit program

try:
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()  # Start listening

except KeyboardInterrupt:
    print("Exiting...")
    motor.run(Raspi_MotorHAT.RELEASE)  # Stop motor