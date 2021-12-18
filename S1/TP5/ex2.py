nombres = [n for n in range(20)]
print(nombres)
print(nombres[2:18:2])
print(nombres[::2])
print(nombres[1::2])

# liste[a:b:c] renvoie la liste de a inclus à b exclu avec un pas de c
# si a et/ou b est absent, python prends depuis le début ou la fin.
# liste[::-1] est valide et renvoie la liste à l'envers.
