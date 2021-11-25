class Perchiste():

    sportifs = {}

    def __init__(self, nom, sauts):
        self.nom = nom
        self.sauts = sauts
        
        # adds to the sportifs dictionnary the mean of the jumps. The list can contain a real or the letter 'X' if the jump is not valid
        sautsValids = [saut for saut in sauts if saut != 'X']
        Perchiste.sportifs[nom] = sum(sautsValids) / len(sautsValids)

    def __del__(self):
        del Perchiste.sportifs[self.nom]
    
    def mean(self):
        sautsValids = [saut for saut in self.sauts if saut != 'X']
        # print(f"moyenne des sauts : {sum(sautsValids) / len(sautsValids)}")
        return sum(sautsValids) / len(sautsValids)

    def affiche(self):
        print(f"{self.nom} : {self.mean()} en moyenne")
        print(f"détail des sauts : {self.sauts}")

    
    @classmethod
    def afficheSportifs(cls):
        """prints the sportifs and their mean jumps in alphabetical order"""
        for nom, saut in sorted(cls.sportifs.items()):
            print(f"{nom} : {saut}")
    
s1 = Perchiste("Renaud Lavillenie", [5.65,5.70,"X",5.81,"X",5.9,6.0])
s2 = Perchiste("Sergueï Bubka", [5.6,5.82,"X",5.91,6])

s1.affiche()

Perchiste.afficheSportifs()

# print a separator
print("-" * 50)

del s2

Perchiste.afficheSportifs()


