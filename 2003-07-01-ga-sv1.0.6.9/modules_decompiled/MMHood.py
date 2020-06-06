# File: M (Python 2.2)

from ShowBaseGlobal import *
import Hood
import MMTownLoader
import MMSafeZoneLoader
from ToontownGlobals import *

class MMHood(Hood.Hood):
    
    def __init__(self, parentFSM, doneEvent, dnaStore):
        Hood.Hood.__init__(self, parentFSM, doneEvent, dnaStore)
        self.id = MinniesMelodyland
        self.townLoaderClass = MMTownLoader.MMTownLoader
        self.safeZoneLoaderClass = MMSafeZoneLoader.MMSafeZoneLoader
        self.storageDNAFile = 'phase_6/dna/storage_MM.dna'
        self.skyFile = 'phase_6/models/props/MM_sky'
        self.titleColor = (1.0, 0.5, 0.5, 1.0)

    
    def load(self):
        Hood.Hood.load(self)
        self.parentFSM.getStateNamed('MMHood').addChild(self.fsm)

    
    def unload(self):
        self.parentFSM.getStateNamed('MMHood').removeChild(self.fsm)
        Hood.Hood.unload(self)

    
    def enter(self, *args):
        Hood.Hood.enter(self, *args)

    
    def exit(self):
        Hood.Hood.exit(self)


