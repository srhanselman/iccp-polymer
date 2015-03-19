import numpy as np

class chain:
  def __init__(self,N):
    self.N=N
    self.positions=np.zeros((self.N,3),dtype=float)
    self.prob=1
    print 'chain created'
    
  def add_particle(self):
    self.N+=1
    
      
      

