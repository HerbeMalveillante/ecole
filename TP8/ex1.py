def afficherLignesEtLongueur(source):
    # On affiche chaque ligne du fichier source et sa longueur.
    try:
        with open(source, "r", encoding="utf-8") as f:
            for ligne in f:
                print(ligne)
                lineFeed = 0
                if ligne[-1] == "\n":
                    lineFeed = 1
                print("Longueur :", len(ligne) - lineFeed)
    except IOError:
        print("Lecture du fichier", source, "impossible.")


def nombreLignes(source):
    """returns the number of line of the source file"""
    try:
        with open(source, "r", encoding="utf-8") as f:
            return len(f.readlines())
    except IOError:
        print("Lecture du fichier", source, "impossible.")
        return 0


def longueurPlusGrandeLigne(source):
    """returns the lenght of the longest line in the source file"""
    try:
        with open(source, "r", encoding="utf-8") as f:
            max = 0
            for ligne in f:
                if len(ligne) > max:
                    max = len(ligne)
            return max
    except IOError:
        print("Lecture du fichier", source, "impossible.")
        return 0


source = "musique.txt"
print(nombreLignes(source))
print(longueurPlusGrandeLigne(source))
