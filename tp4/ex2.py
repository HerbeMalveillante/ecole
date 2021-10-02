import random

def saisieSomme():
    entree = None
    while entree not in range(2, 13):entree = int(input("Entrez un nombre entre 2 et 12 inclus : "))
    return entree

def sommeDeuxDes():

    de1 = random.randint(1, 6)
    de2 = random.randint(1, 6)

    print("valeur du dé 1 :", de1, "| valeur du dé 2 :", de2)
    print("Somme :", de1+de2)

    return de1 + de2

def jouer():

    print("Gagné !" if saisieSomme() == sommeDeuxDes() else "Perdu !")

jouer()