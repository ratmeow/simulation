from abc import abstractmethod, ABC
from app.map import Map
from app.entity import Entity, Grass, Rock, Tree, Herbivore, Predator


class Action(ABC):

    @abstractmethod
    def execute(self, map_: Map):
        pass


class Generate(Action):

    def execute(self, map_: Map):
        pass


class GenerateRocks(Generate):

    def execute(self, map_: Map):
        for cell in map_.schema:
            if cell[0] == cell[1]:
                map_.schema[cell] = Rock()


class GenerateTree(Generate):
    def execute(self, map_: Map):
        for cell in map_.schema:
            if cell[0] == 0 or cell[0] == map_.height - 1:
                map_.schema[cell] = Tree()


new_map = Map(5, 5)
actions = [GenerateRocks(), GenerateTree()]
for a in actions:
    a.execute(map_=new_map)
print(new_map.schema)

# загяться отрисовкой
