# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс)
# этого проекта — одежда,
#  которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов
#  одежды существуют
# параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
# (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать '
# абстрактные классы для основных классов проекта,
#  проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class WearAbstractClass(ABC):
    @property
    @abstractmethod
    def consumption(self):
        pass


class Wear(WearAbstractClass):
    def __init__(self, title, x):
        self.title = title
        self.x = x

    @property
    def consumption(self):
        return None


class Coat(Wear):
    @property
    def consumption(self):
        return round(self.x / 6.5 + 0.5, 2)


class Costume(Wear):
    @property
    def consumption(self):
        return round(2 * self.x + 0.3, 2)


c = Coat('D&G', 52)
print(c.title)
print(c.consumption)

print()

co = Costume('Love', 1.85)
print(co.title)
print(co.consumption)

print()
print(c.consumption + co.consumption)
