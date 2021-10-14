from math import pi


def cinqun():
    valid = []
    for i in range(10):  # 0 à 9
        if (i + 1) % 3 == 0 or (i + 1) % 5 == 0:
            valid.append(i)

    print(
        f"Il y a {len(valid)} entiers entre 1 et 10 divisibles par 3 ou 5. Leur somme vaut {sum(valid)}."
    )


def cinqdeux():
    valid = []
    for i in range(10):  # 0 à 9
        j = i + 1
        if j % 3 == 0 and j % 5 == 0:
            valid.append(i)

    print(
        f"Il y a {len(valid)} entiers entre 1 et 10 divisibles par 3 et 5. Leur somme vaut {sum(valid)}."
    )


def cinqtrois():
    valid = []
    for i in range(1000000):  # 0 à 9
        j = i + 1
        if j % 3 == 0 or j % 5 == 0:
            valid.append(i)

    print(
        f"Il y a {len(valid)} entiers entre 1 et 1000000 divisibles par 3 ou 5. Leur somme vaut {sum(valid)}."
    )


def cinqquatre():
    valid = []
    for i in range(1000000):  # 0 à 9
        j = i + 1
        if j % 3 == 0 and j % 5 == 0:
            valid.append(i)

    print(
        f"Il y a {len(valid)} entiers entre 1 et 1000000 divisibles par 3 et 5. Leur somme vaut {sum(valid)}."
    )


def sixun(n):
    somme = 0
    for i in range(n):
        j = i + 1
        somme += 1 / (j ** 2)

    print(f"somme({n}) = {somme}")


sixun(2)
sixun(3)
sixun(4)
sixun(100)
sixun(10000)

print(f"valeur de pi au carré sur six : {pi**2 / 6}")
