def suiteArithmetique(prTerme, raison, n):
    i = 0
    u = prTerme

    while i != n:
        u = u + raison
        i += 1

    return u


def suiteGeometrique(prTerme, raison, n):
    i = 0
    u = prTerme
    while i != n:
        u = u * raison
        i += 1
    return u


def main():

    prTerme = int(input("Entrez le premier terme : "))
    raison = int(input("Entrez la raison : "))
    n = int(input("Entrez le rang souhaité : "))

    entree = None
    while entree not in ["g", "a"]:
        entree = input("Entrez a pour arithmétique, g pour géométrique : ")

    if entree == "g":
        print(suiteGeometrique(prTerme, raison, n))
    else:
        print(suiteArithmetique(prTerme, raison, n))


main()
