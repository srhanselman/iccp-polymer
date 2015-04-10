from listsofchains2D import Active_Chains
from plotter2D import plotter,plotData

print "hello world"

#constants
kb=1
T=1
sigma=0.8
epsilon=0.25
numberofchains=10000
numberofparticles=250
num_options=6

ChainList=Active_Chains(numberofchains,numberofparticles,num_options)
ChainList.run()
#ChainList.show()
print "Number of chains:",len(ChainList.List)
#for i in xrange(0,len(ChainList.List)):
 # plotter(ChainList.List[i].positions[0:ChainList.List[i].N],i)

plotData(ChainList.end2endData,'Number of beads','end to end radii squared','end2end','end2end',True)
print 'klaar!'