"""
Components Used:
1. Raspberry Pi
2. I2C LCD Display (16x2)
3. Push Button
4. Breadboard
5. Jumper Wires

Install Required Library:
pip install RPLCD smbus2 --break-system-packages
"""
from RPLCD.i2c import CharLCD
import RPi.GPIO as GPIO
import time

# GPIO setup for push button
button_pin = 21  # GPIO pin connected to button
GPIO.setmode(GPIO.BCM)  # Use BCM pin numbering
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Enable internal pull-up resistor

# Initialize LCD (change address if needed)
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, cols=16, rows=2)

try:
    while True:
        # Ask user for countdown time
        count = int(input("Enter time: "))

        # Show ready message on LCD
        lcd.clear()
        lcd.write_string("Press to Start")

        # Wait until button is pressed
        while GPIO.input(button_pin):
            pass

        time.sleep(0.3)  # Small debounce delay

        # Countdown loop
        for i in range(count, -1, -1):
            lcd.cursor_pos = (1, 0)  # Second row
            lcd.write_string(f"Time:{i:<5}")  # Display remaining time

            time.sleep(1)  # 1-second delay

            # Check if button pressed again ? Stop
            if not GPIO.input(button_pin):
                lcd.clear()
                lcd.write_string("Stopped")  # Stop message
                break

        else:
            # If countdown completes normally
            lcd.clear()
            lcd.write_string("Time Up")  # Final message

except KeyboardInterrupt:
    lcd.clear()      # Clear LCD on exit
    GPIO.cleanup()  # Reset GPIO pins
