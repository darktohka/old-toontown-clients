# File: D (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from direct.interval.IntervalGlobal import *
import DistributedCCharBase
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import ClassicFSM
from direct.fsm import State
import CharStateDatas
import CCharChatter
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer

class DistributedDonald(DistributedCCharBase.DistributedCCharBase):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedDonald')
    
    def __init__(self, cr):
        
        try:
            pass
        except:
            self.DistributedDonald_initialized = 1
            DistributedCCharBase.DistributedCCharBase.__init__(self, cr, TTLocalizer.Donald, 'd')
            self.fsm = ClassicFSM.ClassicFSM(self.getName(), [
                State.State('Off', self.enterOff, self.exitOff, [
                    'Neutral']),
                State.State('Neutral', self.enterNeutral, self.exitNeutral, [
                    'Walk']),
                State.State('Walk', self.enterWalk, self.exitWalk, [
                    'Neutral'])], 'Off', 'Off')
            self.fsm.enterInitialState()


    
    def disable(self):
        self.fsm.requestFinalState()
        DistributedCCharBase.DistributedCCharBase.disable(self)
        del self.neutralDoneEvent
        del self.neutral
        del self.walkDoneEvent
        del self.walk
        del self.walkStartTrack
        del self.neutralStartTrack
        self.fsm.requestFinalState()

    
    def delete(self):
        
        try:
            pass
        except:
            self.DistributedDonald_deleted = 1
            del self.fsm
            DistributedCCharBase.DistributedCCharBase.delete(self)


    
    def generate(self):
        DistributedCCharBase.DistributedCCharBase.generate(self)
        name = self.getName()
        self.neutralDoneEvent = self.taskName(name + '-neutral-done')
        self.neutral = CharStateDatas.CharNeutralState(self.neutralDoneEvent, self)
        self.walkDoneEvent = self.taskName(name + '-walk-done')
        self.walk = CharStateDatas.CharWalkState(self.walkDoneEvent, self)
        self.walkStartTrack = self.actorInterval('trans-back')
        self.neutralStartTrack = self.actorInterval('trans')
        self.fsm.request('Neutral')

    
    def enterOff(self):
        pass

    
    def exitOff(self):
        pass

    
    def enterNeutral(self):
        self.notify.debug('Neutral ' + self.getName() + '...')
        self.neutral.enter(startTrack = self.neutralStartTrack, playRate = 0.5)
        self.acceptOnce(self.neutralDoneEvent, self._DistributedDonald__decideNextState)

    
    def exitNeutral(self):
        self.ignore(self.neutralDoneEvent)
        self.neutral.exit()

    
    def enterWalk(self):
        self.notify.debug('Walking ' + self.getName() + '...')
        self.walk.enter(startTrack = self.walkStartTrack)
        self.acceptOnce(self.walkDoneEvent, self._DistributedDonald__decideNextState)

    
    def exitWalk(self):
        self.ignore(self.walkDoneEvent)
        self.walk.exit()

    
    def _DistributedDonald__decideNextState(self, doneStatus):
        self.fsm.request('Neutral')

    
    def setWalk(self, srcNode, destNode, timestamp):
        if destNode and not (destNode == srcNode):
            self.walk.setWalk(srcNode, destNode, timestamp)
            self.fsm.request('Walk')
        

    
    def walkSpeed(self):
        return ToontownGlobals.DonaldSpeed


