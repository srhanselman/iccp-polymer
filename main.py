from listsofchains import Active_Chains
#import plotly.plotly as py
#from plotly.graph_objs import *

print "hello world"

#constants
kb=1
T=1
sigma=0.8
epsilon=0.25
numberofchains=20
numberofparticles=99
max_num_part=100
num_options=5

ChainList=Active_Chains()
ChainList.run(numberofchains,numberofparticles,max_num_part,num_options)
ChainList.show()

print 'klaar!'