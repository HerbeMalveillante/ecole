relBin = {
    "a":["a", "b", "c", "d"],
    "b":["a", "b", "c", "d"],
    "c":["c", "d"],
    "d":["d"],
    "e":["c", "d", "e"]
}

def ensemble(R):
    ensembleListe = []
    for i in R :
        for j in R[i]:
            if j not in ensembleListe:
                ensembleListe.append(j)
    return ensembleListe

def identite(E):
    relBin = {}
    for i in E:
        relBin[i] = [i]
    
    return relBin

def est_reflexive(R):
    for i in R :
        if i not in R[i]:
            return False
    return True

def est_symetrique(R):
    for i in R :
        for j in R[i]:
            if i not in R[j]:
                return False
    return True

def est_antiSymetrique(R):
    for i in R :
        for j in R[i]:
            if i in R[j]:
                if i != j :
                    return False
    return True

print(ensemble(relBin))
print(identite(["1", "2", "3", "4"]))
print(est_reflexive(relBin))
print(est_reflexive(identite(["1", "2", "3", "4"])))
print(est_symetrique(relBin))
print(est_symetrique(identite(["1", "2", "3", "4"])))
print(est_antiSymetrique(relBin))
print(est_antiSymetrique(identite(["1", "2", "3", "4"])))