#!/usr/bin/python
# -*- coding: utf8 -*-
"""
Lesson6 Task1.
Ivanyuk D 28.04.2020
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
from time import sleep


class TrafficLight:
    __color = 'Red'

    def running(self):
        i = 0
        while i < 2:
            self.__color = "Red"
            print(self.__color)
            sleep(5)
            self.__color = "Yellow"
            print(self.__color)
            sleep(2)
            self.__color = "Green"
            print(self.__color)
            sleep(10)
            i += 1


turn = TrafficLight()
turn.running()
