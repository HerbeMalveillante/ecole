import random


def jeu1():
    choice = random.randint(0, 1)
    print(
        f"Perdu ! On attendait un nombre {'pair' if choice == 1 else 'impair'}"
        if int(input("Entrer un entier : ")) % 2 == choice
        else f"Gagné ! On attendait un nombre {'pair' if choice == 1 else 'impair'}"
    )


def jeu2():
    choice = random.choice(["+", "=", "-"])
    dicoSmiley = {"+": ")", "=": "I", "-": "("}
    userChoice = input("Entrez '+', '=' ou '-' : ")
    print(
        f":-{dicoSmiley[userChoice]} {'perdu' if choice != userChoice else 'gagné'} on attendait :-{dicoSmiley[choice]}"
    )


def jeu():
    while True:
        choice = input(
            "Entrez 1 ou 2 pour choisir un jeu. Si vous voulez quitter, entrez autre chose : "
        )
        if choice not in ["1", "2"]:
            break
        elif choice == "1":
            jeu1()
        else:
            jeu2()
    print("Merci d'avoir joué !")


jeu()
