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
    nCartas = int(input())
    if nCartas == 0:
        break
    pilha = []
    discarted = []


    # Monta pilha
    for carta in range(nCartas):
        pilha.append(carta + 1)
    pilha.reverse()

    # Enquanto tiver 2 ou mais cartas na pilha.
    while (len(pilha) >= 2):
        # Descarta topo
        discarted.append(pilha[len(pilha)-1])
        del pilha[len(pilha)-1]

        # Desce 2a pra base
        pilha.insert(0, pilha[len(pilha)-1])

        del pilha[len(pilha)-1]


    # Imprime Discarded cards
    print('Discarded cards:', str(discarted)[1:-1])
    # Imprime Remaining card
    print('Remaining card:',str(pilha)[1:-1])
