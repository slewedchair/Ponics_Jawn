import seeed_ds18b20
from grove.gpio import GPIO
import time

def main():
    DS18B20 = seeed_ds18b20.grove_ds18b20()
    print("Please use Ctrl C to quit")
    while True:
        temp_c,temp_f = DS18B20.read_temp
        print(f"Water temp (Celsius: {temp_c:.2f} | Fahrenheit: {temp_f:.2f})")
        time.sleep(1)

if __name__ == "__main__":
    main()   