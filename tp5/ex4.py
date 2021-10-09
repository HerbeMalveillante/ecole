nombres = [1, -1, 2, -2, 3, -3, 0]


def tri1():
    tries = sorted(nombres)
    print(tries)
    print(nombres)
def tri2():
    tries = nombres.sort()
    print(tries)
    print(nombres)

# sorted(liste) renvoie une copie de la liste triée
# liste.sort() trie la liste en place et ne renvoie rien

def triReverse():
    """Pour trier une liste dans l'ordre décroissant"""
    tries = nombres.sort(reverse=True)
    print(tries)
    print(nombres)

triReverse()