alfabeto = 'abcdefghijklmnopqrstuvwxyz'
N = int(input())

for x in range(N):
    frase = input()
    frase = frase.lower()

    saida = ''
    # [letra, count]
    maior = ['', 0]
    for letra in alfabeto:

        #Se achou maior, substitui
        if (frase.count(letra) > maior[1]):
            saida = ''
            maior[0] = letra
            maior[1] = frase.count(letra)
            saida = letra
        #Se achou igual, adiciona
        elif (frase.count(letra) == maior[1]):
            saida+=  letra

    print(saida)
