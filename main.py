# 2 º informática vespertino
# integrantes
# Douglas Arthur da Silva Bento
# Jefferson Bruno de Sousa Marconde
# Robson André Reis de Oliveira
# Wandell da Costa Mota

import random
from classAthlete import athlete
import os
import time
from printSpecial import text

#Função para carregamento no terminal
def toLoad(text, str, times):
    for i in range(3):
        for i in range(times):
            points = str*i
            print(text, points)
            time.sleep(0.4)
            os.system("cls")
#Função do titulo
def printTitle(title):
    print("=============================")
    print("        Hello World!         ")
    print("=============================")
    print(f"{title}                     ")
#Comparar as cards de acordo com os atributos
def comparsion(firstLetter, secondLetter):
    if chooseAttribute == 0:
        firstLetter.compareLetter(secondLetter, "forca", "A força do(a) atleta da carta carta")
        
    elif chooseAttribute == 1:
        firstLetter.compareLetter(secondLetter, "fisico", "O físico do(a) atleta da carta carta")
        
    elif chooseAttribute == 2:
        firstLetter.compareLetter(secondLetter, "melhorLancamento", "O melhor lançamento do(a) atleta da carta")
        
    elif chooseAttribute == 3:
        firstLetter.compareLetter(secondLetter, "tecnica", "A técnica do(a) atleta da carta")
