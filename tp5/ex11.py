import random


def valeursCommunes(l1, l2):
    val = []
    for i in l1:
        if i not in val and i in l2:
            val.append(i)
    for i in l2:
        if i not in val and i in l1:
            val.append(i)
    return val


l1 = [random.randint(0, 10) for i in range(5)]
l2 = [random.randint(0, 10) for i in range(5)]

print(l1, l2)
print(valeursCommunes(l1, l2))
