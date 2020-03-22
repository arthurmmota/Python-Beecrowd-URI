import random
import sys


#import ditc.py
from builtins import print
from typing import List, Any


def sayHello():
	return "Ola"
def call_numbers():
	mega_Numeros = []
	'''for i in range(0,6):

		numero = random.randint(1,60)
		if numero not in mega_Numeros:
			mega_Numeros.append(numero)
		else:
			i = i -1
		print("NUMERO ", (random.randint(1,60)))'''

	while len(mega_Numeros) <6:
		numero = random.randint(1, 60)
		if numero not in mega_Numeros:
			mega_Numeros.append(numero)
	print(sorted(mega_Numeros))


def call_numbers_pre( mega_Numeros):
	while len(mega_Numeros) < 6:
		numero = random.randint(1, 60)
		if numero not in mega_Numeros:
			mega_Numeros.append(numero)
	print(sorted(mega_Numeros))
'''teclado = sys.stdin.readline()'''



print("Digite 1 para 6 aletorios /n 2 para 6-x digitados")

teclado = input()
if int(teclado) == 1:
	call_numbers()
elif int(teclado) == 2:
	numeros = list(map(int, input("Valores: ").split()))
	call_numbers_pre(numeros)
else:
	print("Valor inválido!")

