import turtle
import math

turtle.speed(0)

def dragon(l, n, c):
  
    turtle.color("red")

    if n == 0 :
        turtle.forward(l)
    else :

        # h^2 = a^2 + b^2
        # or a = b
        # h^2 = 2*a^2
        # a^2 = h^2/2
        # a = sqrt(h^2/2)

        newLen = math.sqrt(l**2 / 2)
        turtle.left(45)
        dragon(newLen, n-1, c)
        turtle.right(90)
        dragon(newLen, n-1, c)
        turtle.left(45)

# dragon(100, 8, "red")

def dragon_gauche(l,n,c):
    turtle.color("red")

    if n == 0 :
        turtle.forward(l)
    else :

        # h^2 = a^2 + b^2
        # or a = b
        # h^2 = 2*a^2
        # a^2 = h^2/2
        # a = sqrt(h^2/2)

        newLen = math.sqrt(l**2 / 2)
        turtle.left(45)
        dragon_gauche(newLen, n-1, c)
        turtle.right(90)
        dragon_droite(newLen, n-1, c)
        turtle.left(45)

def dragon_droite(l,n,c):
    turtle.color("red")

    if n == 0 :
        turtle.forward(l)
    else :

        # h^2 = a^2 + b^2
        # or a = b
        # h^2 = 2*a^2
        # a^2 = h^2/2
        # a = sqrt(h^2/2)

        newLen = math.sqrt(l**2 / 2)
        turtle.right(45)
        dragon_gauche(newLen, n-1, c)
        turtle.left(90)
        dragon_droite(newLen, n-1, c)
        turtle.right(45)

dragon_gauche(100, 8, "red")