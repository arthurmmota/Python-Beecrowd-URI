N = int(input())

for x in range(N):
    frase = list(input())
    fraseesquerda = frase[:len(frase)//2]
    frasedireita = frase[len(frase)//2:]
    frasedireita.reverse()
    fraseesquerda.reverse()
    frase= ''
    for letra in fraseesquerda:
        frase+= letra

    for letra in frasedireita:
        frase+= letra
    print(frase)