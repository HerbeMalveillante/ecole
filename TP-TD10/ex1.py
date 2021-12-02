class Legume():
    def __init__(self, nom, stock, prix):
        self.nom = nom
        self.stock = stock
        self.prix = prix
    
    def __str__(self):
        return "Nom: {}, Stock: {}, Prix: {} par kg".format(self.nom, self.stock, self.prix)
    
    def metAJour(self, stock):
        self.stock += stock
        print(f"{abs(stock)} kg de {self.nom} en {'plus' if stock > 0 else 'moins'},valeur : {self.prix}€, il reste {self.stock} kg")

class Courge(Legume):

    def __init__(self, nom, stock, prix, rayon):
        super().__init__(nom, stock, prix)
        self.rayon = rayon

    def volume(self):
        print(f"Volume moyen de la courge : {round((4/3)*3.14*(self.rayon**3),2)} m**3")


c1 = Courge("Courgette", 10, 1.5, 0.5)
print(c1)
c1.metAJour(5)
c1.volume()