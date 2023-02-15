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

tamanhoVetor = int(input())
menorValor = 0
posicaoMenor = 0

elemento = [int(item) for item in input().split()]


for item in range(tamanhoVetor-1):

    # Primeiro elemento
    if (item == 0):
        menorValor = elemento[item]
        posicaoMenor = item
    # Se menorValor > elemento, menorValor = elemento

    elif menorValor > elemento[item]:
        menorValor =  elemento[item]
        posicaoMenor = item

print("Menor valor:", menorValor)
print("Posicao:", posicaoMenor)
