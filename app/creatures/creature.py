from abc import abstractmethod

from app.entities import Entity
from app.map import Map


class Creature(Entity):
    def __init__(self, speed: int, hp: int, position: tuple[int, int]):
        self.speed = speed
        self.hp = hp
        self.eating_flag = False
        self.position = position

    def make_move(self, map_: Map):
        """Сделать ход"""
        if self.eating_flag:
            self.eating_flag = False
            return

        path = self.find_path(map_)
        if path is not None:
            if self.speed >= len(path):
                new_position = path[-1]
            else:
                new_position = path[self.speed]
            if self.should_eat(map_, new_position):
                self.eat(map_=map_, meal_position=new_position)

            self.move(map_=map_, new_position=new_position)

    @abstractmethod
    def eat(self, map_: Map, meal_position: tuple[int, int]):
        """Съесть желаемый объект."""
        pass

    @abstractmethod
    def find_path(self, map_: Map):
        """Найти путь до желаемого объекта."""
        pass

    def move(self, map_, new_position):
        """Переместиться на новую позицию."""
        map_.move_entity(old_position=self.position, new_position=new_position)
        self.position = new_position

    def should_eat(self, map_: Map, new_position: tuple[int, int]) -> bool:
        """Проверка, нужно ли есть объект на новой позиции."""
        return False
