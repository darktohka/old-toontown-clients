# File: L (Python 2.2)

import Entity

class LevelMgrBase(Entity.Entity):
    
    def __init__(self, level, entId):
        Entity.Entity.__init__(self, level, entId)

    
    def destroy(self):
        Entity.Entity.destroy(self)
        self.ignoreAll()


