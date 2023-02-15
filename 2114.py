import time
import sys
import os
import math
import random
import pickle
import urllib
import re
import cgi
import socket

# Poker 2114
from typing import List, Any, Union

'''
jogo #  
     1 - Carta mais alta: qualquer mão que não se enquadre em nenhum dos demais tipos. No desempate, as cinco cartas são comparadas uma a uma, da mais valiosa para a menos, até uma mão apresentar uma carta com valor maior que o da outra.
     2 - Um par: duas cartas de mesmo valor. O desempate é análogo ao da carta mais alta comparando primeiro o valor do par e depois as demais cartas;
     3 - Dois pares: dois pares. O desempate é análogo ao da carta mais alta comparando primeiro o valor do par mais valioso, depois o valor do par menos valioso e por fim a carta restante;
     4 - Trinca: três cartas de mesmo valor. O desempate é análogo ao do par;
     5 - Straight: sequência de cinco cartas de valores consecutivos. Neste caso o Ás pode tomar o valor tanto de carta mais baixa (antes do 2) ou de mais alta (depois do Rei). O desempate é feito pela carta de maior valor, sendo que excepcionalmente o Ás tem o menor valor se aparecer antes do 2;
     6 - Flush: cinco cartas do mesmo naipe. O desempate é feito pelo critério da carta mais alta;
     7 - Full House: uma trinca e um par. No desempate é comparado primeiro o valor da trinca. Persistindo o empate, é comparado o valor do par;
     8 - Quadra: quatro cartas com um mesmo valor. No desempate compara-se o valor da quadra e depois a carta restante;
     9 - Straight Flush: straight e ﬂush simultaneamente. O desempate é feito como no straight.
    Caracter 	Carta
    '2'- '9' 	2 - 9
    'T' 	10
    'J' 	Valete
    'Q' 	Dama
    'K' 	Rei
    'A' 	Ás
    'e' 	Espadas
    'c' 	Copas
    'p' 	Paus
    'o' 	Ouros




'''
'''
Quadra
Ke Kp
Jc 9p
Kc Ko 2c Ac 
Dupla
Ke Kp
Jc 9p
Kc Ko 2c Ac

trinca

Ke Kp
Jc 9p
Kc 2o 2c Ac
t
'''
sequencia = (["2", 2],["3", 3],["4", 4],["5", 5],["6", 6],["7", 7],["8", 8],["9", 9],["T", 10],["J", 11],["Q", 12],["K", 13],["A", 14])



def verificaMaiorCarta(carta1, carta2):
    valorCarta1 = 0
    valorCarta2 = 0
    for x in range(0, len(sequencia)):
        if sequencia[x][0] == carta1:
            valorCarta1 = sequencia[x][1]
    for x in range(0, len(sequencia)):
        if sequencia[x][0] == carta2:
            valorCarta2 = sequencia[x][1]
    if valorCarta1 == valorCarta2:
        return 0
    elif valorCarta1 > valorCarta2:
        return carta1
    else:
        return carta2



def verificaFlush():
    return


def verificaStraight():
    return

def ordenaCartas(player, mesa):
    #Ordem de agordo com sequencia

    
    return


def verificaStraighteFLush(player, mesa):
    #Ordena player+mesa

    #Verifica Flush
    #Se flush
        #Verifica Straight
            #Se Straight
                #StraightFlush
            #Apenas Flush
    #Verifica Straight
        #Se sim
            #Straight
        #Senao
            #0




    return


def verificaIguais(player, mesa):
    iguais = 1
    iguaisC1 = 1
    iguaisC2 = 1

    carta1 = list(player[0])
    carta2 = list(player[1])

    #print("maior carta",verificaMaiorCarta(carta1[0],carta2[0]))

    # Par na mão
    if carta1[0] == carta2[0]:
        iguais += 1
        # compara par com a mesa
        #mesa.count(carta1[0])

        for mc in range(0, len(mesa)):
            cartaM = list(mesa[mc])
            if carta1[0] == cartaM[0]:
                iguais += 1
        # Par
        if iguais == 2:
            return 2
        # Trinca
        elif iguais == 3:
            return 4
        # Quadra
        elif iguais == 4:
            return 8
        # Sem cartas iguais
        else:
            return 0

    #Sem par na mão
    else:
        # compara primeira carta com a mesa
        for mc in range(0, len(mesa)):
            cartaM = list(mesa[mc])
            if carta1[0] == cartaM[0]:
                iguaisC1 += 1
        # compara segunda carta com a mesa
        for mc in range(0, len(mesa)):
            cartaM = list(mesa[mc])
            if carta1[1] == cartaM[0]:
                iguaisC2 += 1

        # Full house, 02 pares 02 trincas
        if iguaisC1 > 1 and iguaisC2 > 1:
            # 02 pares
            if (iguaisC1 == 2 and iguaisC2 == 2):
                # verfica maior carta
                return 3
            #02 trincas
            elif iguaisC1 == 3 and iguaisC2 == 3:
                # verfica maior carta
                return 4
            # Full house
            elif (iguaisC1 == 3 and iguaisC2 == 2) or (iguaisC1 == 2 and iguaisC2 == 3):
                return 7
        else:
            # Par
            if iguaisC1 == 2 or iguaisC2 == 2:

                return 2
            # Trinca
            elif iguaisC1 == 3 or iguaisC2 == 3:
                # verfica maior carta
                return 4
            # Quadra
            elif iguaisC1 == 4 or iguaisC2 == 4:
                # verfica maior carta
                return 8
            # Sem cartas iguais
            else:
                return 0


while True:
    try:
        player1 = input().split(' ')
        player2 = input().split(' ')
        mesa = input().split(' ')
        #carta =
        mesa2 = []
        print(player1, player2, mesa)
        for item in mesa:
            mesa2.append(item.split())
        print(mesa2)
        carta = list(player2[0])
        naipe = list(player2[1])

        #print(verificaMaiorCarta('T','A'))

        print(verificaIguais(player1, mesa))


        # print(carta[0])
    except EOFError:
        break
