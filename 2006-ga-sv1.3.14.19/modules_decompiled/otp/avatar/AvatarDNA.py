# File: A (Python 2.2)

import whrandom
from pandac.PandaModules import *
from direct.directnotify.DirectNotifyGlobal import *
import random
from direct.distributed.PyDatagram import PyDatagram
from direct.distributed.PyDatagramIterator import PyDatagramIterator
notify = directNotify.newCategory('AvatarDNA')

class AvatarDNA:
    
    def __str__(self):
        return 'avatar parent class: type undefined'

    
    def makeNetString(self):
        notify.error('called makeNetString on avatarDNA parent class')
        return None

    
    def printNetString(self):
        string = self.makeNetString()
        dg = PyDatagram(string)
        dg.dumpHex(ostream)

    
    def makeFromNetString(self, string):
        notify.error('called makeFromNetString on avatarDNA parent class')
        return None

    
    def getType(self):
        notify.error('Invalid DNA type: ', self.type)
        return type


