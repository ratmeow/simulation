import itertools
from typing import Optional
from entity import Entity


class Map:
    __schema: dict[tuple, Optional[Entity]] = None

    def __init__(self, height: int, weight: int):
        self.weight = weight
        self.height = height
        self.__schema = {(x, y): None for x, y in itertools.product(range(weight), range(height))}

    @property
    def schema(self):
        return self.__schema
