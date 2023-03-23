# Integrantes do grupo 2º informática vespertino
# Douglas Arthur
# Jefferson Bruno
# Robson André
# Wandell Mota
from tkinter import *
import os

from printSpecial import text

class athlete:
    def __init__(self,name,sex,strength,bestBid,physicit,technique):
        self.athleteName = name
        self.athleteSex = sex
        self.strengthAthlete = strength
        self.bestBid = bestBid
        self.physicist = physicit
        self.techniqueAthlete = technique

    def letter(self):

        window = Tk()

        pastaApp = os.path.dirname(__file__)

        window.title("Cartas dos atletas de atletismo")
        window.config(width=360, height=500)
        imgAthelete = PhotoImage(file=pastaApp+"\\images/"+self.athleteName+".png")
        labelAthelete = Label(
            window,
            image=imgAthelete
        )
        labelAthelete.place(x=0, y=0)

        window.mainloop()

