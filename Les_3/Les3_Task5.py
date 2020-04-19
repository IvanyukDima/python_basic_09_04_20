"""
Lesson3 Task5.
Ivanyuk D 19.04.2020
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
ранее сумме и после этого завершить программу.
"""


def sum_func(num_list: list, var_c: bool):
    '''
    Рассчитываетмя сумма чисел из списка. Если прилетает не число,
    то считается сумма до символа и параметр меняется на False
    '''
    sum = 0
    for itm in num_list:
        if itm.isdigit():
            sum = sum + int(itm)
        else:
            var_c = False
            return sum, var_c
    return sum, var_c

res = ()
var_cont = True
result = 0.
# Просим ввести числа и суммируем до спецсимвола
while var_cont == True:
    str_inp = input("Введите строку из чисел, разделённых пробелами: ")
    num_lst = str_inp.split(' ') # Create a list
    res = sum_func(num_lst, var_cont)
    result = result + res[0]
    var_cont = res[1]

print(result)

