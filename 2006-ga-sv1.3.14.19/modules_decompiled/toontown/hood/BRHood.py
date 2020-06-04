# File: B (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
import ToonHood
from toontown.town import BRTownLoader
from toontown.safezone import BRSafeZoneLoader
from toontown.toonbase.ToontownGlobals import *

class BRHood(ToonHood.ToonHood):
    
    def __init__(self, parentFSM, doneEvent, dnaStore, hoodId):
        ToonHood.ToonHood.__init__(self, parentFSM, doneEvent, dnaStore, hoodId)
        self.id = TheBrrrgh
        self.townLoaderClass = BRTownLoader.BRTownLoader
        self.safeZoneLoaderClass = BRSafeZoneLoader.BRSafeZoneLoader
        self.storageDNAFile = 'phase_8/dna/storage_BR.dna'
        self.holidayStorageDNADict = {
            WINTER_DECORATIONS: [
                'phase_8/dna/winter_storage_BR.dna'] }
        self.skyFile = 'phase_6/models/props/BR_sky'
        self.titleColor = (0.29999999999999999, 0.59999999999999998, 1.0, 1.0)

    
    def load(self):
        ToonHood.ToonHood.load(self)
        self.parentFSM.getStateNamed('BRHood').addChild(self.fsm)

    
    def unload(self):
        self.parentFSM.getStateNamed('BRHood').removeChild(self.fsm)
        ToonHood.ToonHood.unload(self)

    
    def enter(self, *args):
        ToonHood.ToonHood.enter(self, *args)

    
    def exit(self):
        ToonHood.ToonHood.exit(self)


