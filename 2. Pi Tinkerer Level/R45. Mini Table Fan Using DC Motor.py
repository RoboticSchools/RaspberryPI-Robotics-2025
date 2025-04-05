"""
Components Used:
- Raspberry Pi
- Pi DC Motor HAT
- DC Motor
- Servo Motor
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
fanMotor = mh.getMotor(1)

# Pin configuration
buttonOn = 12
buttonOff = 16
servoButton = 21

# Initialize GPIO settings
GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonOn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buttonOff, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(servoButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Servo pin setup (PWM for servo)
servoPin = 18
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
            dutyCycle = 2 + (angle / 18)
            servo_pwm.ChangeDutyCycle(dutyCycle)
            time.sleep(0.1)
        for angle in range(180, -1, -5):  # Move servo from 180 back to 0
            dutyCycle = 2 + (angle / 18)
            servo_pwm.ChangeDutyCycle(dutyCycle)
            time.sleep(0.1)

# Main program loop
try:
    while True:
        # DC Motor Control
        if GPIO.input(buttonOn) == 0:  # If DC motor ON button is pressed
            fanMotor.setSpeed(255)
            fanMotor.run(Raspi_MotorHAT.FORWARD)
            servoRunning = True
            print("DC Motor ON, Servo Start")
        
        if GPIO.input(buttonOff) == 0:  # If DC motor OFF button is pressed
            fanMotor.run(Raspi_MotorHAT.RELEASE)
            servoRunning = False 
            print("DC Motor OFF, Servo Stop")
        
        if GPIO.input(servoButton) == 0:  # If Servo Start/Stop button is pressed
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
    GPIO.cleanup()  # Cleanup GPIO settings
