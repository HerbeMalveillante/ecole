import math


def exercice_1():


    def perimetre(rayon):
        return 2 * math.pi * rayon
    
    def aire(rayon):
        return math.pi * rayon**2

    def demandeRayon():
        answer = -1
        while answer < 0:
            answer = float(input("Entrez le rayon du cercle : "))
        
        return answer

    def pous():
        answer = None
        while answer not in ["p", "s"]:
            answer = input("Entrez p ou s : ")
        return answer
    
    def final():
        fonction = pous()

        if fonction == "p":
            print(perimetre(demandeRayon()))
        else : 
            print(aire(demandeRayon()))

    final()

exercice_1()