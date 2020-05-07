#!/usr/bin/python
# -*- coding: utf8 -*-
"""
Lesson5 Task4.
Ivanyuk D 25.04.2020
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

try:
    with open("L5_T4_t.txt", 'r', encoding='UTF-8') as my_file:
        txt = my_file.read()
except IOError:
    print("error!")
finally:
    my_file.close()

num_dict = {'1': "Один", '2': "Два", '3': "Три", '4': "Четыре"}
# convert data to list of tuples
num_list = [tuple(itm.split('-')) for itm in txt.split('\n')]
# new list with replaced data
num_list_r = [(num_dict.get(itm[1]), itm[1]) for itm in num_list]
# new text for file
txt_list = [str(itm[0] + '-' + itm[1] + '\n')for itm in num_list_r]

try:
    with open("L5_T4_t1.txt", 'w', encoding='UTF-8') as my_file_r:
        my_file_r.writelines(txt_list)
except IOError:
    print("error!")
finally:
    my_file_r.close()









