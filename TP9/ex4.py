class Vecteur():

    def __init__(self, coord):
        self.coord = coord
    
    def affiche(self):
        print(self.coord)
    
    def prodScal(self, vect):
        prodScal = 0
        for i in range(len(self.coord)):
            prodScal += self.coord[i]*vect.coord[i]
        return prodScal
    
    def somme(self, vect):
        somme = []
        for i in range(len(self.coord)):
            somme.append(self.coord[i] + vect.coord[i])
        return Vecteur(tuple(somme))
    


vect1 = Vecteur((1,2))
vect2 = Vecteur((3,4))
print(vect1.prodScal(vect2))
print(vect1.somme(vect2).coord)