# File: L (Python 2.2)

from PandaObject import *
import DistributedChar
import LocalAvatar
import ChatManager
import Char

class LocalChar(DistributedChar.DistributedChar, LocalAvatar.LocalAvatar):
    
    def __init__(self, cr):
        
        try:
            pass
        except:
            self.LocalChar_initialized = 1
            DistributedChar.DistributedChar.__init__(self, cr)
            LocalAvatar.LocalAvatar.__init__(self, cr)
            self.setNameVisible(0)
            Char.initializeDialogue()

        return None


