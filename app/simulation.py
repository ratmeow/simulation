import threading
import time

import keyboard

from app.actions import Action, GenerateHerbivore, GeneratePredator, GenerateWorld, Move
from app.map import Map
from app.map.renderer import Renderer


class Simulation:
    def __init__(
        self,
        map_h: int = 5,
        map_w: int = 5,
        max_turn: int = 30,
        world_speed: float = 2,
        herbivore_count: int = 1,
        predator_count: int = 1,
    ):
        self.map: Map = Map(height=map_h, width=map_w)
        self.max_turn = max_turn
        self.world_speed = world_speed
        self.renderer: Renderer = Renderer()

        self.counter: int = 0
        self.pause_flag = threading.Event()
        self.stop_flag = threading.Event()
        self.key_thread = threading.Thread(target=self._monitor_keys, daemon=True)
        self.key_thread.start()

        self.init_actions: list[Action] = [GenerateWorld()]
        if herbivore_count > 0:
            self.init_actions.append(GenerateHerbivore(herbivore_count))
        if predator_count > 0:
            self.init_actions.append(GeneratePredator(predator_count))

        self.turn_actions: list[Action] = [Move()]

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

    def start(self):
        print("Start simulation...")
        while not self.stop_flag.is_set() and self.counter < self.max_turn:
            if not self.pause_flag.is_set():
                self.next_turn()
                time.sleep(self.world_speed)

        print("Simulation has been stopped")

    def _monitor_keys(self):
        """Отслеживание нажатия клавиш в отдельном потоке."""
        while True:
            if keyboard.is_pressed("space"):
                print("Pause. Press 2 to continue...")
                self.pause_flag.set()
                keyboard.wait("space")
                self.pause_flag.clear()
                print("Simulation is running...")

            if keyboard.is_pressed("enter"):
                print("Stopping simulation ...")
                self.stop_flag.set()
                break
            time.sleep(0.1)
