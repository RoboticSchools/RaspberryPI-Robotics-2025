"""
Components Used:
- Raspberry Pi
- Joystick (2 analog axes: X-axis and Y-axis)
- ADS1115 ADC (to read joystick analog values)
- Jumper Wires
"""

import time
import busio
from adafruit_ads1x15.ads1115 import ADS1115
from adafruit_ads1x15.analog_in import AnalogIn
import board

# Setup I2C for ADS1115 (to read joystick analog values)
i2c = busio.I2C(board.SCL, board.SDA)  # Initialize I2C interface
ads = ADS1115(i2c)  # Initialize ADS1115

# Define the analog input channels for X-axis and Y-axis
x_axis_channel = AnalogIn(ads, ADS1115.P0)  # Joystick X-axis connected to A0
y_axis_channel = AnalogIn(ads, ADS1115.P1)  # Joystick Y-axis connected to A1

def read_joystick():
    """Reads the joystick values from X and Y axes."""
    x_value = x_axis_channel.value  # Read the X-axis analog value (0-65535)
    y_value = y_axis_channel.value  # Read the Y-axis analog value (0-65535)
    
    # Print the joystick values
    print(f"X-axis Value: {x_value}")
    print(f"Y-axis Value: {y_value}")
    
    return x_value, y_value

# Start reading joystick input in a loop
try:
    while True:
        read_joystick()  # Get joystick input
        time.sleep(0.1)  # Short delay for smoother operation
except KeyboardInterrupt:
    print("Exiting joystick input loop.")
