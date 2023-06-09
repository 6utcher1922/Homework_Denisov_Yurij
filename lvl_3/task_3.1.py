# Задача 3.1.
# Создайте класс матрицы (или таблицы).
# Требования к классу:
#   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
#   - в каждой ячейке содержится либо число, либо None
#   - доступы следующие методы матрицы:
#       * принимать новые значения, 
#       * заменять существующие значения, 
#       * выводить число строк и колонок.

# Пример матрицы 10 на 10 из единиц:
# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# Примечание! 
#   - новый класс не запрещено строить на базе существующих типов данных: списков, словарей и тд.
#   - отображать в таблице/матрице название колонки не обязательно!
#   - проявите фантазию :)

# Моё решение:

class Matrix:
    def __init__(self, x, y, val=None):
        self.__num_column = x
        self.__num_row = y
        self.__table = [[val for _ in range(x)] for _ in range(y)]

    def set_value(self, x, y, val):
        if x >= self.__num_column or y >= self.__num_row:
            raise ValueError('Index out of range')
        self.__table[y][x] = val

    def replace_value(self, x, y, val):
        if x >= self.__num_column or y >= self.__num_row:
            raise ValueError('Index out of range')
        if self.__table[y][x] is None:
            raise ValueError("Can't replace None")
        self.__table[y][x] = val

    def get_value(self, x, y):
        return self.__table[y][x]
    def num_row(self):
        return self.__num_row
    def num_column(self):
        return self.__num_column
    def print(self):
        for y in range(self.__num_row):
            print('\t'.join((str(r) if r is not None else 'N') for r in self.__table[y]))
        print()

matrix = Matrix(5, 5)
matrix.print()

matrix.set_value(1, 2, 4)
matrix.print()

matrix.set_value(1 , 1, 10)
matrix.print()
