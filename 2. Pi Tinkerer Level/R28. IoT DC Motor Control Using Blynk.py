"""
Components Used:
1. Raspberry Pi
2. DC Motor HAT
3. DC Motor
4. Battery Holder with 18650 Batteries
5. Blynk App

Install Required Library:
pip install blynklib --break-system-packages
"""

from BlynkLib import Blynk
from Raspi_MotorHAT import Raspi_MotorHAT
import time

BLYNK_AUTH = "YOUR_BLYNK_AUTH_TOKEN"  # Enter your Blynk auth token

mh = Raspi_MotorHAT(addr=0x6f)  # Initialize Motor HAT

motor = mh.getMotor(3)  # Select motor (port 3)
motor.setSpeed(150)     # Set motor speed (0–255)

blynk = Blynk(BLYNK_AUTH)  # Connect to Blynk server

def move_forward():
    motor.run(Raspi_MotorHAT.FORWARD)  # Rotate motor forward
    print("Motor Forward")

def move_backward():
    motor.run(Raspi_MotorHAT.BACKWARD)  # Rotate motor backward
    print("Motor Backward")

def stop_motor():
    motor.run(Raspi_MotorHAT.RELEASE)  # Stop motor
    print("Motor Stopped")

# Called when Forward button (V1) is pressed/released
@blynk.on("V1")
def forward_handler(value):
    if int(value[0]) == 1:   # Button pressed
        move_forward()
    else:                    # Button released
        stop_motor()

# Called when Backward button (V2) is pressed/released
@blynk.on("V2")
def backward_handler(value):
    if int(value[0]) == 1:
        move_backward()
    else:
        stop_motor()

try:
    print("Waiting for Blynk control...")  # Status message
    while True:
        blynk.run()        # Handle Blynk communication
        time.sleep(0.05)   # Small delay for stability

except KeyboardInterrupt:
    print("Exiting...")
    stop_motor()  # Ensure motor stops on exit