#manter um loop do jogo
while True:
    #sorteia um numero para caso seja igual a pessoa recebe uma carta especial
    idUser = random.randint(1, 4)
    specialLatter = random.randint(1, 4)
    #set da varivel para reiniciar o jogo
    game = 0
    printTitle("Super Trunfo Arremesso de peso")
    text("bem vindo ao nosso jogo muito legal")

    #sorteio das cards
    cards = ["Andre", "Beth", "Ana", "Geisa", "Darlan"]
    #Cartas do jogador
    playerCards = []
    #Cartas da maquina
    machineCards = []
    #aleatorizando as cartas
    random.shuffle(cards)
    #Escolha carta do jogador
    for i in range(2):
        chooseLetter = input(f"Escolha um número de 1 a {len(cards)}: ")
        lenCartas = str(len(cards))
        #caso o usuario insira algo errado
        while chooseLetter != "1" and chooseLetter != "2" and chooseLetter != "3" and chooseLetter != "4" and chooseLetter != lenCartas:
            text("Digite um número valido")
            chooseLetter = input(f"Escolha um número de 1 a {len(cards)}: ")

        chooseLetter = int(chooseLetter)
        chooseLetter -= 1

        playerCard = cards[chooseLetter]
        #verificando qual carta é
        if playerCard == "Andre":
            cards.remove("Andre")
            chosenCard = athlete("André", "M", 910 , 15.7, 510, 800)

        elif playerCard == "Beth":
            cards.remove("Beth")
            chosenCard = athlete("Beth", "F", 770 , 7.52, 820, 650)

        elif playerCard == "Ana":
            cards.remove("Ana")
            chosenCard = athlete("Ana", "F", 620 , 19.0, 870, 640)

        elif playerCard == "Geisa":
            cards.remove("Geisa")
            chosenCard = athlete("Geisa", "F", 800 , 9.19, 710, 590)

        elif playerCard == "Darlan":
            cards.remove("Darlan")
            chosenCard = athlete("Darlan", "M", 940 , 16.16, 750, 485)
            
        if i == 0:
            playerCards.insert(0, chosenCard)
        else:
            playerCards.insert(1, chosenCard)
    #Escolha carta da Maquina
    for i in range(2):
        chooseMachine = random.randint(1, len(cards))
        chooseMachine -=1

        letterMachine = cards[chooseMachine]

        if letterMachine == "Andre":
            cards.remove("Andre")
            chosenCard = athlete("André", "M", 910 , 15.7, 510, 800)

        elif letterMachine == "Beth":
            cards.remove("Beth")
            chosenCard = athlete("Beth", "F", 770 , 7.52, 820, 650)

        elif letterMachine == "Ana":
            cards.remove("Ana")
            chosenCard = athlete("Ana", "F", 620 , 19.0, 870, 640)

        elif letterMachine == "Geisa":
            cards.remove("Geisa")
            chosenCard = athlete("Geisa", "F", 800 , 9.19, 710, 590)

        elif letterMachine == "Darlan":
            cards.remove("Darlan")
            chosenCard = athlete("Darlan", "M", 940 , 16.16, 750, 485)
            
        if i == 0:
            machineCards.insert(0, chosenCard)
        else:
            machineCards.insert(1, chosenCard)

    toLoad("Carregando cartas da maquina", ".", 4)
    #pegunta do nome
    name = input('Qual é seu nome\nR:')
    name = name.upper()
    #caso o usuário seja especial ele recebe a carta especial
    if idUser == specialLatter or name == 'CAMILA':
        var = True
        playerCards[0].setSpecialCard(var,playerCards)

    #Mostrar para o jogador as cards
    print("As suas cartas são:")
    playerCards[0].displayInformation()
    playerCards[1].displayInformation()
    #set da lista atributos para manipulação da maquina
    attributes = ["forca", "fisico", "melhorLancamento", "tecnica"]
    
    text("Escolha qual Atributo você deseja comparar as informações da sua carta")
    playerCards[0].displayInformation()
    chooseAttribute = input("[1]Força\n[2]Fisíco\n[3]Melhor Lançamento\n[4]Técnica\nR: ")

    while chooseAttribute != "1" and chooseAttribute != "2" and chooseAttribute != "3" and chooseAttribute != "4" and chooseAttribute != len(attributes):
            text("Digite um número valido")
            chooseAttribute = input("[1]Força\n[2]Fisíco\n[3]Melhor Lançamento\n[4]Técnica\nR: ")

    chooseAttribute = int(chooseAttribute)
    chooseAttribute -= 1

    #manter a batalha de cartas
    while True:
        #caso o jogador ganhe, parar o código
        if len(playerCards) == 4:
            text("Você ganhou! Parabéns")
            game += 1
            break
        #caso a maquina ganhe, parar o código
        if len(machineCards) == 4:
            text("GAME OVER!")
            game += 1
            break
        #comparando as cartas
        comparsion(playerCards[0], machineCards[0])
        #verificando qual o ganhador, usuário ou maquina
        winner = playerCards[0].defineWinner()
        #ganhador usuário
        if winner == 0:
            print("Parabéns você ganhou uma carta")
            playerCards.insert(2, machineCards[0])
            machineCards[0].displayInformation()
            machineCards.pop(0)
            if len(playerCards) == 4:
                text("Você ganhou! Parabéns")
                game += 1
                break
            text("Escolha qual Atributo você deseja comparar as informações da sua carta")
            playerCards[0].displayInformation()
            chooseAttribute = input("[1]Força\n[2]Fisíco\n[3]Melhor Lançamento\n[4]Técnica\nR: ")

            while chooseAttribute != "1" and chooseAttribute != "2" and chooseAttribute != "3" and chooseAttribute != "4" and chooseAttribute != len(attributes):
                text("Digite um número valido")
                chooseAttribute = input("[1]Força\n[2]Fisíco\n[3]Melhor Lançamento\n[4]Técnica\nR: ")

            chooseAttribute = int(chooseAttribute)
            chooseAttribute -= 1
        #ganhador maquina
        elif winner == 1:
            print("Você perdeu a competição")
            print("Diga adeus a sua carta")
            playerCards[0].displayInformation()
            chooseAttribute = random.randint(1, len(attributes))
            chooseAttribute -= 1
            machineCards.insert(2, playerCards[0])
            playerCards.pop(0)
            if len(machineCards) == 4:
                text("GAME OVER!")
                game += 1
                break
            time.sleep(3)
            print("Maquina esta jogando espere...")
            time.sleep(2)
    #exibir opção de reiniciar o jogo
    if game == 1:
        text("Deseja jogar novamente?")
        resume = input("[1]Sim\n[2]Não\nR: ")
        while resume != "1" and resume != "2":
            text("Digite um número valido")
            resume = input("[1]Sim\n[2]Não\nR: ")
        if resume == "1":
            toLoad("Ok reiniciando", ".", 4)
        elif resume == "2":
            toLoad("Ok Desligando", ".", 4)
            quit()