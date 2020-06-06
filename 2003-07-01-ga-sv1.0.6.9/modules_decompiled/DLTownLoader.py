# File: D (Python 2.2)

import TownLoader
import DLStreet
import Suit

class DLTownLoader(TownLoader.TownLoader):
    
    def __init__(self, hood, parentFSM, doneEvent):
        TownLoader.TownLoader.__init__(self, hood, parentFSM, doneEvent)
        self.streetClass = DLStreet.DLStreet
        self.musicFile = 'phase_8/audio/bgm/DL_SZ.mid'
        self.activityMusicFile = 'phase_8/audio/bgm/DL_SZ_activity.mid'
        self.townStorageDNAFile = 'phase_8/dna/storage_DL_town.dna'

    
    def load(self, zoneId):
        TownLoader.TownLoader.load(self, zoneId)
        Suit.loadSuits(3)
        dnaFile = 'phase_8/dna/donalds_dreamland_' + str(self.branchZone) + '.dna'
        self.createHood(dnaFile)

    
    def unload(self):
        Suit.unloadSuits(3)
        TownLoader.TownLoader.unload(self)


