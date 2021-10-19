# Fichier main de gestion des ressources du robot

from micropython import const
from machine import Pin
from machine import Timer
from DRV8833 import *
import time

#Variables globales pour moteurs et pont en H
DRV8833_Sleep_pin = 'P20' # Pin SLEEP
DRV8833_AIN1 = 'P22' # Entrée PWM moteur A : AIN1
DRV8833_AIN2 = 'P21' # Entrée PWM moteur A : AIN2
DRV8833_BIN1 = 'P19' # Entrée PWM moteur B : BIN1
DRV8833_BIN2 = 'P12' # Entrée PWM moteur B : BIN2

# Vitesse de rotation des roues
V_MAX = 1.0
V_MOYEN = 0.5
V_MIN = 0.25
#---------------------------------------------------------------------------
# Routines de déplacements du robot
def Avancer (vitesse) :
    Moteur_Droit.Cmde_moteur(SENS_HORAIRE, vitesse)
    Moteur_Gauche.Cmde_moteur(SENS_ANTI_HORAIRE, vitesse)
def Reculer (vitesse) :
    Moteur_Droit.Cmde_moteur(SENS_ANTI_HORAIRE, vitesse)
    Moteur_Gauche.Cmde_moteur(SENS_HORAIRE, vitesse)
def Pivoter_droite (vitesse) :
    Moteur_Droit.Cmde_moteur(SENS_ANTI_HORAIRE, vitesse)
    Moteur_Gauche.Cmde_moteur(SENS_ANTI_HORAIRE, vitesse)
def Pivoter_gauche (vitesse) :
    Moteur_Droit.Cmde_moteur(SENS_HORAIRE, vitesse)
    Moteur_Gauche.Cmde_moteur(SENS_HORAIRE, vitesse)
def Arret () :
    Moteur_Droit.Arret_moteur()
    Moteur_Gauche.Arret_moteur()
#------------------------------------------------------------------------
# Initialisation des moteurs
# IN1_pin : entrée PWM 1 DRV8833
# IN2_pin : entrée PWM 2 DRV8833
# sleep_pin : SLP pin pour désactiver les ponts en H du DRV8833
# timer_number : dans [0,1,2,3]. Choix du timer utilisé pour générer le signal pwm
# freq : fréquence du signal pwm
# num_channel_pwm_In1 : numéro de l'Id du canal PWM associé à la broche In1_pin
# num_channel_pwm_In2 : numéro de l'Id du canal PWM associé à la broche In2_pin
# DRV8833 (In1_pin, In2_pin, sleep_pin, timer_number, freq, num_channel_pwm_In1, num_channel_pwm_In2)

Moteur_Gauche = DRV8833 (DRV8833_AIN1, DRV8833_AIN2, DRV8833_Sleep_pin, 1, 500, 0, 1) # Sur connecteur Encoder1
Moteur_Droit = DRV8833 (DRV8833_BIN1, DRV8833_BIN2, DRV8833_Sleep_pin, 1, 500, 2, 3) # Sur connecteur Encoder2
Arret()
while True :
    time.sleep (0.5)
    print('Sequence de mouvements du robot : begin')
    print('Avancer')
    Avancer (V_MOYEN)
    time.sleep (1)
    print('Reculer')
    Reculer (V_MOYEN)
    time.sleep (1)
    print('Pivoter droite')
    Pivoter_droite (V_MOYEN)
    time.sleep (0.5)
    print('Pivoter gauche')
    Pivoter_gauche (V_MOYEN)
    time.sleep (0.5)
    Arret ()
    print('Sequence de mouvements du robot : end')
'''
Index = 0
while True :
    print('Index : ', Index)
    # Définition d'une séquence de mouvements
    time.sleep(0.25)
    Index +=1
'''
