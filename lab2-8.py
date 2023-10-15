try:
    w = int(input())
    if 15 <= w <= 60:
        print("Light weight")
    elif 60 < w <= 64:
        print("First welterweight")
    else:
        print("Welterweight")
except ValueError:
    print("Ввод данных неверный")