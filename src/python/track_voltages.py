import numpy as np


def initTrackNeurons(T, dt):
    num_neurons_tracked = int(input("How many neurons want to be tracked?"))
    tracked_voltages = np.zeros([num_neurons_tracked, int(T/dt)])
    return tracked_voltages, num_neurons_tracked

def trackVoltages(tracked_voltages, voltages, num_neurons_tracked, t):
    for i in range(num_neurons_tracked):
        tracked_voltages[i-1, int(t)] = voltages[i-1, 0]
    return tracked_voltages
