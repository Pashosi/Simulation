import copy
from abc import ABC, abstractmethod
from random import randint


class Entity(ABC):
    """Корневой абстрактный класс"""

    @abstractmethod
    def __init__(self, row, colm):
        self.name = 'Корневой класс'
        self.coordinate = (row, colm)

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

    def __init__(self, row, colm):
        super().__init__(row, colm)
        self.name = 'Камень'

    def __repr__(self):
        return self.name


class Tree(Entity):
    """Дерево. Статичный объект"""

    def __init__(self, row, colm):
        super().__init__(row, colm)
        self.name = 'Дерево'

    def __repr__(self):
        return 'Дерево'


class Grass(Entity):
    """Трава. Ресурс для травоядных"""

    def __init__(self, row, colm):
        super().__init__(row, colm)
        self.name = 'Трава'

    def __repr__(self):
        return self.name


class Creature(Entity):
    """Существо"""

    def __init__(self, row, colm):
        super().__init__(row, colm)
        self.step = 1
        self.hit_points = 10
        self.name = 'Существо'

    @abstractmethod
    def make_move(self):
        """Сделать ход"""
        pass


class Herbivore(Creature):
    """Травоядное"""

    def __init__(self, row, colm):
        super().__init__(row, colm)
        self.name = 'Травоядное'

    def make_move(self):
        pass

    def __repr__(self):
        return 'Травоядное'


class Predator(Creature):
    """Хищник"""

    def __init__(self, row, colm):
        super().__init__(row, colm)
        self.power_attack = 10
        self.name = 'Хищник'

    def make_move(self):
        pass

    def __repr__(self):
        return 'Хищник'


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
                key = (key[0], key[1] + 1)
                self.add_obj(Predator(key[0], key[1]), key[0], key[1])

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


class Simulation:
    """
    Главный класс приложения.
    Включает: карту, счетчик ходов, рендер поля, Actions- список действий
    """

    def __init__(self, rows, colms):
        self.progress_counter = 0
        self.map = Actions(rows, colms).get_map()

    def next_turn(self):
        """Просимулировать и отрендерить один ход"""
        self.map.changing_obj_field()

    def start_simulation(self):
        """Запуск бесконечного цикла симуляции и рендеринга"""
        pass

    def render_map(self):
        """Отрендерить карту"""
        for i in range(5):
            for j in range(5):
                print(f'{self.map[i, j]:^10}', end=' ')
            print()

    def pause_simulation(self):
        """Приостановить бесконечный цикл симуляции и рендеринга"""
        pass


class Actions:
    """Действие совершаемое над миром. Например, сходить всеми существами"""

    def __init__(self, rows, colms):
        self.map = Map(rows, colms)
        self.init_actions(self.map)

    def init_actions(self, obj_map):
        """Действия, совершаемые перед началом симуляции. Например, расставить объекты и существ на карте"""
        list_actions = [
            Herbivore,
            Predator,
            Rock,
            Grass,
            Tree,
        ]
        for action in list_actions:
            coord_row, coord_colm = obj_map.get_empty_coordin()
            obj_map.add_obj(action(coord_row, coord_row), coord_colm, coord_row)

    def get_map(self):
        return self.map

    def turn_actions(self):
        """
        Действия, совершаемые за ход. Примеры - передвижение существ, добавить травы или травоядных,
        если их осталось слишком мало
        """
        pass


simulation = Simulation(4, 4)
simulation.render_map()
simulation.next_turn()
print()
simulation.render_map()
print()
simulation.next_turn()
simulation.render_map()
# m = {(0, 0): '_', (0, 1): '_', (0, 2): '_', (0, 3): '_', (0, 4): '_', (1, 0): '_', (1, 1): '_', (1, 2): '_',
#      (1, 3): '_', (1, 4): '_', (2, 0): '_', (2, 1): '_', (2, 2): 'Хищник', (2, 3): '_', (2, 4): '_', (3, 0): '_',
#      (3, 1): '_', (3, 2): '_', (3, 3): '_', (3, 4): '_', (4, 0): '_', (4, 1): '_', (4, 2): '_', (4, 3): '_',
#      (4, 4): '_'}

