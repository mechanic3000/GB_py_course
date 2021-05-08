"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
 В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
 преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
 и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Data:
    def __init__(self, date_list):
        self.data_list = date_list

    @classmethod
    def date_split(cls, string=''):
        try:
            date_list = list(map(int, string.split("-")))
            if Data.check_date(date_list):
                return cls(date_list)
            else:
                raise Exception("Введенная дата не верна")
        except ValueError:
            raise Exception("Ошибка значения. Введите дату в формате ДД-ММ-ГГГГ")

    @staticmethod
    def check_date(date_list):
        done = True
        if date_list[0] not in range(1, 32) or date_list[1] not in range(1, 13):
            done = False
        return done


DATE = "01-01-2021"
c = Data.date_split(DATE)
print(c.data_list)



