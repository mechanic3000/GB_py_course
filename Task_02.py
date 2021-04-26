# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

f = open('task_02.txt', 'r')
text = f.readlines()
f.close()

line_count = len(text)
print("Всего в тексте строк - " + str(line_count))
print("Количество слов в каждой строке:")

word_count = 0
line_number = 1
for line in text:
    word_count = line.count(' ') + 1
    print('Строка {} - {}'.format(line_number, word_count))
    line_number += 1