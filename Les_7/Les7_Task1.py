#!/usr/bin/python
# -*- coding: utf8 -*-
"""
Lesson7 Task1.
Ivanyuk D 02.05.2020
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
"""


#  class matrix
class Matrix:
    def __init__(self, *args):
        self.mtx1 = args[0]
        self.mtx2 = args[1]

    # reload add sum matrix1 + matrix1
    def __add__(self):
        mtrx = self.mtx1
        for i in range(len(self.mtx1)):
            for j in range(len(self.mtx2[i])):
                mtrx[i][j] = self.mtx1[i][j] + self.mtx2[i][j]
        self.mtrx = mtrx
        return self.mtrx

    #  formatting to string
    def __str__(self):
        return '\n'.join(' '.join(str(e) for e in el) for el in self.mtrx)


mtrx1 = [[1, 2, 3], [3, 4, 6]]
mtrx2 = [[3, 4, 5], [4, 2, 5]]

m = Matrix(mtrx1, mtrx2)

print(m.__add__())
print(m.__str__())
