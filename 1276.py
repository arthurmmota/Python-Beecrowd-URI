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

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while True:
    try:
        entrada = []
        entrada = input()

        # Verifica vazia
        if entrada == "":
            print()
            continue

        # Verifica Faixa
        primeiraLetra = ''
        ultimaLetra = ''
        letraAlpha = 0
        count = 0
        ultimoIndex = -1
        saida = []
        saidaAux = ""
        # Pecorre alfabeto
        for letraAlpha in range(letraAlpha, len(alfabeto)):

            count = 0
            if (alfabeto[letraAlpha] in entrada) and (letraAlpha > ultimoIndex):
                primeiraLetra = alfabeto[letraAlpha]
                count = letraAlpha
                # Pecorre subString em Entrada
                for x in range(count, len(alfabeto)):
                    if (count == 26):
                        print(count)
                        letraAlpha += count
                        break
                    elif (alfabeto[count] in entrada):

                        ultimaLetra = alfabeto[count]
                        ultimoIndex = count
                        count += 1
                    else:
                        letraAlpha += count
                        break

                saida.insert(len(saida),'{0}:{1}'.format(primeiraLetra, ultimaLetra))

        # imprimir Saída
        for x in range(len(saida)):
            if (x == 0):
                saidaAux += saida[x]
            else:
                saidaAux += ", "
                saidaAux += saida[x]

        print(saidaAux[0: len(saidaAux) - 0])




    except EOFError:
        break
