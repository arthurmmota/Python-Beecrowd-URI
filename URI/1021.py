N = float(input())
notas = [['100.00',0],['50.00',0],['20.00',0],['10.00',0],['5.00',0],['2.00',0]]
moedas =[['1.00',0],['0.50',0],['0.25',0],['0.10',0],['0.05',0],['0.01',0]]
N+= 0.001
for nota in notas:
    if(N//float(nota[0]) > 0):
        nota[1] = N//float(nota[0])
        N-= float(nota[1] * float(nota[0]))
        if (N == 0.0):
            break

if (N != 0.0):
    for moeda in moedas:
        if (N // float(moeda[0]) > 0):
            moeda[1] = N // float(moeda[0])
            N -= float(moeda[1] *float(moeda[0]))
            if (N == 0.0):
                break
print('NOTAS:')
for nota in notas:
    print('{0} nota(s) de R$ {1}'.format(int(nota[1]), nota[0]))
print('MOEDAS:')
for moeda in moedas:
    print('{0} moeda(s) de R$ {1}'.format(int(moeda[1]), moeda[0]))

