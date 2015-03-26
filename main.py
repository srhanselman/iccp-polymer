from listsofchains import Active_Chains
#import plotly.plotly as py
#from plotly.graph_objs import *

print "hello world"

#constants
kb=1
T=1
sigma=0.8
epsilon=0.25

ChainList=Active_Chains()
ChainList.run(20,99,100)
ChainList.show()



print 'klaar!'