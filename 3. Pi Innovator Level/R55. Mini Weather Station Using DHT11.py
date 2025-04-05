"""
Components Used:
- Raspberry Pi
- DHT11 Sensor (Temperature & Humidity)
- LCD Display with I2C
- Breadboard
- Jumper Wires
"""

import time
import adafruit_dht
from RPLCD.i2c import CharLCD
import board

# Set up the DHT11 sensor (on GPIO17)
dht_device = adafruit_dht.DHT11(board.D17)

# Set up the LCD display with I2C (corrected line)
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=16, rows=2, backlight_enabled=True)

try:
    while True:
        temperature = dht_device.temperature  # Get temperature
        humidity = dht_device.humidity  # Get humidity

        if temperature is not None and humidity is not None:
            lcd.clear()
            lcd.cursor_pos = (0, 0)
            lcd.write_string(f'Temp: {temperature}C')
            lcd.cursor_pos = (1, 0)
            lcd.write_string(f'Humidity: {humidity}%')
        else:
            lcd.clear()
            lcd.cursor_pos = (0, 0)
            lcd.write_string("Sensor error!")

        time.sleep(2)
        
except KeyboardInterrupt:
    print("Program interrupted. Exiting...")
    dht_device.exit()
    lcd.clear()
