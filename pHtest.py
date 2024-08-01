import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

#TODO: calibration

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c, address=0x08)  # Use the I2C address of your ADC

# Create single-ended input on channel 0
chan = AnalogIn(ads, ADS.P0)

while True:
    # Read the voltage
    voltage = chan.voltage
    print(f"Voltage: {voltage:.6f} V")
    time.sleep(1)