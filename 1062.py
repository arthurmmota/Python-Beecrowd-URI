


def avaliaTrem(vagoes, a):

    estacao = [0*vagoes]
    B = [0*vagoes]
    for vagao in range(vagoes,0,-1):


        # Verifica B e estacao
        if(len(estacao) > 1 and len(B) > 1 ):
            # move da estacao para B
            estacaoOrdenada= True

            while (estacaoOrdenada == True):
                if( estacao[-1] == B[-1] - 1):
                    estacaoOrdenada = True


                    B.append(estacao[-1])
                    estacao.remove(estacao[-1])


                    #print("Estacao while:", estacao)
                    #print("B while:", B)
                    #print("-------")
                    #print("Vagao while:", B[-1] )
                    #print("valor :", estacao[-1])
                else:
                    estacaoOrdenada = False

        if((a[vagao-1] == vagoes) or (a[vagao-1]  == B[-1] -1) ):
            B.append(a[vagao-1] )
        else:
            estacao.append(a[vagao-1])

        #print("vagao = ", a[vagao-1])
        #print("A:", a)
        #print("Estacao", estacao)
        #print("B", B)
        #print("**********")
    #print("Estação:", estacao)
    if(len(estacao) > 1):

        for x in range(len(estacao)):

            if (estacao[-1] == B[-1] - 1 and len(estacao) > 0):

                #print(estacao[-1])
                B.append(estacao[-1])
                estacao.remove(estacao[-1])


        if (len(estacao) > 0):
            print("No")
        else:
            print("Yes")
    else:
        print("Yes")
flagFim = False
flag0 = False

while True:


    entrada = list(int(entrada) for entrada in input().split())
    if (len(entrada) == 1):
        if (entrada[0] == 0):
            flagFim = True

            if(flagFim == True and flag0 == False):
                flag0 = True
                print()
            else:
                break
        else:
            flag0 = False
            vagoes = entrada[0]
            flagFim = False


    else:
        a = entrada
        #print("Vagoes:", vagoes)
        #print("A:", a)
        avaliaTrem(vagoes, a)





