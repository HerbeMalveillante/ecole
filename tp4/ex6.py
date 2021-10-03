import math


def approximation():

    n = int(input("Entrez un entier naturel n : "))
    x = -1.0
    while x <= 0 :
        x = float(input("Entrez un réel x > 0 : "))

    

    for i in range(n+1):
        if i == 0 :
            u = x
            v = 1
        else :
            u, v = (u+v)/2 , (2*u*v)/(u+v) 
        
        print(f"u_{i} = {u} | v_{i} = {v}")
    
    print(f"Racine carrée de {x} = {math.sqrt(x)}")


def approximation2():

    x = -1.0
    while x < 0 :
        x = float(input("Entrez un réel x >= 0 : "))
    
    d = -1.0
    while d <= 0 :
        d = float(input("Entrez un réel d > 0 : "))

    u = x
    v = 1

    racine = math.sqrt(x)

    i = 0
    while u - racine > d and racine - v > d:
        u, v = (u+v)/2 , (2*u*v)/(u+v)
        i += 1
    
    print(f"Valeur appr. de sqrt({x}) à {d} près : ")
    print(f"Par défaut : {v}")
    print(f"Par excès : {u}")
    print(f"obtenues au rang {i}")