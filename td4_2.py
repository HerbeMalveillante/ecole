import turtle


def sontPairs(x,y):
    if x%2 == 0 and y%2 == 0:
        return True
    else : 
        return False

def sontPairsListe(liste):return True if all([i%2==0 for i in liste]) else False


def f(x):
    if x>0:
        return 2*x, x+2


def fact(n):
    n = int(n)
    total = 1
    for i in range(n):
        total = total * (i+1)

    return total

def afficheTroisFactorielles():
    solutions = []
    for i in range(100,1000):
        nombreStr = str(i)
        a, b, c = nombreStr
        if fact(a) + fact(b) + fact(c)== i:
            solutions.append(i)


    print(solutions)

def fleurVie(rayon):
    turtle.speed(0)
    for i in range(6):
        turtle.circle(rayon)
        turtle.right(60)
    
    turtle.penup()
    turtle.right(90)
    turtle.forward(rayon)
    turtle.left(90)
    turtle.pendown()
    turtle.circle(rayon)
    turtle.penup()
    turtle.left(90)
    turtle.forward(rayon)
    turtle.right(90)
    turtle.pendown()


import random

def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    turtle.color(R, G, B)

for i in range(360):
    fleurVie(150)
    change_color()
    turtle.right(1)