maListe = list("Un Texte")
print(maListe)
monEnsemble = set("Un Texte")
print(monEnsemble)

# la conversion en set retourne le string sans doublons
def memesLettres(s1, s2):
    return set(s1) == set(s2)


s1 = "abdccd"
s2 = "caabddd"
s3 = "bcd"

print(memesLettres(s1, s2))
print(memesLettres(s2, s3))
