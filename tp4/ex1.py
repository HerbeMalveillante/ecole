import math

def saisie():
    entree = -1
    while entree <= 0:entree = int(input("Entrez un entier positif : "))
    return entree

def afficherTerme(n):

    print("valeur de pi^2/6 : ", math.pi**2 / 6)

    somme = 0
    for i in range(1, n+1):
        somme += 1/i**2

    print("valeur approchée calculée grâce à la somme : ", somme)


afficherTerme(10000)