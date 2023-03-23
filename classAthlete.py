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

        if self.athleteSex == "M" or self.athleteSex == 'm':
            text(f"\033[0;33m\nNome do Atleta: {self.athleteName}\n")
            text(f"\033[0;33mSexo do Atleta: {self.athleteSex} \n")
            text(f"\033[0;33mForça do Atleta: {self.strengthAthlete} \n")
            text(f"\033[0;33mMelhor Lançamneto do Atleta: {self.bestBid} \n")
            text(f"\033[0;33mCondicionamento Fisico do Atleta: {self.physicist} \n")
            text(f"\033[0;33mTecnica do Atleta: {self.techniqueAthlete} \n")

        elif self.athleteSex == "F" or self.athleteSex == 'f':
            text(f"\033[0;33m\nNome da Atleta: {self.athleteName}\n")
            text(f"\033[0;33mSexo da Atleta: {self.athleteSex} \n")
            text(f"\033[0;33mForça da Atleta: {self.strengthAthlete} \n")
            text(f"\033[0;33mMelhor Lançamneto da Atleta: {self.bestBid} \n")
            text(f"\033[0;33mCondicionamento Fisico da Atleta: {self.physicist} \n")
            text(f"\033[0;33mTecnica da Atleta: {self.techniqueAthlete} \n")

        else:
            text("Digite 'F' ou 'f' para atletas femininos e 'M' ou 'm' para atletas masculinos")

        window.mainloop()