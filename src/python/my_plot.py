import matplotlib.pyplot as plt

def plotRaster(spikes):
    plt.eventplot(spikes, orientation='horizontal', colors='b')
    return

