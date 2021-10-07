import turtle
turtle.speed(0)
turtle.hideturtle()

def motif(rayon):
    pos = turtle.pos()
    theta = turtle.heading()
    turtle.right(200)
    r = rayon
    turtle.fillcolor("blue")
    for i in range(5):
        turtle.begin_fill()
        turtle.circle(r+i*5, -360)
        turtle.end_fill()
        turtle.circle(r+i*5, -150)
        turtle.right(180)
    for i in range(4):
        turtle.begin_fill()
        turtle.circle(r+(3-i)*5, 360)
        turtle.end_fill()
        turtle.circle(r+(3-i)*5, 150)
        turtle.right(180)

    turtle.penup()
    turtle.goto(pos)
    turtle.setheading(theta)
    turtle.pendown()



def repetition(rayon):

    for i in range(6):
        turtle.penup()
        turtle.circle(rayon*8, 60)
        turtle.pendown()
        motif(rayon)
    
    turtle.penup()
    turtle.left(90)
    turtle.forward(rayon*7)
    turtle.right(90)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(rayon)
    turtle.end_fill()

    input("")

    

repetition(5)