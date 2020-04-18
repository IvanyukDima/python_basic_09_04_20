"""
Lesson3 Task3.
Ivanyuk D 18.04.2020
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
 и возвращает сумму наибольших двух аргументов.
"""
#  Просим пользователя ввести 3 числа
while True:
    num1_inp = input("Введите первое число: ")
    num2_inp = input("Введите второе число: ")
    num3_inp = input("Введите третье число: ")
    if num1_inp.isdigit() and num2_inp.isdigit() and num3_inp.isdigit():
        num1_inp = int(num1_inp)
        num2_inp = int(num2_inp)
        num3_inp = int(num3_inp)
        break
    else:
        print('Ошибка ввода, введите натуральные числа')


def my_func(a1, a2, a3):
    """
    функцию принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов
    """
    lst = [a1, a2, a3]
    lst.sort()
    return lst[1] + lst[2]

# Выводим сумму наибольших из них
print(my_func(num1_inp, num2_inp, num3_inp))
