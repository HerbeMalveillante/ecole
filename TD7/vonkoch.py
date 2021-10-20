import turtle

turtle.speed(0)
turtle.tracer(0,0)

colors = ['red', 'green', 'blue', 'pink', 'purple']

def segment(l,n):
    if n == 0:
        turtle.forward(l)
    else :
        segment(l/3,n-1)
        turtle.left(60)
        segment(l/3, n-1)
        turtle.right(120)
        segment(l/3, n-1)
        turtle.left(60)
        segment(l/3, n-1)

def triangle(l,n):
    turtle.begin_fill()
    for i in range(3):
        segment(l,n)
        turtle.right(120)
    turtle.end_fill()

for i in range(5):
    turtle.color(colors[i])
    triangle(300, 5-i-1)
turtle.update()
turtle.exitonclick()