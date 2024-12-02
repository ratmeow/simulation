from app.map import Map
import os


class Renderer:
    @staticmethod
    def render(map_: Map):
        os.system('cls')
        i = 0
        for cell in map_.schema:
            print(map_.schema[cell].get(), end=" ")
            i += 1
            if i == map_.weight:
                print()
                i = 0
