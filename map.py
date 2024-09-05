import copy
from random import randint

from main import Predator


class Map:
    """Поле"""

    def __init__(self, rows=4, cols=4):
        self.rows = rows
        self.cols = cols
        self.field = self.game_field(self.rows, self.cols)
        self.coordinates_objects = {}

    def game_field(self, rows, cols):
        """Создание словаря с координатами в виде ключей и нулями в виде значения"""
        field = {}
        for i in range(rows + 1):
            for j in range(cols + 1):
                field.setdefault((i, j), 0)
        return field

    def add_obj(self, obj, rows, cols):
        """Добавление объекта в словарь поля"""
        self.coordinates_objects[(rows, cols)] = obj
        self.field[rows, cols] = obj

    def is_free(self, row, col):
        """Проверка поля на наличие свободного места"""
        if 0 <= row <= self.rows and 0 <= col <= self.cols and (row, col) not in self.coordinates_objects:
            return True
        else:
            return False

    def get_empty_coordin(self):
        """Получение рандомной, свободной координаты на поле"""
        while True:
            coord_row, coord_colm = randint(0, self.rows), randint(0, self.cols)
            if self.field[(coord_colm, coord_row)] == 0:
                return coord_row, coord_colm

    def changing_obj_field(self):
        """Изменение положения объекта на поле"""
        for key, value in copy.copy(self.coordinates_objects).items():
            if value.name == 'Хищник':
                self.field[key] = 0
                del self.coordinates_objects[key]
                step = [(0, -1), (-1, 0), (0, 1), (1, 0)]
                count = 0
                for row, col in step:
                    new_key = (key[0] + row, key[1] + col)
                    if self.is_free(new_key[0], new_key[1]):
                        self.add_obj(Predator(new_key[0], new_key[1]), new_key[0], new_key[1])
                        break
                    else:
                        count += 1
                if count == 4:
                    raise ValueError('Занято')

    def __getitem__(self, item):
        return self.field.get(item)

    def __setitem__(self, key, value):
        self.field[key] = value

    def __delitem__(self, key):
        self.field[key] = 0

    def __iter__(self):
        yield from self.field.items()

    def __str__(self):
        return f'{self.field}'
