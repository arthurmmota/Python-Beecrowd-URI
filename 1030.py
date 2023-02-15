
nc = int(input())


def roda(pessoas, salto):

    ultimo = False
    i = 0
    while len(pessoas) !=1 :
        #print(pessoas)
        if (i + salto-1 >= len(pessoas)):

            if (salto > len(pessoas)):

                auxsalto = salto
                #volta 1 para corrigir
                i-=1
                while  auxsalto >0:
                    #volta pro i par ao inicio caso esteja no ultimo
                    if (i == len(pessoas) -1):
                        i = -1
                    else:
                        i+=1
                        #reduz 1 de salto para achar posicao final de i
                        auxsalto-=1
                #print('pass >> {0}'.format(i))
                pessoas.pop(i)

            else:
                faltam = len(pessoas)- i
                #vai por inicio
                i = salto - faltam-1
                #remove
                #print('i + salto > len(pessoas) e vai inicio >> {0} e i = {1}'.format(pessoas[i], i))
                #print(pessoas[i])
                pessoas.pop(i)
        else:
            i+= salto-1
            #print('i + salto < len(pessoas) >> {0} e i = {1}'.format(pessoas[i], i))
            pessoas.pop(i)



for x in range(nc):
    caso = input().split(" ")
    pessoas = list(range(1,int(caso[0])+1))
    salto = int(caso[1])

    roda(pessoas,salto)

    print("Case {0}: {1}".format(x+1, pessoas[0]))
