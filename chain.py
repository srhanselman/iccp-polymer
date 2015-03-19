import numpy as np
import f90pot

class chain:
  def __init__(self):
    self.N=1
    self.positions=np.zeros((self.N,3),dtype=float)
    self.prob=1
    self.d=1 #distance between two connected particles
    print 'chain created'

  def add_particle(self,num_options):
    options=self.optional_pos(num_options)
    rand=np.random.uniform(0,1,1)
    pot=np.zeros((num_options,1),dtype=float)
    pot=self.calc_pot(pot,options,num_options)
    W=np.sum(np.exp(-pot))
    
    self.N+=1
   
  def optional_pos(self,num_options):   
    options=np.zeros((num_options,3),dtype=float)
    angles1=np.random.uniform(0,2*np.pi,size=num_options)
    angles2=np.random.uniform(0,np.pi,size=num_options)
    for i in xrange(0,num_options): 
      options[i]=self.positions[self.N-1]+[np.cos(angles1[i])*np.sin(angles2[i])*self.d,np.sin(angles1[i])*self.d*np.sin(angles2[i]),np.cos(angles2[i])]
    return options
  
  def calc_pot(self,pot,options,num_options):
    #print f90pot.calc_pot.__doc__
    pot=f90pot.calc_pot(self.positions,options,pot,[self.N,num_options])
    return pot