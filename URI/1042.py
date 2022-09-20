from copy import  deepcopy

'''Leia 3 valores inteiros e ordene-os em ordem crescente. 
No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, 
os valores na sequência como foram lidos.'''

valores = list(int(entrada) for entrada in input().split())
valoresOrdenados = deepcopy(valores)

valoresOrdenados.sort()

#mostre os valores em ordem crescente,
for x in valoresOrdenados:
    print(x)
#uma linha em branco
print()
#os valores na sequência como foram lidos.
for x in valores:
    print(x)