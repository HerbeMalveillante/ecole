import random
import copy

class Jeu():

    def __init__(self, lignes):
        self.allumettes = []
        self.lignes = lignes
        nombreAllumettes = 1
        for i in range(lignes):
            self.allumettes.append(nombreAllumettes)
            nombreAllumettes += 2
    
    def __str__(self):
        lstGraphique = []
        for i in range(len(self.allumettes)):
            lstGraphique.append(str(i)+ "] "+" "*(self.lignes-1-i) +  "|"*self.allumettes[i])
        return "\n".join(lstGraphique)+"\n"+"-"*10
    
    def retire(self, ligne, nombre):

        if len(self.allumettes)-1 < ligne or ligne < 0 or nombre < 1:
            return False
        if self.allumettes[ligne] < nombre:
            return False 
        self.allumettes[ligne] -= nombre
        return True
    
    def testValide(self, ligne, nombre):
        if len(self.allumettes)-1 < ligne or ligne < 0 or nombre < 1:
            return False
        if self.allumettes[ligne] < nombre:
            return False
        if self.totalAllumettes() - nombre < 1 : # on vérifie que le coup ne nous fait pas perdre
            return False
        return True
    
    def totalAllumettes(self):
        return sum(self.allumettes)
    
    def checkPosition(self):

        # on récupère le tableau des allumettes en binaire
        listBinaire = []
        for i in self.allumettes:
            listBinaire.append(str(bin(i))[2:])
        print(listBinaire)
        maxLen = max([len(i) for i in listBinaire])
        finalList = [i.zfill(maxLen) for i in listBinaire]
        print(finalList)


        sommeColonnes = []
        for i in range(len(finalList[0])):
            sommeColonnes.append(sum(int(j[i]) for j in finalList))
                    
        print(sommeColonnes)
        return all([i%2 == 0 for i in sommeColonnes])
    
class Partie():

    def __init__(self, aleatoire = False):
        self.aleatoire = aleatoire
        print("\n"*20+"-"*20)
        print("Bienvenue dans le jeu de Marienbad")
        print("-"*20)

        print("Un nombre aléatoire de lignes entre 3 et 6 va être choisi pour commencer le jeu.")
        nbLignes = random.randint(3,6)

        self.jeu = Jeu(nbLignes)
        print(self.jeu)

        print("Un joueur aléatoire entre le joueur et le robot va commencer la partie.")
        self.joueurActuel = random.choice(["joueur", "robot"])
        print(f"Le hasard a décidé : c'est le {self.joueurActuel} qui va commencer.")
    
    def checkFin(self):
        if self.jeu.totalAllumettes() == 0 :
            return "zero"
        elif self.jeu.totalAllumettes() == 1 :
            return "un"
        else :
            return False

    

    
    def tour(self):

        while not self.checkFin():

            if self.joueurActuel == "joueur":

                nbLigne = int(input("Entrez le numéro de la ligne dans laquelle vous souhaitez retirer des allumettes : "))
                nbAllumette = int(input("Entrez la quantité d'allumettes à retirer sur cette ligne : "))

                if self.jeu.retire(nbLigne, nbAllumette):
                    print(f"Le joueur retire {nbAllumette} allumettes sur la ligne {nbLigne}.")
                    print(self.jeu)
                    self.joueurActuel = "robot"
                else :
                    print("Desolé, votre entrée est invalide (soit parce que le numéro de ligne est invalide, soit parce vous voulez retirer plus d'allumettes qu'elle n'en contient.)")
            else :
                
                if self.aleatoire :

                    listeIndexDisponibles = [i for i in range(len(self.jeu.allumettes)) if self.jeu.allumettes[i] > 0]
                    nbLigne = random.choice(listeIndexDisponibles)
                    nbAllumette = random.randint(1, self.jeu.allumettes[nbLigne])

                    self.jeu.retire(nbLigne, nbAllumette)
                    print(f"Le robot retire {nbAllumette} allumettes sur la ligne {nbLigne}.")
                    print(self.jeu)
                    self.joueurActuel = "joueur"
                
                else :

                    positionsValides = []
                    # on génère un mouvement aléatoire / on teste tous les mouvements
                    for i in range(len(self.jeu.allumettes)): # numéro de ligne
                        for j in range(1, self.jeu.allumettes[i]+1): # nombre d'allumettes
                            if self.jeu.testValide(i, j):
                                positionsValides.append((i, j))
                    print(positionsValides)

                    position = None
                    for i in positionsValides:
                        # on copie le jeu
                        jeuCopy = copy.deepcopy(self.jeu) # on utilise le module copy pour éviter de modifier des références.
                        jeuCopy.retire(i[0], i[1])
                        good = jeuCopy.checkPosition()

                        if good :
                            position = i
                            break
                    
                    if position == None :
                        print("Aucune possibilité de gagner. Le robot a perdu")
                        return
                    else :
                        nbLigne, nbAllumette = position
                        self.jeu.retire(nbLigne, nbAllumette)
                        print(f"Le robot retire {nbAllumette} allumettes sur la ligne {nbLigne}.")
                        print(self.jeu)
                        self.joueurActuel = "joueur"
                    
                    # on l'applique sur une copie du jeu d'allumettes
                    # et on vérifie si la position est gagnante.
                    # si la position est gagnante on applique le mouvement sur le vrai jeu
                    # sinon on essaie le prochain mouvement


                    # TODO : Changer la condition de victoire parce que je l'ai fait dans le mauvais sens
        
        state = self.checkFin()
        if state == "zero":
            print(f"Il ne reste plus d'allumettes sur le plateau : le {'robot' if self.joueurActuel == 'joueur' else 'joueur'} a gagné !")
        else :
            print(f"Il ne reste plus qu'une allumette sur le plateau : le {'robot' if self.joueurActuel == 'joueur' else 'joueur'} a perdu !")


p = Partie(aleatoire = False)
p.tour()
