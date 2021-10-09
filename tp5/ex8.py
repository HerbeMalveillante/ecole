notes = [15, 12.5, 6, 9, 16.5]
print(notes)
print(min(notes), max(notes), sum(notes), sep=" ;")

# min renvoie le plus petit item, max le plus grand item, sum la somme des items

# les fonctions ne fonctionnent que si la liste ne contient que des nombres.

def premierNb(lis):
    for i in lis:
        if type(i) == int:
            return i

print(premierNb(["abs", "pas là", 12, "abj", 9.5, "absent", 17]))

def purge(li):
    """renvoie la liste avec uniquement les chiffres"""
    return [i for i in li if type(i) == int or type(i) == float]

def mini(li):
    return min(purge(li))

def maxi(li):
    return max(purge(li))

def summ(li):
    return sum(purge(li))

notes = ["abs", "pas là", 12, "abj", 9.5, "absent", 17, -12, True]
print(notes)
print(mini(notes), maxi(notes), summ(notes), sep=" ;")