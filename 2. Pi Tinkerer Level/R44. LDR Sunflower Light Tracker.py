"""
Components Used:
1. Raspberry Pi
2. 2 LDR Sensors (Left & Right)
3. Servo Motor (SG90)
4. Breadboard
5. Jumper Wires
"""

import time
import RPi.GPIO as gpio

servo_pin = 18      # Servo pin
right_sensor = 16   # Right LDR
left_sensor = 12    # Left LDR

gpio.setmode(gpio.BCM)  # Use BCM numbering
gpio.setup(right_sensor, gpio.IN)
gpio.setup(left_sensor, gpio.IN)
gpio.setup(servo_pin, gpio.OUT)

pwm = gpio.PWM(servo_pin, 50)  # 50Hz for servo
pwm.start(0)

servo_angle = 90  # Start from center

def move_servo(angle):
    duty_cycle = 2 + (angle / 18)  # Convert angle
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.03)
    pwm.ChangeDutyCycle(0)  # Reduce jitter

# Initial position
move_servo(servo_angle)

try:
    while True:
        right_ldr = gpio.input(right_sensor)
        left_ldr = gpio.input(left_sensor)

        # Logic: move towards light
        if left_ldr == 1 and right_ldr == 0 and servo_angle < 180:
            servo_angle += 1  # Move right

        elif left_ldr == 0 and right_ldr == 1 and servo_angle > 0:
            servo_angle -= 1  # Move left

        move_servo(servo_angle)  # Update position
        time.sleep(0.02)  # Smooth movement

except KeyboardInterrupt:
    print("Exiting...")
    pwm.stop()
    gpio.cleanup()