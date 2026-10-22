import brian2 as b2
import numpy as np
import scipy as sp
import numpy as np
from brian2 import mV, pF, mohm, second

import init_neurons
import init_network
import compute_neuron

t = 0
T = int(input("Simulated seconds")) * second
dt = float(input("Discrete timestep value (in seconds)")) * second
steps = int(T/dt)

start_stim_time = float(input("Start stimulus time"))
stop_stim_time = float(input("Stop stimulus time"))
start_stim_steps = int(start_stim_time/dt)
stop_stim_steps = int(stop_stim_time/dt)

leak = 10.6 * mV # leak currrent

(numNeurons, voltages, capacitances,
 r_excit, r_inhib) = init_neurons.get_neurons()
currents = init_neurons.get_currents(numNeurons)
weights = init_network.configure_network(numNeurons)

print(f"{voltages},\n {capacitances},\n {r_excit},\n {r_inhib},\n {capacitances}")
print(weights)

spikes = np.zeros((numNeurons, steps))
while t < steps:
    voltages = compute_neuron.computeVoltages(
        numNeurons, voltages, spikes, leak,
        r_excit, r_inhib, capacitances,
        currents, start_stim_steps, stop_stim_steps,
        t, dt)
    voltages, spikes = compute_neuron.getSpikes(voltages, spikes, numNeurons, t)

print(spikes)

# next step is to implement a while loop that updates the
# neuronal network while within the time constraint

