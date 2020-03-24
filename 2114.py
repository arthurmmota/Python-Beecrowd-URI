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
def verificaFlush():
    return


def verificaStraight():
    return


def verificaStraightFLush():
    return


def verificaFULL():
    return


def verifica2par():
    return


def verificaPar():
    return


def verificaIgauis(player, mesa):
    iguais = 1
    iguaisC1 = 1
    iguaisC2 = 1

    carta1 = list(player[0])
    carta2 = list(player[1])

    #Par na mão
    if carta1[0] == carta2[0]:
        iguais += 1
        #compara par com a mesa
        for mc in range(0, len(mesa)):
            cartaM = list(mesa[mc])
            if carta1[0]  == cartaM[0]:
                iguais += 1
        # Par
        if iguais == 2:
            return 2
        # Trinca
        elif iguais == 3:
            return 4
        #Quadra
        elif iguais == 4:
            return 8
        #Sem cartas iguais
        else:
            return 0


    else:
        #compara primeira carta com a mesa
        for mc in range(0, len(mesa)):
            cartaM = list(mesa[mc])
            if carta1[0] == cartaM[0]:
                iguaisC1 += 1
        #compara segunda carta com a mesa
        for mc in range(0, len(mesa)):
            cartaM = list(mesa[mc])
            if carta1[1] == cartaM[0]:
                iguaisC2 += 1
        #Full house ou 02 pares
        if iguaisC1 > 1 and iguaisC2 > 1:
            #02 pares
            if (iguaisC1 == 2 and iguaisC2 == 2):
                    return 3
            #Full house
            elif (iguaisC1 == 3 and iguaisC2 == 2) or (iguaisC1 == 2 and iguaisC2 == 3):
                return 7
        else:
            #Par
            if iguaisC1 == 2 or iguaisC2 == 2:
                #verfica maior carta
                return 2
            #Trinca
            elif iguaisC1 == 3 or iguaisC2 == 3:
            # verfica maior carta
                return 4
            #Quadra
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
        print(player1, player2, mesa)
        carta = list(player2[0])
        naipe = list(player2[1])
        print(verificaIgauis(player1, mesa))
        # print(carta[0])
    except EOFError:
        break
