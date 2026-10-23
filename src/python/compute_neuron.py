import brian2 as b2
from brian2 import mV, mohm, pF, mamp, ms
import scipy as sp

def computeVoltages(numNeurons, voltages, spikes, leak,
                    r_excit, r_inhib, capacitances,
                    currents, start_stim_step, stop_stim_step,
                    t, dt):
    if start_stim_step<t<stop_stim_step:
        dV = ((currents + ((voltages - leak)/r_excit))/capacitances)*dt # LIF with driving current
        #dV = (dV + ((25 * spikes[:, t]).T) *mV*ms^(-1)) # synaptic currents! big step!
    else:
        dV = (((leak - voltages) / (r_excit * capacitances)))*dt  # LIF w/o driving current
        # dV = (dV + (( * mV * spikes[:, t]).T))
        voltages = voltages + dV
    return voltages

def getSpikes(voltages, spikes, numNeurons, t):
    for i in range(0, numNeurons-1):
        if voltages[0, i] > (-55*mV):
            voltages[0, i] = -70*mV
            spikes[i, t] = 1
    return voltages, spikes
