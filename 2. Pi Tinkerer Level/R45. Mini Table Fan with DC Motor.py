"""
Components Used:
- Raspberry Pi
- Raspi Motor HAT
- DC Motor (Connected via Motor HAT)
- Servo Motor (Connected via GPIO 18)
- 3 Push Buttons (DC Motor ON, DC Motor OFF, Servo Start/Stop)
- Breadboard
- Jumper Wires
"""

import RPi.GPIO as GPIO
import time
from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor

# Initialize Motor HAT (Default I2C address 0x6F)
mh = Raspi_MotorHAT(addr=0x6f)

# Create motor objects for the DC motor
fanMotor = mh.getMotor(1)  # Motor 1 for DC motor

# Button pins (for controlling the motor and servo)
buttonOn = 17  # DC Motor ON button (GPIO 17)
buttonOff = 27  # DC Motor OFF button (GPIO 27)
servoButton = 22  # Servo start/stop button (GPIO 22)

# Initialize GPIO settings
GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonOn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buttonOff, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(servoButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Servo pin setup (PWM for servo)
servoPin = 18  # Servo motor connected to GPIO 18
GPIO.setup(servoPin, GPIO.OUT)
servo_pwm = GPIO.PWM(servoPin, 50)  # 50Hz PWM frequency

# Start PWM for servo (initial angle is 0)
servo_pwm.start(0)

# Flag to control servo movement
servoRunning = False
servoAngle = 0

# Function to move the servo motor
def move_servo():
    global servoAngle
    if servoRunning:
        for angle in range(0, 181, 5):  # Move servo from 0 to 180
            dutyCycle = 2 + (angle / 18)  # Calculate duty cycle for the angle
            servo_pwm.ChangeDutyCycle(dutyCycle)
            time.sleep(0.1)
        for angle in range(180, -1, -5):  # Move servo from 180 back to 0
            dutyCycle = 2 + (angle / 18)  # Calculate duty cycle for the angle
            servo_pwm.ChangeDutyCycle(dutyCycle)
            time.sleep(0.1)

# Main program loop
try:
    while True:
        # DC Motor Control
        if GPIO.input(buttonOn) == GPIO.LOW:  # If DC motor ON button is pressed
            fanMotor.setSpeed(255)  # Set max speed for motor
            fanMotor.run(Raspi_MotorHAT.FORWARD)  # Start the motor
            servoRunning = True  # Start servo movement
            print("DC Motor ON, Servo Start")
        
        if GPIO.input(buttonOff) == GPIO.LOW:  # If DC motor OFF button is pressed
            fanMotor.run(Raspi_MotorHAT.RELEASE)  # Stop the motor
            servoRunning = False  # Stop servo movement
            print("DC Motor OFF, Servo Stop")
        
        if GPIO.input(servoButton) == GPIO.LOW:  # If Servo Start/Stop button is pressed
            if servoRunning:
                servoRunning = False  # Stop servo
                print("Servo Stop")
            else:
                servoRunning = True  # Start servo
                print("Servo Start")

        # If servo is running, move it back and forth
        if servoRunning:
            move_servo()
        
        time.sleep(0.1)  # Delay to debounce button presses

except KeyboardInterrupt:
    print("Program terminated")

# Cleanup GPIO when exiting
GPIO.cleanup()  # Cleanup GPIO settings
print("GPIO cleanup and program exit")
