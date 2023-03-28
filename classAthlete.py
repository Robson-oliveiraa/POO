# Integrantes do grupo 2º informática vespertino
# Douglas Arthur
# Jefferson Bruno
# Robson André
# Wandell Mota
from tkinter import *
import os
from printSpecial import text

cor = ""

def invalid ():
    print("Erro, você inseriu algo invalido, tente novamente")
             
class athlete:
    def __init__(self,name,sex,strength,bestBid,physicit,technique):
        self.athleteName = name
        self.athleteSex = sex
        self.strengthAthlete = strength
        self.bestBid = bestBid
        self.physicist = physicit
        self.techniqueAthlete = technique

    def exibirInformacoes(self):

        window = Tk()

        pastaApp = os.path.dirname(__file__)

        window.title(self.athleteName)
        window.config(width=360, height=500)
        imgAthelete = PhotoImage(file=pastaApp+"\\images/"+self.athleteName+".png")
        labelAthelete = Label(
            window,
            image=imgAthelete
        )
        labelAthelete.place(x=0, y=0)
        upperSex = self.athleteSex.upper()

        if upperSex == "M":
            self.printCard()
            self.arremessar()
            self.treinar()
            self.treinarParaCompetição()
            self.receberFeedback()
            window.mainloop()


        elif upperSex == "F":
            self.printCard()
            self.arremessar()
            self.treinar()
            self.treinarParaCompetição()
            self.receberFeedback()
            window.mainloop()

        else:
            text("Digite 'F' ou 'f' para atletas femininos e 'M' ou 'm' para atletas masculinos")

        