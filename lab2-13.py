try:
    a = int(input())
    b = int(input())
    c = int(input())
    if a + b > c and b + c > a and a + c > b:
        if a == b and b == c:
            print("Equilateral")
        elif a == b or b == c or a == c:
            print("Isosceles")
        else:
            print("Versatile")
    else:
        print("Triangle is not defined!")
except ValueError:
    print("Ввод данных неверный")