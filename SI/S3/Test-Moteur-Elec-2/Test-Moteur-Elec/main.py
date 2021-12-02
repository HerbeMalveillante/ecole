# Fichier main de gestion des ressources du robot

from micropython import const
from machine import *
from DRV8833 import *
from BME280 import *
import pycom
import time
import os

# Variables globales pour moteurs et pont en H
DRV8833_Sleep_pin = "P20"  # Pin SLEEP
DRV8833_AIN1 = "P22"  # Entrée PWM moteur A : AIN1
DRV8833_AIN2 = "P21"  # Entrée PWM moteur A : AIN2
DRV8833_BIN1 = "P19"  # Entrée PWM moteur B : BIN1
DRV8833_BIN2 = "P12"  # Entrée PWM moteur B : BIN2

# Vitesse de rotation des roues
V_MAX = 1.0
V_MOYEN = 0.5
V_MIN = 0.25
# ---------------------------------------------------------------------------
# Routines de déplacements du robot
def Avancer(vitesse):
    Moteur_Droit.Cmde_moteur(SENS_HORAIRE, vitesse)
    Moteur_Gauche.Cmde_moteur(SENS_ANTI_HORAIRE, vitesse)


def Reculer(vitesse):
    Moteur_Droit.Cmde_moteur(SENS_ANTI_HORAIRE, vitesse)
    Moteur_Gauche.Cmde_moteur(SENS_HORAIRE, vitesse)


def Pivoter_droite(vitesse):
    Moteur_Droit.Cmde_moteur(SENS_ANTI_HORAIRE, vitesse)
    Moteur_Gauche.Cmde_moteur(SENS_ANTI_HORAIRE, vitesse)


def Pivoter_gauche(vitesse):
    Moteur_Droit.Cmde_moteur(SENS_HORAIRE, vitesse)
    Moteur_Gauche.Cmde_moteur(SENS_HORAIRE, vitesse)


def Arret():
    Moteur_Droit.Cmde_moteur(SENS_HORAIRE, 0)
    Moteur_Gauche.Cmde_moteur(SENS_HORAIRE, 0)


# ------------------------------------------------------------------------
# Initialisation des moteurs
# IN1_pin : entrée PWM 1 DRV8833
# IN2_pin : entrée PWM 2 DRV8833
# sleep_pin : SLP pin pour désactiver les ponts en H du DRV8833
# timer_number : dans [0,1,2,3]. Choix du timer utilisé pour générer le signal pwm
# freq : fréquence du signal pwm
# num_channel_pwm_In1 : numéro de l'Id du canal PWM associé à la broche In1_pin
# num_channel_pwm_In2 : numéro de l'Id du canal PWM associé à la broche In2_pin
# DRV8833 (In1_pin, In2_pin, sleep_pin, timer_number, freq, num_channel_pwm_In1, num_channel_pwm_In2)

Moteur_Gauche = DRV8833(
    DRV8833_AIN1, DRV8833_AIN2, DRV8833_Sleep_pin, 1, 500, 0, 1
)  # Sur connecteur Encoder1
Moteur_Droit = DRV8833(
    DRV8833_BIN1, DRV8833_BIN2, DRV8833_Sleep_pin, 1, 500, 2, 3
)  # Sur connecteur Encoder2
Arret()

bus_i2c = I2C()
bus_i2c.init(I2C.MASTER, baudrate=400000)
adr = bus_i2c.scan()

Id_BME280 = bus_i2c.readfrom_mem(BME280_I2C_ADR, BME280_CHIP_ID_ADDR, 1)

capteur_BME280 = BME280(BME280_I2C_ADR, bus_i2c)  # --Calibrage du capteur

capteur_BME280.Calibration_Param_Load()

rtc = RTC()
rtc.init((2020, 10, 26, 0, 0, 0, 0, 0))
jour = rtc.now()

date = "Date : " + str(jour[0]) + "/" + str(jour[1]) + "/" + str(jour[2])


print("L'adresse du périphérique I2C est :", adr)
print("Valeur ID BME280 :", hex(Id_BME280[0]))
while True:
    jour = rtc.now()
    temps = str(jour[3]) + "h " + str(jour[4]) + "m " + str(jour[5]) + "s"
    temp = capteur_BME280.read_temp()
    humi = capteur_BME280.read_humidity()
    pres = capteur_BME280.read_pression()
    print("-------------------------------------------------------------------")
    print(
        "Temps passé :",
        temps,
        "- Température :",
        "%.2f" % temp,
        "- Humidité :",
        "%.2f" % humi,
        "- Préssion :",
        "%.2f" % pres,
    )

    print("--------------")
    print("-> Démarage")
    print("-Avancer")
    Avancer(V_MIN)
    time.sleep(2)
    print("-Reculer")
    Reculer(V_MIN)
    time.sleep(2)
    print("-Pivoter droite")
    Pivoter_droite(V_MIN)
    time.sleep(2)
    print("-Pivoter gauche")
    Pivoter_gauche(V_MIN)
    time.sleep(2)
    print("-> Arret")
    Arret()
    time.sleep(2)
"""
Index = 0
while True :
    print('Index : ', Index)
    # Définition d'une séquence de mouvements
    time.sleep(0.25)
    Index +=1
"""
