from unittest import mock
import pygame

WIDTH = 768
HEIGHT = 256
EFFECTIVE_WIDTH = 48
EFFECTIVE_HEIGHT = 16
FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


letters = {

    ":":[
        [0],
        [1],
        [1],
        [0],
        [0],
        [1],
        [1],
        [0]
    ],

    "0":[
        [0,1,1,1,0],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [0,1,1,1,0],

    ],

    "1":[
        [0,0,0,0,1],
        [0,0,0,1,1],
        [0,0,1,0,1],
        [0,1,0,0,1],
        [1,0,0,0,1],
        [0,0,0,0,1],
        [0,0,0,0,1],
        [0,0,0,0,1]
    ]


}


smol_letters = {
    "0":[
        [0,1,1],
        [1,0,1],
        [1,0,1],
        [1,0,1],
        [1,1,0]
    ],
    "1":[
        [0,1,0],
        [1,1,0],
        [0,1,0],
        [0,1,0],
        [1,1,1]
    ],
    "2":[
        [1,1,0],
        [0,0,1],
        [0,1,0],
        [1,0,0],
        [1,1,1]
    ],
    "3":[
        [1,1,0],
        [0,0,1],
        [1,1,0],
        [0,0,1],
        [1,1,0]
    ],
    "4":[
        [1,0,1],
        [1,0,1],
        [0,1,1],
        [0,0,1],
        [0,0,1]
    ],
    "5":[
        [1,1,1],
        [1,0,0],
        [1,1,0],
        [0,0,1],
        [1,1,0]
    ],
    "6":[
        [0,1,1],
        [1,0,0],
        [1,1,0],
        [1,0,1],
        [0,1,1]
    ],
    "7":[
        [1,1,1],
        [0,0,1],
        [0,1,0],
        [0,1,0],
        [0,1,0]
    ],
    "8":[
        [0,1,1],
        [1,0,1],
        [0,1,0],
        [1,0,1],
        [1,1,0]
    ],
    "9":[
        [1,1,0],
        [1,0,1],
        [0,1,1],
        [0,0,1],
        [1,1,0]
    ],

    "/":[
        [0,0,0],
        [0,0,1],
        [0,1,0],
        [1,0,0],
        [0,0,0]
    ]
}



## initialize pygame and create window
pygame.init()
pygame.mixer.init()  ## For sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("HORLOGE PONG")
clock = pygame.time.Clock()     ## For syncing the FPS

def plot(x, y):
    pygame.draw.circle(screen, WHITE, (x*16+8, y*16+8), 8, 0)

def plot_letter(letter, x, y):
    if letter in letters:
        for i in range(len(letters[letter])):
            for j in range(len(letters[letter][i])):
                if letters[letter][i][j] == 1:
                    plot(x+j, y+i)
def plot_letter_smol(letter,x,y):
    if letter in smol_letters:
        for i in range(len(smol_letters[letter])):
            for j in range(len(smol_letters[letter][i])):
                if smol_letters[letter][i][j] == 1:
                    plot(x+j, y+i)


def mockup_classique():
    plot_letter("1", 9, 1)
    plot_letter("0", 16, 1)
    plot_letter(":", 23, 1)
    plot_letter("1", 26, 1)
    plot_letter("0", 33, 1)

    for indice, i in enumerate("29/07/2022"):
        plot_letter_smol(i, indice*4+4, 10)

def mockup_pong():
    
    plot(0, 3)
    plot(1, 3)
    plot(0, 4)
    plot(1, 4)
    plot(0, 5)
    plot(1, 5)
    plot(0, 6)
    plot(1, 6)

    plot(47, 8)
    plot(46, 8)
    plot(47, 9)
    plot(46, 9)
    plot(47, 10)
    plot(46, 10)
    plot(47, 11)
    plot(46, 11)

    plot_letter_smol("1", 15, 0)
    plot_letter_smol("0", 19, 0)
    plot_letter_smol("0", 26, 0)
    plot_letter_smol("9", 31, 0)

    plot(15,10)


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

    mockup_pong()

    ## Done after drawing everything to the screen
    pygame.display.flip()       

pygame.quit()