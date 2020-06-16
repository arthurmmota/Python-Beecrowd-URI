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

rodadas = int(input())
for x in range(rodadas):
    diamantes = []
    entrada = input()


    # Remove areia
    for item in entrada:
        if(item == "<" or item == ">"):
            diamantes.append(item)

    # Verifica se há pelo menos 1 fechamento de diamante
    if (diamantes.count(">") == 0 or diamantes.count("<") == 0):
        print(0)
        continue

    esquerda = 0
    direita = 0
    cont =0
    # Pecorre diamantes
    for item in range(1,len(diamantes)):
        # <
        if diamantes[item] == "<":
            esquerda += 1
        if item == 1 and diamantes[item-1] == "<":
            esquerda += 1

        # <<<> or <>
        if(esquerda > 0 and diamantes[item] == ">" ) or (diamantes[item] == ">" and diamantes[item-1] == "<" ):
            cont+=1
            esquerda-=1

    print(cont)
