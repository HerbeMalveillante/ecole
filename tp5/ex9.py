from random import randint

ls = [randint(-5, 5) for i in range(3)]
print(ls)
if ls[0] > ls[1]:
    ls[0], ls[1] = ls[1], ls[0]
if ls[1] > ls[2]:
    ls[1], ls[2] = ls[2], ls[1]
if ls[0] > ls[1]:
    ls[0], ls[1] = ls[1], ls[0]
print(ls)

# le code précédent trie une liste de trois éléments

def bubbleSort(lis):
    for i in range(len(lis)-1):

        for j in range(0, len(lis)-i-1):
            if lis[j] > lis[j+1]:
                lis[j], lis[j+1] = lis[j+1], lis[j]

    return lis

randomList = [randint(-10, 10) for i in range(10)]
print(randomList)
print(bubbleSort(randomList))