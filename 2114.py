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
#Poker 2114
'''
    Carta mais alta: qualquer mão que não se enquadre em nenhum dos demais tipos. No desempate, as cinco cartas são comparadas uma a uma, da mais valiosa para a menos, até uma mão apresentar uma carta com valor maior que o da outra.
    Um par: duas cartas de mesmo valor. O desempate é análogo ao da carta mais alta comparando primeiro o valor do par e depois as demais cartas;
    Dois pares: dois pares. O desempate é análogo ao da carta mais alta comparando primeiro o valor do par mais valioso, depois o valor do par menos valioso e por fim a carta restante;
    Trinca: três cartas de mesmo valor. O desempate é análogo ao do par;
    Straight: sequência de cinco cartas de valores consecutivos. Neste caso o Ás pode tomar o valor tanto de carta mais baixa (antes do 2) ou de mais alta (depois do Rei). O desempate é feito pela carta de maior valor, sendo que excepcionalmente o Ás tem o menor valor se aparecer antes do 2;
    Flush: cinco cartas do mesmo naipe. O desempate é feito pelo critério da carta mais alta;
    Full House: uma trinca e um par. No desempate é comparado primeiro o valor da trinca. Persistindo o empate, é comparado o valor do par;
    Quadra: quatro cartas com um mesmo valor. No desempate compara-se o valor da quadra e depois a carta restante;
    Straight Flush: straight e ﬂush simultaneamente. O desempate é feito como no straight.
'''
def verificaFlush():
    return
def verificaStraight():
    return
def verificaStraightFLush():
    return
def verificaFULL()
    return
def()


while True:
    try:
        player1 = input().split(' ')
        player2 = input().split(' ')
        mesa    = input().split(' ')
        print(player1,player2,mesa)
        carta = list(player2[0])
        naipe = list(player2[1])
        print(carta[0])
    except EOFError:
        break