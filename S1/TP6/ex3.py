import random


def genere():
    return "".join([random.choice([":", "-", "(", ")"]) for i in range(10)])


def joue():
    chaine = genere()
    print(chaine)
    if ":-)" in chaine:
        print("Gagné !")
    else:
        print("Perdu !")


joue()
