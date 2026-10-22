import numpy as np
import random as rnd
import sympy as sy
from brian2 import mV, ms, pF

# V = sy.symbols('V', real=True)
# I = sy.symbols('I', real=True) # maybe for later

def configure_network(numNeurons):
    weights = (np.ones((numNeurons, numNeurons))-np.eye(numNeurons)) * rnd.random()
    return weights

    

