class Inventaire(dict):
    
    def __str__(self):
        return "Inventaire :\n" + "\n".join(["\t" + str(k) + " : " + str(v) for k, v in sorted(self.items())])
    
    def __add__(self, other):
        newInv = other.copy()
        for k,v in self.items():
            if k in newInv:
                newInv[k] += v
            else:
                newInv[k] = v
        return Inventaire(newInv)

inv1 = Inventaire({'pomme': 1, 'poire': 2, 'banane': 3})
print(inv1)

inv2 = Inventaire({'banane': 1, 'pomme': 5, 'poire': 2, 'orange': 3})
print(inv2)

print(inv1 + inv2)