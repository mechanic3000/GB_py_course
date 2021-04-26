# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
#  Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней
#  величины дохода сотрудников.

f = open('text_3.txt', 'r')

workers_list = list()
for line in f:
    workers_list.append(line.strip().split(' '))
f.close()

sum_salary = 0
print('Сотрудники с окладом меньше 20`000:')
for worker in workers_list:
    if float(worker[1]) < 20_000:
        print(worker[0])
    sum_salary += float(worker[1])

print(f'\nСредняя ЗП сотрудников - {str(sum_salary/len(workers_list))}')
