#!/usr/bin/python
# -*- coding: utf8 -*-
"""
Lesson5 Task3.
Ivanyuk D 25.04.2020
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

try:
    with open("L5_T3_t.txt", 'r', encoding='UTF-8') as my_file:
        txt = my_file.read()
except IOError:
    print("error!")
finally:
    my_file.close()
# convert data to list of tuples
sal_list = [tuple(itm.split(' ')) for itm in txt.split('\n')]
# salary < 20
em_les20 = [itm[0] for itm in sal_list if itm[1] < '20']
# avarage value of salary
sal_av = sum(int(s[1]) for s in sal_list)/len(sal_list)
print(sal_list)
print(em_les20)
print(sal_av)

#File content:
# Ivanov 10
# Petrov 15
# Sidorov 25