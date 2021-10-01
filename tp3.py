# TP3 Python
import math
import random
import turtle

def exercice1():

    def factoriel(n):
        resu=1
        for i in range(1, n+1):
            resu = resu*i
        return resu

    print(factoriel(0))

    # factoriel(0) retourne 1

    def somme(n):

        total = 0
        for i in range(n+1):
            total += 1/factoriel(i)
        return(total)

    print(somme(5))

    def estimation(delta):
        euler = round(math.exp(1), delta)
        for i in range(10000):
            if round(somme(i), delta) == euler:
                return(i)
        return("error ! No match found for this precision")

    print(estimation(20))

def exercice2():

    def termeSuite1(m,n):
        u=m
        for i in range(1, n+1):
            u = u**2 - 5
        return u

    print(termeSuite1(4, 3))

    # m correspond à u_0 tandis que n correspond au rang qu'on désire calculer

    # 3. en faisant ça, on fait l'inverse puisqu'on a inversé la position des paramètres m et n

    def sommeTermes(n, x):
        
        u = x
        somme = u
        for i in range(1, n+1):
            u = 3/u
            somme+=u
        
        return somme

    print(sommeTermes(5, 3.2))


def exercice3():

    def fct(n):
        m = 2*n

        return (n,m)


    # fct() retourne un tuple

    def division_euclidienne(dividende, diviseur):
        # return(dividende//diviseur, dividende%diviseur)

        q = 0
        r = dividende
        while r >= diviseur:
            q += 1
            r = r-diviseur
        return(q, r)

    def verification_automatique():

        for i in range(100):
            q = random.randint(1, 1000)
            d = random.randint(1, 1000)
            
            if (q//d, q%d) != division_euclidienne(q, d):
                return False
            
        return True


    verification_automatique()


def exercice4():

    def estPremier(n):return False if any([n%i == 0 for i in range(2, n)]) else True
    def crible(maxi):return [i if estPremier(i) else 0 for i in range(1,maxi)]
    def crible_list(maxi): return [ j for j in [i if estPremier(i) else None for i in range(2, maxi)] if j]
    def verifList(list): return all([estPremier(i) for i in list])

    print(crible(10))
    print(crible_list(16))
    print(verifList([1,2,3,4,5,6]))
    print(verifList(crible_list(20)))

def exercice5():
    
    def estPremier(n):return False if any([n%i == 0 for i in range(2, n)]) else True
    def crible_list(maxi): return [ j for j in [i if estPremier(i) else None for i in range(2, maxi)] if j]

    def euclide(a, b):

        while True:
            if b == 0 :
                return a
            r = a%b
            a = b
            b = r
    
    def verifManuelle():return all([euclide(221, 782) == 17, euclide(1000,56)==8, euclide(555,333)==111, euclide(1234,34)==2])

    def verifAuto():

        crible = crible_list(150)

        for i in range(100):
            p,m1,m2 = random.choices(crible, k=3)

            if euclide(p*m1, p*m2) != p and m1 != m2:
                return True


        return False


    print(verifAuto())

def exercice6():

    def cube(x):
        return(3*x, x**3)
    
    a,b = cube(2)
    print(a, b)

    # cette fonction retourne un tuple.
    # on assigne deux variables à la fois.


def exercice7():

    def verification_base(chaine, base):return all([int(i) < base for i in chaine])


    def str_vers_int(n, b):
        if n == 0:
            return [0]
        digits = []
        while n:
            digits.append(int(n % b))
            n //= b
        return digits[::-1]


    print(verification_base([1, 2, 3, 4, 5, 6], 3))

    print(str_vers_int("8", 2))


def exercice10():

    def triangle(etages):


        output = []
        spaces = etages-1

        while spaces >= 0:
            output.append(" "*spaces + ((2*etages-1)-2*spaces)*"X" + " "*spaces )
            spaces -=1

        return output


    def sapin(etages):

        output = []

        tri = triangle(etages*2)
        
        for i in range(etages) :
            troisLignes = tri[i:i+3]
            output+=troisLignes

        for i in range(etages):
            largeur = len(tri[-1])
            spaces = int((largeur-3) / 2)

            output.append(" "*spaces + "I"*3 + " "*spaces)

        return output



    def triangleTurtle(LONGUEUR):

        if not turtle.isdown():
            turtle.pendown()
        
        turtle.color("black", "green")

        turtle.begin_fill()
        for i in range(3):
            turtle.forward(LONGUEUR)
            turtle.left(120)
        turtle.end_fill()


        

        
    
    def tronc(LONGUEUR):

        if not turtle.isdown():
            turtle.pendown()

        turtle.color("black", "brown")

        turtle.begin_fill()
        for i in range(4):
            turtle.forward(LONGUEUR)
            turtle.left(90)
        turtle.end_fill()

    def sapinTurtle(etages, LONGUEUR):

        
        sapinChar = sapin(etages)

        for ligne in sapinChar:
            for char in ligne:
                if char == "X":
                    triangleTurtle(LONGUEUR)
                elif char == "I":
                    tronc(LONGUEUR)

                if turtle.isdown():
                    turtle.penup()
                turtle.forward(LONGUEUR)


            if turtle.isdown():
                turtle.penup()
            turtle.forward(LONGUEUR)
            turtle.backward(LONGUEUR*(len(sapinChar[-1])+1))
            turtle.right(90)
            turtle.forward(LONGUEUR)
            turtle.left(90)

    def foret(sapins):
        turtle.hideturtle()
        turtle.speed(0)
        taille = turtle.screensize()

        for i in range(1000):
            turtle.penup()
            turtle.goto(random.randint(-400, 400), random.randint(-400, 400))
            turtle.pendown()
            sapinTurtle(random.randint(2, 7), random.randint(5, 10))

    
        input("")


    foret(10)

exercice10()













# >o)
# (_> HM