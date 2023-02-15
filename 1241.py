def encaixa(A,B):

    if (len(B) > len(A)):
        return 'nao encaixa'
    else:
        if(A[-len(B):]) == B:
            return 'encaixa'
        else:
            return 'nao encaixa'
N = int(input())

for x in range(N):
    numeros = list(input().split(' '))
    print(encaixa(numeros[0],numeros[1]))
