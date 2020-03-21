import math
import sys

count1 = int(input())
notas = []
y: int
x: int
for x in range(count1):
    total = 0
    maior = 0
    notas.clear()
    notas = sys.stdin.readline().split(" ")
    notas[-1] =  notas[-1].strip()
    notas = [int(i) for i in notas]
    #print(notas[0])
    for y in range(1,len(notas)):
        total += notas[y]
        #print(notas[y])

    media = total / (notas[0])
    for z in range(1,len(notas)):
        if notas[z] > media:
            maior += 1
            #print(notas[z])
    #print(media)
    print("{:.3%}".format(float(maior /notas[0])))

