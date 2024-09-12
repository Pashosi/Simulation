import copy
from abc import ABC, abstractmethod
from collections import deque


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
        self.hit_points = 20

    def accepting_attack(self, attack: int):
        """Получение урона"""
        self.hit_points -= attack

    def __repr__(self):
        return self.name


class Creature(Entity):
    """Существо"""

    def __init__(self, row, colm):
        super().__init__(row, colm)
        self.step = 1
        self.hit_points = 20
        self.name = 'Существо'

    def accepting_attack(self, attack: int):
        """Получение урона"""
        self.hit_points -= attack

    @abstractmethod
    def make_move(self):
        """Сделать ход"""
        step = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        pass


class Herbivore(Creature):
    """Травоядное"""

    def __init__(self, row, colm):
        super().__init__(row, colm)
        self.name = 'Травоядное'
        self.power_attack = 5
        self.hit_points = 20

    def make_move(self, map):
        """Алгоритм поиска цели"""
        target_stop = 'Трава'
        rows, cols = map.rows, map.cols
        # Возможные направления движения (вверх, вниз, влево, вправо)
        step = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        # Очередь для BFS, в ней хранятся кортежи: текущая позиция и путь до неё
        queue = deque([(self.coordinate, [self.coordinate])])
        # Множество для хранения посещённых клеток
        visited = set()
        visited.add(self.coordinate)

        map = map.get_map()
        while queue:
            (x, y), path = queue.popleft()
            # Если достигли целевой точки, возвращаем путь
            if str(map[(x, y)]) == target_stop:
                # print(path[1])
                return path
            # Проходим по всем возможным направлениям
            for dx, dy in step:
                nx, ny = x + dx, y + dy
                # Проверяем, находится ли новая позиция в пределах массива и проходима ли она
                if 0 <= nx <= rows and 0 <= ny <= cols and (map[(nx, ny)] == 0 or str(map[(nx, ny)]) == target_stop):
                    new_position = (nx, ny)
                    if new_position not in visited:
                        visited.add(new_position)
                        queue.append((new_position, path + [new_position]))

    def step_in_map(self, map):
        """Сделать ход"""
        path = self.make_move(map)
        if map.is_free(path[1][0], path[1][1]):
            new_obj = Herbivore(path[1][0], path[1][1])
            new_obj.hit_points = self.hit_points
            map.add_obj(new_obj, path[1][0], path[1][1])
        else:
            if repr(map.get_obj(path[1][0], path[1][1])) == 'Трава':
                new_obj = Herbivore(path[0][0], path[0][1])
                new_obj.hit_points = self.hit_points
                map.add_obj(new_obj, path[0][0], path[0][1])
                stop_obj = map.get_obj(path[1][0], path[1][1])
                stop_obj.accepting_attack(self.power_attack)
                print('рализация атаки, травы осталось', stop_obj.hit_points)

    def __repr__(self):
        return 'Травоядное'


class Predator(Creature):
    """Хищник"""

    def __init__(self, row, colm):
        super().__init__(row, colm)
        self.power_attack = 5
        self.hit_points = 20
        self.name = 'Хищник'

    def attack(self, obj):
        obj.accepting_attack(self.power_attack)

    def make_move(self, map):
        target_stop = 'Травоядное'
        rows, cols = map.rows, map.cols
        # Возможные направления движения (вверх, вниз, влево, вправо)
        step = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        # Очередь для BFS, в ней хранятся кортежи: текущая позиция и путь до неё
        queue = deque([(self.coordinate, [self.coordinate])])
        # Множество для хранения посещённых клеток
        visited = set()
        visited.add(self.coordinate)

        map = map.get_map()
        while queue:
            (x, y), path = queue.popleft()
            # Если достигли целевой точки, возвращаем путь
            if str(map[(x, y)]) == target_stop:
                return path
            # Проходим по всем возможным направлениям
            for dx, dy in step:
                nx, ny = x + dx, y + dy
                # Проверяем, находится ли новая позиция в пределах массива и проходима ли она
                if 0 <= nx <= rows and 0 <= ny <= cols and (map[(nx, ny)] == 0 or str(map[(nx, ny)]) == target_stop):
                    new_position = (nx, ny)
                    if new_position not in visited:
                        visited.add(new_position)
                        queue.append((new_position, path + [new_position]))

    def step_in_map(self, map):
        """Сделать ход"""
        path = self.make_move(map)
        if map.is_free(path[1][0], path[1][1]):
            map.add_obj(Predator(path[1][0], path[1][1]), path[1][0], path[1][1])
        else:
            stop_obj = map.get_obj(path[1][0], path[1][1])
            if repr(stop_obj) == 'Травоядное':
                print('рализация атаки, травоядный', stop_obj.hit_points)
                stop_obj.accepting_attack(self.power_attack)
            map.add_obj(Predator(path[0][0], path[0][1]), path[0][0], path[0][1])

    def __repr__(self):
        return 'Хищник'
