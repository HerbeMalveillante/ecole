import turtle


def trapeze(base, cote, sup, couleur):

    turtle.fillcolor(couleur)
    turtle.begin_fill()
    turtle.forward(base)
    turtle.left(120)
    turtle.forward(cote)
    turtle.left(60)
    turtle.forward(sup)
    turtle.left(60)
    turtle.forward(cote)
    turtle.left(120)
    turtle.end_fill()
    turtle.left(60)
    turtle.forward(cote)
    turtle.right(60)


def triangle(longueur, couleurs):

    for i in range(3):
        trapeze(
            longueur / 3 * (3 - i), longueur / 3, longueur / 3 * (2 - i), couleurs[i]
        )

    input("")


triangle(300, ["orange", "purple", "red"])
