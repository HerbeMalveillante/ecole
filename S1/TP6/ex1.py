from time import time
from random import randint


def comp():
    for m in range(5, 25):
        debut = time()
        print(sum([n ** 2 for n in range(2 ** m)]))
        print(m, ":", time() - debut)

    # le code est de plus en plus long à s'éxecuter à mesure que
    # m augmente.


def tri_bulle(liste_entree):
    liste = liste_entree[:]
    n = len(liste)
    for j in range(1, n):
        for i in range(n - j):
            if liste[i] > liste[i + 1]:
                liste[i], liste[i + 1] = liste[i + 1], liste[i]
    return liste


def compare_tris():
    for m in range(5, 25):
        debut = time()
        liste = [randint(0, 1000) for i in range(2 ** m)]
        sorted(liste)
        print(m, " (tri python) :", time() - debut)
        debut = time()
        tri_bulle(liste)
        print(m, " (tri bulle) : ", time() - debut)


compare_tris()

# on constate que la fonction de python est de loin plus rapide
# que le tri à bulle.
