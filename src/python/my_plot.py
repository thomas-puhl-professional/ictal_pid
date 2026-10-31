import matplotlib.pyplot as plt
import numpy as np

def plotRaster(spikes, dt, experiment_name):
    neuron_id , spike_time = np.where(spikes == 1)
    spike_time = spike_time*dt
    plt.scatter(spike_time, neuron_id, s=1)
    plt.xlabel('Time (s)')
    plt.ylabel('Neuron ID')
    plt.title(experiment_name)
    plt.show()
    return

