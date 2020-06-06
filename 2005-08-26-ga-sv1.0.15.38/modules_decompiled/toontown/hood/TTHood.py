# File: T (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
import ToonHood
from toontown.town import TTTownLoader
from toontown.safezone import TTSafeZoneLoader
from toontown.toonbase.ToontownGlobals import *
import SkyUtil

class TTHood(ToonHood.ToonHood):
    
    def __init__(self, parentFSM, doneEvent, dnaStore, hoodId):
        ToonHood.ToonHood.__init__(self, parentFSM, doneEvent, dnaStore, hoodId)
        self.id = ToontownCentral
        self.townLoaderClass = TTTownLoader.TTTownLoader
        self.safeZoneLoaderClass = TTSafeZoneLoader.TTSafeZoneLoader
        self.storageDNAFile = 'phase_4/dna/storage_TT.dna'
        self.holidayStorageDNADict = {
            WINTER_DECORATIONS: [
                'phase_4/dna/winter_storage_TT.dna',
                'phase_4/dna/winter_storage_TT_sz.dna'] }
        self.skyFile = 'phase_3.5/models/props/TT_sky'
        self.titleColor = (1.0, 0.5, 0.40000000000000002, 1.0)

    
    def load(self):
        ToonHood.ToonHood.load(self)
        self.parentFSM.getStateNamed('TTHood').addChild(self.fsm)

    
    def unload(self):
        self.parentFSM.getStateNamed('TTHood').removeChild(self.fsm)
        ToonHood.ToonHood.unload(self)

    
    def enter(self, *args):
        ToonHood.ToonHood.enter(self, *args)

    
    def exit(self):
        ToonHood.ToonHood.exit(self)

    
    def skyTrack(self, task):
        return SkyUtil.cloudSkyTrack(task)

    
    def startSky(self):
        SkyUtil.startCloudSky(self)


