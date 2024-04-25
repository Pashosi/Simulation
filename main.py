from abc import ABC, abstractmethod
import numpy as np
from random import randint

class Entity(ABC):
    """Корневой абстрактный класс"""

    @abstractmethod
    def __init__(self):
        pass


class Rock:
    """Камень. Статичный объект"""
    pass


class Tree:
    """Дерево. Статичный объект"""
    pass


class Grass:
    """Трава. Ресурс для травоядных"""
    pass


class Creature(Entity):
    """Существо"""

    def __init__(self):
        self.step = 1
        self.hit_points = 10

    @abstractmethod
    def make_move(self):
        """Сделать ход"""
        pass


class Herbivore(Creature):
    """Травоядное"""

    def make_move(self):
        pass


class Predator(Creature):
    """Хищник"""

    def __init__(self):
        super().__init__()
        self.power_attack = 10

    def make_move(self):
        pass


class Map:
    """Поле"""

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.field = np.zeros((self.rows, self.cols), dtype=int)

    def __getitem__(self, item):
        return self.field[item]

    def __str__(self):
        return f'{self.field}'


class Simulation:
    """
    Главный класс приложения.
    Включает: карту, счетчик ходов, рендер поля, Actions- список действий
    """

    def next_turn(self):
        """Просимулировать и отрендерить один ход"""
        pass

    def start_simulation(self):
        """Запуск бесконечного цикла симуляции и рендеринга"""
        pass

    def pause_simulation(self):
        """Приостановить бесконечный цикл симуляции и рендеринга"""
        pass


class Actions:
    """Действие совершаемое над миром. Например, сходить всеми существами"""

    def init_actions(self, rows, colms):
        """Действия, совершаемые перед началом симуляции. Например, расставить объекты и существ на карте"""
        map = Map(rows, colms)
        for _ in range(3):
            x, y = randint(rows-1, colms-1), randint(rows-1, colms-1)
            while not map[x][y]:
                map[x][y] = Tree()
        return map

    def turn_actions(self):
        """
        Действия, совершаемые за ход. Примеры - передвижение существ, добавить травы или травоядных,
        если их осталось слишком мало
        """
        pass


# m = Map(3, 3)
#
# print(m)

# action = Actions()
# print(action.init_actions(5, 5))

m = np.zeros((3, 4), dtype=int)
print(m)
print(np.insert(m, 1, 1, axis=-2))
