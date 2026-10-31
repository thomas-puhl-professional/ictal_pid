import numpy as np
from brian2 import mV, pF, Mohm, mamp
import random as rnd

rng = np.random.default_rng()

def get_neurons():
    numNeurons = int(input("Input an integer number of neurons for the network"))
    voltages = (np.ones((1, numNeurons), dtype=np.double)
                * (-65 * rng.random([1, numNeurons])) * mV)
    capacitances = (np.ones((1, numNeurons))
                    * (300 - (250*rng.random([1, numNeurons]))) *pF)
    r_excit = (np.ones((1, numNeurons))
               * (500 - (450 * rng.random([1, numNeurons]))) * Mohm)
    r_inhib = (np.ones((1, numNeurons))
               * (500 - (450 * rng.random([1, numNeurons]))) * Mohm)
    return numNeurons, voltages, capacitances, r_excit, r_inhib

def get_currents(numNeurons):
    currents =  (2.5)*(10^(-5))*(rng.random([1, numNeurons])) * mamp
    return currents