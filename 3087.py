import numpy

while True:
    try:
        largura = int(input())
        loja = int(input())
        matrix = []  # lista vazia

        # Criar Matriz largura x largura
        for l in range(0, largura):
            linha = []  # lista vazia
            for c in range(0, largura):
                linha.append(0)
            matrix.append(linha)
        print(matrix)
        # print(matrix[1][1])
        count = 1

        # preenche matriz
        center = int(largura / 2)  # Meio da matriz

        vertical, horizontal = center, center

        NORTH, S, W, E = (0, -1), (0, 1), (-1, 0), (1, 0)  # directions
        turn_right = {NORTH: E,
                      E: S,
                      S: W,
                      W: NORTH}  # old -> new direction

        count = 0

        dx, dy = NORTH  # initial direction

        while (count <= largura ^ 2):
            count += 1
            # try to turn right

            matrix[horizontal][vertical] = count
            new_dx, new_dy = turn_right[dx, dy]
            new_x, new_y = vertical + new_dx, horizontal + new_dy

            if (0 <= new_x < largura and 0 <= new_y < largura and
                    matrix[new_y][new_x] == 0):  # can turn right
                vertical, horizontal = new_x, new_y
                dx, dy = new_dx, new_dy
            else:  # try to move straight
                vertical, horizontal = vertical + dx, horizontal + dy
                print( horizontal,vertical,count+1)
                if not (0 <= vertical < largura and 0 <= horizontal < largura):
                    continue



        print(matrix)

        # Achar o centro e preencher até largura²
        # Localizar loja

    except EOFError:
        break
