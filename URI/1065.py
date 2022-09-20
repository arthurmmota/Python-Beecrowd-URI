'''Faça um programa que leia 5 valores inteiros. Conte quantos destes valores digitados são pares e mostre esta informação.'''
countpares =0

for x in range(5):
    entrada = int(input())
    if(entrada % 2 == 0):
        countpares+= 1

print(countpares,'valores pares')