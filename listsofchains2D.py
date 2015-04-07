import numpy as np
from chain2D import chain
class Active_Chains:
  def __init__(self,numberofchains,numberofparticles,max_num_part,num_options):
    self.List=list()
    self.container=CONTAINER()
    self.num_chains=numberofchains
    self.num_part=numberofparticles
    self.max_num_part=max_num_part
    self.num_options=num_options
    self.init_list()
    
  def init_list(self):
    for i in xrange(0,self.num_chains):
      self.add_chain(chain(self.max_num_part))
      
  def show(self):
    print "List of Active Chains:"
    print "Number of chains:",len(self.List)
    for i in xrange(0,len(self.List)):
      print "Chain ",i," :"
      self.List[i].show()
    print "Trash :",len(self.container.trash)
  
  def add_chain(self,chain):
    self.List.append(chain)    
    
  def run(self):
    for i in xrange(0,len(self.List)):
      for j in xrange(0,self.num_part):
        self.List[i].add_particle(self.num_options)
        #self.selector()
#      if self.List[i].prob<10**-15:
#          self.container.add_trash(self.List[i])
#          self.List[i]=chain(max_particles)
#          self.List[i].add_number_of_particles(num_part,num_options) 
#      #print i
  def prune(self):
    for i in xrange(0,len(self.List)):
      if self.List[i].Bool==False:
        self.trash(self.List[i])
    Avprob=np.mean(chain.W for chain in self.List)
    UpLim=2*Avprob/prob3
    LowLim=1.2*Avprob/prob3
    
  def trash(self,chain):
    self.container.add_trash(chain)
    self.List.remove(chain)
class CONTAINER:
  def __init__(self):
    self.trash=list()
  def add_trash(self,chain):
      self.trash.append(chain)
      