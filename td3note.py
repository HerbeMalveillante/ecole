# Pacôme Renimel--Lamiré
# Galdric Vigué
# Peip1 Maths

import math
import statistics
import random

def ecartType(population):

    # on pourrait utiliser le module statistics et sa fonction pstdev()
    # mais ça serait un peu de la triche alors on va le calculer à la main.
    
    # on commence par calculer la moyenne arithmétique de la liste.
    moyenne = sum(population)/len(population)

    # on calcule ensuite la somme des carrés de l'écart à la moyenne de chacune des valeurs de la série.

    sommeCarresEcart = sum([abs(i - moyenne)**2 for i in population])

    # on calcule ensuite l'écart type en prenant la racine carrée du résultat précédent divisé par l'effectif de la série.

    ecartTypeVar = math.sqrt(sommeCarresEcart/len(population))

    return ecartTypeVar


def demoExo5():

    listeSample = [6, 2, 3, 1]

    print(f"On calcule l'écart type d'une liste sample : {listeSample}")
    print(ecartType(listeSample))
    print("on peut comparer avec le resultat du module statistics :")
    print(statistics.pstdev(listeSample))
    print("on constate que le résultat est similaire.")

    print("on peut ensuite tester avec des grandes listes aléatoires :")
    print("-----------------")
    for i in range(5):
        print(ecartType([random.randint(1, 1000) for i in range(random.randint(300, 1000))]))
    print("On constate que même avec des listes aléatoires de grande taille, l'écart type est toujours assez similaire.")


def dixSuivants():
    depart = int(input("Rentrez votre nombre de départ : "))

    for i in range(10):
        if depart+1 > 1000:
            break
        else : 
            depart+=1
            print(depart)

def isPerfectSquare(number):
    return int(math.sqrt(number) + 0.5)**2 == number

def troisCarresParfaits():
    solutions = []
    for N in range(1000, 10000):

        # on vérifie dans un premier temps si N est un carré parfait.
        if not isPerfectSquare(N):
            continue # si non ce n'est même pas la peine de continuer

        # on isole les quatre chiffres qui composent N
        a = str(N)[0]
        b = str(N)[1]
        c = str(N)[2]
        d = str(N)[3]

        # on calcule P et Q
        P = int(c + b + a + d)
        Q = int(b + c + a + d)

        if isPerfectSquare(P) and isPerfectSquare(Q):
            solutions.append(N)
    return(solutions)



# lancer ces fonctions une par une dans l'ordre pour voir les resultats des exos.
"""
demoExo5()
dixSuivants()

"""
print(troisCarresParfaits())


# >o)
# (_> HM