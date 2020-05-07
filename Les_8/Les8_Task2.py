#!/usr/bin/python
# -*- coding: utf8 -*-
"""
Lesson8 Task2.
Ivanyuk D 07.05.2020
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""

class Exc:
    def __init__(self, div, den):
        self.div = div
        self.den = den

    @staticmethod
    def divide(div,den):
        try:
            return (div / den)
        except:
            return (f"Делить на ноль нельзя")

d1 = Exc(5, 6)
print(d1.divide(3, 2))
print(d1.divide(19, 0))