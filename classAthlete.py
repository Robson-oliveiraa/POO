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

    def definirGanhador(self):

        if self.comparison > self.comparison1:
            text(f"{self.printAttributos} {self.athleteName} é maior que carta {self.anotherLetter.athleteName}")
            ganhador = 0
        else:
            text(f"{self.printAttributos} {self.anotherLetter.athleteName} é maior que da carta {self.athleteName}")
            ganhador = 1
        return(
            ganhador
        )
    
    def compararCartas(self, anotherLetter, comparison, printAttributos):

        self.comparison1 = " "
        self.comparsion = comparison
        self.printAttributos = printAttributos
        self.anotherLetter = anotherLetter

        if comparison == "forca":
            self.comparison = self.strengthAthlete
            self.comparison1 = anotherLetter.strengthAthlete
        elif comparison == "melhorLancamento":
            self.comparison = self.bestBid
            self.comparison1 = anotherLetter.bestBid
        elif comparison == "fisico":
            self.comparison = self.physicist
            self.comparison1 = anotherLetter.physicist
        elif comparison == "tecnica":
            self.comparison = self.techniqueAthlete
            self.comparison1 = anotherLetter.techniqueAthlete

    def exibirInformacoes(self):

        text(f"{self.athleteName} {self.athleteSex} {self.strengthAthlete} {self.physicist} {self.bestBid} {self.techniqueAthlete}")

    def definirCartaExpecial(self,var,cartasDoJogador):

        if var == True:
            
            text('Você tem uma carta ultra espercial')
            cartasDoJogador.pop(0)
            cartaEspecial = athlete('@$$$$@', '#', 999, 99.99, 999, 999)
            cartasDoJogador.insert(0,cartaEspecial)