import numpy as np
import f90pot2D

class chain:
  def __init__(self,finalamount):
    self.N=2
    self.positions=np.zeros((finalamount,2),dtype=float)
    self.positions[1]=[0,1]
    self.prob=1
    self.d=1 #distance between two connected particles
    self.Bool=True #Am I a not completely hopeless chain?
    self.weight=1 #total chain weight yay
  
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
    if all(w==0.0):
      self.stop_chain()
      return
    i,p,W=self.weighted_random_choice(num_options,w)
    self.positions[self.N]=options[i]
    self.prob=self.prob*p
    self.weight=self.weight*W
    self.N+=1
    
  def add_number_of_particles(self,num_particles,num_options):
    for i in xrange(0,num_particles):
      self.add_particle(num_options)
      if self.Bool==False:
          return
   
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
     
  def stop_chain(self):
      self.prob=0
      self.Bool=False
      self.weight=0
      #print 'I am a hopeless chain! :('
