class Voiture:
    """defines a class representing a car with a brand, a model and a mileage
    creates an initialisation class that the mileage being set to 0
    creates a 'move' function that takes a number of miles in parameter and increases the mileage by this amount
    creates a 'display' function that displays all the attributes of the car."""

    def __init__(self, marque, modele):
        self.marque = marque
        self.modele = modele
        self.mileage = 0

    def roule(self, nb_km):
        self.mileage += nb_km

    def affiche(self):
        print(
            "La voiture est une",
            self.marque,
            self.modele,
            "et elle a parcouru",
            self.mileage,
            "km.",
        )


class Conducteur:
    def __init__(self, nom):
        self.nom = nom

    def conduit(self, voiture, nb_km):
        voiture.roule(nb_km)
        voiture.affiche()
        print(
            f"{self.nom} a conduit une {voiture.marque} {voiture.modele} pendant {nb_km}km."
        )


voiture1 = Voiture("Peugeot", "206")
voiture2 = Voiture("Renault", "Clio")
voiture3 = Voiture("Citroën", "C4")

voiture1.affiche()
voiture1.roule(1000)
voiture1.affiche()
voiture2.roule(500)
voiture2.affiche()
voiture3.affiche()

conducteur1 = Conducteur("Jean-Pierre")
conducteur1.conduit(voiture1, 1000)
conducteur1.conduit(voiture2, 500)
conducteur2 = Conducteur("Jean-Jacques")
conducteur2.conduit(voiture3, 1000)
