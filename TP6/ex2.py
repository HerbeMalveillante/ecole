for i in range(32, 128):
    print(i, ":",chr(i))
print()

# les lettres non accentuées ont un code ASCII allant de 97 à 122 (minuscule)
# et de 65 à 90 (majuscules)

# les chiffres vont de 48 à 57.

def parcourir(s):
    print(f"Longueur : {len(s)}")
    for index, i in enumerate(s) :
        print(f"Caractère n°{index} : {i} code ASCII : {ord(i)}")

parcourir("Texte")

def grec():
    t1 = "".join([chr(i) for i in range(945, 969)])
    t2 = "".join([chr(i) for i in range(913, 937)])

    return t1, t2

print(grec())