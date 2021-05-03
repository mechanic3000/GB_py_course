# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который
# должен принимать данные (список списков) для
#  формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, matrix_list=()):
        self.__matrix_list = list(matrix_list)

    def __str__(self):
        p_matrix = ''
        for row in self.__matrix_list:
            for column in row:
                p_matrix += str(column) + " "
            p_matrix = p_matrix.rstrip() + "\n"

        return p_matrix.rstrip("\n")

    def __add__(self, other):
        n_matrix = list(map(lambda x, y: map(lambda j, k: j + k, x, y), self, other))
        return Matrix(n_matrix)

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        try:
            m_line = self.__matrix_list[self.n]
        except IndexError:
            raise StopIteration()
        self.n += 1
        return m_line


m1 = Matrix(((1, 2, 3), (4, 5, 6), (7, 8, 9)))
print(m1)
print()

m2 = Matrix(((9, 8, 7), (6, 5, 4), (3, 2, 1)))
print(m2)
print()

m3 = m1 + m2
print(m3)