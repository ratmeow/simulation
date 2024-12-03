import random
from typing import Type

from app.entities import Entity, Grass, Rock, Terra, Tree
from app.map import Map

from .action import Action


class GenerateStaticObjects(Action):
    def __init__(
        self,
        entity: Type[Entity],
        ratio: float = 0.1,
        sparse: float = 0.2,
    ):
        self.ratio = ratio
        self.sparse = sparse
        self.entity = entity

    def execute(self, map_: Map):
        count = int(map_.height * map_.width * self.ratio)
        clusters = int(count * self.sparse)
        entities = []
        for _ in range(clusters):
            x = random.randint(0, map_.width - 1)
            y = random.randint(0, map_.height - 1)

            entities.append((x, y))

            for _ in range(10):
                if len(entities) >= count:
                    break

                nx, ny = x + random.choice([-1, 0, 1]), y + random.choice([-1, 0, 1])
                if (nx, ny) in map_.get_all_available_positions():
                    entities.append((nx, ny))
                    x, y = nx, ny

        for pos in entities:
            map_.add_entity(position=pos, item=self.entity())


class GenerateRocks(GenerateStaticObjects):
    def __init__(self, ratio, sparse):
        super().__init__(ratio=ratio, sparse=sparse, entity=Rock)


class GenerateTree(GenerateStaticObjects):
    def __init__(self, ratio, sparse):
        super().__init__(ratio=ratio, sparse=sparse, entity=Tree)


class GenerateGrass(GenerateStaticObjects):
    def __init__(self, ratio, sparse):
        super().__init__(ratio=ratio, sparse=sparse, entity=Grass)


class GenerateWorld(Action):
    def execute(self, map_: Map):
        all_positions = map_.get_all_positions()
        for pos in all_positions:
            map_.add_entity(position=pos, item=Terra())

        GenerateRocks(ratio=0.1, sparse=0.2).execute(map_)
        GenerateTree(ratio=0.15, sparse=0.33).execute(map_)
        GenerateGrass(ratio=0.1, sparse=0.33).execute(map_)
