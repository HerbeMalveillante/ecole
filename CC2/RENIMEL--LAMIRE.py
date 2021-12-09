import math

class Client():

    nbClients = 0
    num = 0

    def __init__(self, nom, contact=("","","")):
        self.nom = nom
        self.contact = contact
        self.montantTotal = 0
        Client.num += 1
        Client.nbClients += 1
        self.numero = Client.num
    
    def modifMontant(self, montant):
        self.montantTotal += montant
    
    def __del__(self):
        Client.nbClients -= 1
    
    def __str__(self):
        return f"Client : {self.nom} ; numero {self.numero}\n{Client.chaineContact(self.contact)}Montant total des commandes : {self.montantTotal}"

    @staticmethod
    def chaineContact(t):
        contactString = "Contact(s)\n"
        if t[0] != "":
            contactString += "Téléphone: " + t[0] + "\n"
        if t[1] != "":
            contactString += "Email: " + t[1] + "\n"
        if t[2] != "":
            contactString += "Adresse postale: " + t[2] + "\n"
        
        return contactString

class ClientPremium(Client):

    def __init__(self, nom, contact=("","",""), achats=[], remise={}):
        super().__init__(nom, contact)
        self.pointsFid = 50
        self.achats = achats
        self.montantTotal = sum(self.achats)
        self.remise = remise
    
    def affiche(self):
        print(self)

        strRemises = []
        for i in self.remise:
            if len(self.remise[i]) > 1:
                strRemises.append(f"{i} : -{self.remise[i][1]} euros pour {self.remise[i][0]} euros d'achat")
            else : 
                strRemises.append(f"{i} : {self.remise[i][0]}% de réduction")

        print(f"\nVous avez {self.pointsFid} points fidélités\nVos réductions en cours :\n{' ; '.join(strRemises)} ;")
    
    def calculReduc(self, montant):
        maxReduc = (0, "Prix de base")
        for i in self.remise:
            if len(self.remise[i]) > 1: # si la réduction est par minimum d'achat
                if montant >= self.remise[i][0]: # si le montant est supérieur au montant minimum
                    if self.remise[i][1] > maxReduc[0]: # si la réduction est supérieure à la réduction précédente
                        maxReduc = (self.remise[i][1], i)
            else : # si la réduction est par pourcentage
                if montant*self.remise[i][0]*.01 > maxReduc[0]: # si la réduction est supérieure à la réduction précédente
                    maxReduc = (montant*self.remise[i][0]*.01, i)
        
        return maxReduc

    def prixFinal(self, montant):
        reducSelectionnee = self.calculReduc(montant)
        reducPoints = 0
        if self.pointsFid >= 150:
            reducPoints = montant*0.05
        else :
            self.pointsFid += int((montant - reducSelectionnee[0] - reducPoints) // 10) # on ajoute les points fidélité (1 point par tranche de 10 euros d'achats)
        
        self.achats.append(montant - reducSelectionnee[0] - reducPoints)
        self.montantTotal += montant - reducSelectionnee[0] - reducPoints

        print(f"Votre total est de {montant - reducSelectionnee[0] - reducPoints} euros, vous avez bénéficié de la réduction {reducSelectionnee[1]}.")

            


# Question 1
print("--- Question 1 ---")
c1 = Client("Albert Reanol", ("","","16 rue des trisoles 37000 Tours"))
c1.modifMontant(100)
print(c1.montantTotal)

# Question 2
print("\n--- Question 2 ---")
c2 = Client("Alex Trampullo", ("02.47.58.25.14", "alex.t@outlook.fr", ""))
print(Client.num)
print(Client.nbClients)
del c2
print(Client.num)
print(Client.nbClients)

# Question 3
print("\n--- Question 3 ---")
print(Client.chaineContact(("06.12.12.12.12", "", "")))
print(Client.chaineContact(("06.12.12.12.12","","5 rue des Champs, 37000 Tours")))
print(c1)

# Question 4
print("\n--- Question 4 ---")
c3 = ClientPremium("Amandine Goca", ("06.35.78.41.22", "amandine.go@gmail.com", "9 bis rue de la Milli, 5700 art"), [24, 18, 32.5], {"blackFriday":(25,), "Soldissime":(120,30), "Monchèque":(80,21)})
c3.affiche()

# Question 5
print("\n--- Question 5 --- (/!\ erreur dans l'énoncé, blackFriday est bel est bien plus avantageux que Soldissime tant que cette dernière est à 30€, valeur donnée dans l'énoncé.)")
print(c3.calculReduc(85.30))
print(c3.calculReduc(121))
print("-"*30)
c3.prixFinal(121)
c3.affiche()
