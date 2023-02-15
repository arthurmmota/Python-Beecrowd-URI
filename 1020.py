'''Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias'''

dias = int(input())
anos = dias // 365
dias %=  365
meses = dias // 30
dias %= 30

print(anos, 'ano(s)')
print(meses,'mes(es)')
print(dias, 'dia(s)')