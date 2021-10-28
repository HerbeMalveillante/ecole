inventaire = {'orange':378, 'pomme':545, 'banane':422, 'poire':269}

def nombre(d):
    return len(d)
print(nombre(inventaire))

def stockTotal(d):
    return(sum(d[i] for i in d))
print(stockTotal(inventaire))

def afficher(d):
    for i in sorted([i for i in d]):
        print(f"Fruit : {i}, Stock : {d[i]}")

afficher(inventaire)

# la question 4 n'a pas trop de sens : comment on considère qu'un fruit a un stock "le plus important" ou pas ?

inventaire2={'raisin' : 315, 'noix' : 164}
def fusion(d1, d2):
    d3 = d1.copy()
    d3.update(d2)
    return d3

print(fusion(inventaire, inventaire2))
print(inventaire)
print(inventaire2)




