import random
from typing import Type
from abc import abstractmethod, ABC
from app.map import Map
from app.specific_entities import Grass, Rock, Tree, Herbivore, Predator, Creature, Terra
from app.entity import Entity


class Action(ABC):

    @abstractmethod
    def execute(self, map_: Map):
        pass


class GenerateStaticObjects(Action):
    def __init__(self, entity: Type[Entity], ratio: float = 0.1, sparse: float = 0.2, ):
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


class GenerateCreature(Action):
    def __init__(self, count: int = 1):
        self.count = count

    def create_creature(self, position: tuple[int, int]) -> Entity:
        pass

    def execute(self, map_: Map):
        available_positions = random.sample(map_.get_all_available_positions(), self.count)
        for pos in available_positions:
            map_.add_creature(position=pos, item=self.create_creature(position=pos))


class GenerateHerbivore(GenerateCreature):
    def create_creature(self, position: tuple[int, int]) -> Entity:
        return Herbivore(speed=1, hp=3, position=position)


class GeneratePredator(GenerateCreature):
    def create_creature(self, position: tuple[int, int]) -> Entity:
        return Predator(speed=2, hp=10, position=position, attack_power=3)


class Move(Action):

    def execute(self, map_: Map):
        alive_creatures = map_.get_alive_creatures()
        for creature in alive_creatures:
            creature.make_move(map_=map_)
