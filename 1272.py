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

cases = int(input())
codigo = ""

for x in range(cases):
    #Lê um a 50 caracteres, formado por letras minúsculas (‘a’-‘z’) ou espaços (‘ ’).
    linha = input()

    #descodifica
    for y in range(len(linha)):
        if( linha[y] != " "):
            if ( y == 0):
                codigo+= linha[y]
            elif(linha[y-1] == " " ):
                #codigo.append(linha[y])
                codigo += linha[y]

    #Imprime o codigo
    print(codigo)
    codigo = ""

