import random
from abc import abstractmethod, ABC
from app.map import Map
from app.entity import Entity, Grass, Rock, Tree, Herbivore, Predator, Creature
from random import randint as rnd


class Action(ABC):

    @abstractmethod
    def execute(self, map_: Map):
        pass


class Generate(Action):

    def execute(self, map_: Map):
        pass


class GenerateRocks(Generate):

    def execute(self, map_: Map):
        for cell in map_.schema:
            if cell[1] == 0 or cell[1] == map_.weight - 1:
                map_.schema[cell] = Rock()


class GenerateTree(Generate):
    def execute(self, map_: Map):
        for cell in map_.schema:
            if cell[0] == 0 or cell[0] == map_.height - 1:
                map_.schema[cell] = Tree()


class GenerateGrass(Generate):
    def __init__(self, count: int = 4):
        self.count = count

    def execute(self, map_: Map):
        positions = [(rnd(0, map_.height - 1), rnd(0, map_.weight - 1)) for i in range(self.count)]
        for pos in positions:
            map_.schema[pos] = Grass()


class GenerateHerbivore(Generate):
    def __init__(self, count: int = 4):
        self.count = count

    def execute(self, map_: Map):
        positions = [(rnd(0, map_.height - 1), rnd(0, map_.weight - 1)) for i in range(self.count)]
        for pos in positions:
            map_.schema[pos] = Herbivore(speed=1, hp=3)


class GeneratePredator(Generate):
    def __init__(self, count: int = 2):
        self.count = count

    def execute(self, map_: Map):
        positions = [(rnd(0, map_.height - 1), rnd(0, map_.weight - 1)) for i in range(self.count)]
        for pos in positions:
            map_.schema[pos] = Predator(speed=1, hp=3, attack_power=2)


class Move(Action):

    def execute(self, map_: Map):
        for cell in map_.schema:
            if isinstance(map_.schema[cell], Creature):
                map_.schema[cell].make_move(field=map_, start=cell)
