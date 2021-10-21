import random

# Question 1
def afficheTermeUn(n):
    for i in range(n+1):
        if i == 0:
            u = 0.5
        else :
            u = 1/(u+1)**2 - 1/4
        
        print("u_"+str(i) + " = " + str(u))

afficheTermeUn(3)

# Question 2
def calculeTermeVn(n):
    for i in range(n+1):
        if i == 0:
            v_0 = -2
            v_1 = 1
        else :
            nouveauV = 2*v_1 - 3*v_0**2 + 1 
            v_0 = v_1
            v_1 = nouveauV
    
    return v_0

print(calculeTermeVn(4))

# Question 3
def sommeTermes(p, x):
    somme = 0
    for i in range(p+1):
        if i == 0:
            w = x
        else :
            w = 4*w-1
        
        somme+=w
    
    return w

print(sommeTermes(5, 1.2))

# Question 4
def saisie():
    entree = -1
    while True :
        entree = input("Entrez un nombre entier supérieur ou égal à 1 : ")
        try :
            entree = int(entree)
        except : 
            continue
        if entree >= 1 :
            break
    return entree


    

def saisieSansTry():

    def check(entree):
        chiffres = "0123456789"
        for char in entree :
            if char not in chiffres :
                return False  
        return True 

    while True :
        entree = input("Entrez un nombre entier supérieur ou égal à 1 : ")

        # on vérifie que entrée ne possède que des chiffres
        if not check(entree) :
            continue
        if int(entree) >= 1:
            break
    return entree

print(saisieSansTry())




# Question 5
def alea(n, a, b):
    listeRandom = []
    for i in range(n):
        listeRandom.append(random.randint(a,b))
    
    return listeRandom

print(alea(10, 1, 18))

# Question 6
def aleaUnique(n,a,b):
    if (b - a) + 1 < n :
        print("Desolé, il n'est pas possible de créer une liste de valeurs uniques avec les arguments rentrés.")
        return

    # ici je fais pas l'algorithme le plus simple, mais celui
    # ci n'implique pas de temps d'execution aléatoire (= prendre un nombre au pif et
    # vérifier si il n'est pas déjà dans la liste), qui est une mauvaise pratique en
    # général.
    listeRandom = []
    choice = list(range(a,b+1))
    for i in range(n):
        listeRandom.append(choice.pop(random.randint(0, len(choice)-1)))
    return listeRandom

print(aleaUnique(10, 1, 15))


def aleaUnique2(n,a,b):
    if (b - a) + 1 < n :
        print("Desolé, il n'est pas possible de créer une liste de valeurs uniques avec les arguments rentrés.")
        return
    
    # cette version est moins optimisée mais plus simple à comprendre
    listeRandom = []
    while len(listeRandom) < n :
        choice = random.randint(a, b)
        if choice not in listeRandom:
            listeRandom.append(choice)
    return listeRandom

print(aleaUnique2(10, 1, 15))

# Question 7
def ecart(e):
    VALEUR_EXACTE = 0.32209960580139874
    i = 0
    while True :
        if i == 0:
            u = 0.5
        else :
            u = 1/(u+1)**2 - 1/4
        if abs(u - VALEUR_EXACTE) <= e:
            return i
        i+=1

print(ecart(0.0001))


