"""
Lesson4 Task1.
Ivanyuk D 22.04.2020
2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
"""

my_list = [7, 8, 2, 4, 9, 6]
my_list1 = [el for i, el in enumerate(my_list) if i > 0 and my_list[i-1] < my_list[i]]
print(my_list1)


# lst = []
# for i, el in enumerate(my_list):
#     if i > 0:
#      if my_list[i-1] < my_list[i]:
#          lst.append(el)
#
# print(lst)



