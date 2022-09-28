#num/posicao[0,1,2,3,4,5,6,7,8,9]
num_leds =  [6,2,5,5,4,5,6,3,7,6]

N = int(input())

for x in range(N):
    qntled = 0
    valor = list(input())

    # verifica qntled
    for num in valor:
        qntled+= num_leds[int(num)]
    print('{0} leds'.format(qntled))