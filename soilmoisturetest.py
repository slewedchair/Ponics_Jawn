import time
from grove.adc import ADC

adc = ADC()
channel = 2  # A2 corresponds to channel 2

while True:
    moisture = adc.read(channel)
    moisture_percentage = (1 - (moisture / 1023)) * 100
    print(f"Soil Moisture: {moisture_percentage:.2f}%  Raw: {moisture}")
    time.sleep(1)