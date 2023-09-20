import math

exit = False

while not exit:
    print("")
    print("Какую операцию вы хотите выполнить?")
    print("1 Сложение")
    print("2 Вычитание")
    print("3 Деление")
    print("4 Умножение")
    print("5 Факториал")
    print("6 Найти квадратный корень из числа")
    print("7 Возвести число в степень N")
    print("8 Синус")
    print("9 Косинус")
    print("10 Тангенс")
    print("11 Выйти из калькулятора")

    v = int(input())
    r = 0
    t = ""
    q1 = 0
    q2 = 0
    m = 0
    s = 0
    l = 0

    if 1 <= v <= 4:
        q1 = int(input("Введите число 1: "))
        q2 = int(input("Введите число 2: "))
    elif 5 <= v <= 6:
        m = int(input("Введите число: "))
    elif v == 7:
        s = int(input("Введите число: "))
        l = int(input("Введите N: "))
        
    elif 8 <= v <= 10:
        m = int(input("Введите число: "))

    if v == 1:
        r = q1 + q2
        t = "сложения"
    elif v == 2:
        r = q1 - q2
        t = "вычитания"
    elif v == 3:
        if q2 != 0:
            r = q1 / q2
            t = "деления"
        else:
            print("Ошибка: нельзя делить на ноль.")
            continue
    elif v == 4:
        r = q1 * q2
        t = "умножения"
    elif v == 5:
        r = math.factorial(m)
        t = "факториала"
   
    elif v == 6:
        if m >= 0:
            r = math.sqrt(m)
            t = "квадратного корня из числа"
        else:
            print("Ошибка: нельзя извлекать квадратный корень из отрицательного числа.")
            continue
    elif v == 7:
        r = s ** l
        t = "возвести число в степень"
    elif v == 8:
        r = math.sin(math.radians(m))
        t = "синуса"
    elif v == 9:
        r = math.cos(math.radians(m))
        t = "косинуса"
    elif v == 10:
        r = math.tan(math.radians(m))
        t = "тангенса"
    elif v == 11:
        print("Выход из программы.")
        exit = True
        break
    else:
        print("Ошибка: неверный выбор операции.")
        continue

    print("Результат " + t + " = " + str(r))
