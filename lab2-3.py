try:
    #вводим три числа
    n1=int(input())
    n2=int(input())
    n3=int(input())
    #условие арифметической прогрессии
    if n2-n1==n3-n2:
        print('YES')
    else:
        print('NO')
except ValueError:
    print("Input is not correct")