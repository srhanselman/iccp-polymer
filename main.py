from chain import chain
from listsofchains import Active_Chains
print "hello world"

#constants
kb=1
T=1
sigma=0.8
epsilon=0.25

ChainList=Active_Chains()
ChainList.run(20,20)
ChainList.show()
print 'klaar!'