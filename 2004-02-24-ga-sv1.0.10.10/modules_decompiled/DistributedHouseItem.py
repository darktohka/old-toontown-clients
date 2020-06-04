# File: D (Python 2.2)

from ToontownGlobals import *
from IntervalGlobal import *
from ClockDelta import *
import ToontownGlobals
import DistributedObject
import Localizer
import ToontownDialog

class DistributedHouseItem(DistributedObject.DistributedObject):
    notify = directNotify.newCategory('DistributedHouseItem')
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)

    
    def generate(self):
        DistributedObject.DistributedObject.generate(self)

    
    def announceGenerate(self):
        DistributedObject.DistributedObject.announceGenerate(self)
        self.load()

    
    def load(self):
        pass

    
    def disable(self):
        DistributedObject.DistributedObject.disable(self)

    
    def delete(self):
        DistributedObject.DistributedObject.delete(self)


