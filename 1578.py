def calculaMaxColuna(matriz, ncoluna ,lc):
    # vertical
    coluna = []
    for l in range(lc):
        coluna.append(int(matriz[l][ncoluna]))
    #coluna = array(coluna)
    coluna.sort()

    return str(coluna[lc-1])

N = int(input())
for x in range(N):

    lc = int(input())

    if (x + 4 != 4):
        print('')
    print('Quadrado da matriz #{0}:'.format(x+4))

    matriz = []
    for y in range(lc):
        if(lc != 1):

            matriz.append(list(str(int(entrada)**2) for entrada in input().split()))
        else:
            entrada = int(input())**2

            print(str(entrada))

    if(lc != 1):

        for c in range(lc):
            maximo = 0
            casasMaximo = 0
            for l in range(lc):
                if(l == 0 or  maximo == matriz[l][c]):
                    maximo = calculaMaxColuna(matriz, c, lc)
                    casasMaximo = len(maximo)

                #calcula casas no quadrado e alinha

                casasNumero = len(matriz[l][c])
                espacos = ' '*(casasMaximo-casasNumero)
                matriz[l][c] = espacos+matriz[l][c]

        for linha in range(lc):
            for coluna in range(lc):
                if(coluna != lc-1):
                    print(matriz[linha][coluna]+' ',  end="")
                else:
                    print(matriz[linha][coluna])

