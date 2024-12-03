from app.simulation import Simulation

if __name__ == "__main__":
    simulation = Simulation(map_h=10, map_w=10, herbivore_count=5, predator_count=1)
    simulation.start()
