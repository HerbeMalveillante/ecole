class Ruche:
    def __init__(self, lieu, poids, humidite):
        self.lieu = lieu
        self.poids = poids
        self.humidite = humidite

    def moyenne(self):
        liste7H = [i[0] for i in self.poids]
        return round(sum(liste7H) / len(liste7H), 5)

    def alerte(self):
        troisDerniers = []

        for i in self.humidite:
            troisDerniers.append(i)
            if len(troisDerniers) > 3:
                troisDerniers.pop(0)

            if min(troisDerniers) >= 80:
                print("Attention à l'humidité !")
                return
        print("Pas de problème d'humidité.")
        return

    @staticmethod
    def difference(tupleList):
        newList = []
        for i in tupleList:
            newList.append(round(i[0] - i[1], 2))
        return newList

    def picActivite(self):
        activiteList = self.difference(self.poids)
        indexMax = [i for i, j in enumerate(activiteList) if j == max(activiteList)]
        Max = max(activiteList)
        print(
            f"Activité maximale : {Max} kg le(s) jour(s) {';'.join([str(i+1) for i in indexMax])}"
        )

    def affiche(self):
        print(f"Ruche située à {self.lieu}")
        print(f"Poids : {self.moyenne()} kg")
        self.alerte()
        self.picActivite()


class RucheParrainee(Ruche):

    parrainages = {}

    def __init__(self, lieu, poids, humidite, nomParrain, montantVerse):
        super().__init__(lieu, poids, humidite)
        self.nomParrain = nomParrain
        self.montantVerse = montantVerse

        RucheParrainee.parrainages[self.lieu] = (self.nomParrain, self.montantVerse)

    def __del__(self):
        del RucheParrainee.parrainages[self.lieu]

    @classmethod
    def afficheToutes(cls, nom):
        ruchesParrainees = []
        for i in cls.parrainages:
            if cls.parrainages[i][0] == nom:
                ruchesParrainees.append(i)

        print(
            f"{len(ruchesParrainees)} ruches parrainées par {nom} : {' ; '.join(ruchesParrainees)}"
        )
        print(
            f"Valeur totale : {sum([cls.parrainages[i][1] for i in ruchesParrainees])} €"
        )


r1 = RucheParrainee(
    "Bois de Houx a2",
    [
        (32.6, 31.9),
        (32.7, 31.6),
        (32.8, 31.8),
        (32.9, 31.6),
        (33.1, 32.9),
        (33.1, 32.7),
        (33.2, 31.9),
        (33.4, 33.1),
    ],
    [50, 80, 60, 50, 80, 80, 0, 80, 20, 10],
    "Alfred",
    3500,
)
r2 = RucheParrainee(
    "Bois de Houx a3",
    [
        (32.6, 31.9),
        (32.7, 31.6),
        (32.8, 31.8),
        (32.9, 31.6),
        (33.1, 32.9),
        (33.1, 32.7),
        (33.2, 31.9),
        (33.4, 33.1),
    ],
    [50, 80, 60, 50, 80, 80, 0, 80, 20, 10],
    "Alfred",
    4100,
)
r3 = RucheParrainee(
    "Bois de Houx a4",
    [
        (32.6, 31.9),
        (32.7, 31.6),
        (32.8, 31.8),
        (32.9, 31.6),
        (33.1, 32.9),
        (33.1, 32.7),
        (33.2, 31.9),
        (33.4, 33.1),
    ],
    [50, 80, 60, 50, 80, 80, 0, 80, 20, 10],
    "Gerard",
    2500,
)

RucheParrainee.afficheToutes("Alfred")

del r2

RucheParrainee.afficheToutes("Alfred")
