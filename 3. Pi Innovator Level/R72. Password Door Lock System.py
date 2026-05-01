"""
Components Used:
1. Raspberry Pi
2. 4x4 Keypad
3. Servo Motor (via PWM Driver)
4. I2C LCD Display
5. Jumper Wires

Install Required Library:
pip install RPLCD numpy --break-system-packages
"""

# Import required libraries
import time
import numpy as np
import RPi.GPIO as gpio
from RPLCD.i2c import CharLCD
from Raspi_PWM_Servo_Driver import PWM

# ---------------- LCD Setup ----------------
lcd_display = CharLCD(i2c_expander='PCF8574', address=0x27, cols=16, rows=2)

# ---------------- Keypad Layout ----------------
keypad_layout = [
    ["1","2","3","A"],
    ["4","5","6","B"],
    ["7","8","9","C"],
    ["*","0","#","D"]
]

row_pins = [5, 6, 13, 19]
column_pins = [12, 16, 20, 21]

# ---------------- GPIO Setup ----------------
gpio.setmode(gpio.BCM)

# Set rows as OUTPUT (HIGH)
for row_pin in row_pins:
    gpio.setup(row_pin, gpio.OUT)
    gpio.output(row_pin, gpio.HIGH)

# Set columns as INPUT
for column_pin in column_pins:
    gpio.setup(column_pin, gpio.IN, pull_up_down=gpio.PUD_DOWN)

# ---------------- Servo Setup (PWM Driver) ----------------
pwm_driver = PWM(0x6F)
pwm_driver.setPWMFreq(60)

servo_channel = 0

def angle_to_pwm(angle):
    return int(np.interp(angle, [0, 180], [150, 600]))

def unlock_door():
    pwm_driver.setPWM(servo_channel, 0, angle_to_pwm(90))  # Unlock
    time.sleep(3)
    pwm_driver.setPWM(servo_channel, 0, angle_to_pwm(0))   # Lock

# ---------------- Password ----------------
correct_password = "1234"
entered_password = ""

# ---------------- Display Initial ----------------
lcd_display.clear()
lcd_display.write_string("Enter Password:")

# ---------------- Read Keypad ----------------
def read_keypad():
    for row_index, row_pin in enumerate(row_pins):
        gpio.output(row_pin, gpio.LOW)

        for col_index, column_pin in enumerate(column_pins):
            if gpio.input(column_pin) == gpio.HIGH:
                time.sleep(0.2)  # debounce
                gpio.output(row_pin, gpio.HIGH)
                return keypad_layout[row_index][col_index]

        gpio.output(row_pin, gpio.HIGH)

    return None

# ---------------- Main Loop ----------------
try:
    while True:
        pressed_key = read_keypad()

        if pressed_key:
            lcd_display.clear()

            # ---- Add input ----
            if pressed_key not in ("#", "*"):
                entered_password += pressed_key
                lcd_display.write_string(entered_password)

            # ---- Submit ----
            elif pressed_key == "#":
                lcd_display.clear()

                if entered_password == correct_password:
                    lcd_display.write_string("Access Granted")
                    unlock_door()
                else:
                    lcd_display.write_string("Access Denied")

                time.sleep(2)
                entered_password = ""
                lcd_display.clear()
                lcd_display.write_string("Enter Password:")

            # ---- Clear ----
            elif pressed_key == "*":
                entered_password = ""
                lcd_display.clear()
                lcd_display.write_string("Enter Password:")

        time.sleep(0.1)

# ---------------- Cleanup ----------------
except KeyboardInterrupt:
    gpio.cleanup()
    lcd_display.clear()
    lcd_display.write_string("Stopped")
    print("Exiting...")