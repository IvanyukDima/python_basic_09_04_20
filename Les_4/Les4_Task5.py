"""
Lesson4 Task5.
Ivanyuk D 22.04.2020
5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""
from functools import reduce

def my_func(prev_el, el):
    # prev_el - предыдущий элемент
    # el - текущий элемент
    return prev_el + el

def my_func(prev_el, el):
    # prev_el - предыдущий элемент
    # el - текущий элемент
    return prev_el + el


my_list = [el for el in range(100, 1001) if el % 2 == 0]
a = reduce(my_func, [el for el in range(100, 1001) if el % 2 == 0])
print(my_list)
print(a)






