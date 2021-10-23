import math

# 10:23


def saisie_lat():
    # Degrés
    entreeDeg = int(
        input("Pour la Latitude, entrer les degrés (42 <= entier <= 51 ) : ")
    )
    while not 42 <= entreeDeg <= 51:
        entreeDeg = int(input("Incorrect, recommencez : "))

    # Minutes
    entreeMin = int(
        input("Pour la Latitude, entrer les minutes (0 <= entier <= 59 ) : ")
    )
    while not 0 <= entreeMin <= 59:
        entreeMin = int(input("Incorrect, recommencez : "))

    # Secondes
    entreeSec = int(
        input("Pour la Latitude, entrer les secondes (0 <= entier <= 59 ) : ")
    )
    while not 0 <= entreeSec <= 59:
        entreeSec = int(input("Incorrect, recommencez : "))

    return [entreeDeg, entreeMin, entreeSec]


def saisie_long():
    # Orientation
    orientation = input("Quelle orientation pour la Longitude (E/W) ? : ").upper()
    while orientation not in ["E", "W"]:
        orientation = input(
            "Réessayer : l'orientation choisie est incorrecte. (E/W) : "
        )

    # Degrés
    seuil = 5 if orientation == "E" else 8
    degres = int(input("Pour la Longitude, entrer les degrés  : "))
    while not 0 <= degres <= seuil:
        degres = int(input(f"Incorrect (<{seuil}), recommencez : "))

    # Minutes
    entreeMin = int(
        input("Pour la Longitude, entrer les minutes (0 <= entier <= 59 ) : ")
    )
    while not 0 <= entreeMin <= 59:
        entreeMin = int(input("Incorrect, recommencez : "))

    # Secondes
    entreeSec = int(
        input("Pour la Longitude, entrer les secondes (0 <= entier <= 59 ) : ")
    )
    while not 0 <= entreeSec <= 59:
        entreeSec = int(input("Incorrect, recommencez : "))

    return orientation, [degres, entreeMin, entreeSec]


def convertir_lat(d, m, s):
    return (d + m / 60 + s / 3600) * (math.pi / 180)


def convertir_long(d, m, s, o):
    return (d + m / 60 + s / 3600) * (math.pi / 180) * (-1 if o == "W" else 1)
    # On peut s'épargner un test sur plusieurs lignes en multipliant par 1 ou -1, sélectionné avec un opérateur ternaire.
    # C'est ce que j'ai fait ici même si ça n'a pas fait en classe, mais ça revient à stocker 1 ou -1 dans une variable
    # Grâce à des tests classiques et à multiplier par cette variable dans le return.


# Batterie de tests, laissés parce qu'ils ne monopolisent pas le terminal en demandant une entrée.
# J'ai pris la liberté de retirer les tests qui monopolisent le terminal pour simplifier
# L'execution du programme. Toutes les fonctions de saisie impliquées sont de toute manière testables
# Par la suite lors de la mesure de la distance entre une ville et Toulouses.
print(convertir_lat(47, 22, 59))
print(convertir_long(0, 40, 59, "E"))
print(convertir_long(0, 40, 59, "W"))
print("-" * 20)


Longitude, Latitude = [], []

# Sélection des coordonnées pour la ville de tours
print("Entrez les coordonnées de la ville de votre choix (Tours)")
latV1 = saisie_lat()
oriV1, longV1 = saisie_long()
latRadV1 = convertir_lat(latV1[0], latV1[1], latV1[2])
longRadV1 = convertir_long(longV1[0], longV1[1], longV1[2], oriV1)
Longitude.append(longRadV1)
Latitude.append(latRadV1)

# On ajoute directement les coordonnées de toulouses dans la liste
Longitude.append(convertir_long(1, 26, 37, "E"))
Latitude.append(convertir_lat(43, 36, 15))

print(f"Latitude= {Latitude}")
print(f"Longitude= {Longitude}")


def distance(latv1, latv2, longv1, longv2):
    return 6378167 * math.acos(
        math.sin(latv1) * math.sin(latv2)
        + math.cos(latv1) * math.cos(latv2) * math.cos(longv1 - longv2)
    )


print(f"Distance = {distance(Latitude[0], Latitude[1], Longitude[0], Longitude[1])}")
