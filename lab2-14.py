try:
    a = int(input())
    b = int(input())
    c = int(input())
    d = int (input())
    if d == b + 1 and (c == a + 1 or c == a - 1):
        print("YES")
    else:
        print("NO")
except ValueError:
    print("Ввод данных неверный")