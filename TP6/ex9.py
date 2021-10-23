import turtle
import math

turtle.penup()
turtle.goto(-(turtle.screensize()[0] / 2), -(turtle.screensize()[1] / 2))
turtle.pendown()


def affichePendu(n):
    if n == 1:
        turtle.forward(10)
        turtle.backward(5)
    elif n == 2:
        turtle.left(90)
        turtle.forward(150)
    elif n == 3:
        turtle.right(90)
        turtle.forward(75)
    elif n == 4:
        turtle.backward(75)
        turtle.left(90)
        turtle.backward(20)
        turtle.right(45)
        turtle.forward(math.sqrt(2 * 20 ** 2))
    elif n == 5:
        turtle.right(45)
        turtle.forward(55)
        turtle.right(90)
        turtle.forward(20)
    elif n == 6:
        turtle.right(90)
        turtle.begin_fill()
        turtle.circle(5)
        turtle.end_fill()
        turtle.circle(5, 180)
    elif n == 7:
        turtle.right(90)
        turtle.forward(50)
    elif n == 8:
        turtle.backward(30)
        turtle.left(90)
        turtle.backward(10)
        turtle.forward(20)
    elif n == 9:
        turtle.backward(10)
        turtle.right(90)
        turtle.forward(30)
        turtle.left(30)
        turtle.forward(30)
    elif n == 10:
        turtle.backward(30)
        turtle.right(60)
        turtle.forward(30)


def testPendu():
    for i in range(10):
        affichePendu(i + 1)


def initMot(mot):
    return (mot[0] + "*" * (len(mot) - 2) + mot[-1]).lower()


def remplaceCar(mot, ch, c):
    motList = [i for i in mot]
    chList = [i for i in ch]
    for i in range(len(mot)):
        if motList[i] == c and chList[i] == "*":
            chList[i] = c
    return "".join(chList)


def joue(mot):
    motCache = initMot(mot)

    n = 0
    while motCache != mot:
        print(motCache)
        print(n)
        entree = input("Rentrez une lettre : ")[0]
        remplace = remplaceCar(mot, motCache, entree)
        if remplace == motCache and entree not in mot:
            n += 1
            affichePendu(n)
        else:
            motCache = remplace

        if n >= 10:
            print("Perdu !")
            print(f"Le mot était {mot}")
            break
    print("Partie terminée !")


joue(input("Entrez un mot à faire deviner : "))


turtle.exitonclick()
