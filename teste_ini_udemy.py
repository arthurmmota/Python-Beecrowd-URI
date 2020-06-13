import random

A = 5
B = 7
print(A + B)

valorHora = 4
dias = 30
horasTrabalho = 8

Vencimento = valorHora * dias * horasTrabalho

nome = 'Thiago'

print(Vencimento)
float(Vencimento)
print(Vencimento)

# Strings

nome = 'Thiago Macedo'
print(nome)
# Thiago 0 ate 6
print(nome[0:6])
# Macedo
print(nome[7:13])
# True
print('T' in nome)

# Listas

lista = []
lista = [1, 2, 3, "thiago", True]
print(lista)
# Adicionar
lista.append("python")
lista.append(True)

print(lista)

# Qual a posição

print(lista.index('python'))

# Quantos há
print(lista.count('thiago'))

# Remover
'''lista.remove(True) Não funcionou
'''
lista.remove('thiago')
print(lista)

# Reverter
lista.reverse()
print(lista)

lista2 = []

for item in range(10):
    lista2.append(item + 5)
lista2.append(12)
print(lista2)

# Ordenar
lista2.sort()
print(lista2)

# Dicionarios {'':5}
telefones = {"Eu": 31, "Tu": 33, "Vos": 45}
print(telefones)

# adicionar
telefones["ele"] = 1
print(telefones)

# Apagar um telemóvel
del telefones["Tu"]
print(telefones)

# Tuplas Não é possivel adicionar um item

tupla = ("Arthur", 26, True)
print(tupla)
print(tupla[2])

print(tupla[0:2])
# print(tupla[2:2])

# Comprimento
print(len(tupla))
tuplaNum01 = (1, 2, 3)
tuplaNum02 = (10, 20, 30)

# Somar tuplas soma os final
print(tuplaNum01 + tuplaNum02)
print(tuplaNum01 * 5)
# Verifica a existencia de um item
print(False in tupla)

# Converter listas para tuplas
listaT = [1, 4, "hehe"]
tupla02 = tuple(listaT)
print(listaT)

# IF AND ELSE

numero = 2
if numero == 1:
    print("é vero")
else:
    print("No vero")

lastName = "Ferrari"
if ("z" in lastName):
    print("ZzZ")
elif ("f" in lastName):
    print("fff")
else:
    # print(lastName)
    pass

# Loop FOR

for x in range(0, 120):
    if (x % 17 == 0):
        # print(">> %d " %x)
        print(">> ", x)
for x in nome:
    print(x)
for valor in listaT:
    print(valor)

'''        >> > things = 5

        >> > 'You have %d things.' % things  # % interpolation
        'You have 5 things.'

        >> > 'You have {} things.'.format(things)  # str.format()
        'You have 5 things.'

        >> > f'You have {things} things.'  # f-string (since Python 3.6)
        'You have 5 things.'

        ...
        mas
        também
        permite
        controlar
        como
        os
        valores
        são
        exibidos:

        >> > value = 5
        >> > sq_root = value ** 0.5
        >> > sq_root
        2.23606797749979

        >> > 'The square root of %d is %.2f (roughly).' % (value, sq_root)
        'The square root of 5 is 2.24 (roughly).'

        >> > 'The square root of {v} is {sr:.2f} (roughly).'.format(v=value, sr=sq_root)
        'The square root of 5 is 2.24 (roughly).'

        >> > f'The square root of {value} is {sq_root:.2f} (roughly).'
        'The square root of 5 is 2.24 (roughly).'

'''

# Loop While

while (numero < 10):
    print(numero)
    numero += 1

# Pass break continue
cont = 0
while (True):
    numero = random.randint(1, 100)
    cont+=1
    if numero == 2:
        print("oi", cont)
        break
    elif (numero % 5 == 0):
        print("Continue", cont, numero)
        continue
    else:
        pass

