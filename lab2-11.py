try:
    # вводим два числа
    n1 = int(input())
    n2 = int(input())
    # задаем условие чтобы определить наименьшее среди двух введенных чисел
    if n1 < n2:
        print(n1)
    else:
         print(n2)
except ValueError:
    print("Ввод данных неверный")