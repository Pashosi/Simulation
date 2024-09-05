from creatures import Herbivore, Predator, Rock, Grass, Tree
from map import Map


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
        """Возвращение экземляра поля"""
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
simulation.next_turn()
print()
simulation.render_map()
simulation.next_turn()
print()
simulation.render_map()
# print()
# simulation.next_turn()
# simulation.render_map()
# m = {(0, 0): '_', (0, 1): '_', (0, 2): '_', (0, 3): '_', (0, 4): '_', (1, 0): '_', (1, 1): '_', (1, 2): '_',
#      (1, 3): '_', (1, 4): '_', (2, 0): '_', (2, 1): '_', (2, 2): 'Хищник', (2, 3): '_', (2, 4): '_', (3, 0): '_',
#      (3, 1): '_', (3, 2): '_', (3, 3): '_', (3, 4): '_', (4, 0): '_', (4, 1): '_', (4, 2): '_', (4, 3): '_',
#      (4, 4): '_'}
