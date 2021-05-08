"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
 определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
 данных, можно использовать любую подходящую структуру, например словарь.
"""


class Warehouse:
    dic = {1: {1: "Принтеры", 2: "Сканеры", 3: "Копиры"},
           2: {0: "Название", 1: "Модель", 2: "Год выпуска"},
           3: {0: "Склад", 1: "Директор", 2: "Офис", 3: "Торговый зал"},
           4: {1: "Принтер", 2: "Сканер", 3: "Копир"}}

    def __init__(self):
        self.name = "Склад оргтехники"
        self.store = {1: [], 2: [], 3: []}

    def get_equipment(self):
        for key, val in self.store.items():
            print(f'{Warehouse.dic[1].get(key):-^20}')
            for num, eq in enumerate(val, 1):
                if not eq.deleted:
                    print(f'{num}. {eq.name}: {eq.model} # {Warehouse.dic[3].get(eq.place)}')
        return None

    def add_equipment(self, obj_item):
        if obj_item.type == "Printer":
            self.store[1].append(obj_item)
        elif obj_item.type == "Scanner":
            self.store[2].append(obj_item)
        elif obj_item.type == "Copier":
            self.store[3].append(obj_item)
        return None

    def get_equipment_id(self):
        while True:
            eq_type = int(input(", ".join(f'{x}-{y}' for x, y in Warehouse.dic[1].items()) + ": "))
            if eq_type not in Warehouse.dic[1].keys():
                print("Номер введен не верно")
                continue
            else:
                break
        while True:
            eq_id = int(input("Введи порядковй номер устройства из списка: "))
            if eq_id > len(self.store[eq_type]):
                print("Устройтсво не найдено")
                continue
            else:
                break

        return eq_type, eq_id-1

    def change_place(self, eq, place):
        pass


class Equipment:
    def __init__(self, name, model, date_of_prod):
        self.name = name
        self.model = model
        self.date_of_prod = date_of_prod
        self.place = 0
        self.type = None
        self.deleted = False


class Printer(Equipment):
    def __init__(self, name, model, date_of_prod, color):
        super().__init__(name, model, date_of_prod)
        self.color = color
        self.type = 'Printer'


class Scanner(Equipment):
    def __init__(self, name, model, date_of_prod, type_of):
        super().__init__(name, model, date_of_prod)
        self.type = type_of
        self.type = 'Scanner'


class Copier(Equipment):
    def __init__(self, name, model, date_of_prod, format_of):
        super().__init__(name, model, date_of_prod)
        self.format = format_of
        self.type = 'Copier'


class Program:
    def __init__(self):
        self.warehouse = Warehouse()
        self.main_menu = {1:
                          {1: "Вывести список оргтехники",
                           2: "Принять на склад",
                           3: "Списать",
                           4: "Передать в подразделение",
                           5: "Завершить работу"},
                          2:
                              {1: "Принтер",
                               2: "Сканер",
                               3: "Копир"}
                          }

        self.print_menu()

    def print_menu(self, level=1):
        print("M Е Н Ю")
        for key, val in self.main_menu[level].items():
            print(f'{str(key)}. --- {val}')

    def do(self):
        while True:
            print()
            try:
                action = int(input("Выбери действие (показать меню - 0) : "))
            except ValueError:
                continue
            if action == 1:
                self.warehouse.get_equipment()
            elif action == 2:
                self.print_menu(2)
                while True:
                    sub_action = int(input("Выбери тип устройства: "))
                    if sub_action in Warehouse.dic[1].keys():
                        break
                    else:
                        print("Введено неверное знаечение")
                        continue
                eq_params = []
                for string in self.warehouse.dic.get(2).values():
                    eq_params.append(input(f'Введи {string}: '))
                if sub_action == 1:
                    eq_params.append(input(f'Цветной (да/нет): '))
                    new_equipment = Printer(*eq_params)
                elif sub_action == 2:
                    eq_params.append(input(f'Тип сканера : '))
                    new_equipment = Scanner(*eq_params)
                elif sub_action == 3:
                    eq_params.append(input(f'Формат : '))
                    new_equipment = Copier(*eq_params)

                self.warehouse.add_equipment(new_equipment)
            elif action == 3:
                eq_type, eq_id = self.warehouse.get_equipment_id()
                self.warehouse.store[eq_type][eq_id].deleted = True
                print(f'{Warehouse.dic[4].get(eq_type)} {self.warehouse.store[eq_type][eq_id].name} списан')
            elif action == 4:
                eq_type, eq_id = self.warehouse.get_equipment_id()
                self.warehouse.store[eq_type][eq_id].place = int(input(
                    ", ".join(f'{x}-{y}' for x, y in Warehouse.dic[3].items()) + ": "))
                print(f'{Warehouse.dic[4].get(eq_type)} {self.warehouse.store[eq_type][eq_id].name} перемещён')
            elif action == 0:
                self.print_menu()
            else:
                print("Работа программы завершена")
                return None


base = Program()

# предварительный ввод тестовых данных.

base.warehouse.store[1].append(Printer("HP", "1010", "2000", "B/W"))
base.warehouse.store[1].append(Printer("Canon", "mf3110", "2010", "B/W"))
base.warehouse.store[2].append(Printer("Canon", "lide120", "2010", "планшет"))
base.warehouse.store[2].append(Printer("Canon", "lide120", "2010", "планшет"))
base.warehouse.store[3].append(Printer("Xerox", "123", "1999", "A3"))
base.warehouse.store[3].append(Printer("Xerox", "123", "1999", "A3"))

base.do()