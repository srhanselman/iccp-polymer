import numpy as np
import f90pot2D

class chain:
  def __init__(self,finalamount):
    self.N=2
    self.positions=np.zeros((finalamount,2),dtype=float)
    self.positions[1]=[0,1]
    self.prob=1
    self.d=1 #distance between two connected particles
    self.weight=1 #total chain weight yay
    self.weight3=1
  
  def show(self):
    print 'Chain:'
    print 'N=',self.N
    print 'positions: ',self.positions[0:self.N]
    print 'probability ',self.prob

  def add_particle(self,num_options):
    options=self.optional_pos(num_options)
    pot=np.zeros(num_options)
    pot=self.calc_pot(pot,options,num_options)
    w=np.exp(-pot) #weights
    if all(w==0.0):
      i=0   #we cheat a bit to avoid problems with all weights being rounded to 0.0
      p=0.  
      W=0.  #weight of this chain is 0, so it will be pruned anyway
    else:
      i,p,W=self.weighted_random_choice(num_options,w)
    self.positions[self.N]=options[i]
    self.prob=self.prob*p
    self.weight=self.weight*W*(1/(0.55*num_options))
    self.N+=1
    if self.N==3:
      self.weight3=self.weight
    
  def add_number_of_particles(self,num_particles,num_options):
    for i in xrange(0,num_particles):
      self.add_particle(num_options)
   
  def optional_pos(self,num_options):   
    options=np.zeros((num_options,2),dtype=float)
    rand1=np.random.uniform(0,2*np.pi,size=1)
    angles1=rand1+2*np.pi/num_options*np.arange(0,num_options,dtype=float)
    for i in xrange(0,num_options): 
      options[i]=self.positions[self.N-1]+[np.cos(angles1[i])*self.d,np.sin(angles1[i])*self.d]
    return options
  
  def calc_pot(self,pot,options,num_options):
    #print f90pot.calc_pot.__doc__
    pot=f90pot2D.calc_pot(self.positions,options,pot,self.N,[self.positions.shape[0],num_options])
    return pot
    
  def weighted_random_choice(self,num_options,w):
    W = sum(w)
    if W==0.0:
      print 'W',W
      print  'w',w
    pick = np.random.uniform(0, W)
    current = 0
    for i in xrange(0,num_options):
      current += w[i]
      if current >= pick:
        return i,w[i]/W,W
    print 'pick',pick,'current',current       
     
  def Calc_end2end(self):
    end2end=np.sum(self.positions[self.N-1]**2)
    return end2end