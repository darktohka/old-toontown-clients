# File: S (Python 2.2)

import CogHood
import ToontownGlobals
import SellbotCogHQLoader

class SellbotHQ(CogHood.CogHood):
    
    def __init__(self, parentFSM, doneEvent, dnaStore, hoodId):
        CogHood.CogHood.__init__(self, parentFSM, doneEvent, dnaStore, hoodId)
        self.id = ToontownGlobals.SellbotHQ
        self.cogHQLoaderClass = SellbotCogHQLoader.SellbotCogHQLoader
        self.storageDNAFile = None
        self.skyFile = 'phase_9/models/cogHQ/cog_sky'
        self.titleColor = (0.5, 0.5, 0.5, 1.0)

    
    def load(self):
        CogHood.CogHood.load(self)
        self.sky.setScale(2.0)
        self.parentFSM.getStateNamed('SellbotHQ').addChild(self.fsm)

    
    def unload(self):
        self.parentFSM.getStateNamed('SellbotHQ').removeChild(self.fsm)
        CogHood.CogHood.unload(self)

    
    def enter(self, *args):
        CogHood.CogHood.enter(self, *args)
        ToontownGlobals.DefaultCameraFov = ToontownGlobals.CogHQCameraFov
        base.camLens.setFov(ToontownGlobals.CogHQCameraFov)
        base.camLens.setNearFar(ToontownGlobals.CogHQCameraNear, ToontownGlobals.CogHQCameraFar)

    
    def exit(self):
        ToontownGlobals.DefaultCameraFov = ToontownGlobals.OriginalCameraFov
        base.camLens.setFov(ToontownGlobals.DefaultCameraFov)
        base.camLens.setNearFar(ToontownGlobals.DefaultCameraNear, ToontownGlobals.DefaultCameraFar)
        CogHood.CogHood.exit(self)


