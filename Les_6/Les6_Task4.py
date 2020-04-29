#!/usr/bin/python
# -*- coding: utf8 -*-
"""
Lesson6 Task4.
Ivanyuk D 28.04.2020
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Выполните вызов методов и также покажите результат.
"""

from random import randint


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return print(self.name, 'start')

    def stop(self):
        return print(self.name, 'stop')

    def turn(self, direction):
        return print(self.name, direction)

    def show_speed(self):
        self.speed = randint(0, 220)
        return self.speed

class TownCar(Car):
    def __init__(self, speed, color, name,is_police ):
        super().__init__(speed, color, name,is_police )

    def show_speed(self):
        self.speed = randint(0, 220)
        if self.speed > 60:
            print('Превышение скорости!', self.speed)
        return self.speed

class SportCar(Car):
    def __init__(self, speed, color, name,is_police ):
        super().__init__(speed, color, name,is_police )


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police ):
        super().__init__(speed, color, name, is_police )

    def show_speed(self):
        self.speed = randint(0, 180)
        if self.speed > 40:
            print('Превышение скорости!', self.speed)
        return self.speed

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police ):
        super().__init__(speed, color, name, is_police)


car1 = Car(200,'Green','Ford',False)
car2 = TownCar(200,'Green','Ford',False)
print(car2.speed,car2.name,car2.color)
car2.show_speed()
car2.stop()
car3 = WorkCar(150,'Red','KAMAZ',False)
print(car3.speed,car3.name,car3.color)
car4 = SportCar(150,'Yellow','Mazda',False)
print(car4.speed,car4.name,car4.color)
car5 = PoliceCar(180,'White','Lada',True)
print(car5.speed,car5.name,car5.color,car5.is_police)