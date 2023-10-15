try:
    #вводим четыре числа задающие номер столбца и номер строки
    c1=int(input())
    r1=int(input())
    c2=int(input())
    r2=int(input())
    #задаем условие если столбцы или строки равны
    if c1==c2 or r1==r2:
        print('YES')
    else:
        print('NO')
except ValueError:
    print("Input is not correct")