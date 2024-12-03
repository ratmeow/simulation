from abc import ABC, abstractmethod

from app.map import Map


class Action(ABC):
    @abstractmethod
    def execute(self, map_: Map):
        pass
