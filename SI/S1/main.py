import pycom
import time

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
