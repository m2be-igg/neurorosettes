"""Script to simulate the formation of Homer-Wright rosettes."""

import numpy as np

from neurorosettes.simulation import Simulation, Container


def create_tissue(container: Container) -> None:
    """Creates and registers new neurons in the simulation world."""
    radius = 24.0
    number_of_cells = 9
    t = np.linspace(0, 2*np.pi, number_of_cells, endpoint=False)

    x = radius * np.cos(t)
    y = radius * np.sin(t)

    for x_coord, y_coord in zip(x, y):
        neuron = container.create_new_neuron(coordinates=[x_coord, y_coord, 0])
        neuron.set_outgrowth_axis(np.subtract(np.zeros(3), neuron.cell.position))

def main():
    # Initialize simulation objects
    sim_world = Simulation.from_file("config/config.yml")
    # Create initial configuration
    create_tissue(sim_world.container)
    # Plot the current state of the simulation
    sim_world.container.animator.set_camera(height=400.0)
    sim_world.container.animator.show()
    # Run the simulation to check if springs work
    sim_world.run()
    # Plot the results (mark interactive as False to automatically  close the window)
    sim_world.container.animator.show(interactive=True)


if __name__ == "__main__":
    main()
