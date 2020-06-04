# File: D (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from direct.fsm import ClassicFSM
from direct.fsm import State
from direct.directnotify import DirectNotifyGlobal
import DistributedSuitBase

class DistributedTutorialSuit(DistributedSuitBase.DistributedSuitBase):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedTutorialSuit')
    
    def __init__(self, cr):
        
        try:
            pass
        except:
            self.DistributedSuit_initialized = 1
            DistributedSuitBase.DistributedSuitBase.__init__(self, cr)
            self.fsm = ClassicFSM.ClassicFSM('DistributedSuit', [
                State.State('Off', self.enterOff, self.exitOff, [
                    'Walk',
                    'Battle']),
                State.State('Walk', self.enterWalk, self.exitWalk, [
                    'WaitForBattle',
                    'Battle']),
                State.State('Battle', self.enterBattle, self.exitBattle, []),
                State.State('WaitForBattle', self.enterWaitForBattle, self.exitWaitForBattle, [
                    'Battle'])], 'Off', 'Off')
            self.fsm.enterInitialState()

        return None

    
    def generate(self):
        DistributedSuitBase.DistributedSuitBase.generate(self)

    
    def announceGenerate(self):
        self.setState('Walk')

    
    def disable(self):
        self.notify.debug('DistributedSuit %d: disabling' % self.getDoId())
        self.setState('Off')
        DistributedSuitBase.DistributedSuitBase.disable(self)
        return None

    
    def delete(self):
        
        try:
            pass
        except:
            self.DistributedSuit_deleted = 1
            self.notify.debug('DistributedSuit %d: deleting' % self.getDoId())
            del self.fsm
            DistributedSuitBase.DistributedSuitBase.delete(self)

        return None

    
    def d_requestBattle(self, pos, hpr):
        self.cr.playGame.getPlace().setState('WaitForBattle')
        self.sendUpdate('requestBattle', [
            pos[0],
            pos[1],
            pos[2],
            hpr[0],
            hpr[1],
            hpr[2]])
        return None

    
    def _DistributedTutorialSuit__handleToonCollision(self, collEntry):
        toonId = base.localAvatar.getDoId()
        self.notify.debug('Distributed suit: requesting a Battle with ' + 'toon: %d' % toonId)
        self.d_requestBattle(self.getPos(), self.getHpr())
        self.setState('WaitForBattle')
        return None

    
    def enterWalk(self):
        self.enableBattleDetect('walk', self._DistributedTutorialSuit__handleToonCollision)
        self.loop('walk', 0)
        pathPoints = [
            Vec3(50, 15, 0),
            Vec3(50, 25, 0),
            Vec3(20, 25, 0),
            Vec3(20, 15, 0),
            Vec3(50, 15, 0)]
        self.tutWalkTrack = self.makePathTrack(self, pathPoints, 4.5, 'tutFlunkyWalk')
        self.tutWalkTrack.loop()

    
    def exitWalk(self):
        self.disableBattleDetect()
        self.tutWalkTrack.pause()
        self.tutWalkTrack = None
        return None


