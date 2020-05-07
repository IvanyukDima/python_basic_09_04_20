#!/usr/bin/python
# -*- coding: utf8 -*-
"""
Lesson7 Task2.
Ivanyuk D 03.05.2020
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""


class Cloth:
    def __init__(self, value, height):
        self.value = value
        self.height = height

    def get_square_coat(self):
        return self.value / 6.5 + 0.5

    def get_square_jack(self):
        return self.height * 2 + 0.3

    @property
    def square(self):
        return (self.value / 1 + 0.5) + (self.height * 2 + 0.3)


class Coat(Cloth):
    def __init__(self, value, height):
        super().__init__(value, height)
        self.square_coat = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь на пальто {self.square_c}'


class Jacket(Cloth):
    def __init__(self, value, height):
        super().__init__(value, height)
        self.square_jack = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Площадь на костюм {self.square_jack}'


ct = Cloth(3, 6)
print(ct.get_square_coat())
jk = Cloth(3, 6)
print(jk.get_square_jack())
print(jk.square)