# 3) Реализовать базовый класс Worker (работник), в котором определить атрибуты: name,
# surname, position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность)
# на базе класса Worker. В классе Position реализовать методы получения полного имени сотрудника (get_full_name)и дохода
# с учетом премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

    @property
    def wage(self):
        return self._income['wage']

    @property
    def bonus(self):
        return self._income['bonus']


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return f"Полный доход сотрудника = {self.wage + self.bonus}"


w1 = Position("Василий", "Пупкин", "дворник", 1000, 150)
print(w1.position)
print(w1.get_full_name())
print(w1.get_total_income())
print()

w2 = Position("Тимур", "Пыжиков", "специалист", 5000, 1150)
print(w2.position)
print(w2.get_full_name())
print(w2.get_total_income())
