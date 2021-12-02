class Livre:

    dictISBN = {}

    def __init__(self, isbn, titre, liste_auteur, nbPages, prix):
        self.isbn = isbn
        self.titre = titre
        self.liste_auteur = liste_auteur
        self.nbPages = nbPages
        self.prix = prix
        self.dictISBN[isbn] = self.liste_auteur

    def __del__(self):
        del self.dictISBN[self.isbn]

    def prixParPage(self):
        print(
            f"Le prix de '{self.titre}' est de {round(self.prix / self.nbPages, 3)}€ par page."
        )
        return round(self.prix / self.nbPages, 3)

    def revientPlusCher(self, autreLivre):
        prixLivre1 = self.prixParPage()
        prixLivre2 = autreLivre.prixParPage()
        if prixLivre1 == prixLivre2:
            print(f"Les deux livres ont le même prix par page.")
        elif prixLivre1 > prixLivre2 or prixLivre1 < prixLivre2:
            print(
                f"Le prix par page de {self.titre if prixLivre1 > prixLivre2 else autreLivre.titre} est plus cher que {self.titre if prixLivre1 < prixLivre2 else autreLivre.titre}"
            )

    @staticmethod
    def extraction(listeChaines):
        return ", ".join(listeChaines) + "."

    def affiche(self):
        print(f"{self.titre} de : {self.extraction(self.liste_auteur)}")
        print(f"{self.nbPages} pages     {self.prix}€      ISBN:{self.isbn}")

    @staticmethod
    def aCommun(l1, l2):
        return len(set(l1) & set(l2)) > 0

    def auteursCommuns(self, autreLivre):
        if self.aCommun(self.liste_auteur, autreLivre.liste_auteur):
            print(
                f"Les auteurs en commun sont : {self.extraction(set(self.liste_auteur) & set(autreLivre.liste_auteur))}"
            )
        else:
            print(f"Les deux livres n'ont pas de auteurs en commun.")

    @classmethod
    def afficheAuteursEditeurs(cls, zone, editor_number):
        """the ISBN number contains information about a book such as the zone and the editor number (among others) separated by a dash.
        The second digit represents the zone and the third digit represents the editor.

        Displays all the authors that have written a book that corresponds the specified zone and editor number, without repetition."""
        authorList = []
        for isbn, auteurs in cls.dictISBN.items():
            livreZone = isbn.split("-")[2]
            livreEditor = isbn.split("-")[1]
            if livreZone == zone and livreEditor == editor_number:
                authorList += auteurs

        print(
            f"Les auteurs de livres édités par l'éditeur {editor_number} dans la zone {zone} sont : {cls.extraction(set(authorList))}"
        )


l1 = Livre(
    "978-2-1234-5678-9", "Le Petit Prince", ["Antoine de Saint-Exupéry"], 336, 24.99
)
l2 = Livre(
    "979-3-4321-8765-0",
    "Voyage au centre de la terre",
    ["Jules Verne", "Mon Daron"],
    320,
    19.99,
)
l3 = Livre(
    "124-3-4321-0987-4",
    "Histoire des locomotives",
    ["Mon Daron", "Jean-Paul Sartre"],
    276,
    2,
)

l1.revientPlusCher(l2)
l1.affiche()
l2.affiche()
l3.affiche()
l1.auteursCommuns(l2)
l2.auteursCommuns(l3)


print(Livre.dictISBN)

del l1

print(Livre.dictISBN)

Livre.afficheAuteursEditeurs("4321", "3")
Livre.afficheAuteursEditeurs("1234", "2")
