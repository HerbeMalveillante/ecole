import pycom
import time
from BME280 import *


def pyms():

    pycom.heartbeat(False)

    delay = 1

    while True:
        # colors in hexadecimal (0xRRGGBB)
        pycom.rgbled(0xFF0000)  # Red
        time.sleep(delay)
        pycom.rgbled(0x00FF00)  # Green
        time.sleep(delay)
        pycom.rgbled(0x0000FF)  # Blue
        time.sleep(delay)

        delay -= 0.01

bus_i2c = I2C(0)
bus_i2c.init(I2C.MASTER, baudrate = 400000)
adr = bus_i2c.scan()
print("Adresse périphérique I2C :", adr)
