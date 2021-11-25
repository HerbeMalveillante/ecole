from turtle import *
import random

speed(0)



class Toile():

    def __init__(self):
        self.dessineToile()
        self.posMouches = []

    def dessineToile(self):

        tracer(0,0)

        posStart = pos()
        for i in range(200):
            forward(i/2)
            right(25)

        for i in range(6):
            up()
            right(60)
            goto(posStart)
            down()
            forward(250)

        update()
    
    def ajouteMouche(self):

        while True :
            x = random.randint(-150, 150)
            y = random.randint(-200, 200)
            if (x, y) not in self.posMouches:
                self.posMouches.append((x, y))
                break
        
        self.mouche((x,y), random.randint(0, 360))
                

    @staticmethod
    def mouche(coord, angle):
        setheading(angle)
        up()
        goto(coord)
        down()
        begin_fill()
        circle(10,110)
        left(60)
        circle(10,110)
        end_fill()
        begin_fill()
        circle(10,110)
        left(60)
        circle(10,110)
        forward(5)
        end_fill()
        begin_fill()
        circle(4)
        end_fill()



    

t = Toile()

for i in range(100):
    t.ajouteMouche()

exitonclick()