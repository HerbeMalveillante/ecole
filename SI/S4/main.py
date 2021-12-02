# Fichier main de gestion des ressources du robot

from micropython import const
from machine import *
from DRV8833 import *
from BME280 import *
from VL6180X import *
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
    Moteur_Gauche.Cmde_moteur(SENS_ANTI_HORAIRE, vitesse - 0.2)


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

# CAPTEUR DE DISTANCE
# Variables globales pour les trois capteurs VL6180X
# tableaux de 3 cases initialisees a -1
DISTANCE = [-1, -1]
LUMINOSITE = [-1.0, -1.0]
# Nombre de capteurs VL6180X utilisés
N_VL6180X = const(2)

# Ressource GIPo de la carte WiPy3.0 affectée au contrôle
# du capteur VL6180X
VL6180X_CE_Pin = ("P3", "P5")
# Adressage I2C des capteurs VL6180X : par défaut 0x29 soit 41
VL6180X_I2C_adr_defaut = const(0x29)
VL6180X_I2C_Adr = (const(0x2A), const(0x2B))

print("Configuration des broches CE des capteurs VL6180X")
# Liste des variables Pin correspondant aux broches CE
VL6180X_GPIO_CE_Pin = []
for pin in VL6180X_CE_Pin:
    VL6180X_GPIO_CE_Pin.append(Pin(pin, mode=Pin.OUT))
    # inhiber chacun des capteurs de distances
    VL6180X_GPIO_CE_Pin[-1].value(0)
print("Fin de la configuration des broches CE des capteurs VL6180X")
print("Initialisation des capteurs de distance")
capteur_VL6180X = []
for i in range(N_VL6180X):
    VL6180X_GPIO_CE_Pin[i].value(1)
    time.sleep(0.002)
    capteur_VL6180X.append(VL6180X(VL6180X_I2C_adr_defaut, bus_i2c))
    # init nouvelle adr I2C
    capteur_VL6180X[i].Modif_Adr_I2C(
        VL6180X_GPIO_CE_Pin[i], VL6180X_I2C_Adr[i], VL6180X_I2C_adr_defaut
    )
print("Fin de l'initialisation des capteurs de distance")


# configuration de la broche dédiée au contrôle du capteur :
# VL6180X_GPIO_CE_Pin = Pin(VL6180X_CE_Pin, mode=Pin.OUT)
# VL6180X_GPIO_CE_Pin.value(1) # Activer le capteur de distance
# capteur_d_l_VL6180X = VL6180X(VL6180X_I2C_adr_defaut, bus_i2c)

date = "Date : " + str(jour[0]) + "/" + str(jour[1]) + "/" + str(jour[2])

print("L'adresse du périphérique I2C est :", adr)
print("Valeur ID BME280 :", hex(Id_BME280[0]))

while True:

    # pression et température
    jour = rtc.now()
    temps = str(jour[3]) + "h " + str(jour[4]) + "m " + str(jour[5]) + "s"
    temp = capteur_BME280.read_temp()
    humi = capteur_BME280.read_humidity()
    pres = capteur_BME280.read_pression()

    for i in range(N_VL6180X):
        DISTANCE[i] = capteur_VL6180X[i].range_mesure()
        LUMINOSITE[i] = capteur_VL6180X[i].ambiant_light_mesure()

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
    print("Distance", DISTANCE)
    print("Luminosité", LUMINOSITE)
    print("--------------")

    print(LUMINOSITE)

    nombreAlea = int(str(LUMINOSITE[0] * LUMINOSITE[1])[-1])
    print("nombreAlea", nombreAlea)

    if nombreAlea % 4 == 0:
        print("CHANGEMENT DE DIRECTION ALEATOIRE")
        direction = "gauche" if nombreAlea % 2 == 0 else "droite"
        if direction == "gauche":
            Pivoter_gauche(V_MOYEN)
            print("PIVOTER GAUCHE")
            time.sleep(2)
        else:
            Pivoter_droite(V_MOYEN)
            print("PIVOTER DROITE")
            time.sleep(2)
    else:
        if DISTANCE[0] >= 100:
            Avancer(V_MOYEN)
            print("AVANCER")
            time.sleep(1)
        else:
            print("OULALAH ON VA SE COGNER")
            direction = "gauche" if nombreAlea % 2 == 0 else "droite"
            if direction == "gauche":
                Pivoter_gauche(V_MOYEN)
                print("ON EVITE PAR LA GAUCHE")
                time.sleep(2)
            else:
                Pivoter_droite(V_MOYEN)
                print("ON EVITE PAR LA DROITE")
                time.sleep(2)
