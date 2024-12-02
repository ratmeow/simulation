import random
from abc import abstractmethod, ABC
from app.map import Map
from app.specific_entities import Grass, Rock, Tree, Herbivore, Predator, Creature, Terra


class Action(ABC):

    @abstractmethod
    def execute(self, map_: Map):
        pass


class GenerateEntities(Action):
    def __init__(self, count: int = 1):
        self.count = count

    def execute(self, map_: Map):
        pass


class GenerateWorld(Action):
    def execute(self, map_: Map):
        all_positions = map_.get_all_positions()
        for pos in all_positions:
            map_.add_entity(position=pos, item=Terra())


class GenerateRocks(GenerateEntities):
    def execute(self, map_: Map):
        available_positions = random.sample(map_.get_all_available_positions(), self.count)
        for pos in available_positions:
            map_.add_entity(position=pos, item=Rock())


class GenerateTree(GenerateEntities):
    def execute(self, map_: Map):
        available_positions = random.sample(map_.get_all_available_positions(), self.count)
        for pos in available_positions:
            map_.add_entity(position=pos, item=Tree())


class GenerateGrass(GenerateEntities):
    def execute(self, map_: Map):
        available_positions = random.sample(map_.get_all_available_positions(), self.count)
        for pos in available_positions:
            map_.add_entity(position=pos, item=Grass())


class GenerateHerbivore(GenerateEntities):
    def execute(self, map_: Map):
        available_positions = random.sample(map_.get_all_available_positions(), self.count)
        for pos in available_positions:
            herbivore = Herbivore(speed=1, hp=3, position=pos)
            map_.add_creature(position=pos, item=herbivore)


class GeneratePredator(GenerateEntities):
    def execute(self, map_: Map):
        available_positions = random.sample(map_.get_all_available_positions(), self.count)
        for pos in available_positions:
            predator = Predator(speed=2, hp=3, position=pos, attack_power=1)
            map_.add_creature(position=pos, item=predator)


class Move(Action):

    def execute(self, map_: Map):
        alive_creatures = map_.get_alive_creatures()
        for creature in alive_creatures:
            creature.make_move(map_=map_)
