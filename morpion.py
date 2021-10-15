# si on commence on a gagné : on doit s'arranger pour faire un carré : 

# grille de trois par trois (peut être représenté par un nombre en binaire de huit bits)
# chaque tour, on place une, deux, ou trois croix sur une même ligne ou colonne (pas en diagonale)
# le joueur qui place la dernière croix a gagné.

# Le plus simple resterait de faire une interface graphique avec tkinter et un canvas


import tkinter as tk
from tkinter import ttk


class MorpionNim(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("640x640")
        self.title("Title Here")

        # label = ttk.Label(self, text="Tkinter window")
        # label.config(font=("Comic Sans MS",40))
        # label.pack()

        self.canvas = tk.Canvas(self, height=640, width=640)
        self.canvas.pack()
    
    def drawGrid(self):
        

root = MorpionNim()
 
root.mainloop()

