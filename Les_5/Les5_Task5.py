#!/usr/bin/python
# -*- coding: utf8 -*-
"""
Lesson5 Task5.
Ivanyuk D 25.04.2020
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
# create data
lst = [1, 2, 3, 4, 5, 6]
txt = ' '.join(str(itm) for itm in lst)
# write
try:
    with open("L5_T5_t.txt", 'w', encoding='UTF-8') as my_file:
        my_file.writelines(txt)
except IOError:
    print("error!")
finally:
    my_file.close()

# read
try:
    with open("L5_T5_t.txt", 'r', encoding='UTF-8') as my_file:
        txt_p = my_file.read()
except IOError:
    print("error!")
finally:
    my_file.close()

# convert, calculate and print
dt_lst = list(map(int, txt_p.split(' ')))
print(sum(dt_lst))