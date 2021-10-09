def modifier(li):
    for x in li:
        if x%2 == 0:
            x = x//2
    return li

malis = [72, 9, 84, 71, 6]
print(malis)
malis2 = modifier(malis)
print(malis2)

# La fonction ne modifie pas la liste...

def modifierCorrige(li):
    return [i if i%2 == 1 else i//2 for i in li]

malis = [72, 9, 84, 71, 6]
print(malis)
malis2 = modifierCorrige(malis)
print(malis2)

def tousImpairs(li):
    for x in li:
        if x%2 == 1:
            res = True
        else :
            res = False
    return res

# la fonction retourne uniquement si le dernier terme est impair...


def tousImpairs(li):
    for x in li:
        if x%2 == 1:
            return True
        else:
            return False

# la fonction retourne uniquement si le premier terme est impair...

def tousVraimentImpairs(li):
    return all([i%2==1 for i in li])
# cette fonction fonctionne !

print(tousVraimentImpairs([1, 3, 7, 9, 999]))
print(tousVraimentImpairs([1, 3, 7, 9, 999, 2]))
print(tousVraimentImpairs([2, 6, 8, 2]))