class Chat():

    def __init__(self, nom, race, poids, naissance):
        self.nom = nom
        self.race = race
        self.poids = poids
        self.naissance = naissance

    def affiche(self):
        print(f"""Carte d'identité de {self.nom} :
    Race : {self.race}
    Poids : {self.poids}
    Année de naissance : {self.naissance}""")

    def estPlusGros(self, autreChat):
        if self.poids == autreChat.poids : 
            print(f"{self.nom} et {autreChat.nom} ont le même poids")
        elif self.poids > autreChat.poids or self.poids < autreChat.poids :
            print(f"{self.nom if self.poids > autreChat.poids else autreChat.nom} est plus gros que {self.nom if self.poids < autreChat.poids else autreChat.nom} ")

    def estPlusVieux(self, autreChat):
        if self.naissance == autreChat.naissance : 
            print(f"{self.nom} et {autreChat.nom} ont la même année de naissance")
        elif self.naissance > autreChat.naissance or self.naissance < autreChat.naissance :
            print(f"{self.nom if self.naissance < autreChat.naissance else autreChat.nom} est plus vieux que {self.nom if self.naissance > autreChat.naissance else autreChat.nom} ")

chat = Chat("Popaul", "Sphinx", "13kg", "2001")
chat2 = Chat("Louis", "Sphinx", "12kg", "2002")
chat3 = Chat("Léo", "Angora", "13kg", "2001")
chat.affiche()
chat.estPlusGros(chat2)
chat.estPlusGros(chat3)
chat2.estPlusGros(chat)
chat.estPlusVieux(chat2)
chat.estPlusVieux(chat3)