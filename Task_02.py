# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.
#

def my_func(fname='-', sname='-', birth_year='-', city='-', email='-', phone='-'):
    return (f"Имя: {fname}, Фамилия: {sname}, год рождения: {birth_year}, "
            f"город проживания: {city}, e-mail: {email}, телефон: {phone}")


v_print = my_func(fname="Иван", birth_year="1983", city="Калифорния", phone="+78889997766")
print(v_print)
