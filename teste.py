class athlete:
    def __init__(self,name,sex,strength,bestBid,physicit,technique):
        self.athleteName = name
        self.athleteSex = sex
        self.strengthAthlete = strength
        self.bestBid = bestBid
        self.physicist = physicit
        self.techniqueAthlete = technique

    def compararCartas(self, anotherLetter, comparison, printAttributos):

        if comparison == "forca":
            comparison = self.strengthAthlete
            comparison1 = anotherLetter.strengthAthlete
        elif comparison == "melhorLancamento":
            comparison = self.bestBid
            comparison1 = anotherLetter.bestBid
        elif comparison == "fisico":
            comparison = self.physicist
            comparison1 = anotherLetter.physicist
        
        
        if comparison > comparison1:
            print(f"{printAttributos} {self.athleteName} é maior que {anotherLetter.athleteName}")
        else:
            print(f"{printAttributos} {anotherLetter.athleteName} é maior que {self.athleteName}")