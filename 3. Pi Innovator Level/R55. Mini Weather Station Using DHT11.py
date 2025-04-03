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

# Set up the LCD display with I2C
lcd = CharLCD('PCF8574', 0x27, auto_linebreaks=True, columns=16, rows=2)

try:
    while True:
        try:
            temperature = dht_device.temperature  # Get temperature
            humidity = dht_device.humidity  # Get humidity
            
            if temperature is not None and humidity is not None:
                # Display on LCD
                lcd.clear()
                lcd.write_string(f'Temp: {temperature}C')
                lcd.crlf()
                lcd.write_string(f'Humidity: {humidity}%')
            else:
                # Display error message on LCD
                lcd.clear()
                lcd.write_string("Sensor error!")
        except Exception as e:
            lcd.clear()
            lcd.write_string(f"Error: {e}")
        
        time.sleep(2)  # Delay for 2 seconds before next reading

except KeyboardInterrupt:
    print("Program interrupted. Exiting...")
    dht_device.exit()  # Cleanup DHT device
    lcd.clear()
