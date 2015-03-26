from chain import chain
class Active_Chains:
  def __init__(self):
    self.List=list()
    self.container=CONTAINER()
  
  def add_chain(self,chain):
    self.List.append(chain)
    
  def show(self):
    print "List of Active Chains:"
    print "Number of chains:",len(self.List)
    #for i in xrange(0,len(self.List)):
      #print "Chain ",i," :"
      #self.List[i].show()
    print "Trash :",len(self.container)
    
  def run(self,num_chains,num_part,max_particles):
    for j in xrange(0,num_chains):
      self.add_chain(chain(max_particles))
    for i in xrange(0,len(self.List)):
      self.List[i].add_number_of_particles(num_part)
      if self.List[i].prob==0:
          self.container.add_trash(self.List[i])
          self.List[i]=chain(max_particles)
          self.List[i].add_number_of_particles(num_part)
      print i
      

class CONTAINER:
  def __init__(self):
    self.trash=list()
  def add_trash(self,chain):
      self.trash.append(chain)
      