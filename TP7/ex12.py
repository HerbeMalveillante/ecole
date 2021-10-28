def ajouter(index, entree, numero):
    if entree not in index :
        index[entree] = [numero]
    else : 
        if numero in index[entree]:
            print("numéro de page déjà dans l'index à cette entrée.")
        else : 
            index[entree].append(numero)
    
def listeNumeroDePage(l):
    return " ".join([str(i) for i in l])

def afficherIndex(index):
    for i in index :
        pages = listeNumeroDePage(sorted(index[i]))
        print(f"{i} : {pages}")

index={}
ajouter(index, 'Liste', 32)
ajouter(index, 'Liste', 58)
ajouter(index, 'Liste', 47)
ajouter(index, 'Dictionnaire', 58)
ajouter(index, 'Dictionnaire', 62)
ajouter(index, 'Python', 14)
ajouter(index, 'Python', 32)
ajouter(index, 'Python', 29)
afficherIndex(index)

def creationIndexPages(index):
    indexPages = {}

    for i in index :
        for page in index[i]:
            if page not in indexPages:
                indexPages[page] = [i]
            else :
                indexPages[page].append(i)
    
    return indexPages

def listeEntree(l):
    return " ".join(l)

def afficherIndexPages(indexPages):
    for i in sorted(indexPages.keys()) :
        pages = listeEntree(sorted(indexPages[i]))
        print(f"{i} : {pages}")

afficherIndexPages(creationIndexPages(index))