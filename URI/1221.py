#Algoritmo de Fermat
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

