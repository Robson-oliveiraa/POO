# Integrantes do grupo 2º informática vespertino
# Douglas Arthur
# Jefferson Bruno
# Robson André
# Wandell Mota

from printSpecial import text
#criação da classe         
class athlete:
    #função construtora com atributos
    def __init__(self,name,sex,strength,bestBid,physicit,technique):

        self.athleteName = name
        self.athleteSex = sex
        self.strengthAthlete = strength
        self.bestBid = bestBid
        self.physicist = physicit
        self.techniqueAthlete = technique
    #metodo para definir qual o ganhador do jogo
    def defineWinner(self):
        #verifica se a primeira carta comparada a segunda é maior ou menos
        if self.comparison > self.comparison1:
            text(f"{self.printAttributos} {self.athleteName} é maior que carta {self.anotherLetter.athleteName}")
            text("Você ganhou a batalha")
            winner = 0
        else:
            text(f"{self.printAttributos} {self.anotherLetter.athleteName} é maior que da carta {self.athleteName}")
            text("Você perdeu a batalha")
            winner = 1
        return(
            #retorana quem ganha
            winner
        )
    #compara as cartas
    def compareLetter(self, anotherLetter, comparison, printAttributos):
        #setando alguns "atributos"
        self.comparison1 = " "
        self.comparsion = comparison
        self.printAttributos = printAttributos
        self.anotherLetter = anotherLetter
        #verificando qual é a comparação a ser feita
        if comparison == "forca":
            #compara um com outro
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
    #exibindo carta
    def displayInformation(self):
        text(f"Nome: {self.athleteName} Sexo: {self.athleteSex}\nForça: {self.strengthAthlete} Físico: {self.physicist} Melhor lançamento: {self.bestBid} técnica: {self.techniqueAthlete}")
    #criação de uma carta especial
    def setSpecialCard(self,var,playerCards):

        if var == True:
            text('Você tem uma carta ultra especial')
            #retira a primeira carta do jogador
            playerCards.pop(0)
            #set da carta especial
            specialCard = athlete('@$$$$@', '#', 999, 99.99, 999, 999)
            #adiciona a carta especial na primeira carta do jogador
            playerCards.insert(0,specialCard)