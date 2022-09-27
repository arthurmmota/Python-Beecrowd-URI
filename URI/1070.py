entrada = int(input())
if (entrada%2 == 0):
    entrada+=1
    for impar in range(entrada, entrada+12,2):
        print(impar)

else:
    for impar in range(entrada, entrada + 12, 2):
        print(impar)
