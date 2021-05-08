"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
 и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""

import re


class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @classmethod
    def prepare(cls, string):
        a, b = (string[0:re.search('[+\-]', string).start()],
                string[re.search('[+\-]', string).start():-1])

        return Complex(int(a), int(b))

    def __str__(self):
        return f"({self.a}{'+' if self.b>=0 and self.b != 0 else ''}{self.b if self.b != 0 else ''}" \
               f"{'i' if self.b !=0 else ''})"

    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        return Complex(self.a - other.a, self.b - other.b)

    def __truediv__(self, other):
        return Complex((self.a * other.a + self.b * other.b)/(other.a ** 2 + other.b ** 2),
                       (other.a * self.b - self.a * other.b)/(other.a ** 2 + other.b ** 2))

    def __mul__(self, other):
        return Complex(self.a * other.a - self.b * other.b, self.a * other.b + other.a * self.b)


A = Complex.prepare("4+5i")
B = Complex.prepare("3-5i")

print(A + B)
print(A - B)
print(A / B)
print(A * B)
