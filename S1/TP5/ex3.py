def affiche(listeChaines1, listeChaines2):
    if len(listeChaines1) != len(
        listeChaines2
    ):  # si les deux listes n'ont pas la même longueur
        print(
            "Pb : nombre d'éléments différents"
        )  # on ne fait rien et on affiche une erreur
    else:
        print("Scientifiques :")
        for i in range(len(listeChaines1)):  # pour chaque index dans la liste
            s = (
                listeChaines1[i] + " " + listeChaines2[i]
            )  # on créée un nom de scientifique avec le nom de chaque liste en position i
            print(s)  # et on l'affiche


def construction(lis1, lis2):
    if len(lis1) != len(lis2):
        return []

    total = []

    for i in range(len(lis1)):
        total.append(lis1[i])
        total.append(lis2[i])

    return total


def eclatement(lis):
    lis1 = []
    lis2 = []

    for i in range(len(lis)):
        if i % 2 == 0:
            lis1.append(lis[i])
        else:
            lis2.append(lis[i])

    return lis1, lis2


def rassemble(lis):
    if len(lis) % 2 != 0:
        return []

    total = []
    l1, l2 = eclatement(lis)
    for i in range(len(l1)):
        total.append(f"{l1[i]} {l2[i]}")
    return total


lis1 = ["Albert", "Marie", "Raymond"]
lis2 = ["Einstein", "Curie", "Poincaré"]
print(rassemble(["Albert", "Einstein", "Marie", "Curie", "Raymond", "Poincaré"]))
