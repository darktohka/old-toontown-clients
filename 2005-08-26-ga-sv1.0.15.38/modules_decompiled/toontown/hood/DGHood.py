# File: D (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
import ToonHood
from toontown.town import DGTownLoader
from toontown.safezone import DGSafeZoneLoader
from toontown.toonbase.ToontownGlobals import *
import SkyUtil

class DGHood(ToonHood.ToonHood):
    
    def __init__(self, parentFSM, doneEvent, dnaStore, hoodId):
        ToonHood.ToonHood.__init__(self, parentFSM, doneEvent, dnaStore, hoodId)
        self.id = DaisyGardens
        self.townLoaderClass = DGTownLoader.DGTownLoader
        self.safeZoneLoaderClass = DGSafeZoneLoader.DGSafeZoneLoader
        self.storageDNAFile = 'phase_8/dna/storage_DG.dna'
        self.holidayStorageDNADict = {
            WINTER_DECORATIONS: [
                'phase_8/dna/winter_storage_DG.dna'] }
        self.skyFile = 'phase_3.5/models/props/TT_sky'
        self.titleColor = (0.80000000000000004, 0.59999999999999998, 1.0, 1.0)

    
    def load(self):
        ToonHood.ToonHood.load(self)
        self.parentFSM.getStateNamed('DGHood').addChild(self.fsm)

    
    def unload(self):
        self.parentFSM.getStateNamed('DGHood').removeChild(self.fsm)
        ToonHood.ToonHood.unload(self)

    
    def enter(self, *args):
        ToonHood.ToonHood.enter(self, *args)

    
    def exit(self):
        ToonHood.ToonHood.exit(self)

    
    def skyTrack(self, task):
        return SkyUtil.cloudSkyTrack(task)

    
    def startSky(self):
        SkyUtil.startCloudSky(self)


