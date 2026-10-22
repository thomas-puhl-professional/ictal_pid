import numpy as np
from brian2 import mV, pF, mohm, mamp
import random as rng


def get_neurons():
    numNeurons = int(input("Input an integer number of neurons for the network"))
    voltages = np.ones((1, numNeurons)) * (-65 * rng.random()) * mV
    capacitances = np.ones((1, numNeurons)) * 100 * pF * rng.random() *pF
    r_excit = np.ones((1, numNeurons))  * rng.random() * mohm
    r_inhib = np.ones((1, numNeurons))  * rng.random() * mohm
    return numNeurons, voltages, capacitances, r_excit, r_inhib

def get_currents(numNeurons):
    currents = np.ones((1, numNeurons)) * (rng.random()) * mamp
    return currents