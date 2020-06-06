# File: D (Python 2.2)

from ShowBaseGlobal import *
from ClockDelta import *
import DirectNotifyGlobal
import FSM
import DistributedObject

class DistributedAnimatedProp(DistributedObject.DistributedObject):
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.fsm = FSM.FSM('DistributedAnimatedProp', [
            State.State('off', self.enterOff, self.exitOff, [
                'playing',
                'attract']),
            State.State('attract', self.enterAttract, self.exitAttract, [
                'playing']),
            State.State('playing', self.enterPlaying, self.exitPlaying, [
                'attract'])], 'off', 'off')
        self.fsm.enterInitialState()

    
    def generate(self):
        DistributedObject.DistributedObject.generate(self)

    
    def disable(self):
        self.fsm.request('off')
        DistributedObject.DistributedObject.disable(self)

    
    def delete(self):
        del self.fsm
        DistributedObject.DistributedObject.delete(self)

    
    def setPropId(self, propId):
        self.propId = propId

    
    def setAvatarInteract(self, avatarId):
        self.avatarId = avatarId

    
    def setState(self, state, timestamp):
        self.fsm.request(state, [
            globalClockDelta.localElapsedTime(timestamp)])

    
    def _DistributedAnimatedProp__getPropNodePath(self):
        if not self.__dict__.has_key('propNodePath'):
            self.propNodePath = self.cr.playGame.hood.loader.geom.find('**/prop' + self.propID + ':*_DNARoot')
        
        return self.propNodePath

    
    def enterTrigger(self, args = None):
        messenger.send('DistributedAnimatedProp_enterTrigger')
        self.sendUpdate('requestInteract')

    
    def exitTrigger(self, args = None):
        messenger.send('DistributedAnimatedProp_exitTrigger')
        self.sendUpdate('requestExit')

    
    def rejectInteract(self):
        self.cr.playGame.getPlace().setState('walk')

    
    def avatarExit(self, avatarId):
        pass

    
    def enterOff(self):
        pass

    
    def exitOff(self):
        pass

    
    def enterAttract(self, ts):
        pass

    
    def exitAttract(self):
        pass

    
    def enterPlaying(self, ts):
        pass

    
    def exitPlaying(self):
        pass


