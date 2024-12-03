from abc import ABC


class Entity(ABC):
    pass


class Terra(Entity):
    def __str__(self):
        return "🏾"


class Grass(Entity):
    def __str__(self):
        return "🌿"


class Rock(Entity):
    def __str__(self):
        return "🗿"


class Tree(Entity):
    def __str__(self):
        return "🌳"
