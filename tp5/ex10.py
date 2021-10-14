def _1():
    ls = [1, 2, 3]
    ks = ls
    ks[0], ks[1] = ks[1], ks[0]
    print(ls)
    print("Identifiant de ls :", id(ls))
    print("Identifiant de ks :", id(ks))


def _2():
    ls = [1, 2, 3]
    ks = ls[:]
    ks[0], ks[1] = ks[1], ks[0]
    print(ls)
    print("Identifiant de ls :", id(ls))
    print("Identifiant de ks :", id(ks))


_1()
_2()

# on constate que quand on fais var = liste, on ne copie pas la liste mais on stocke une référence de cette dernière dans la variable.


def bubbleSort(liste):

    lis = liste[:]

    for i in range(len(lis) - 1):

        for j in range(0, len(lis) - i - 1):
            if lis[j] > lis[j + 1]:
                lis[j], lis[j + 1] = lis[j + 1], lis[j]

    return lis
