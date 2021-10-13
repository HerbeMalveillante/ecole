def verif(s):
    stringPair = ""
    stringImpair = ""

    # création des deux trucs
    for i in range(len(s)):
        if i %2 == 0: # pair
            stringPair += s[i]
        else : # impair
            stringImpair += s[i]

    # check de la taille du truc
    if len(s)%2 != 0:
        return False
    
    existingLetters = []
    for i in stringPair:
        if i in existingLetters:
            return False 
        else : 
            existingLetters.append(i)
    
    existingLetters = []
    for i in stringImpair:
        if i in existingLetters:
            return False 
        else : 
            existingLetters.append(i)
    
    return True

def saisieCle():
    while True:
        entree = input("entrez une clef :")
        if verif(entree) :
            return entree

def eclate(key):
    stringPair = ""
    stringImpair = ""

    # création des deux trucs
    for i in range(len(key)):
        if i %2 == 0: # pair
            stringPair += key[i]
        else : # impair
            stringImpair += key[i]
    
    return (stringPair, stringImpair)

def cryptage(s, cle):

    pair, impair = eclate(cle)

    crypte = ""

    for i in s : 
        if i in pair :
            crypte += impair[pair.index(i)]
        else :
            crypte += i

    return crypte 

print(cryptage("maman a tort","myturtleiskind"))