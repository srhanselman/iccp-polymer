import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


def plotter(coords,i):    
    print 'coords',coords
    x=coords[:,0]
    y=coords[:,1]
    z=coords[:,2]
    mpl.rcParams['legend.fontsize'] = 10    
    fig = plt.figure(1)
    ax = fig.gca(projection='3d')
    ax.plot(x,y,z, label='polymer chain %d' %i)
    ax.legend()    
    plt.show()