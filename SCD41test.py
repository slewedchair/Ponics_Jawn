import time
import board
import busio
from adafruit_scd4x import SCD4X

#TODO: calibration

def main():
    # Initialize I2C bus
    i2c = busio.I2C(board.SCL, board.SDA)

    # Initialize the SCD4X sensor
    scd4x = SCD4X(i2c)
    scd4x.start_periodic_measurement()
    print("Waiting for first measurement....")

    while True:
        if scd4x.data_ready:
            co2 = scd4x.CO2
            temperature = scd4x.temperature
            humidity = scd4x.relative_humidity

            print(f"CO2: {co2} ppm")
            print(f"Temperature: {temperature:.2f} C")
            print(f"Humidity: {humidity:.2f} %")
            print()

            time.sleep(1)
        else:
            print("Data not ready, waiting...")
            time.sleep(1)

if __name__ == '__main__':
    main()