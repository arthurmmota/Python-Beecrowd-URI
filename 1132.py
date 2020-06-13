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

x = int(input())
y = int(input())
soma = 0

#Verifica qual é maior
if x > y:
    aux = x
    x = y
    y = aux


#Calcula a soma dos números que não são múltiplos de 13 entre X e Y
for nDivisor in range(x,y+1):
    if(nDivisor % 13 != 0):
        soma+=nDivisor
#Imprime soma
print(soma)