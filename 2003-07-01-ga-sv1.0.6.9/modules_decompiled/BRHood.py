# File: B (Python 2.2)

from ShowBaseGlobal import *
import Hood
import BRTownLoader
import BRSafeZoneLoader
from ToontownGlobals import *

class BRHood(Hood.Hood):
    
    def __init__(self, parentFSM, doneEvent, dnaStore):
        Hood.Hood.__init__(self, parentFSM, doneEvent, dnaStore)
        self.id = TheBrrrgh
        self.townLoaderClass = BRTownLoader.BRTownLoader
        self.safeZoneLoaderClass = BRSafeZoneLoader.BRSafeZoneLoader
        self.storageDNAFile = 'phase_8/dna/storage_BR.dna'
        self.skyFile = 'phase_6/models/props/BR_sky'
        self.titleColor = (0.29999999999999999, 0.59999999999999998, 1.0, 1.0)

    
    def load(self):
        Hood.Hood.load(self)
        self.parentFSM.getStateNamed('BRHood').addChild(self.fsm)

    
    def unload(self):
        self.parentFSM.getStateNamed('BRHood').removeChild(self.fsm)
        Hood.Hood.unload(self)

    
    def enter(self, *args):
        Hood.Hood.enter(self, *args)

    
    def exit(self):
        Hood.Hood.exit(self)


