# 2) Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width
# (ширина). Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу:
# длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна.
# Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т


class Road:
    def __init__(self, length=0, width=0, weight=25, thickness=5):
        self._length = length
        self._width = width
        self._weight = weight
        self._thickness = thickness

    def _calc(self):
        return int(self._length * self._width * self._thickness * self._weight / 1000)

    @property
    def result(self):
        return str(self._calc())+" т."


r = Road(5000, 20)  # протяженность дороги (м), ширина дороги (м)
print(r.result)
