from machine import Pin
import time

from BME280 import *

from machine import SD
import os
from machine import RTC


# Initialisation
bus_i2c = I2C(0)
bus_i2c.init(I2C.MASTER, baudrate=400000)
adr = bus_i2c.scan()
print("listes des adresses i2c : ", adr)
id_bme280 = bus_i2c.readfrom_mem(BME280_I2C_ADR, BME280_CHIP_ID_ADDR, 1)
print("Valeur Id BME280: ", hex(id_bme280[0]))
capteur_BME280 = BME280(BME280_I2C_ADR, bus_i2c)
capteur_BME280.Calibration_Param_Load()


sd = SD()
os.mount(sd, "/sd")

with open("/sd/info.csv", "w") as f:

    rtc = RTC()
    # Bouble Princiale
    # while True:
    for i in range(50):

        heure = rtc.now()

        temp = capteur_BME280.read_temp()
        press = capteur_BME280.read_pression()
        humi = capteur_BME280.read_humidity()
        print("Température = ", temp)
        print("Pression = ", press)
        print("Humidité = ", humi)
        print("-------------")

        f.write(
            str(heure[0])
            + ";"
            + str(heure[1])
            + ";"
            + str(heure[2])
            + ";"
            + str(heure[3])
            + ";"
            + str(heure[4])
            + ";"
            + str(heure[5])
            + ";"
            + str(temp)
            + ";"
            + str(humi)
            + ";"
            + str(press)
            + "\r\n"
        )

        time.sleep(2)
