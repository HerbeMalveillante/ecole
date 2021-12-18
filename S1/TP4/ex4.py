import turtle
import colorsys


turtle.speed(0)


def polygone(taille, nbCotes):
    for i in range(nbCotes):
        turtle.forward(taille)
        turtle.left(360 / nbCotes)


def rosace(taille, nbCotes):
    for i in range(36):
        polygone(taille, nbCotes)
        turtle.right(10)


def rosaceColoree(taille, nbCotes):
    """Fonctionne quelque soit le nombre de polygones qu'on veut"""

    N = 36  # N représente le nombre de polygones
    HSV_tuples = [(x * 1.0 / N, 0.5, 0.5) for x in range(N)]
    RGB_tuples = map(lambda x: colorsys.hsv_to_rgb(*x), HSV_tuples)

    for i in RGB_tuples:
        turtle.color(i)
        polygone(taille, nbCotes)
        turtle.right(360 / N)


def rosaceColoree2(taille, nbCotes):
    """Sans utiliser colorsys, donc uniquement avec 36 polygones"""

    for i in range(36):
        if i < 12:
            color = ((1 / 12) * ((i + 1) % 12), 0, 0)
        elif i < 24:
            color = (0, (1 / 12) * ((i + 1) % 12), 0)
        else:
            color = (0, 0, (1 / 12) * ((i + 1) % 12))

        print(color)
        turtle.color(color)

        polygone(taille, nbCotes)
        turtle.right(10)


rosaceColoree(75, 5)
input("")
