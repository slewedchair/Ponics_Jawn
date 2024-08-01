import math
import time
from grove.adc import ADC

#TODO: Calibration

class GroveTDS:

    def __init__(self, channel):
        self.channel = channel
        self.adc = ADC()

    @property
    def TDS(self):
        value = self.adc.read(self.channel)
        if value != 0:
            voltage = value * 5 / 1024.0
            tdsValue = (133.42 * voltage ** 3 - 255.86 * voltage ** 2 + 857.39 * voltage) * 0.5
            return tdsValue
        else:
            return 0

Grove = GroveTDS

def main():
    sensor = GroveTDS(0)  # Automatically use channel 0 (A0)
    print('Detecting TDS...')

    while True:
        print('TDS Value: {0}'.format(sensor.TDS))
        time.sleep(1)

if __name__ == '__main__':
    main()
