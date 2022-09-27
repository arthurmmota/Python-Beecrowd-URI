N = int(input())

for x in range(N):
    frase = input().split(' ')
    #Seleciona maior palavra
    if (len(frase[0]) >= len(frase[1]) ):
        maior = frase[0]
        menor = frase[1]
    else:
        maior = frase[1]
        menor = frase[0]



    combinado = ''
    #Combinando ate o menor
    for letra in range(0, len(menor)):
        combinado+= frase[0][letra]
        combinado+= frase[1][letra]

    #Combinando o retante do maior
    for letra in range (len(menor), len(maior)):

        combinado+= maior[letra]

    print(combinado)
