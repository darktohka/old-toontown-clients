# File: D (Python 2.2)

from ShowBaseGlobal import *
from IntervalGlobal import *
import DistributedCCharBase
import DirectNotifyGlobal
import FSM
import State
import ToontownGlobals
import CharStateDatas
import StateData
import Task
import Localizer

class DistributedPluto(DistributedCCharBase.DistributedCCharBase):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedPluto')
    
    def __init__(self, cr):
        
        try:
            pass
        except:
            self.DistributedPluto_initialized = 1
            DistributedCCharBase.DistributedCCharBase.__init__(self, cr, Localizer.Pluto, 'p')
            self.fsm = FSM.FSM('DistributedPluto', [
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
        taskMgr.remove('enterNeutralTask')
        taskMgr.remove('enterWalkTask')
        del self.neutralDoneEvent
        del self.neutral
        del self.walkDoneEvent
        del self.walk
        del self.neutralStartTrack
        del self.walkStartTrack
        self.fsm.requestFinalState()

    
    def delete(self):
        
        try:
            pass
        except:
            self.DistributedPluto_deleted = 1
            del self.fsm
            DistributedCCharBase.DistributedCCharBase.delete(self)


    
    def generate(self):
        DistributedCCharBase.DistributedCCharBase.generate(self)
        self.neutralDoneEvent = self.taskName('pluto-neutral-done')
        self.neutral = CharStateDatas.CharNeutralState(self.neutralDoneEvent, self)
        self.walkDoneEvent = self.taskName('pluto-walk-done')
        self.walk = CharStateDatas.CharWalkState(self.walkDoneEvent, self)
        self.walkStartTrack = Sequence(self.actorInterval('stand'), Func(self.stand))
        self.neutralStartTrack = Sequence(self.actorInterval('sit'), Func(self.sit))
        self.fsm.request('Neutral')

    
    def stand(self):
        self.dropShadow.setScale(0.90000000000000002, 1.3500000000000001, 0.90000000000000002)
        self.collNodePath.setScale(1.0, 1.5, 1.0)

    
    def sit(self):
        self.dropShadow.setScale(0.90000000000000002)
        self.collNodePath.setScale(1.0)

    
    def enterOff(self):
        pass

    
    def exitOff(self):
        pass

    
    def enterNeutral(self):
        self.notify.debug('Neutral ' + self.getName() + '...')
        self.neutral.enter(self.neutralStartTrack)
        self.acceptOnce(self.neutralDoneEvent, self._DistributedPluto__decideNextState)

    
    def exitNeutral(self):
        self.ignore(self.neutralDoneEvent)
        self.neutral.exit()

    
    def enterWalk(self):
        self.notify.debug('Walking ' + self.getName() + '...')
        self.walk.enter(self.walkStartTrack)
        self.acceptOnce(self.walkDoneEvent, self._DistributedPluto__decideNextState)

    
    def exitWalk(self):
        self.ignore(self.walkDoneEvent)
        self.walk.exit()

    
    def _DistributedPluto__decideNextState(self, doneStatus):
        self.fsm.request('Neutral')

    
    def setWalk(self, srcNode, destNode, timestamp):
        if destNode and not (destNode == srcNode):
            self.walk.setWalk(srcNode, destNode, timestamp)
            self.fsm.request('Walk')
        

    
    def walkSpeed(self):
        return ToontownGlobals.PlutoSpeed


