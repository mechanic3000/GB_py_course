# 4) Реализуйте базовый класс Car.У данного класса должны быть следующие атрибуты: speed, color,name,is_police (булево).
# А также методы: go,stop,turn(direction),которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar,SportCar,WorkCar,PoliceCar.Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar)и 40 (WorkCar)должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
# атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

import random


class Car:
    def __init__(self, name, color, is_police=False):
        self.name = name
        self.color = color
        self._is_police = is_police
        self._speed = 0

    def go(self):
        self._speed = 5
        print(f'{"✰✰✰ " if self._is_police else ""}Автомобиль {self.color} {self.name} тронулся. Скорость '
              f'{self._speed} км/ч')

    def stop(self):
        self._speed = 0
        print(f'{"✰✰✰ " if self._is_police else ""}Автомобиль {self.color} {self.name} остановился')

    def turn(self, direction):
        print(f'{"✰✰✰ " if self._is_police else ""}Автомобиль {self.color} {self.name} повернул {direction}')

    def set_speed(self, speed):
        self._speed = speed
        self.show_speed()

    def show_speed(self):
        print(f'{"✰✰✰ " if self._is_police else ""}Скорость автомобиля {self.color} {self.name} - {self._speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        print(f"Скорость автомобиля {self.color} {self.name} - {self._speed} км/ч")
        PoliceCar.looking(self._speed)


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(f"Скорость автомобиля {self.color} {self.name} - {self._speed} км/ч")
        PoliceCar.looking(self._speed)


class PoliceCar(Car):
    @staticmethod
    def looking(speed):
        if speed > 40:
            print("ПРЕВЫЕШЕНИЕ СКОРОСТИ!!!")
            if random.choice([True, False]):
                print("Oooops, его засекли!")
                some_p_car = PoliceCar("Ford", "белый", True)
                some_p_car.set_speed(90)
            else:
                print("На этот раз ему повезло! Его не заметили.")


t_car1 = TownCar("Toyota", "белый")
t_car1.go()
t_car1.set_speed(30)
t_car1.turn("налево")
t_car1.turn("направо")
t_car1.set_speed(65)


s_car1 = SportCar("Lamborghini Diablo", "желтый")
s_car1.go()
s_car1.set_speed(250)
