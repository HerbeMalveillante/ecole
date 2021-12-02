class Arbre:

    listeDesArbresOK = []

    def __init__(self, ref, hauteur=10, rayon=0.5, etatOK=True):
        self.ref = ref
        self.hauteur = hauteur
        self.rayon = rayon
        self.etatOK = etatOK

        if etatOK:
            Arbre.listeDesArbresOK.append(self)

    def __del__(self):
        if self.etatOK:
            Arbre.listeDesArbresOK.remove(self)

    @classmethod
    def nombreArbreOk(cls):
        print(f"nombre d'arbres en bon état : {len(cls.listeDesArbresOK)}")

    @classmethod
    def afficheUneEssence(cls, essence):
        print(f"Coordonnées des {essence} en bon état :")
        for arbre in cls.listeDesArbresOK:
            if arbre.ref.split(" ")[0] == essence:
                print(arbre.ref.split(" ")[1] + " " + arbre.ref.split(" ")[2])

    @staticmethod
    def volTronc(hauteur, rayon):
        return 3.14 * rayon ** 2 * hauteur

    def affiche(self):
        print(
            f"Essence : {self.ref.split(' ')[0]} ; position : ({self.ref.split(' ')[1]} ; {self.ref.split(' ')[2]})\nhauteur : {self.hauteur} ; rayon : {self.rayon} ; volume du tronc : {self.volTronc(self.hauteur, self.rayon)} m3\netat : {'bon' if self.etatOK else 'mauvais'}"
        )


class ArbreTraite(Arbre):
    def __init__(self, ref, traitement, dates, hauteur=10, rayon=0.5, etatOK=True):
        super().__init__(ref, hauteur, rayon, etatOK)
        self.traitement = traitement
        self.dates = dates

    def affiche(self):
        super().affiche()
        print(f"Traitement : {self.traitement} effectué {len(self.dates)} fois:")
        for i in self.dates:
            print(f"{' '*3}le {i[0]}/{i[1]}/{i[2]}")

    def traitementAnnee(self, annee):
        count = 0
        for i in self.dates:
            if i[2] == annee:
                count += 1
        print(
            f"Essence : {self.ref.split(' ')[0]} ; position : ({self.ref.split(' ')[1]};{self.ref.split(' ')[2]}) ; Traitement effectué {count} fois en {annee}"
        )


a1 = Arbre("essence1 47 0.9", 158, 1.5, True)

a1.affiche()

a2 = Arbre("essence1 89 12", 160, 12, True)
a3 = Arbre("essence1 08 11", 10, 1, False)
a4 = Arbre("essence2 100 112", 134, 14, True)

Arbre.nombreArbreOk()
Arbre.afficheUneEssence("essence1")

print("____________________________________________")
at1 = ArbreTraite(
    "Chêne 47.052547 4.383553",
    "Pulvérisation de bacille de Thuringe",
    [(5, 9, 2017), (12, 4, 2018), (15, 6, 2018)],
    108,
    3,
)
at1.affiche()

at1.traitementAnnee(2018)
