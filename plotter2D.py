import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy.optimize as optimization

def plotter(coords,i):    
    x=coords[:,0]
    y=coords[:,1]
    mpl.rcParams['legend.fontsize'] = 10    
    fig = plt.figure(1)
    ax = fig.gca()
    ax.plot(x,y, marker='.',label='polymer chain %d' %i)
    ax.legend()    
    plt.show()
    
def plotData(data,xlabel,ylabel,title,label,end2end):
  plt.figure()
  #plt.xscale('log')
  plt.yscale('log',nonposy='clip')
  plt.ylim(1E1,1E5)
  xData=data[:,0]
  yData=data[:,1]
  yError=data[:,2]
  popsize=data[:,3]
  plt.errorbar(xData,yData,linestyle='-',yerr=yError,marker='',label=label)
  plt.plot(xData,popsize,marker='o',label='polulation size')
  if end2end==True:
    a=fit(data)
    plt.plot(xData,func(xData,a),label='fit')  
  plt.xlabel(xlabel)
  plt.ylabel(ylabel)
  plt.title(title)
  plt.legend()

def fit(data):
  N=data[:,0]
  y=data[:,1]
  sigma=data[:,2]
  x0=0.0
  fit,var=optimization.curve_fit(func, N, y, x0, sigma)
  return fit
  
def func(N,a):
  return a*((N-1)**0.75)
  

