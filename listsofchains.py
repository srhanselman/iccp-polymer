from chain import chain
class Active_Chains:
  def __init__(self):
    self.List=list()
  
  def add_chain(self,chain):
    self.List.append(chain)
    
  def show(self):
    print "List of Active Chains:"
    print "Number of chains:",len(self.List)
    for i in xrange(0,len(self.List)):
      print "Chain ",i," :"
      self.List[i].show()
    
  def run(self,num_chains,num_part):
    for j in xrange(0,num_chains):
      self.add_chain(chain(100))
    for i in xrange(0,len(self.List)):
      self.List[i].add_number_of_particles(num_part)