# File: T (Python 2.2)

from ShowBaseGlobal import *
import Hood
import TutorialTownLoader
from ToontownGlobals import *
import SkyUtil

class TutorialHood(Hood.Hood):
    
    def __init__(self, parentFSM, doneEvent, dnaStore):
        Hood.Hood.__init__(self, parentFSM, doneEvent, dnaStore)
        self.id = Tutorial
        self.townLoaderClass = TutorialTownLoader.TutorialTownLoader
        self.safeZoneLoaderClass = None
        self.storageDNAFile = None
        self.skyFile = 'phase_3.5/models/props/TT_sky'
        self.titleColor = (1.0, 0.5, 0.40000000000000002, 1.0)

    
    def load(self):
        Hood.Hood.load(self)
        self.parentFSM.getStateNamed('TutorialHood').addChild(self.fsm)

    
    def unload(self):
        self.parentFSM.getStateNamed('TutorialHood').removeChild(self.fsm)
        Hood.Hood.unload(self)

    
    def enter(self, *args):
        Hood.Hood.enter(self, *args)

    
    def exit(self):
        Hood.Hood.exit(self)

    
    def skyTrack(self, task):
        return SkyUtil.cloudSkyTrack(task)

    
    def startSky(self):
        SkyUtil.startCloudSky(self)


