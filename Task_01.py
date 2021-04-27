# 1) Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего
# (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке (красный,
# желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении
# выводить соответствующее сообщение и завершать скрипт.

import time
import turtle


class TrafficLight:
    __color_list = ['red', 'yellow', 'green']  # название цветов светофора
    __cur_color = 0
    __stop = False
    __sleep_time = [7, 2, 10]  # время работы каждого цвета
    __circle_size = 40  # размер окружности

    def __init__(self):
        turtle.hideturtle()
        turtle.speed(0)

    def show_clear_lighter(self):
        turtle.color("black", "white")
        turtle.begin_fill()
        turtle.goto(0, 0)
        turtle.circle(self.__circle_size)
        turtle.up()
        turtle.goto(0, -2 * self.__circle_size - 5)
        turtle.down()
        turtle.circle(self.__circle_size)
        turtle.up()
        turtle.goto(0, -4 * self.__circle_size - 10)
        turtle.down()
        turtle.circle(self.__circle_size)
        turtle.up()
        turtle.end_fill()

    def set_color(self):
        if self.__cur_color == 0:
            turtle.goto(0, 0)
            turtle.down()
            turtle.fillcolor(self.__color_list[self.__cur_color])
            turtle.begin_fill()
            turtle.circle(self.__circle_size)
            turtle.end_fill()
            turtle.up()
        elif self.__cur_color == 1:
            turtle.goto(0, -2 * self.__circle_size - 5)
            turtle.down()
            turtle.fillcolor(self.__color_list[self.__cur_color])
            turtle.begin_fill()
            turtle.circle(self.__circle_size)
            turtle.end_fill()
            turtle.up()
        else:
            turtle.goto(0, -4 * self.__circle_size - 10)
            turtle.down()
            turtle.fillcolor(self.__color_list[self.__cur_color])
            turtle.begin_fill()
            turtle.circle(self.__circle_size)
            turtle.end_fill()
            turtle.up()

    def running(self):
        while not self.__stop:
            self.show_clear_lighter()
            self.set_color()
            time.sleep(self.__sleep_time[self.__cur_color])
            self.__cur_color += 1 if self.__cur_color < 2 else -2

    @property
    def get_color(self):
        return self.__color_list[self.__cur_color]

    def set_stop(self):
        self.__stop = True


tr_lght = TrafficLight()
tr_lght.running()

