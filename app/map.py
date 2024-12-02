import itertools
from typing import Optional
from app.entity import Entity


class Cell:

    def __init__(self):
        self.storage = []

    def append(self, item):
        self.storage.append(item)

    def pop(self):
        return self.storage.pop()

    def get(self):
        return self.storage[-1]

    def is_available(self):
        if len(self.storage) < 2:
            return True
        return False


class Map:
    __schema: dict[tuple, object] = None
    creature_storage = []

    def __init__(self, height: int, weight: int):
        self.weight = weight
        self.height = height
        self.__schema: dict[tuple, Cell] = {(x, y): Cell() for x, y in itertools.product(range(height), range(weight))}

    @property
    def schema(self):
        return self.__schema

    def get_all_positions(self) -> list[tuple]:
        return list(itertools.product(range(self.height), range(self.weight)))

    def get_all_available_positions(self) -> list[tuple]:
        available_positions = []
        for position in self.__schema:
            if self.__schema[position].is_available():
                available_positions.append(position)

        return available_positions

    def add_entity(self, position: tuple, item: Entity):
        self.__schema[position].append(item)

    def remove_entity(self, position: tuple):
        return self.__schema[position].pop()

    def move_entity(self, old_position: tuple, new_position: tuple):
        entity = self.remove_entity(position=old_position)
        self.add_entity(position=new_position, item=entity)

    def add_creature(self, position: tuple, item: Entity):
        self.add_entity(position=position, item=item)
        self.creature_storage.append(item)

    def remove_creature(self, position: tuple):
        entity = self.remove_entity(position=position)
        self.creature_storage.remove(entity)

    def get_alive_creatures(self):
        return self.creature_storage

    def get_cell(self, position: tuple):
        return self.__schema[position].get()

    # def remove_entity(self, position: tuple, item: Entity):
    #     self.__schema[position].append(item)
