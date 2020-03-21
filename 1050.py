# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

DDD = {'61': 'Brasilia', '71': 'Salvador', '11': 'Sao Paulo', '21': 'Rio de Janeiro',
       '32': 'Juiz de Fora', '19': 'Campinas', '27': 'Vitoria', '31': 'Belo Horizonte'}
entrada = input()
entradaInt =  str(entrada)

if entradaInt in DDD:
    print(DDD.get(entradaInt))
else:
    print("DDD nao cadastrado")

