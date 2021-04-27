# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
#  Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from functools import reduce

file_name = "text_5.txt"

file = open(file_name, "w", encoding="utf-8")
file.write(input("Введи числа, разделенные пробелами: "))
file.close()

sum_of = 0
with open(file_name, encoding="utf-8") as file:
    for _ in file:
        sum_of = reduce(lambda x, y: x + y, map(int, _.split(" ")))

print(sum_of)
