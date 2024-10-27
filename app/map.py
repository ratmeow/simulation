import itertools
from typing import Optional


class Map:
    __schema: dict[tuple, object] = None

    def __init__(self, height: int, weight: int):
        self.weight = weight
        self.height = height
        self.__schema = {(x, y): None for x, y in itertools.product(range(height), range(weight))}

    @property
    def schema(self):
        return self.__schema
