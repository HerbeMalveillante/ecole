import turtle
import random

INSTANT = False
COLOR = 0
MAXCOLOR = 16777215

if INSTANT:
    turtle.tracer(0,0)
turtle.speed(0)
turtle.hideturtle()
turtle.penup()
turtle.backward(200)
turtle.right(90)
turtle.forward(200)
turtle.left(90)
turtle.pendown()

def triangle(l,n):
    global COLOR

    if n == 0 :
        turtle.color("#"+"%06x" % random.randint(0, 0xFFFFFF))
        turtle.begin_fill()
        for i in range(3):
            turtle.penup()
            turtle.forward(l)
            turtle.left(120)
            turtle.pendown()
        turtle.end_fill()

    else :
        for i in range(3):
            triangle(l/2,n-1)
            turtle.penup()
            turtle.forward(l)
            turtle.left(120)
            turtle.penup()

triangle(500,7)
if INSTANT:
    turtle.update()
turtle.exitonclick()
