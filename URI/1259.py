pares = []
impares = []
N =  int(input())
#Lê N impares e pares
for x in range(N):
    entrada = int(input())
    pares.append(entrada) if (entrada % 2 == 0) else impares.append(entrada)

pares.sort()
impares.sort(reverse=True)

for num in pares:
    print(num)
for num in impares:
    print(num)

