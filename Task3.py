"""
Task3.
Ivanyuk D 10.04.2020
3. Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
Считаем 3 + 33 + 333 = 369.
"""
#  Запрашиваем число
num_inp = int(input("Введите число: "))
# Преобразуем в тип сроку и расчитываем
num1 = str(num_inp)
num2 = str(num_inp)*2
num3 = str(num_inp)*3
# Считаем результат
result = int(num1) + int(num2) + int(num3)

print(result)