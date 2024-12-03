import random

from app.creatures import Herbivore, Predator
from app.entities import Entity
from app.map import Map

from .action import Action


class GenerateCreature(Action):
    def __init__(self, count: int = 1):
        self.count = count

    def create_creature(self, position: tuple[int, int]) -> Entity:
        pass

    def execute(self, map_: Map):
        available_positions = random.sample(
            map_.get_all_available_positions(), self.count
        )
        for pos in available_positions:
            map_.add_creature(position=pos, item=self.create_creature(position=pos))


class GenerateHerbivore(GenerateCreature):
    def create_creature(self, position: tuple[int, int]) -> Entity:
        return Herbivore(speed=1, hp=3, position=position)


class GeneratePredator(GenerateCreature):
    def create_creature(self, position: tuple[int, int]) -> Entity:
        return Predator(speed=2, hp=10, position=position, attack_power=3)
