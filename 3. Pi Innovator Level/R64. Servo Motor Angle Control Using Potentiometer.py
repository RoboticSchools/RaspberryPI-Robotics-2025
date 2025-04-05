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
import board
import RPi.GPIO as GPIO
from adafruit_ads1x15.ads1115 import ADS1115
from adafruit_ads1x15.analog_in import AnalogIn

# setup GPIO pin for servo motor
servo_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

# initialize PWM on the servo pin (50Hz for servo motors)
pwm = GPIO.PWM(servo_pin, 50)
pwm.start(0)

# setup i2c and ads1115 adc for potentiometer
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS1115(i2c)
pot_channel = AnalogIn(ads, ADS1115.P0)

try:
    print("Servo control using potentiometer started...")

    # main loop to read potentiometer and control servo
    while True:
        pot_value = pot_channel.value
        angle = int((pot_value * 180) / 65535)     # map pot value to 0–180 degrees
        duty = (angle / 18) + 2                    # convert angle to duty cycle

        pwm.ChangeDutyCycle(duty)

        print(f"Servo Angle: {angle}°")
        time.sleep(0.1)

except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
    print("Servo stopped.")
