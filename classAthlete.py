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
        #Dica de como fazer ai em baixo, n esqueça de utilizar o self.

        print(" ") # igonra esse print, é só para n dar erro
        # if self.comparison > self.comparison1:
        #     print(f"{self.printAttributos} {self.athleteName} é maior que carta {self.anotherLetter.athleteName}")
        # else:
        #     print(f"{self.printAttributos} {self.anotherLetter.athleteName} é maior que da carta {self.athleteName}")

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

        self.definirGanhador()
        
        

        