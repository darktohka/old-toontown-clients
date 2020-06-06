# File: D (Python 2.2)

import DistributedAvatar
import Char

class DistributedChar(DistributedAvatar.DistributedAvatar, Char.Char):
    
    def __init__(self, cr):
        
        try:
            pass
        except:
            self.DistributedChar_initialized = 1
            DistributedAvatar.DistributedAvatar.__init__(self, cr)
            Char.Char.__init__(self)

        return None

    
    def playDialogue(self, *args):
        Char.Char.playDialogue(self, *args)

    
    def setHp(self, hp):
        self.hp = hp
        return None


