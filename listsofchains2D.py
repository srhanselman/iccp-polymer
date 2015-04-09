import numpy as np
import copy
from chain2D import chain
class Active_Chains:
  def __init__(self,numberofchains,numberofparticles,num_options):
    self.List=list()
    self.num_chains=0
    self.numberofparticles=numberofparticles
    self.num_options=num_options
    self.init_list(numberofchains)
    self.weight3=self.calc_w3()
    
  def init_list(self,numberofchains):
    for i in xrange(0,numberofchains):
      self.add_chain(chain(self.numberofparticles))
      
  def show(self):
    print "List of Active Chains:"
    print "Number of chains:",self.num_chains
    j=0
    for i in self.List:
      print "Chain ",j," :"
      print "N:",i.N
      print "weight:",i.weight
      print "probability:",i.prob
      print "Boolean:",i.Bool
      j+=1
  
  def add_chain(self,chain):
    self.List.append(chain)
    self.num_chains+=1    
    
  def run(self):
    for j in xrange(0,self.numberofparticles-2):
      for i in xrange(len(self.List) - 1, -1, -1): #looping backwards
        if self.List[i].Bool==True:
          self.List[i].add_particle(self.num_options)
        else:
          del self.List[i]
      self.prune()

  def prune(self):
    Avweight=np.sum(chain.weight for chain in self.List)/len(self.List)
    UpLim=2.0*Avweight/self.weight3
    LowLim=1.2*Avweight/self.weight3
    for i in xrange(len(self.List) - 1, -1, -1): #looping backwards
      self.List[i].weight=self.List[i].weight/(0.75*len(self.List))
      if self.List[i].weight>UpLim:
        self.List[i].weight=self.List[i].weight*0.5
        self.add_chain(copy.deepcopy(self.List[i])) #python does weird referencings!
        print ":D"
      else:
        if self.List[i].weight<=LowLim:
          rand=np.random.uniform(0.0,1.0,size=1)
          if rand<0.5:
           del self.List[i]
           print "rejected :("
          else:
              self.List[i].weight=self.List[i].weight*2      
              
  def calc_w3(self):
    w3chain=chain(3)
    w3chain.add_particle(self.num_options)
    return w3chain.weight  
    
  def trash(self,chain):
    self.List.remove(chain)
    self.num_chains-=1
    
