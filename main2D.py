from listsofchains2D import Active_Chains
from plotter2D import plotter
#import plotly.plotly as py
#from plotly.graph_objs import *

print "hello world"

#constants
kb=1
T=1
sigma=0.8
epsilon=0.25
numberofchains=20
numberofparticles=99 #add this many in chain if possible
max_num_part=100 #allocating space per chain
num_options=6

ChainList=Active_Chains(numberofchains,numberofparticles,max_num_part,num_options)
ChainList.run()
ChainList.show()
for i in xrange(0,len(ChainList.List)):
  plotter(ChainList.List[i].positions[0:ChainList.List[i].N-1],i)
print 'klaar!'