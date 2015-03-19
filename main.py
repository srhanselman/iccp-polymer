from chain import chain
from listsofchains import Active_Chains
print "hello world"

#constants
kb=1
T=1
sigma=0.8
epsilon=0.25

chain1=chain()
chain1.add_particle(5)

Active=Active_Chains()
Active.add_chain(chain1)
print 'klaar!'