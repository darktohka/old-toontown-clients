# File: D (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
import DistributedCCharBase
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import ClassicFSM
from direct.fsm import State
import CharStateDatas
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer

class DistributedMinnie(DistributedCCharBase.DistributedCCharBase):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedMinnie')
    
    def __init__(self, cr):
        
        try:
            pass
        except:
            self.DistributedMinnie_initialized = 1
            DistributedCCharBase.DistributedCCharBase.__init__(self, cr, TTLocalizer.Minnie, 'mn')
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
        self.neutralDoneEvent = None
        self.neutral = None
        self.walkDoneEvent = None
        self.walk = None
        self.fsm.requestFinalState()

    
    def delete(self):
        
        try:
            pass
        except:
            self.DistributedMinnie_deleted = 1
            del self.fsm
            DistributedCCharBase.DistributedCCharBase.delete(self)


    
    def generate(self):
        DistributedCCharBase.DistributedCCharBase.generate(self)
        self.neutralDoneEvent = self.taskName('minnie-neutral-done')
        self.neutral = CharStateDatas.CharNeutralState(self.neutralDoneEvent, self)
        self.walkDoneEvent = self.taskName('minnie-walk-done')
        self.walk = CharStateDatas.CharWalkState(self.walkDoneEvent, self)
        self.fsm.request('Neutral')

    
    def enterOff(self):
        pass

    
    def exitOff(self):
        pass

    
    def enterNeutral(self):
        self.neutral.enter()
        self.acceptOnce(self.neutralDoneEvent, self._DistributedMinnie__decideNextState)

    
    def exitNeutral(self):
        self.ignore(self.neutralDoneEvent)
        self.neutral.exit()

    
    def enterWalk(self):
        self.walk.enter()
        self.acceptOnce(self.walkDoneEvent, self._DistributedMinnie__decideNextState)

    
    def exitWalk(self):
        self.ignore(self.walkDoneEvent)
        self.walk.exit()

    
    def _DistributedMinnie__decideNextState(self, doneStatus):
        self.fsm.request('Neutral')

    
    def setWalk(self, srcNode, destNode, timestamp):
        if destNode and not (destNode == srcNode):
            self.walk.setWalk(srcNode, destNode, timestamp)
            self.fsm.request('Walk')
        

    
    def walkSpeed(self):
        return ToontownGlobals.MinnieSpeed


