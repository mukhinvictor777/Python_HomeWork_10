"""
Создать не менее двух дескрипторов для атрибутов классов, которые вы создали ранее в ДЗ
"""


class ToPositiveInteger:

    def __set_name__(self, owner, quantity):
        self.quantity = quantity

    def __set__(self, instance, value):
        try:
            int(value)
        except ValueError:
            raise ValueError("Количество ячеек может быть только целым числом больше нуля")
        if value % 1 != 0:
            raise ValueError("Количество ячеек может быть только целым числом больше нуля")
        if value < 0:
            raise ValueError("Количество ячеек может быть только целым числом больше нуля")
        instance.__dict__[self.quantity] = value


class Cell:

    quantity = ToPositiveInteger()

    def __init__(self, quantity):
        try:
            int(quantity)
        except ValueError:
            print(f'Количество ячеек может быть только целым числом')
        quantity = int(quantity)
        if quantity < 1:
            print(f'Количество ячеек может быть только целым числом больше нуля')
        else:
            self.quantity = quantity

    def __add__(self, other):
        return f'Число ячеек общей клетки равно, полученной в результате сложения двух клеток равно: ' \
               f'{self.quantity + other.quantity}'

    def __sub__(self, other):
        if self.quantity > other.quantity:
            return f'Число ячеек общей клетки равно, полученной в результате вычитания двух клеток равно: ' \
                   f'{self.quantity - other.quantity}'
        else:
            return f'Нельзя произвести вычитание данных клеток. Первая клетка должна быть строго больше второй '

    def __mul__(self, other):
        return f'Число ячеек общей клетки, полученной в результате умножения двух клеток равно: ' \
               f'{self.quantity * other.quantity}'

    def __truediv__(self, other):
        return f'Число ячеек общей клетки, полученной в результате деления двух клеток равно: ' \
               f'{self.quantity // other.quantity}'

    def make_order(self, row):
        result = ''
        for i in range(self.quantity // row):
            result += '*' * row + '\n'
        result += '*' * (self.quantity % row)
        return result


cell1 = Cell(30)
cell2 = Cell(25)
cell3 = Cell(10)
cell4 = Cell(15)

print()
print(cell1.quantity)
"""
# Проверяем работает ли валидация по 2м параметрам (целое число, больше нуля)

cell1.quantity = 'text'
print()
cell1.quantity = 40.4
print()
print(cell1.quantity)
cell1.quantity = -50
print()
print(cell1.quantity)
"""

print()
print("Складываем")
print(cell1 + cell2)
print()
print("Вычитаем")
print(cell2 - cell1)
print(cell4 - cell3)
print()
print("Умножаем")
print(cell2 * cell1)
print()
print("Делим")
print(cell1 / cell2)
print()

print("Организация ячеек по рядам")
print()
print(cell1.make_order(5))
print(cell2.make_order(10))
