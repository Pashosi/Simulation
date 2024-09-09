import time

from creatures import Herbivore, Predator, Rock, Grass, Tree
from map_simulation import Map


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
        self.map.chang_obj_field('Травоядное')
        self.map.chang_obj_field('Хищник')
        self.progress_counter += 1

    def get_progress_counter(self):
        return self.progress_counter

    def start_simulation(self):
        """Запуск бесконечного цикла симуляции и рендеринга"""
        while True:
            self.render_map()
            self.next_turn()
            time.sleep(3)

    def render_map(self):
        """Отрендерить карту"""
        for i in range(self.map.rows + 1):
            for j in range(self.map.cols + 1):
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
            coord_row, coord_colm = obj_map.get_empty_coordinate()
            obj_map.add_obj(action(coord_row, coord_colm), coord_row, coord_colm)

    def get_map(self):
        """Возвращение экземляра поля"""
        return self.map

    def turn_actions(self):
        """
        Действия, совершаемые за ход. Примеры - передвижение существ, добавить травы или травоядных,
        если их осталось слишком мало
        """
        pass


if __name__ == '__main__':
    simulation = Simulation(10, 10)
    simulation.start_simulation()
    # simulation.render_map()
    # simulation.next_turn()
    # print(simulation.get_progress_counter())
    # print()
    # simulation.render_map()
    # simulation.next_turn()
    # print()
    # simulation.render_map()
    # simulation.next_turn()
    # print()
    # simulation.render_map()
    # simulation.next_turn()
    # print()
    # simulation.render_map()
    # print(simulation.get_progress_counter())
