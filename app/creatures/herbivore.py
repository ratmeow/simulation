from app.entities import Grass, Rock, Tree
from app.map import Map
from app.utils import a_star_retrieve

from .creature import Creature


class Herbivore(Creature):
    def __init__(self, speed: int, hp: int, position: tuple[int, int]):
        super().__init__(speed, hp, position)
        self.obstacles = (Tree, Rock, Creature)
        self.meal = Grass

    def eat(self, map_: Map, meal_position: tuple[int, int]):
        self.eating_flag = True
        map_.remove_entity(position=meal_position)

    def find_path(self, map_: Map):
        return a_star_retrieve(
            graph=map_,
            start=self.position,
            desired_object=self.meal,
            obstacle=self.obstacles,
        )

    def should_eat(self, map_: Map, new_position: tuple[int, int]) -> bool:
        return isinstance(map_.get_cell(position=new_position), self.meal)

    def __str__(self):
        return "💤".ljust(2) if self.eating_flag else "🐇".ljust(2)
