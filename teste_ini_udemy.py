A = 5
B = 7
print(A+B)


valorHora = 4
dias = 30
horasTrabalho = 8

Vencimento= valorHora * dias * horasTrabalho

nome = 'Thiago'

print(Vencimento)
float(Vencimento)
print(Vencimento)

# Strings

nome = 'Thiago Macedo'
print(nome)
#Thiago 0 ate 6
print(nome[0:6])
#Macedo
print(nome[7:13])
#True
print('T' in nome)


#Listas

lista=[]
lista=[1,2,3,"thiago",True]
print(lista)
#Adicionar
lista.append("python")
lista.append(True)

print(lista)

#Qual a posição

print(lista.index('python'))

#Quantos há
print(lista.count('thiago'))

#Remover
'''lista.remove(True) Não funcionou
'''
lista.remove('thiago')
print(lista)

#Reverter
lista.reverse()
print(lista)

lista2 =[]

for item in range(10):
    lista2.append(item+5)
lista2.append(12)
print(lista2)

#Ordenar
lista2.sort()
print(lista2)


#Dicionarios {'':5}
telefones = {"Eu":31,"Tu":33,"Vos":45}
print(telefones)

#adicionar
telefones["ele"] = 1
print(telefones)

#Apagar um telemóvel
del  telefones["Tu"]
print(telefones)

#Tuplas Não é possivel adicionar um item

tupla = ("Arthur",26,True)
print(tupla)
print(tupla[2])

print(tupla[0:2])
#print(tupla[2:2])

#Comprimento
print(len(tupla))
tuplaNum01 = (1,2,3)
tuplaNum02 = (10,20,30)

#Somar tuplas soma os final
print(tuplaNum01 + tuplaNum02)
print(tuplaNum01 * 5)
#Verifica a existencia de um item
print(False in tupla)

#Converter listas para tuplas
listaT = [1,4,"hehe"]
tupla02 = tuple(listaT)
print(listaT)









