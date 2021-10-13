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
    
    lastLetter = None
    for i in stringPair:
        if i == lastLetter:
            return False
        else :
            lastLetter = i
    
    lastLetter = None
    for i in stringImpair:
        if i == lastLetter:
            return False
        else :
            lastLetter = i
    
    return True

