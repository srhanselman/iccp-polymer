import numpy as np
import f90pot

class chain:
  def __init__(self,finalamount):
    self.N=1
    self.positions=np.zeros((finalamount,3),dtype=float)
    self.prob=1
    self.d=1 #distance between two connected particles
    print 'chain created'
  
  def show(self):
    print 'Chain:'
    print 'N=',self.N
    print 'positions: ',self.positions[0:self.N]
    print 'probability ',self.prob

  def add_particle(self,num_options):
    options=self.optional_pos(num_options)
    pot=np.zeros((num_options,1),dtype=float)
    pot=self.calc_pot(pot,options,num_options)
    w=np.exp(-pot) #weights
    i,p=self.weighted_random_choice(num_options,w)
    #print 'options[i]', options[i]
    #print 'pos',self.positions
    self.positions[self.N]=options[i]
    self.prob=self.prob*p
    self.N+=1
    
  def add_number_of_particles(self,num_particles):
    for i in xrange(0,num_particles):
      self.add_particle(5)
   
  def optional_pos(self,num_options):   
    options=np.zeros((num_options,3),dtype=float)
    angles1=np.random.uniform(0,2*np.pi,size=num_options)
    angles2=np.random.uniform(0,np.pi,size=num_options)
    for i in xrange(0,num_options): 
      options[i]=self.positions[self.N-1]+[np.cos(angles1[i])*np.sin(angles2[i])*self.d,np.sin(angles1[i])*self.d*np.sin(angles2[i]),np.cos(angles2[i])]
    return options
  
  def calc_pot(self,pot,options,num_options):
    #print f90pot.calc_pot.__doc__
    pot=f90pot.calc_pot(self.positions,options,pot,self.N,[self.positions.shape[0],num_options])
    return pot
    
  def weighted_random_choice(self,num_options,w):
    max = sum(w)
    pick = np.random.uniform(0, max)
    current = 0
    for i in xrange(0,num_options):
        current += w[i]
        if current > pick:
            return i,w[i]/max