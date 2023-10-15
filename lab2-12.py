try:
    age = int(input("Please enter your age: "))
    if age <= 13:
        print("childhood")
    elif 14 <= age <= 24:
        print("youth")
    elif 25 <= age <= 59:
        print("maturity")
    else:
        print("old")
except ValueError:
    print("Ввод данных неверный")