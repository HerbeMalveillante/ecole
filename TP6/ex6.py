def apparitions(s1, s2):
    indexes = []
    for index, i in enumerate(s1):
        if s1[index:index+len(s2)] == s2:
            indexes.append(index)
    return indexes

print(apparitions("Le mot texte apparaît deux fois dans ce texte.", "texte"))

def soulignement(s1, s2):
    i = 0
    output = ""
    while i < len(s1):
        if s1[i:i+len(s2)] == s2:
            output += "-"*len(s2)
            i += len(s2)
        else :
            output += " "
            i+=1
    
    print(s1)
    print(output)

soulignement("Le mot texte apparaît deux fois dans ce texte.", "texte")
