#!/usr/bin/env python2

import pygame
import random


WIDTH = 768
HEIGHT = 256
EFFECTIVE_WIDTH = 48
EFFECTIVE_HEIGHT = 16
FPS = 30

# Define Colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

## initialize pygame and create window
pygame.init()
pygame.mixer.init()  ## For sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("HORLOGE PONG")
clock = pygame.time.Clock()     ## For syncing the FPS

# 5*5 charmap
CHARMAP = {
    "A":[[1, 1, 1, 1, 1],
         [1, 0, 0, 0, 1],
         [1, 0, 0, 0, 1],
         [1, 1, 1, 1, 1],
         [1, 0, 0, 0, 1]],
    "B":[[1, 1, 1, 1, 1],
         [1, 0, 0, 0, 1],
         [1, 1, 1, 1, 0],
         [1, 0, 0, 0, 1],
         [1, 1, 1, 1, 1]],
    "C":[[1, 1, 1, 1, 1],
         [1, 0, 0, 0, 0],
         [1, 0, 0, 0, 0],
         [1, 0, 0, 0, 0],
         [1, 1, 1, 1, 1]],
    "D":[[1, 1, 1, 1, 0],
         [1, 0, 0, 0, 1],
         [1, 0, 0, 0, 1],
         [1, 0, 0, 0, 1],
         [1, 1, 1, 1, 0]],
    "E":[[1, 1, 1, 1, 1],
         [1, 0, 0, 0, 0],
         [1, 1, 1, 1, 0],
         [1, 0, 0, 0, 0],
         [1, 1, 1, 1, 1]],
    "?":[[0, 1, 1, 1, 0],
         [1, 0, 0, 0, 1],
         [0, 0, 0, 1, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0]]
}


def plot(x, y):
    pygame.draw.circle(screen, WHITE, (x*16+8, y*16+8), 8, 0)

def checkerboard():
    "plots a point every two pixels, creating a checkerboard pattern."
    for x in range(48):
        for y in range(16):
            if (x+y)%2 == 0:
                plot(x, y)

def plot_char(char, x, y):
    "plots a character at a given position."
    if char in CHARMAP:
        char = CHARMAP[char]
    else : 
        char = CHARMAP["?"]
    for i in range(5):
        for j in range(5):
            if char[i][j] == 1:
                plot(x+j, y+i)



## Game loop
running = True
while running:

    #1 Process input/events
    clock.tick(FPS)     ## will make the loop run at the same speed all the time
    for event in pygame.event.get():        # gets all the events which have occured till now and keeps tab of them.
        ## listening for the the X button at the top
        if event.type == pygame.QUIT:
            running = False



    #3 Draw/render
    screen.fill(BLACK)
    

    plot_char("A", 0, 0)
    plot_char("B", 6, 0)
    plot_char("C", 12, 0)

    ## Done after drawing everything to the screen
    pygame.display.flip()       

pygame.quit()