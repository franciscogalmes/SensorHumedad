from machine import Pin, I2C, ADC
from ssd1306 import SSD1306_I2C
import time

# Pin configuration
sensor_pin = 0  # ADC pin for soil moisture sensor
sda_pin = 4     # SDA pin for I2C communication
scl_pin = 5     # SCL pin for I2C communication

# Initialize I2C for OLED display
i2c = I2C(sda=Pin(sda_pin), scl=Pin(scl_pin), freq=100000)
oled = SSD1306_I2C(128, 64, i2c)

# Initialize ADC for soil moisture sensor
adc = ADC(0)

def read_soil_moisture():
    # Read analog value from soil moisture sensor
    sensor_value = adc.read()

    # Map the analog value to a percentage (adjust as needed based on sensor characteristics)
    moisture_percentage = (sensor_value - 1024) / (4095 - 1024) * 100
    moisture_percentage = max(0, min(100, moisture_percentage))  # Ensure the value is between 0 and 100

    return moisture_percentage

while True:
    # Read soil moisture
    moisture = read_soil_moisture()

    # Display on OLED
    oled.fill(0)
    oled.text("Soil Moisture:", 0, 0)
    oled.text("{:.2f}%".format(moisture), 0, 20)
    oled.show()

    # Wait for a moment before the next reading
    time.sleep(5)
