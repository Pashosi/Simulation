from abc import ABC, abstractmethod


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
        step = [(-1, 0), (1, 0), (0, -1), (0, 1)]
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
