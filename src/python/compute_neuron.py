import brian2 as b2
from brian2 import mV, mohm, pF, mamp
import scipy as sp

def computeVoltages(numNeurons, voltages, spikes, leak,
                    r_excit, r_inhib, capacitances,
                    currents, start_stim_step, stop_stim_step,
                    t, dt):
    for i in range(0, numNeurons-1):
        if start_stim_step<t<stop_stim_step:
            dVdt = (currents + ((voltages - leak)/r_excit))/capacitances(1, i) # LIF
            dVdt = dVdt + ((25 * spikes[:, t]).T)
        else:
            dVdt = ((voltages - leak) / r_excit) / capacitances  # LIF
            dVdt = dVdt + ((25 * spikes[:, t]).T)
        voltages = voltages + ((dVdt)*dt)*mV
    return voltages

def getSpikes(voltages, spikes, numNeurons, t):
    for i in range(0, numNeurons-1):
        if voltages[1, i] > (-55*mV):
            voltages[1, i+1] = -70*mV
            spikes[i, t] = 1
    return voltages, spikes
