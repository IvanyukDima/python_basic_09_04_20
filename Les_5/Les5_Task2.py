#!/usr/bin/python
# -*- coding: utf8 -*-
"""
Lesson5 Task2.
Ivanyuk D 25.04.2020
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
try:
    with open("L5_T2_t.txt", 'r', encoding='UTF-8') as my_file:
        txt = my_file.read()
except IOError:
    print("error!")
finally:
    my_file.close()

txt_lst = txt.split('\n')
cnt_lin = len(txt_lst)
print(txt_lst)
print(cnt_lin)
for i, el in enumerate(txt_lst):
    print(i + 1, len(el))





