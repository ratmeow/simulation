import os

from .map import Map


class Renderer:
    @staticmethod
    def render(map_: Map):
        os.system("cls")
        i = 0
        for cell in map_.schema:
            print(map_.schema[cell].get(), end=" ")
            i += 1
            if i == map_.width:
                print()
                i = 0
