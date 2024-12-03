from app.entities import Rock, Tree
from app.map import Map
from app.utils import bfs_retrieve

from .creature import Creature
from .herbivore import Herbivore


class Predator(Creature):
    def __init__(
        self, speed: int, hp: int, position: tuple[int, int], attack_power: int
    ):
        super().__init__(speed, hp, position)
        self.attack_power = attack_power
        self.obstacles = (Tree, Rock, Predator)
        self.meal = Herbivore
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
        return bfs_retrieve(
            graph=map_,
            start=self.position,
            desired_object=self.meal,
            obstacle=self.obstacles,
        )

    def should_eat(self, map_: Map, new_position: tuple[int, int]) -> bool:
        if isinstance(map_.get_cell(position=new_position), self.meal):
            self.attack_mode = True
            return True

    def move(self, map_, new_position):
        if not self.attack_mode:
            super().move(map_=map_, new_position=new_position)

    def __str__(self):
        return "🍖" if self.eating_flag else "🐅"
