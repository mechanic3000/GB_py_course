"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
ситуацию и не завершиться с ошибкой.
"""


class NullDivision(Exception):
    def __init__(self, message):
        self.message = message


a, b = map(int, input("Введи 2 числа через пробел: ").split(" "))
while True:
    try:
        if b == 0:
            raise NullDivision("Деление на 0!")
    except NullDivision:
        b = int(input("Ошибка! Делитель = 0. Введите другое число: "))
    else:
        print(f'a/b = {a/b}')
        break

