"""
Lesson3 Task1.
Ivanyuk D 18.04.2020
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""

#  Просим пользователя ввести 2 числа
while True:
    num1_inp = input("Введите числитель: ")
    num2_inp = input("Введите знаменатель: ")
    if num1_inp.isdigit() and num2_inp.isdigit():
        num1_inp = int(num1_inp)
        num2_inp = int(num2_inp)
        break
    else:
        print('Ошибка ввода, введите целые числа')


# Делим 2 числа
def div_func(num, denom):
    """
    Деление двух чисел
    """
    try:
        res = num / denom
    except ZeroDivisionError:
        print('Деление на ноль запрещено!')
        return

    return res


num_calc = div_func(num1_inp, num2_inp)
print(num_calc)
