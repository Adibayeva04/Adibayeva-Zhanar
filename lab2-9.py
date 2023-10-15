try:
    password_1 = input()
    password_2 = input()
    # задаем условие для того чтобы проверить совпадают ли первый пароль со вторым
    if password_1 == password_2:
         print('Password accepted')
    else:
        print('Password not accepted')
except ValueError:
    print("Ввод данных неверный")