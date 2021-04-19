"""
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с
прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово
состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с
заглавной буквы. Необходимо использовать написанную ранее функцию int_func().
"""


def int_func(word):
    return word.title()


def check_latin(word):
    for c in word:
        if ord(c) in range(65, 91) or ord(c) in range(97, 123):  #  если нужны только маленькие, то первую чать проверки можно убрать.
            continue
        else:
            return False
    return True


def do_title(input_line):
    input_line = input_line.split(" ")
    return " ".join(int_func(x) for x in input_line if check_latin(x))


print(do_title(input("Введи строку из слов латинскими буквами, разделенных пробелами: ")))

