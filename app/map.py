import itertools

from entity import Entity


class Map:
    __map: dict[tuple, Entity] = None

    def __init__(self, height: int, weight: int):
        self.weight = weight
        self.height = height
        self.__map = {(x, y): Entity for x, y in itertools.product(range(weight), range(height))}

    @property
    def map(self):
        return self.__map


new_map = Map(5, 5)
print(new_map.map)
