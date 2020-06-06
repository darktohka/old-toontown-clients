# File: D (Python 2.2)

import TownLoader
import DGStreet
import Suit

class DGTownLoader(TownLoader.TownLoader):
    
    def __init__(self, hood, parentFSM, doneEvent):
        TownLoader.TownLoader.__init__(self, hood, parentFSM, doneEvent)
        self.streetClass = DGStreet.DGStreet
        self.musicFile = 'phase_8/audio/bgm/DG_SZ.mid'
        self.activityMusicFile = 'phase_8/audio/bgm/DG_SZ.mid'
        self.townStorageDNAFile = 'phase_8/dna/storage_DG_town.dna'

    
    def load(self, zoneId):
        TownLoader.TownLoader.load(self, zoneId)
        Suit.loadSuits(3)
        dnaFile = 'phase_8/dna/daisys_garden_' + str(self.branchZone) + '.dna'
        self.createHood(dnaFile)

    
    def unload(self):
        Suit.unloadSuits(3)
        TownLoader.TownLoader.unload(self)


