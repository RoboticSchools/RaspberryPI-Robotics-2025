"""
Components Used:
- Raspberry Pi
- 2 LDR Sensors
- Servo Motor
- Breadboard
- Jumper Wires
"""

import time
import RPi.GPIO as gpio

# GPIO Pin configuration
servo_pin = 18
right_sensor = 16
left_sensor = 12

# GPIO setup
gpio.setmode(gpio.BCM)
gpio.setup(right_sensor, gpio.IN)
gpio.setup(left_sensor, gpio.IN)
gpio.setup(servo_pin, gpio.OUT)

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
        right_ldr = gpio.input(right_sensor)
        left_ldr = gpio.input(left_sensor)

        # LDR sensor detects light as 0 (dark as 1)
        if left_ldr == 1 and right_ldr == 0 and servo_angle < 180:
            servo_angle += 1  # Move servo right
        elif left_ldr == 0 and right_ldr == 1 and servo_angle > 0:
            servo_angle -= 1  # Move servo left

        move_servo(servo_angle)  # Update servo position

except KeyboardInterrupt:
    print("Exiting...")
    pwm.stop()
    gpio.cleanup()
