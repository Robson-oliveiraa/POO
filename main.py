# 2 º informática vespertino
# integrantes
# Douglas Arthur da Silva Bento
# Jefferson Bruno de Sousa Marconde
# Robson André Reis de Oliveira
# Wandell da Costa Mota

from classAthlete import athlete

def cartaDouglas():
    athleteAndre = athlete("Andre","M","910","15,7m","510","810")
    athleteAndre.exibirInformacoes() 

def cartaExtra():
    Beth = athlete("Beth", "f", "770", "7,52 m", "820", "650")
    Beth.exibirInformacoes()

def cartaJeff():

    Ana = athlete("Ana", "F", "620" , "19,0 m" , "870" , "640")
    Ana.exibirInformacoes()

def cartaRobson():
    #Carta Robson:
    Geisa = athlete("Geisa","F","800","9.19m","710","590")
    Geisa.exibirInformacoes()  

def cartaWandell():
    Darlan = athlete ("Darlan", "m", "940", "16,16 m" ,"750" ,"485")
    Darlan.exibirInformacoes()

cartaDouglas()
cartaExtra()
cartaJeff()
cartaRobson()
cartaWandell()