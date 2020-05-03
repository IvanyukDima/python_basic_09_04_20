#!/usr/bin/python
# -*- coding: utf8 -*-
"""
Lesson6 Task5.
Ivanyuk D 28.04.2020
5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return print(self.title, 'Запуск отрисовки')

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
        self.type = type

    def draw(self):
        return print(self.title, 'Подпись')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return print(self.title, 'Карандаш')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return print(self.title, 'Маркер')


pen = Pen(title='Ручка')
pencil = Pencil(title='Карандаш')
handle = Handle(title='Маркер')
pen.draw()
pencil.draw()
handle.draw()

