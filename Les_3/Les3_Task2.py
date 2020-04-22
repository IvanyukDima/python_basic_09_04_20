"""
Lesson3 Task2.
Ivanyuk D 18.04.2020
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""

# Структура справочника
user_str = {
    'name': ("Имя", str),
    'surname': ("Фамилия", str),
    'year': ("Год рождения", int),
    'city': ("Город проживания", str),
    'email': ("email", str),
    'phone': ("Телефон", str)
}

#  заполним данные пользователя
user_dict = {}
for key, value in user_str.items():
    while True:
        user_inp = input(f'{value[0]}: ')
        try:
            user_inp = value[1](user_inp)
        except ValueError as e:
            print(f"{e}\nНеверное значение данных")
            continue
        user_dict[key] = user_inp
        break


# Вывод строки из словаря
def userlist_func(**usrstr):
    '''
    Печатаем строку о пользователе
    '''
    usr_lst = list(usrstr.values())
    usr_str = ' '.join(map(str, usr_lst))
    return print(usr_str)


# Передаем именованные параметры
userlist_func(**user_dict)
