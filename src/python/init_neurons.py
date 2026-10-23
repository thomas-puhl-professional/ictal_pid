import numpy as np
from brian2 import mV, pF, Mohm, mamp
import random as rng


def get_neurons():
    numNeurons = int(input("Input an integer number of neurons for the network"))
    voltages = np.ones((1, numNeurons), dtype=np.float64) * (-65 * rng.random()) * mV
    capacitances = np.ones((1, numNeurons)) * (300 - (250*rng.random())) *pF
    r_excit = np.ones((1, numNeurons))  * (500 - (450 * rng.random())) * Mohm
    r_inhib = np.ones((1, numNeurons))  * (500 - (450 * rng.random())) * Mohm
    return numNeurons, voltages, capacitances, r_excit, r_inhib

def get_currents(numNeurons):
    currents = np.ones((1, numNeurons)) * (rng.random()) * mamp
    return currents