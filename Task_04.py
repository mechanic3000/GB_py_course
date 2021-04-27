# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый
# файл.


numbers_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("text_4.txt", encoding="utf-8") as file:
    new_file = open("new_text_04.txt", "w", encoding="utf-8")
    for _ in file:
        space_position = _.index(" ")
        try:
            new_file.write(numbers_dict[_[0:space_position]] + _[space_position:])
        except KeyError:
            new_file.write(_)
    new_file.close()
