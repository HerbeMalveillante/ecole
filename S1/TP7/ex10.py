def nombreApparitionCaracteres(s):
    dico = {}

    dicoAccents = {"éèêẽë": "e", "ç": "c", "àâã": "a", "ù": "u"}

    newS = ""
    for i in s:
        for j in dicoAccents:
            if i in j:
                i = dicoAccents[j]
                break
        newS += i

    s = newS

    for i in s.lower():
        if i not in dico:
            dico[i] = 1
        else:
            dico[i] += 1

    return dico


print(nombreApparitionCaracteres("Coucou la famille comment ça va ?"))


def afficher(d):
    end = []
    for i in sorted(d.keys()):
        end.append((i, d[i]))
    return end


print(
    afficher(
        (nombreApparitionCaracteres("Portez ce whisky au vieux juge blond qui fume"))
    )
)
print(
    afficher((nombreApparitionCaracteres("Hervé et Hélène se sont rencontrés à Noël.")))
)
