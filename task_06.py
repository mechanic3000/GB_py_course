"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не
должен быть бесконечным. Необходимо предусмотреть условие его завершения.

Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл. Во втором
также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""

from itertools import count
from itertools import takewhile
from itertools import cycle

START_NUMBER = 3
STOP_NUMBER = 10
ELEMENTS_COUNT = 20

list_a = list(takewhile(lambda i: i <= STOP_NUMBER, count(START_NUMBER)))

j = 0
for item in cycle(list_a):
    if j <= ELEMENTS_COUNT:
        print(str(item), end=" ")
        j += 1
    else:
        break


