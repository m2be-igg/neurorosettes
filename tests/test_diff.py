"""Script to test sphere-neurite interactions"""
import time

import numpy as np
import vedo

from neurorosettes.neurons import Neuron
from neurorosettes.subcellular import Neurite
from neurorosettes.simulation import Container
from neurorosettes import utilities
from neurorosettes.physics import default_potentials_repulsion, CylinderInteractions, default_potentials_adhesion

text_align = "center"
text_font = "Courier"
text_pos = (0.65, 0.3)

# Define time variables
timestep = 0.1
total_time = 100.0


pb = utilities.get_simulation_timer(total_time, timestep)

txt = vedo.Text2D(f"Simulation", pos="top right", font=text_font)

# Initialize simulation objects
container = Container(timestep=0.1,
                      viscosity=7.96,
                      grid=[-200, 200, 20])

container.animator.plotter += txt

# Populate environment with cells
neuron = Neuron()
neuron.create_cell(coordinates=np.array([-5.0, 0.0, 0.0]))
neuron.set_outgrowth_axis(np.array([1.0, 0.0, 0.0]))
neuron.clocks.set_clocks(0.0000001, 0.0000001, 0.1)
container.register_neuron(neuron)


container.animator.plotter.show(resetcam=False, interactive=False)

# Run and plot simulation
for t in pb.range():
    if t % 1.0 == 0.0:
        container.advance_cycles()
        container.differentiate()
    container.update_cell_positions()
    container.update_drawings()
    pb.print()
