import random
# import ditc.py
from builtins import print


# !/usr/bin/env python
# -*- coding: utf-8 -*-
def sayHello():
    return "Ola"


def call_numbers():
    for i in range(0, 10):
        print(i * random.randint(1, 101))


J = 5
arq = open('D:/Users/arthu/Desktop/TEXTO.txt', 'w')

for i in range(0, 100):
    if (J * i) % 5 == 0:
        arq.write(" " + str(J * i) + "\n")
arq.close()

arq = open('D:/Users/arthu/Desktop/TEXTO.txt', 'r')

b = arq.readline()
while b != '':
    if int(b)%25 == 0:
        print("Número" + b)
    b = arq.readline()
print("Acabou")
arq.close()
if arq.closed == True:
    print("é vdd")

