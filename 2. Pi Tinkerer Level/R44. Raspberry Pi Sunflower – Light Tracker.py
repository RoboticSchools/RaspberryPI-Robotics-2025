"""
Components Used:
- Raspberry Pi
- 2 LDR Sensors (Configured with Pull-down Resistors)
- Servo Motor
- Breadboard
- Jumper Wires
"""

import time
import RPi.GPIO as gpio

# GPIO Pin configuration
servo_pin = 18    # Servo motor connected to GPIO18 (PWM)
right_sensor = 21  # Right LDR sensor connected to GPIO21
left_sensor = 20   # Left LDR sensor connected to GPIO20

# GPIO setup
gpio.setmode(gpio.BCM)
gpio.setup(right_sensor, gpio.IN)  # Set right LDR as input
gpio.setup(left_sensor, gpio.IN)   # Set left LDR as input
gpio.setup(servo_pin, gpio.OUT)    # Set servo pin as output

# Initialize PWM for servo control
pwm = gpio.PWM(servo_pin, 50)  # 50Hz PWM frequency
pwm.start(0)

# Set initial servo angle to 90 degrees (center position)
servo_angle = 90

def move_servo(angle):
    """Move the servo motor to the given angle."""
    duty_cycle = (angle / 18) + 2.5  # Convert angle to duty cycle
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.05)

# Move servo to initial position
move_servo(servo_angle)

try:
    while True:
        right_ldr = gpio.input(right_sensor)  # Read right LDR sensor
        left_ldr = gpio.input(left_sensor)    # Read left LDR sensor

        # LDR sensor detects light as 0 (dark as 1)
        if right_ldr == 0 and left_ldr == 1 and servo_angle < 180:
            servo_angle += 1  # Move servo right
        elif left_ldr == 0 and right_ldr == 1 and servo_angle > 0:
            servo_angle -= 1  # Move servo left

        move_servo(servo_angle)  # Update servo position

except KeyboardInterrupt:
    print("Exiting...")
    pwm.stop()
    gpio.cleanup()
