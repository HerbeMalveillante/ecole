class Joueur:

    cases = ["   ", "   ", "   "]
    fin = False

    def __init__(self, nom, symbole):
        # strips the name of the player to get the first 20 letters
        self.nom = nom[:20]
        self.symbole = symbole

    @staticmethod
    def afficheConvention():
        print(
            """(1,1) (1,2) (1,3)
(2,1) (2,2) (2,3)
(3,1) (3,2) (3,3)"""
        )

    @classmethod
    def afficheGrille(cls):
        """example of display :
        -------
        | | |x|
        -------
        |o| | |
        -------
        |x|o| |
        -------"""
        print("-------")
        for i in range(3):
            print(f"|{cls.cases[i][0]}|{cls.cases[i][1]}|{cls.cases[i][2]}|")
            print("-------")

    @classmethod
    def gagne(cls):
        """returns True if the player wins, False otherwise"""
        if cls.cases[0][0] == cls.cases[0][1] == cls.cases[0][2] != " ":
            cls.fin = True
        elif cls.cases[1][0] == cls.cases[1][1] == cls.cases[1][2] != " ":
            cls.fin = True
        elif cls.cases[2][0] == cls.cases[2][1] == cls.cases[2][2] != " ":
            cls.fin = True
        elif cls.cases[0][0] == cls.cases[1][0] == cls.cases[2][0] != " ":
            cls.fin = True
        elif cls.cases[0][1] == cls.cases[1][1] == cls.cases[2][1] != " ":
            cls.fin = True
        elif cls.cases[0][2] == cls.cases[1][2] == cls.cases[2][2] != " ":
            cls.fin = True
        elif cls.cases[0][0] == cls.cases[1][1] == cls.cases[2][2] != " ":
            cls.fin = True
        elif cls.cases[0][2] == cls.cases[1][1] == cls.cases[2][0] != " ":
            cls.fin = True
        else:
            cls.fin = False

        return

    def joue(self):
        """asks the coordinates to play to the player until they are valid and the specified case is empty,
        puts the player's symbol at the right place, displays the grid and checks if the player has won."""
        while True:
            self.afficheConvention()
            self.afficheGrille()
            try:
                coord = input(f"{self.nom}, entrez les coordonnées de votre choix : ")
                coord = coord.split(",")
                coord = (int(coord[0]), int(coord[1]))
                if coord[0] > 3 or coord[1] > 3:
                    raise ValueError
                if self.cases[coord[0] - 1][coord[1] - 1] != " ":
                    raise ValueError

                # creates a new string that contains the player's symbol at the selected coordinates
                self.cases[coord[0] - 1] = (
                    self.cases[coord[0] - 1][: coord[1] - 1]
                    + self.symbole
                    + self.cases[coord[0] - 1][coord[1] :]
                )

                self.gagne()
                self.matchNul()
                break
            except ValueError:
                print("Coordonnées invalides.")

    @classmethod
    def matchNul(cls):
        """returns True if the player has played all the cases, False otherwise"""
        for i in range(3):
            for j in range(3):
                if cls.cases[i][j] == " ":
                    return False
        cls.fin = True
        return True


def main():
    j1 = Joueur("Joueur 1", "x")
    j2 = Joueur("Joueur 2", "o")
    currentPlayer = j1
    while not Joueur.fin:
        currentPlayer.joue()
        if Joueur.fin:
            Joueur.afficheGrille()
            if Joueur.matchNul():
                print("Match nul !")
            else:
                print(f"{currentPlayer.nom} a gagné !")
            break
        currentPlayer = j2 if currentPlayer == j1 else j1


main()
