def moyenne(i):

    if "ABI" in i :
        return "défaillant"
    
    nouvelleListe = [i if i != "ABJ" else 0 for i in i]
    return round(sum(nouvelleListe)/len(nouvelleListe), 2)

liste = [12, 18, 14, 15, "ABJ", 19]
print(moyenne(liste))

d={"Barthet" : [14, 7, 12], "Chapuis": [18, 16, 17], "Rey" : ["ABJ", 15, 13], "Varlet":[12, 8, "ABI"], "Frémont":[6, 14, 11]}

def moyenneEtudiants(d):
    listeTuple = []

    for i in d : 
        listeTuple.append((i, moyenne(d[i])))
    return listeTuple

print(moyenneEtudiants(d))
