"""
Lesson2 Task2.
Ivanyuk D 14.04.2020
2. Для списка реализовать обмен значений соседних элементов,
т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

str_inp = input("Введите слово: ")
usr_list = list(str_inp)
#  Cycle 2 symbols from the word and replace
j = 0
for i in range(len(usr_list) // 2):
    usr_list[j], usr_list[j+1] = usr_list[j+1], usr_list[j]
    j = j + 2

print(usr_list)