
import threading
import keyboard
import time

from app.map import Map
from app.renderer import Renderer
from app.action import GenerateTree, GenerateRocks, Action, GenerateGrass, GenerateHerbivore, GeneratePredator, Move
from app.entity import Tree


class Simulation:
    init_actions: list[Action] = [GenerateRocks(), GenerateTree(), GenerateGrass(), GenerateHerbivore(1),
                                  GeneratePredator(0)]
    turn_actions: list[Action] = [Move()]

    def __init__(self, map_h: int = 5, map_w: int = 5):
        self.map: Map = Map(height=map_h, weight=map_w)
        self.counter: int = 0
        self.renderer: Renderer = Renderer()

        self.pause_flag = threading.Event()
        self.stop_flag = threading.Event()

        print("Map Initialize...")
        self.init_map()

    def init_map(self):
        for action in self.init_actions:
            action.execute(self.map)
        self.renderer.render(self.map)

    def next_turn(self):
        for action in self.turn_actions:
            action.execute(self.map)
            self.counter += 1
            self.renderer.render(self.map)
            print(f"Turn: {self.counter}")

    def start_simulation(self):
        print("Start simulation...")
        for i in range(30):
            self.next_turn()
            time.sleep(2)
        print("Simulation was stopped")

    def start_simulation_eternal(self):
        print("Start simulation...")
        while True:
            self.next_turn()
            time.sleep(0.5)
            if keyboard.is_pressed('1'):
                print("Pause. Press 1 to continue...")
                keyboard.wait('2')
                print("Simulation is running...")
                continue
            if keyboard.is_pressed('0'):
                print("Stopping simulation ...")
                break

        print("Simulation was stopped")


