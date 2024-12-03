from abc import ABC


class Entity(ABC):
    pass


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
