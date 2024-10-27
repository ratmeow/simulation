from abc import ABC, abstractmethod
from app.map import Map
from collections import deque
from typing import Optional


class Entity(ABC):
    pass

class Obstacle(ABC):
    pass


class Grass(Entity):
    def __str__(self):
        return "🌿".ljust(3)


class Rock(Entity, Obstacle):
    def __str__(self):
        return "🗿".ljust(3)


class Tree(Entity, Obstacle):
    def __str__(self):
        return "🌳".ljust(2)


class Creature(Entity):

    def __init__(self, speed: int, hp: int):
        self.speed = speed
        self.hp = hp
        self.eating_flag = False

    @abstractmethod
    def make_move(self, field: Map, start: tuple[int, int]):
        pass


class Herbivore(Creature):

    def grass_retrieve(self, field: Map, start: tuple[int, int]) -> Optional[list]:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = deque([start])
        visited = set()
        visited.add(start)

        parent = {start: None}

        while queue:
            current = queue.popleft()
            x, y = current

            if isinstance(field.schema[current], Grass):
                path = []
                while current is not None:
                    path.append(current)
                    current = parent[current]
                path.reverse()
                return path

            for dx, dy in directions:
                neighbor = (x + dx, y + dy)
                if (0 <= neighbor[0] < field.height) and (0 <= neighbor[1] < field.weight) and (
                        neighbor not in visited) and not isinstance(field.schema[neighbor], Obstacle):
                    queue.append(neighbor)
                    visited.add(neighbor)
                    parent[neighbor] = current
        return None

    def make_move(self, field: Map, start: tuple[int, int]):
        if self.eating_flag:
            self.eating_flag = False
            return
        path_to_grass = self.grass_retrieve(field=field, start=start)
        if path_to_grass is not None:
            new_position = path_to_grass[self.speed]
            field.schema[new_position] = self
            field.schema[start] = None
            if len(path_to_grass) == self.speed:
                self.eating_flag = True

    def __str__(self):
        return "🐇".ljust(2)


class Predator(Creature):

    def __init__(self, attack_power: int, speed: int, hp: int):
        super().__init__(speed, hp)
        self.attack_power = attack_power

    def make_move(self):
        print("Predator move")

    def __str__(self):
        return "🐅".ljust(2)
