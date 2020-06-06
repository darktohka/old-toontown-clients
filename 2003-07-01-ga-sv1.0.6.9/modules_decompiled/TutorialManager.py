# File: T (Python 2.2)

from ShowBaseGlobal import *
from PandaObject import *
import DistributedObject
import DirectNotifyGlobal
import ZoneUtil

class TutorialManager(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('TutorialManager')
    neverDisable = 1
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        return None

    
    def generate(self):
        messenger.send('tmGenerate')
        self.accept('requestTutorial', self.d_requestTutorial)
        self.accept('rejectTutorial', self.d_rejectTutorial)
        return None

    
    def disable(self):
        self.ignoreAll()
        return None

    
    def d_requestTutorial(self):
        self.sendUpdate('requestTutorial', [])
        return None

    
    def d_rejectTutorial(self):
        self.sendUpdate('rejectTutorial', [])
        return None

    
    def enterTutorial(self, branchZone, streetZone, shopZone, hqZone):
        toonbase.localToon.inTutorial = 1
        ZoneUtil.overrideOn(branch = branchZone, exteriorList = [
            streetZone], interiorList = [
            shopZone,
            hqZone])
        messenger.send('startTutorial', [
            shopZone])
        self.acceptOnce('stopTutorial', self._TutorialManager__handleStopTutorial)
        self.acceptOnce('toonArrivedTutorial', self.d_toonArrived)

    
    def _TutorialManager__handleStopTutorial(self):
        toonbase.localToon.inTutorial = 0
        self.d_allDone()
        ZoneUtil.overrideOff()

    
    def d_allDone(self):
        self.sendUpdate('allDone', [])
        return None

    
    def d_toonArrived(self):
        self.sendUpdate('toonArrived', [])
        return None


