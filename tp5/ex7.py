import random


def cree(n):
    return [random.randint(0, 20) for i in range(n)]


def apparitions(x, lis):
    return [indice for indice, item in enumerate(lis) if item == x]


entiers = int(input("Saisir le nombre d'entiers de la liste : "))
liste = cree(entiers)
print(f"Liste : {liste}")
entierRecherche = int(input("Saisir l'entier recherché : "))
print(f"Liste des indices d'apparition : {apparitions(entierRecherche, liste)}")
