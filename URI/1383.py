#sudoku
de1a9 = list(range(1,10))

def avaliaLinha(sudoku):


    #horizontal
    for linha in sudoku:
        for numero in de1a9:
            if(linha.count(numero) != 1):
                #print("Numero {0} counta : {1}".format(numero, linha.count(numero)))
                return False
    #vertical
    for c in range(9):
        coluna = []
        for l in range(9):
            coluna.append(sudoku[l][c])

        for numero in de1a9:
            if(coluna.count(numero) != 1):
                #print("Vertical {2} Numero {0} count : {1}".format(numero, coluna.count(numero), c))
                return False

    return True

def avaliaBox(box, b):
    for numero in de1a9:
        if (box.count(numero) != 1):
            #print("Box {2} - Numero {0} count: {1}".format(numero, box.count(numero), b))
            return False
    return True


def pecorreBox(sudoku):
    flagSudoku = True

    for b in range(9):
        box = []
        if (b % 3 == 0):
            inicialLinhas = b
            inicialColunas = 0
        else:

            inicialColunas += 3


        for linha in range(inicialLinhas, inicialLinhas+3):

            for coluna in range(inicialColunas,inicialColunas+3):
                box.append(sudoku[linha][coluna])
                #print("sudoku[{0}][{1}] = {2}".format(linha , coluna, sudoku[linha][coluna]))


        #Logica count
        #print(box)
        flagSudoku = avaliaBox(box,b)
        if(flagSudoku == False):
            return flagSudoku
    return flagSudoku


qnt = int(input())
flag = True

for x in range(qnt):
    sudoku = []
    for linhaSudoku in range(9):
        sudoku.append(list(int(entrada) for entrada in input().split()))
    #print(sudoku)

    flag = avaliaLinha(sudoku)
    print("Instancia {0}".format(x+1))
    if(flag == False):
        print("NAO\n")
    else:
        flag = pecorreBox(sudoku)
        if(flag == False):
            print("NAO\n")
        else:
            print("SIM\n")


