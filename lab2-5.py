try:
    c1 = int(input())
    r1 = int(input())
    c2 = int(input())
    r2 = int(input())
    # условие определяющее может ли король за один ход перейти с первого поля на второе
    if c1 == c2 - 1 and r1 == r2 - 1:
        print ("YES")
    else:
        print ("NO")
except ValueError:
    print("Ввод данных неверный")