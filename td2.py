import random as rd
import turtle

def syracuse(donnee):
    if donnee % 2 == 0 :
        return(donnee // 2)
    else : 
        return(3 * donnee + 1)

def cinquante():
    donnee_initiale = rd.randint(2, 20)
    print(donnee_initiale)

    for i in range(50):
        donnee_initiale = syracuse(donnee_initiale)
        print(donnee_initiale)

# cinquante()

# après avoir effectué la suite plusieurs fois, on constate que dès qu'on
# arrive sur le nombre 1, ça boucle sur 1, 4, 2, 1, 4, 2, etc.

def jusquaun():
    donnee_initiale = rd.randint(2, 20)
    print(donnee_initiale)

    while True:
        donnee_initiale = syracuse(donnee_initiale)
        print(donnee_initiale)
        if donnee_initiale == 1 :
            break

# jusquaun()

def demandeValeur():
    donnee_initiale = int(input("Rentrez la valeur initiale : "))
    print(donnee_initiale)

    while True:
        donnee_initiale = syracuse(donnee_initiale)
        print(donnee_initiale)
        if donnee_initiale == 1 :
            break

# demandeValeur()

def tempsDeVol(donnee):
    print(donnee)
    donnee_initiale = donnee
    # print(donnee_initiale)
    tempsDeVol = 0
    while True:
        tempsDeVol += 1
        donnee_initiale = syracuse(donnee_initiale)
        # print(donnee_initiale)
        if donnee_initiale == 1 :
            return(tempsDeVol)

# tempsDeVol(0)


def maxTempsDeVol():
    print(max([(tempsDeVol(i), i) for i in range(1, 10001)], key = lambda k: k[0]))

# on constate que la valeur de départ ayant le plus long temps de vol est 6171,
# avec un temps de vol de 261.


def monteCarlo():
    for puissance in [2, 3, 4, 5, 6]:
        nb_de_simulations = 10**puissance
        nb_de_cas_positifs = 0
        for i in range(nb_de_simulations):
            if rd.random()**2 + rd.random()**2 < 1:
                nb_de_cas_positifs += 1
        
        print(f"Pour {nb_de_simulations} simulations : {4*nb_de_cas_positifs / nb_de_simulations}")

# monteCarlo()

# le nombre pi apparaît de façon de plus en plus précise en fonction du nombre de simulations qui augmente.

def volumeBoule(rayon, precision):
    nb_de_simulations = 10**precision
    nb_de_cas_positifs = 0
    for i in range(nb_de_simulations):
        if rd.random()**2 + rd.random()**2 < 1:
            nb_de_cas_positifs += 1
    pi = 4*nb_de_cas_positifs / nb_de_simulations

    return (4 * pi * rayon**3 )/3

# print(volumeBoule(2, 6))
# 33,5 environ


# EXERCICE 11

def figure():
    turtle.reset()
    turtle.speed(0)
    for i in range(200):
        if i%2 == 0 :
            turtle.color("blue")
        else :
            turtle.color("red")
        
        turtle.forward(i)
        turtle.left(91)
    
    input("entrée pour fermer")

figure()