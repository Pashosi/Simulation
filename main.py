from abc import ABC, abstractmethod
import numpy as np
from random import randint, shuffle


class Entity(ABC):
    """Корневой абстрактный класс"""

    @abstractmethod
    def __init__(self):
        self.name = 'Корневой класс'
        pass

    def __format__(self, format_spec):
        if format_spec.startswith('^'):
            width = int(format_spec[1:])
            return self.name.center(width)
        else:
            # Если спецификация формата не начинается с ^,
            # то используем стандартное форматирование.
            return format(self.name, format_spec)


class Rock(Entity):
    """Камень. Статичный объект"""

    def __init__(self):
        self.name = 'Камень'

    def __repr__(self):
        return self.name


class Tree(Entity):
    """Дерево. Статичный объект"""

    def __init__(self):
        self.name = 'Дерево'

    def __repr__(self):
        return 'Дерево'


class Grass(Entity):
    """Трава. Ресурс для травоядных"""

    def __init__(self):
        self.name = 'Трава'

    def __repr__(self):
        return self.name


class Creature(Entity):
    """Существо"""

    def __init__(self):
        self.step = 1
        self.hit_points = 10
        self.name = 'Существо'

    @abstractmethod
    def make_move(self):
        """Сделать ход"""
        pass


class Herbivore(Creature):
    """Травоядное"""

    def __init__(self):
        super().__init__()
        self.name = 'Травоядное'

    def make_move(self):
        pass

    def __repr__(self):
        return 'Травоядное'


class Predator(Creature):
    """Хищник"""

    def __init__(self):
        super().__init__()
        self.power_attack = 10
        self.name = 'Хищник'

    def make_move(self):
        pass

    def __repr__(self):
        return 'Хищник'


class Map:
    """Поле"""

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.field = type(self).game_field(self.rows, self.cols)

    @staticmethod
    def game_field(rows, cols):
        field = {}
        for i in range(rows + 1):
            for j in range(cols + 1):
                field.setdefault((i, j), 0)
        return field

    def __getitem__(self, item):
        return self.field.get(item)

    def __setitem__(self, key, value):
        self.field[key] = value

    def __iter__(self):
        yield from self.field.items()

    def __str__(self):
        return f'{self.field}'


class Simulation:
    """
    Главный класс приложения.
    Включает: карту, счетчик ходов, рендер поля, Actions- список действий
    """

    def next_turn(self):
        """Просимулировать и отрендерить один ход"""
        action = Actions()
        m = action.init_actions(10, 10)
        for i in range(10):
            for j in range(10):
                print(f'{m[i, j]:^10}', end=' ')
            print()

    def start_simulation(self):
        """Запуск бесконечного цикла симуляции и рендеринга"""
        pass

    def pause_simulation(self):
        """Приостановить бесконечный цикл симуляции и рендеринга"""
        pass


class Actions:
    """Действие совершаемое над миром. Например, сходить всеми существами"""

    def get_obj_list(self, rows, colms):
        """Составление вспомогательного списка для вставки в поле"""
        len_list = rows * colms
        obj_list = []
        for _ in range(2):
            obj_list.append(Rock())
            obj_list.append(Tree())
            obj_list.append(Grass())
            obj_list.append(Herbivore())
            obj_list.append(Predator())
        obj_list.extend([0 for _ in range(len_list - len(obj_list))])
        shuffle(obj_list)
        return obj_list

    def init_actions(self, rows, colms):
        """Действия, совершаемые перед началом симуляции. Например, расставить объекты и существ на карте"""
        map = Map(rows - 1, colms - 1)
        list_obj = self.get_obj_list(rows, colms)

        for key, value in zip(map, list_obj):
            map[key[0]] = value
        return map

    def turn_actions(self):
        """
        Действия, совершаемые за ход. Примеры - передвижение существ, добавить травы или травоядных,
        если их осталось слишком мало
        """
        pass


simulation = Simulation()
print(simulation.next_turn())
