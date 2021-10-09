nombres_impairs = [i for i in range(100) if i%2 == 1]
print(nombres_impairs)

def somme_puissance_impaire(n, p):
    return sum([i**p for i in range(n+1) if i%2 == 1])