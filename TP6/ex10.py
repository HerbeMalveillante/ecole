def listeMots(s):
    liste = s.split(" ")
    return liste

def nbMots(s):
    return len(listeMots(s))

def motsLesPlusLongs(s):
    liste = listeMots(s)
    maxLen = 0
    maxListe = []
    for i in liste:
        if len(i) > maxLen:
            maxListe = []
            maxListe.append(i)
            maxLen = len(i)
        elif len(i) == maxLen:
            maxListe.append(i)
    
    return maxListe

print(motsLesPlusLongs("Ceci est une phrase à tester"))