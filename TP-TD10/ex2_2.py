class Inventaire():

    def __init__(self, nom, inventaire):
        self.nom = nom
        self.inventaire = inventaire
    
    def __str__(self):
        return f"{self.nom}:\n" + "\n".join(["\t" + str(k) + " : " + str(v) for k, v in sorted(self.inventaire.items())])

    def __add__(self, other):
        newInv = other.inventaire.copy()
        for k,v in self.inventaire.items():
            if k in newInv:
                newInv[k] += v
            else:
                newInv[k] = v
        return Inventaire(f"{self.nom} + {other.nom}", newInv)


inv = Inventaire("Inventaire 1", {"Orange": 2, "Banane": 3, "Pomme": 5})

print(inv)

inv2 = Inventaire("Inventaire 2", {"Orange": 1, "Banane": 2, "Pomme": 3, "Poire": 4})
print(inv + inv2)