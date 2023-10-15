try:
    #вводим число
    num = int(input())
    #задаем условие чтобы определить четное, для этого делим число на 2 без остатка
    if num % 2 == 0:
        print('Odd number')
    else:
        print('Even Value')
except ValueError:
    print("Ввод данных неверный")