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

notas = []
soma = 0

# Recebe Notas
entrada = input()
notas = entrada.split(" ")

for item in notas:
    item = float(item)

#Efetua pesos
notas[0] = float(notas[0])* 2.0
notas[1] = float(notas[1])* 3.0
notas[2] = float(notas[2])* 4.0


for item in notas:
    soma += float(item)

media = soma / 10
# Verifica média
if (media >= 7.0):
    print("Media: %.1f" % media)
    print("Aluno aprovado.")
elif (media < 5.0):
    print("Media: %.1f" % media)
    print("Aluno reprovado.")
else:
    exame = float(input())
    print("Media: %.1f" % media)
    print("Aluno em exame.")
    print("Nota do exame: %.1f" % exame)
    soma += exame
    media = (media + exame) / 2
    if (media >= 5.0):
        print("Aluno aprovado.")
        print("Media final: %.1f" % media)
    else:
        print("Aluno reprovado.")
        print("Media final: %.1f" % media)

