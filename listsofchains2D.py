import numpy as np
import copy
from chain2D import chain
class Active_Chains:
  def __init__(self,numberofchains,numberofparticles,max_num_part,num_options):
    self.List=list()
    self.container=CONTAINER()
    self.num_chains=0
    self.num_part_added=numberofparticles-2
    self.max_num_part=max_num_part
    self.num_options=num_options
    self.init_list(numberofchains)
    self.weight3=self.calc_w3()
    
  def init_list(self,numberofchains):
    for i in xrange(0,numberofchains):
      self.add_chain(chain(self.max_num_part))
      
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
    print "Trash :",len(self.container.trash)
  
  def add_chain(self,chain):
    self.List.append(chain)
    self.num_chains+=1    
    
  def run(self):
    for j in xrange(0,self.num_part_added):
      for i in self.List[:]:
        if i.Bool==True:
          i.add_particle(self.num_options)
      self.prune()

  def prune(self):
    Avprob=np.sum(chain.weight for chain in self.List)
    UpLim=2.0*Avprob/self.weight3
    LowLim=1.2*Avprob/self.weight3
    for i in self.List[:]:
      if i.weight>UpLim:
        i.weight=i.weight*0.5
        self.add_chain(copy.deepcopy(i)) #python does weird referencings!
        #print ":D"
      else:
        if i.weight<=LowLim:
          rand=np.random.uniform(0.0,1.0,size=1)
          if rand<0.5:
            self.trash(i)
            #print ":("
          else:
            i.weight=i.weight*2                     
    
  def calc_w3(self):
    w3chain=chain(3)
    w3chain.add_particle(self.num_options)
    return w3chain.weight  
    
  def trash(self,chain):
    self.container.add_trash(chain)
    self.List.remove(chain)
    self.num_chains-=1
    

class CONTAINER:
  def __init__(self):
    self.trash=list()
  def add_trash(self,chain):
      self.trash.append(chain)
      