# File: D (Python 2.2)

import DistributedNode
import Actor

class DistributedActor(DistributedNode.DistributedNode, Actor.Actor):
    
    def __init__(self, cr):
        
        try:
            pass
        except:
            self.DistributedActor_initialized = 1
            DistributedNode.DistributedNode.__init__(self, cr)
            self.setCacheable(1)

        return None

    
    def disable(self):
        if not self.isEmpty():
            Actor.Actor.unloadAnims(self, None, None, None)
        
        DistributedNode.DistributedNode.disable(self)

    
    def delete(self):
        
        try:
            pass
        except:
            self.DistributedActor_deleted = 1
            DistributedNode.DistributedNode.delete(self)
            Actor.Actor.delete(self)



