"""
Lesson4 Task6.
Ivanyuk D 22.04.2020
5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""

from itertools import count
from itertools import cycle

for i in count(5):
    print(i)

lst = [1,2,3]
for itm in cycle(lst):
    print(itm)