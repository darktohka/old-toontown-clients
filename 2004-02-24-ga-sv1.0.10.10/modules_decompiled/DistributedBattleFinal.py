# File: D (Python 2.2)

from PandaModules import *
from IntervalGlobal import *
from BattleBase import *
import Actor
import AvatarDNA
import DelayDelete
import DirectNotifyGlobal
import DistributedBattleBase
import Emote
import Localizer
import MovieUtil
import Suit
import SuitBattleGlobals
import ToontownBattleGlobals
import ToontownGlobals
import State
import random

class DistributedBattleFinal(DistributedBattleBase.DistributedBattleBase):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedBattleFinal')
    
    def __init__(self, cr):
        townBattle = cr.playGame.hood.loader.townBattle
        DistributedBattleBase.DistributedBattleBase.__init__(self, cr, townBattle)
        self.setupCollisions(self.uniqueBattleName('battle-collide'))
        self.streetBattle = 0
        self.joiningSuitsName = self.uniqueBattleName('joiningSuits')
        self.fsm.addState(State.State('ReservesJoining', self.enterReservesJoining, self.exitReservesJoining, [
            'WaitForJoin']))
        offState = self.fsm.getStateNamed('Off')
        offState.addTransition('ReservesJoining')
        waitForJoinState = self.fsm.getStateNamed('WaitForJoin')
        waitForJoinState.addTransition('ReservesJoining')
        playMovieState = self.fsm.getStateNamed('PlayMovie')
        playMovieState.addTransition('ReservesJoining')

    
    def generate(self):
        DistributedBattleBase.DistributedBattleBase.generate(self)

    
    def disable(self):
        DistributedBattleBase.DistributedBattleBase.disable(self)

    
    def delete(self):
        DistributedBattleBase.DistributedBattleBase.delete(self)
        self.removeCollisionData()

    
    def setBattleNumber(self, battleNumber):
        self.battleNumber = battleNumber

    
    def setBattleSide(self, battleSide):
        self.battleSide = battleSide

    
    def setMembers(self, suits, suitsJoining, suitsPending, suitsActive, suitsLured, suitTraps, toons, toonsJoining, toonsPending, toonsActive, toonsRunning, timestamp):
        if self.battleCleanedUp():
            return None
        
        oldtoons = DistributedBattleBase.DistributedBattleBase.setMembers(self, suits, suitsJoining, suitsPending, suitsActive, suitsLured, suitTraps, toons, toonsJoining, toonsPending, toonsActive, toonsRunning, timestamp)
        if len(self.toons) == 4 and len(oldtoons) < 4:
            self.notify.debug('setMembers() - battle is now full of toons')
            self.closeBattleCollision()
        elif len(self.toons) < 4 and len(oldtoons) == 4:
            self.openBattleCollision()
        

    
    def makeSuitJoin(self, suit, ts):
        self.notify.debug('makeSuitJoin(%d)' % suit.doId)
        self.joiningSuits.append(suit)
        if self.hasLocalToon():
            self.d_joinDone(toonbase.localToon.doId, suit.doId)
        

    
    def _DistributedBattleFinal__showSuitsJoining(self, suits, ts, name, callback):
        import DistributedBossCog
        if DistributedBossCog.OneBossCog == None:
            return None
        
        if self.battleSide:
            openDoor = Func(DistributedBossCog.OneBossCog.doorB.request, 'open')
            closeDoor = Func(DistributedBossCog.OneBossCog.doorB.request, 'close')
        else:
            openDoor = Func(DistributedBossCog.OneBossCog.doorA.request, 'open')
            closeDoor = Func(DistributedBossCog.OneBossCog.doorA.request, 'close')
        suitTrack = Parallel()
        delay = 0
        for suit in suits:
            if self.battleNumber == 2:
                suit.makeSkeleton()
                suit.corpMedallion.hide()
                suit.healthBar.show()
            
            suit.setState('Battle')
            suit.setPos(DistributedBossCog.OneBossCog, 0, 0, 0)
            suit.headsUp(self)
            suit.setScale(3.7999999999999998 / suit.height)
            if suit in self.joiningSuits:
                i = len(self.pendingSuits) + self.joiningSuits.index(suit)
                (destPos, h) = self.suitPendingPoints[i]
                destHpr = VBase3(h, 0, 0)
            else:
                (destPos, destHpr) = self.getActorPosHpr(suit, self.suits)
            suitTrack.append(Track((delay, self.createAdjustInterval(suit, destPos, destHpr)), (delay + 1.5, suit.scaleInterval(1.5, 1))))
            delay += 1
        
        if self.hasLocalToon():
            camera.reparentTo(self)
            if random.choice([
                0,
                1]):
                camera.setPosHpr(20, -4, 7, 60, 0, 0)
            else:
                camera.setPosHpr(-20, -4, 7, -60, 0, 0)
        
        done = Func(callback)
        track = Sequence(openDoor, suitTrack, closeDoor, done, name = name)
        track.start(ts)
        self.activeIntervals[name] = track

    
    def _DistributedBattleFinal__playReward(self, ts, callback):
        toonTracks = Parallel()
        for toon in self.toons:
            toonTracks.append(Sequence(Func(toon.loop, 'victory'), Wait(FLOOR_REWARD_TIMEOUT), Func(toon.loop, 'neutral')))
        
        name = self.uniqueName('floorReward')
        track = Sequence(toonTracks, name = name)
        if self.hasLocalToon():
            camera.setPos(0, 0, 1)
            camera.setHpr(180, 10, 0)
        
        import DistributedBossCog
        track += [
            DistributedBossCog.OneBossCog.makeCageDropMovie(self.hasLocalToon()),
            Func(callback)]
        self.activeIntervals[name] = track
        track.start(ts)

    
    def enterReward(self, ts):
        self.notify.debug('enterReward()')
        self.disableCollision()
        self.delayDeleteMembers()
        self._DistributedBattleFinal__playReward(ts, self._DistributedBattleFinal__handleFloorRewardDone)
        return None

    
    def _DistributedBattleFinal__handleFloorRewardDone(self):
        return None

    
    def exitReward(self):
        self.notify.debug('exitReward()')
        self.clearInterval(self.uniqueName('floorReward'), finish = 1)
        self.membersKeep = None
        NametagGlobals.setMasterArrowsOn(1)
        for toon in self.toons:
            toon.startSmooth()
        
        return None

    
    def enterResume(self, ts = 0):
        if self.hasLocalToon():
            self.removeLocalToon()
        
        self.fsm.requestFinalState()

    
    def exitResume(self):
        return None

    
    def enterReservesJoining(self, ts = 0):
        self.delayDeleteMembers()
        self._DistributedBattleFinal__showSuitsJoining(self.joiningSuits, ts, self.joiningSuitsName, self._DistributedBattleFinal__reservesJoiningDone)

    
    def _DistributedBattleFinal__reservesJoiningDone(self):
        self.membersKeep = None
        self.doneBarrier()

    
    def exitReservesJoining(self):
        self.clearInterval(self.joiningSuitsName)

    
    def enterNoLocalToon(self):
        self.notify.debug('enterNoLocalToon()')
        import DistributedBossCog
        if DistributedBossCog.OneBossCog != None and DistributedBossCog.OneBossCog.hasLocalToon():
            self.enableCollision()
        else:
            self.disableCollision()
        return None

    
    def exitNoLocalToon(self):
        self.disableCollision()
        return None

    
    def enterWaitForServer(self):
        self.notify.debug('enterWaitForServer()')
        return None

    
    def exitWaitForServer(self):
        return None


