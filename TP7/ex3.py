import random

def listeSansDoublons(l):
    return list(set(l))

listeRandom = [random.randint(0,15) for i in range(15)]
print(listeRandom)
print(listeSansDoublons(listeRandom))

def valeursCommunes(l1, l2):
    return list(set([i for i in l1 if i in l2]))

listeRandom2 = [random.randint(0,15) for i in range(15)]
print(listeRandom2)
listeRandom3 = [random.randint(0,15) for i in range(15)]
print(listeRandom3)
print(valeursCommunes(listeRandom2, listeRandom3))