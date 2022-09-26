while True:
    try:
        angulo = int(input())
        print('Y') if (angulo % 6 == 0) else print('N')
    except:
        break
