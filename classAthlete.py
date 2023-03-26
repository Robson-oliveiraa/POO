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

    def physicalTraining (self):
        phrases = ["Light weight baby!", "Yeeeaahh Bodyy", "Uoooouuuooo", "Yeah Baby", "Ligth weigth!"]
        print("Ok! vamos treinar físico hoje, Light weight baby!")
        print("Vamos fazer levantamento terra")
        liftWeight = input('Insira "levantar" para levantar o peso\nR: ')
        i = 0
        liftWeight = liftWeight.upper()
        while liftWeight != "LEVANTAR":
            liftWeight = input('Erro!!, parece que você inseriu a palavra errada tente novamente\nInsira "levantar" para levantar o peso\nR: ')
        while liftWeight == "LEVANTAR" and i < 5:
            print(phrases[i])
            i+=1
            liftWeight = input('Insira "levantar" para levantar o peso\nR: ')
            liftWeight = liftWeight.upper()
            if i == 5:
                print("Parabéns você fez 5 repetições com 120 kg")
        
    def printCard(self):
        upperSex = self.athleteSex.upper()
        if upperSex == "M":
            cor = "\033[32m"
        elif upperSex == "F":
            cor = '\033[31m'
        text(f"{cor}\nNome do Atleta: {self.athleteName}\n")
        text(f"Sexo do Atleta: {upperSex} \n")
        text(f"Força do Atleta: {self.strengthAthlete} \n")
        text(f"Melhor Lançamento do Atleta: {self.bestBid} \n")
        text(f"Condicionamento Fisico do Atleta: {self.physicist} \n")
        text(f"Tecnica do Atleta: {self.techniqueAthlete} \n")

    def arremessar(self):
        list = ["1","2","3","4","5","6","7","8","9","10"]
        print('Para fazer um arremesso escrava "ok"')
        choice = input("R: ")
        choice = choice.upper()
        while choice != "OK":
            invalid()
            choice = input("R: ")
            choice = choice.upper()
        if choice == "OK":   
            throwingStrength = str(input("Em uma escala de 1 a 10 escolha sua força de arremesso: "))

            while throwingStrength not in list:
                invalid()
                throwingStrength = str(input("Em uma escala de 1 a 10 escolha sua força de arremesso: "))
            else:
                throw = float(throwingStrength) + 10.00
                print(f"Parabéns você arremessou {throw} m")

    def pitchTraining(self):
        print("Ok, vamos treinar arremesso")
        self.arremessar()

    def treinarParaCompetição(self):
        print("Vamos treinar para a competição\nvamos fazer um treino mais pesado")
        print("Começando com físico")
        self.physicalTraining()
        print("E agora arremesso")
        self.arremessar()

    def treinar(self):
        list = ["1","2"]
        toTrain = input('Para treinar digite "ok"\nR: ')
        toTrain = toTrain.upper()
        while toTrain != "OK":
            invalid()
            toTrain = input('Para treinar digite "ok"\nR: ')
        if toTrain == "OK":
            typeTrain = str(input("Vamos treinar, escolha uma da opção de treino abaixo: \n[1]Físico\n[2]Arremesso\nR: "))
            while typeTrain not in list:
                invalid()
                typeTrain = str(input("Vamos treinar, escolha uma da opção de treino abaixo: \n[1]Físico\n[2]Arremesso\nR: "))
            if typeTrain == "1":
                self.physicalTraining()
            elif typeTrain == "2":
                self.pitchTraining()

    def receberFeedback(self):
        print("Agora dê um feedback para o atleta")
        feedBack = input("R: ")
        print("Obrigado pelo feedback ;)")

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

        