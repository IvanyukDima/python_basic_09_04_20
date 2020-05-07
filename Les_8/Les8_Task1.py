#!/usr/bin/python
# -*- coding: utf8 -*-
"""
Lesson8 Task1.
Ivanyuk D 07.05.2020
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год
и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""

class Data:
    def __init__(self, d_m_y):
        self.d_m_y = d_m_y

    @classmethod
    def extract(cls, d_m_y):
        my_date = []

        for i in d_m_y.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2019 >= year >= 0:
                    return f'Успешно'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.d_m_y)}'

day = Data('07 - 5 - 2020')
print(day)
print(Data.valid(11, 11, 2022))
print(day.valid(11, 13, 2011))
print(Data.extract('11 - 11 - 2019'))
print(day.extract('11 - 11 - 2020'))
print(Data.valid(1, 11, 2000))




