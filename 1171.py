#  único inteiro N, que indica a quantidade de valores que serão lidos para X (1 ≤ X ≤ 2000)
N = int(input())
numeros = []

#ler valores
for x in range(N):
    numeros.append( int(input()))
#ordernar
numeros.sort()
anterior = -1

#saída
for item in numeros:
    if( item != anterior):
        nvezes = numeros.count(item)
        print("{0} aparece {1} vez(es)".format(item,nvezes))
        anterior = item