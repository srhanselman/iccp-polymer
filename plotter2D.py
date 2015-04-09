import matplotlib as mpl
#from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


def plotter(coords,i):    
    #print 'coords',coords
    x=coords[:,0]
    y=coords[:,1]
    #z=coords[:,2]
    mpl.rcParams['legend.fontsize'] = 10    
    fig = plt.figure(1)
    ax = fig.gca()
    ax.plot(x,y, marker='.',label='polymer chain %d' %i)
    ax.legend()    
    plt.show()
    
def plotData(data,xlabel,ylabel,title):
  plt.figure()
  plt.xscale('log')
  plt.yscale('log')
  xData=data[:,0]
  yData=data[:,1]
  yError=data[:,2]
  popsize=data[:,3]
  plt.errorbar(xData,yData,linestyle='-',yerr=yError,marker='',label='end2end')
  plt.plot(xData,popsize,marker='o',label='polulation size')
  #plt.plot(xData,yData,)
  plt.xlabel(xlabel)
  plt.ylabel(ylabel)
  plt.title(title)
  plt.legend()