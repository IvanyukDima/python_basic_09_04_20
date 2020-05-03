#!/usr/bin/python
# -*- coding: utf8 -*-
"""
Lesson5 Task7.
Ivanyuk D 26.04.2020
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
"""

import json

# Считываем строки из файла
try:
    with open("L5_T7_t.txt", 'r', encoding='UTF-8') as my_file:
        txt = my_file.read()
except IOError:
    print("error!")
finally:
    my_file.close()

# Делаем список из строк
txt_lst = txt.split('\n')
print(txt)

i=0  # счетчик фирм
sm=0  # сумма выручки
firm_list = []  # список для JS
avg_prof = {}  # Словарь со средней прибылью
profit = {}  # Словарь с фирмами и прибылью

#  Бежим по строкам и суммируем выручку
for el in txt_lst:
    firm_lst = el.split()
    pr = int(firm_lst[2]) - int(firm_lst[3])
    if pr >= 0:
        profit[firm_lst[0]] = pr
        i += 1
        sm = sm + pr

# Считаем среднюю выручку и создаем список для JS
avg_pr = sm / i
avg_prof = {'average_profit': avg_pr}
firm_list = [profit, avg_prof]


#  Создаем и сохраняем в файл
j_data = json.dumps(firm_list)

with open('L5_T6.json', 'w') as file_js:
    file_js.write(j_data)

print(j_data)
