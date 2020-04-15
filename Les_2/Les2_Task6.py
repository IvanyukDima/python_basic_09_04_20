"""
Lesson2 Task6.
Ivanyuk D 15.04.2020
6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

Необходимо собрать аналитику о товарах.
Реализовать словарь, в котором каждый ключ — характеристика товара, например название,
а значение — список значений-характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""

prod_list = []  # Структура товара
str_dict = ['название', 'цена', 'количество', 'eд']
#  Создаем структуру данных товары
i = 1
while i < 3:
    str = {}
    prod_lst = []
    for itm in str_dict:
        val = input(f'Введите описание товара в поле {itm} для товара № {i} :')
        str[itm] = val
    prod_lst.append(i)
    prod_lst.append(str)
    prod_tpl = tuple(prod_lst)
    prod_list.append(prod_tpl)
    i += 1

print(prod_list)

#  аналитика
lst_n = []
lst_p = []
lst_c = []
lst_u = []

#  Собираем списки по ключам для аналитик
for itm in prod_list:
    struct = itm[1]
    name = struct.get(str_dict[0])
    price = struct.get(str_dict[1])
    count = struct.get(str_dict[2])
    unit = struct.get(str_dict[3])
    lst_n.append(name)
    lst_p.append(price)
    lst_c.append(count)
    lst_u.append(unit)

#  Оставляем уникальные значения
lst_n = list(dict.fromkeys(lst_n))
lst_p = list(dict.fromkeys(lst_p))
lst_c = list(dict.fromkeys(lst_c))
lst_u = list(dict.fromkeys(lst_u))

# Результат
res = {str_dict[0]: lst_n, str_dict[1]: lst_p, str_dict[2]: lst_c, str_dict[3]: lst_u }
print(res)