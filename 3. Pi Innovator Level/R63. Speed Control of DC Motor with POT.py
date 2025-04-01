"""
Components Used:
- Raspberry Pi
- Raspi Motor HAT
- DC Motor
- Potentiometer
- ADS1115 ADC (to read potentiometer analog values)
- Jumper Wires
"""
import time
import busio
from adafruit_ads1x15.ads1115 import ADS1115
from adafruit_ads1x15.analog_in import AnalogIn
from Raspi_MotorHAT import Raspi_MotorHAT
import board

# Setup I2C bus for ADS1115 (to read potentiometer)
i2c = busio.I2C(board.SCL, board.SDA)  # Initialize I2C interface
ads = ADS1115(i2c)                    # Initialize ADS1115
potentiometer_channel = AnalogIn(ads, ADS1115.P0)  # Connect potentiometer to A0

# Initialize Raspi Motor HAT
mh = Raspi_MotorHAT(addr=0x6F)
motor = mh.getMotor(1)  # Using motor 1 for control

def read_potentiometer():
    """Reads the potentiometer value and maps it to motor speed (0 to 255)."""
    pot_value = potentiometer_channel.value  # Read the potentiometer value (0-65535)
    
    # Map potentiometer value to motor speed (0 to 255)
    motor_speed = int((pot_value * 255) / 65535)
    
    return motor_speed

def control_motor_speed():
    """Control the DC motor speed based on potentiometer input."""
    while True:
        motor_speed = read_potentiometer()  # Get the motor speed from potentiometer
        motor.setSpeed(motor_speed)         # Set motor speed (0-255)
        motor.run(Raspi_MotorHAT.FORWARD)   # Run motor forward
        
        print(f"Motor Speed: {motor_speed}")  # Print the motor speed to the terminal
        
        time.sleep(0.1)  # Small delay for smooth operation

try:
    control_motor_speed()
except KeyboardInterrupt:
    motor.run(Raspi_MotorHAT.RELEASE)  # Stop the motor on keyboard interrupt
    print("Motor stopped.")
