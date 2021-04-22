# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму
# наибольших двух аргументов.

def my_func(a, b, c):
    list_a = [a, b, c]
    list_a.sort(reverse=True)

    return list_a[0] + list_a[1]


print(my_func(4, 3, 9))
