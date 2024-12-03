from app.map import Map

from .action import Action


class Move(Action):
    def execute(self, map_: Map):
        alive_creatures = map_.get_alive_creatures()
        for creature in alive_creatures:
            creature.make_move(map_=map_)
