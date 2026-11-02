import matplotlib.pyplot as plt
import numpy as np
from brian2 import second

def plotRaster(spikes, dt, experiment_name):
    neuron_id , spike_time = np.where(spikes == 1)
    spike_time = spike_time*dt
    plt.scatter(spike_time, neuron_id, s=1)
    plt.xlabel('Time (s)')
    plt.ylabel('Neuron ID')
    plt.title(experiment_name)
    plt.show()
    return

def plotV_of_t(tracked_voltages, experiment_name, T, steps, num_neurons_tracked):
    t = np.linspace(0, (T/second), steps)

    plt.figure()
    for i in range(num_neurons_tracked):
        plt.plot(t, tracked_voltages[i-1,:])
        plt.title(experiment_name)
        plt.xlabel('Time (s)')
        plt.ylabel(f'Voltage {i}')
        plt.show()
    return

