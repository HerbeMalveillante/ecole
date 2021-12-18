dico = {25: 4, 8: 1, 12: 2, 3: 5}
print(dico)
print("5 dans dico ?", 5 in dico)
print("25 dans dico ?", 25 in dico)
dico[9] = 1
dico[8] = 2
print(dico)
del dico[25]
print(dico)
print("-" * 10)

inventaire = {"orange": 378, "pomme": 545, "banane": 422, "poire": 269}


def checkStock():
    fruit = input("Entrez un fruit : ")
    print(
        f"Il y a {inventaire[fruit]} {fruit}s."
        if fruit in inventaire
        else "Desolé, le fruit n'est pas en stock"
    )


checkStock()


def ajouteStock():
    fruit, stock = input(
        "Entrez un fruit et son stock séparés par un espace : "
    ).split()
    stock = int(stock)

    if fruit in inventaire and stock != inventaire[fruit]:
        print(
            "Erreur : le fruit est déjà présent dans l'inventaire avec un stock différent"
        )
        return
    inventaire[fruit] = stock


def supprimerStock():
    fruit = input("Entrez un fruit : ")
    if fruit not in inventaire:
        print("Le fruit n'est pas dans l'inventaire")
        return
    del inventaire[fruit]


ajouteStock()
supprimerStock()
