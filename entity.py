from abc import ABC, abstractmethod


class Entity(ABC):
    pass

class Grass(Entity):
    pass

class Rock(Entity):
    pass

class Tree(Entity):
    pass


class Creature(Entity):

    def __init__(self, speed: int, hp: int):
        self.speed = speed
        self.hp = hp

    @abstractmethod
    def make_move(self):
        pass

class Herbivore(Creature):
    def make_move(self):
        pass

class Predator(Creature):

    def __init__(self, attack_power: int, speed: int, hp: int):
        super().__init__(speed, hp)
        self.attack_power = attack_power
    def make_move(self):
        pass





class Action:
    pass


