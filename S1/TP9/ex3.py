class Vecteur:
    def __init__(self, coords=(0, 0)):
        self.x = coords[0]
        self.y = coords[1]

    def affiche(self):
        print(f"({self.x}, {self.y})")

    def prodScal(self, autreVecteur):
        return self.x * autreVecteur.x + self.y * autreVecteur.y

    def somme(self, autreVecteur):
        return Vecteur((self.x + autreVecteur.x, self.y + autreVecteur.y))
