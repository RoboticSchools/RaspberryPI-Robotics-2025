"""
Components Used:
- Raspberry Pi
- Servo Motor
- Potentiometer
- ADS1115 ADC (to read potentiometer analog values)
- Jumper Wires
"""

import time
import busio
from adafruit_ads1x15.ads1115 import ADS1115
from adafruit_ads1x15.analog_in import AnalogIn
import board
import RPi.GPIO as GPIO

# Set up the GPIO pin for the servo
servo_pin = 18  # GPIO pin 18 for Servo
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

# Set up PWM for the servo
pwm = GPIO.PWM(servo_pin, 50)  # 50Hz frequency for servo
pwm.start(0)  # Start PWM with 0% duty cycle

# Setup I2C for ADS1115 (to read potentiometer)
i2c = busio.I2C(board.SCL, board.SDA)  # Initialize I2C interface
ads = ADS1115(i2c)  # Initialize ADS1115
potentiometer_channel = AnalogIn(ads, ADS1115.P0)  # Connect potentiometer to A0

def read_potentiometer():
    """Reads the potentiometer value and maps it to servo angle (0 to 180 degrees)."""
    pot_value = potentiometer_channel.value  # Read the potentiometer value (0-65535)
    
    # Map potentiometer value to servo angle (0 to 180 degrees)
    angle = int((pot_value * 180) / 65535)
    
    return angle

def set_servo_angle(angle):
    """Sets the angle of the servo motor."""
    duty = (angle / 18) + 2  # Map angle (0 to 180) to duty cycle (2 to 12)
    pwm.ChangeDutyCycle(duty)  # Set the duty cycle to control the servo motor

def control_servo():
    """Control the servo motor angle based on potentiometer input."""
    try:
        while True:
            angle = read_potentiometer()  # Get the angle from the potentiometer
            set_servo_angle(angle)        # Set the servo angle based on potentiometer value
            
            print(f"Servo Angle: {angle}°")  # Print the servo angle to the terminal
            
            time.sleep(0.1)  # Small delay for smooth operation
    except KeyboardInterrupt:
        pwm.stop()  # Stop PWM on keyboard interrupt
        GPIO.cleanup()  # Clean up GPIO settings
        print("Servo stopped.")

# Start controlling the servo motor
control_servo()
