import time
from grove.adc import ADC

#TODO: calibration with water cup and empty air

adc = ADC()
channel2 = 2  # A2 is channel 2
channel3 = 3
channel4 = 4
channel5 = 5

while True:
    moisture2 = adc.read(channel2)
    moisture_percentage2 = (1 - (moisture2 / 1023)) * 100
    # print(f"Soil Moisture 1: {moisture_percentage2:.2f}%  Raw: {moisture2}")
    moisture3 = adc.read(channel3)
    moisture_percentage3 = (1 - (moisture3 / 1023)) * 100
    # print(f"Soil Moisture 2: {moisture_percentage3:.2f}%  Raw: {moisture3}")
    moisture4 = adc.read(channel4)
    moisture_percentage4 = (1 - (moisture4 / 1023)) * 100
    # print(f"Soil Moisture 3: {moisture_percentage4:.2f}%  Raw: {moisture4}")
    moisture5 = adc.read(channel5)
    moisture_percentage5 = (1 - (moisture5 / 1023)) * 100
    # print(f"Soil Moisture 4: {moisture_percentage5:.2f}%  Raw: {moisture5}")
    print(f"SM 1: {moisture_percentage2:.2f}% | SM 2: {moisture_percentage3:.2f}% | SM 3: {moisture_percentage4:.2f}% | SM 4: {moisture_percentage5:.2f}%")
    time.sleep(1)