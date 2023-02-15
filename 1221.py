#Algoritmo de Fermat melhorado com raiz
def Fermat(numero):


    if (numero%2 == 0):
        #Caso 2
        if(numero == 2):
            return 'Prime'
        #Caso Par
        else:
            return 'Not Prime'


    x = int(numero ** (1 / 2))



    # x é fator de numero
    if (x ** 2 == numero):
        return 'Not Prime'
    else:
        # Até raiz de Numero
        for c in range(3, x):
            raiz = numero / c
            if (raiz // 1 == raiz):
                return 'Not Prime'

        while x != (numero + 1)/2:
            x+=1
            y = (x**2 - numero)**(1/2)

            #x+y e x-y  sao fatores de numero
            if (y//1 == y and  x != (numero + 1)/2):
                return 'Not Prime'
        return 'Prime'


N = int(input())
for x in range(N):
    numero = int(input())
    print(Fermat(numero))

