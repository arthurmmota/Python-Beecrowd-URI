while True:

  try:
    flagPremio = False
    contatorPoder = 0

    #inteiro N (2 ≤ N ≤ 100)
    premios = int(input())

    for x in range(premios-1):
      troca = list(int(entrada) for entrada in input().split())

      if(troca[0] == premios):
        if(troca[1] == 0):
          contatorPoder+=1
        flagPremio = True

      elif(flagPremio == True and troca[1] == 1):
        contatorPoder+=1
    print(contatorPoder)

  except EOFError:
    break