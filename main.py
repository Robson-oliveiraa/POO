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
def carregar(text, str, vezes):
    for i in range(3):
        for i in range(vezes):
            pontos = str*i
            print(text, pontos)
            time.sleep(0.4)
            os.system("cls")
#Função do titulo
def printTitle(title):
    print("=============================")
    print("         Helo World!         ")
    print("=============================")
    print(f"{title}                     ")
#Comparar as cartas de acordo com os atributos
def comparacao(primeiraCarta, segundaCarta):
    if escolhaAtributo == 0:
        primeiraCarta.compararCartas(segundaCarta, "forca", "a")
        
    elif escolhaAtributo == 1:
        primeiraCarta.compararCartas(segundaCarta, "fisico", "a")
        
    elif escolhaAtributo == 2:
        primeiraCarta.compararCartas(segundaCarta, "melhorLancamento", "a")
        
    elif escolhaAtributo == 3:
        primeiraCarta.compararCartas(segundaCarta, "tecnica", "a")
        
while True:
    # idUser = random.randint(1, 3)
    # cartaEspecial = random.randint(1, 3)
    jogo = 0
    printTitle("Super Trunfo Arremesso de peso")
    print("bem vindo ao nosso jogo muito legal")

    #sorteio das cartas
    cartas = ["Andre", "Beth", "Ana", "Geisa", "Darlan"]
    #Cartas do jogador
    cartasDoJogador = []
    #Cartas da maquina
    cartasDaMaquina = []
    random.shuffle(cartas)
    #Escolha carta do jogador
    for i in range(2):
        escolhaCarta = input(f"Escolha um número de 1 a {len(cartas)}: ")
        
        while escolhaCarta != "1" and escolhaCarta != "2" and escolhaCarta != "3" and escolhaCarta != "4" and escolhaCarta != len(cartas):
            text("Digite um número valido")
            escolhaCarta = input(f"Escolha um número de 1 a {len(cartas)}: ")

        escolhaCarta = int(escolhaCarta)
        escolhaCarta -= 1

        cartaJogador = cartas[escolhaCarta]

        if cartaJogador == "Andre":
            cartas.remove("Andre")
            cartaEscolhida = athlete("André", "M", 910 , 15.7, 510, 800)

        elif cartaJogador == "Beth":
            cartas.remove("Beth")
            cartaEscolhida = athlete("Beth", "F", 770 , 7.52, 820, 650)

        elif cartaJogador == "Ana":
            cartas.remove("Ana")
            cartaEscolhida = athlete("Ana", "F", 620 , 19.0, 870, 640)

        elif cartaJogador == "Geisa":
            cartas.remove("Geisa")
            cartaEscolhida = athlete("Geisa", "F", 800 , 9.19, 710, 590)

        elif cartaJogador == "Darlan":
            cartas.remove("Darlan")
            cartaEscolhida = athlete("Darlan", "M", 940 , 16.16, 750, 485)
            
        if i == 0:
            cartasDoJogador.insert(0, cartaEscolhida)
        else:
            cartasDoJogador.insert(1, cartaEscolhida)
    #Escolha carta da Maquina
    for i in range(2):
        escolhaMaquina = random.randint(1, len(cartas))
        escolhaMaquina -=1

        cartaMaquina = cartas[escolhaMaquina]

        if cartaMaquina == "Andre":
            cartas.remove("Andre")
            cartaEscolhida = athlete("André", "M", 910 , 15.7, 510, 800)

        elif cartaMaquina == "Beth":
            cartas.remove("Beth")
            cartaEscolhida = athlete("Beth", "F", 770 , 7.52, 820, 650)

        elif cartaMaquina == "Ana":
            cartas.remove("Ana")
            cartaEscolhida = athlete("Ana", "F", 620 , 19.0, 870, 640)

        elif cartaMaquina == "Geisa":
            cartas.remove("Geisa")
            cartaEscolhida = athlete("Geisa", "F", 800 , 9.19, 710, 590)

        elif cartaMaquina == "Darlan":
            cartas.remove("Darlan")
            cartaEscolhida = athlete("Darlan", "M", 940 , 16.16, 750, 485)
            
        if i == 0:
            cartasDaMaquina.insert(0, cartaEscolhida)
        else:
            cartasDaMaquina.insert(1, cartaEscolhida)

    carregar("Carregando cartas da maquina", ".", 4)

    nome = input('Qual é seu nome\nR:')
    nome = nome.upper()
    if idUser == cartaEspecial or nome == 'CAMILA':
        var = True
        cartasDoJogador[0].definirCartaExpecial(var,cartasDoJogador)

    #Mostrar para o jogador as cartas
    print("As suas cartas são:")
    cartasDoJogador[0].exibirInformacoes()
    cartasDoJogador[1].exibirInformacoes()

    atributos = ["forca", "fisico", "melhorLancamento", "tecnica"]

    text("Escolha qual Atributo você deseja comparar as informações da sua carta")
    cartasDoJogador[0].exibirInformacoes()
    escolhaAtributo = input("[1]Força\n[2]Fisíco\n[3]Melhor Lançamento\n[4]Técnica\nR: ")

    while escolhaAtributo != "1" and escolhaAtributo != "2" and escolhaAtributo != "3" and escolhaAtributo != "4" and escolhaAtributo != len(atributos):
            text("Digite um número valido")
            escolhaAtributo = input("[1]Força\n[2]Fisíco\n[3]Melhor Lançamento\n[4]Técnica\nR: ")

    escolhaAtributo = int(escolhaAtributo)
    escolhaAtributo -= 1


    while True:
        if len(cartasDoJogador) == 4:
            text("Você ganhou! Parabéns")
            jogo += 1
            break
        
        if len(cartasDaMaquina) == 4:
            text("GAME OVER!")
            jogo += 1
            break
        
        comparacao(cartasDoJogador[0], cartasDaMaquina[0])
        ganhador = cartasDoJogador[0].definirGanhador()

        if ganhador == 0:
            print("Parabéns você ganhou uma carta")
            cartasDoJogador.insert(2, cartasDaMaquina[0])
            cartasDaMaquina[0].exibirInformacoes()
            cartasDaMaquina.pop(0)
            if len(cartasDoJogador) == 4:
                text("Você ganhou! Parabéns")
                jogo += 1
                break
            text("Escolha qual Atributo você deseja comparar as informações da sua carta")
            cartasDoJogador[0].exibirInformacoes()
            escolhaAtributo = input("[1]Força\n[2]Fisíco\n[3]Melhor Lançamento\n[4]Técnica\nR: ")

            while escolhaAtributo != "1" and escolhaAtributo != "2" and escolhaAtributo != "3" and escolhaAtributo != "4" and escolhaAtributo != len(atributos):
                text("Digite um número valido")
                escolhaAtributo = input("[1]Força\n[2]Fisíco\n[3]Melhor Lançamento\n[4]Técnica\nR: ")

            escolhaAtributo = int(escolhaAtributo)
            escolhaAtributo -= 1
            
        elif ganhador == 1:
            print("Você perdeu a competição")
            print("Diga adeus a sua carta")
            cartasDoJogador[0].exibirInformacoes()
            escolhaAtributo = random.randint(1, len(atributos))
            escolhaAtributo -= 1
            cartasDaMaquina.insert(2, cartasDoJogador[0])
            cartasDoJogador.pop(0)
            if len(cartasDaMaquina) == 4:
                text("GAME OVER!")
                jogo += 1
                break
            time.sleep(3)
            print("Maquina esta jogando espere...")
            time.sleep(2)
    
    if jogo == 1:
        text("Deseja jogar novamente?")
        resume = input("[1]Sim\n[2]Não\nR: ")
        while resume != "1" and resume != "2":
            text("Digite um número valido")
            resume = input("[1]Sim\n[2]Não\nR: ")
        if resume == "1":
            carregar("Ok reiniciando", ".", 4)
        elif resume == "2":
            carregar("Ok Desligando", ".", 4)
            quit()