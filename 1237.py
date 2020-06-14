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

while True:
    try:
        # Menor
        entrada1 = input()
        # Maior
        entrada2 = input()

        tamanhoSubString = 0
        subString = ""
        ultimoX = 0
        count = 0

        # Avalia qual maior
        if (len(entrada1) > len(entrada2)):
            entradaAUX = entrada1
            entrada1 = entrada2
            entrada2 = entradaAUX

        #Avalia Entradas vazias
        if (entrada2 == "" or entrada1 == ""):
            print(0)
            continue

        #Avalia se entrada1 é substring de entrada2
        if (entrada1 in entrada2):
            print(len(entrada1))
            continue



        # Pecorre Entrada1(Menor)
        for letra in range(len(entrada1)):
            count = 0
            # Pecorre substrings de Entrada1(Menor) em Entrada2 (Maior)
            for x in range(letra, len(entrada1)):
                subString += entrada1[letra]
                if (subString in entrada2):

                    count += 1

                    if (count > tamanhoSubString):
                        tamanhoSubString = count
                else:

                    count = 0

                    break
                letra += 1

            subString = ""

        print(tamanhoSubString)
        subString = ""


    except EOFError:
        break
