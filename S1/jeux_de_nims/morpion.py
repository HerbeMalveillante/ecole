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

        self.geometry("800x642")
        self.title("Morpion de Nim")

        # label = ttk.Label(self, text="Tkinter window")
        # label.config(font=("Comic Sans MS",40))
        # label.pack()

        self.canvas = tk.Canvas(self, height=642, width=642)
        self.canvas.pack(side="left")
        self.frame = tk.LabelFrame(self, text="info")
        self.frame.pack(side="right", fill="both", expand="yes")
        self.label = tk.Label(self.frame, text="yooo")
        self.label.pack()

    def drawGrid(self):
        self.canvas.create_line((0, 214), (642, 214), width=10)
        self.canvas.create_line((0, 428), (642, 428), width=10)
        self.canvas.create_line((214, 0), (214, 642), width=10)
        self.canvas.create_line((428, 0), (428, 642), width=10)


root = MorpionNim()
root.drawGrid()

root.mainloop()
