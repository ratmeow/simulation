from app.entity import Entity
from app.map import Map
from app.utils import bfs_retrieve, a_star_retrieve
from abc import ABC, abstractmethod


class Terra(Entity):
    def __str__(self):
        return "_".ljust(3)


class Grass(Entity):
    def __str__(self):
        return "🌿".ljust(3)


class Rock(Entity):
    def __str__(self):
        return "🗿".ljust(3)


class Tree(Entity):
    def __str__(self):
        return "🌳".ljust(2)


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


class Predator(Creature):

    def __init__(self, speed: int, hp: int, position: tuple[int, int], attack_power: int):
        super().__init__(speed, hp, position)
        self.attack_power = attack_power
        self.obstacles = (Tree, Rock, Predator)
        self.meal = Herbivore
        self.attacking: bool = False
        self.attack_mode: bool = False

    def eat(self, map_: Map, meal_position: tuple[int, int]):
        if self.try_kill(map_=map_, meal_position=meal_position):
            self.eating_flag = True
            self.attack_mode = False
            map_.remove_creature(position=meal_position)

    def try_kill(self, map_: Map, meal_position: tuple[int, int]) -> bool:
        prey: Creature = map_.get_cell(position=meal_position)
        prey.hp -= self.attack_power
        if prey.hp <= 0:
            return True
        return False

    def find_path(self, map_: Map):
        return bfs_retrieve(graph=map_, start=self.position, desired_object=self.meal, obstacle=self.obstacles)

    def should_eat(self, map_: Map, new_position: tuple[int, int]) -> bool:
        if isinstance(map_.get_cell(position=new_position), self.meal):
            self.attack_mode = True
            return True

    def move(self, map_, new_position):
        if not self.attack_mode:
            super().move(map_=map_, new_position=new_position)

    def __str__(self):
        return "🍖".ljust(2) if self.eating_flag else "🐅".ljust(2)


class Herbivore(Creature):
    def __init__(self, speed: int, hp: int, position: tuple[int, int]):
        super().__init__(speed, hp, position)
        self.obstacles = (Tree, Rock, Herbivore, Predator)
        self.meal = Grass

    def eat(self, map_: Map, meal_position: tuple[int, int]):
        self.eating_flag = True
        map_.remove_entity(position=meal_position)

    def find_path(self, map_: Map):
        return a_star_retrieve(graph=map_, start=self.position, desired_object=self.meal, obstacle=self.obstacles)

    def should_eat(self, map_: Map, new_position: tuple[int, int]) -> bool:
        return isinstance(map_.get_cell(position=new_position), self.meal)

    def __str__(self):
        return "💤".ljust(2) if self.eating_flag else "🐇".ljust(2)
