# File: S (Python 2.2)

import CogHood
import ToontownGlobals

class SellbotHQ(CogHood.CogHood):
    
    def __init__(self, parentFSM, doneEvent, dnaStore, hoodId):
        CogHood.CogHood.__init__(self, parentFSM, doneEvent, dnaStore, hoodId)
        self.id = ToontownGlobals.SellbotHQ
        self.storageDNAFile = None
        self.titleColor = (0.5, 0.5, 0.5, 1.0)

    
    def load(self):
        CogHood.CogHood.load(self)
        self.parentFSM.getStateNamed('SellbotHQ').addChild(self.fsm)

    
    def unload(self):
        self.parentFSM.getStateNamed('SellbotHQ').removeChild(self.fsm)
        CogHood.CogHood.unload(self)

    
    def enter(self, *args):
        CogHood.CogHood.enter(self, *args)

    
    def exit(self):
        CogHood.CogHood.exit(self)


