# File: D (Python 2.2)

from PandaModules import *
from ToonBaseGlobal import *
from IntervalGlobal import *
from BattleBase import *
from ClockDelta import *
import ToontownBattleGlobals
import DistributedNode
import NodePath
import FSM
import State
import Task
import DirectNotifyGlobal
import Movie
import MovieUtil
import Suit
import Actor
import BattleProps
import ParticleEffect
import BattleParticles
import ZoneUtil
import DelayDelete
import Emote

class DistributedBattleBase(DistributedNode.DistributedNode, BattleBase):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedBattleBase')
    id = 0
    camPos = ToontownBattleGlobals.BattleCamDefaultPos
    camHpr = ToontownBattleGlobals.BattleCamDefaultHpr
    camFov = ToontownBattleGlobals.BattleCamDefaultFov
    camMenuFov = ToontownBattleGlobals.BattleCamMenuFov
    camJoinPos = ToontownBattleGlobals.BattleCamJoinPos
    camJoinHpr = ToontownBattleGlobals.BattleCamJoinHpr
    
    def __init__(self, cr, townBattle):
        DistributedNode.DistributedNode.__init__(self, cr)
        NodePath.NodePath.__init__(self)
        self.assign(render.attachNewNode(self.uniqueBattleName('distributed-battle')))
        BattleBase.__init__(self)
        self.bossBattle = 0
        self.townBattle = townBattle
        self.activeIntervals = { }
        self.localToonJustJoined = 0
        self.choseAttackAlready = 0
        self.toons = []
        self.toonsKeep = None
        self.exitedToons = []
        self.suitTraps = ''
        self.faceOffName = self.uniqueBattleName('faceoff')
        self.localToonBattleEvent = self.uniqueBattleName('localtoon-battle-event')
        self.adjustName = self.uniqueBattleName('adjust')
        self.timerCountdownTaskName = self.uniqueBattleName('timer-countdown')
        self.movie = Movie.Movie(self)
        self.timer = Timer()
        self.needAdjustTownBattle = 0
        self.streetBattle = 1
        self.fsm = FSM.FSM('DistributedBattle', [
            State.State('Off', self.enterOff, self.exitOff, [
                'FaceOff',
                'WaitForInput',
                'WaitForJoin',
                'MakeMovie',
                'PlayMovie',
                'Reward',
                'Resume']),
            State.State('FaceOff', self.enterFaceOff, self.exitFaceOff, [
                'WaitForInput']),
            State.State('WaitForJoin', self.enterWaitForJoin, self.exitWaitForJoin, [
                'WaitForInput',
                'Resume']),
            State.State('WaitForInput', self.enterWaitForInput, self.exitWaitForInput, [
                'WaitForInput',
                'PlayMovie',
                'Resume']),
            State.State('MakeMovie', self.enterMakeMovie, self.exitMakeMovie, [
                'PlayMovie',
                'Resume']),
            State.State('PlayMovie', self.enterPlayMovie, self.exitPlayMovie, [
                'WaitForInput',
                'WaitForJoin',
                'Reward',
                'Resume']),
            State.State('Reward', self.enterReward, self.exitReward, [
                'Resume']),
            State.State('Resume', self.enterResume, self.exitResume, [])], 'Off', 'Off')
        self.fsm.enterInitialState()
        self.localToonFsm = FSM.FSM('LocalToon', [
            State.State('HasLocalToon', self.enterHasLocalToon, self.exitHasLocalToon, [
                'NoLocalToon',
                'WaitForServer']),
            State.State('NoLocalToon', self.enterNoLocalToon, self.exitNoLocalToon, [
                'HasLocalToon',
                'WaitForServer']),
            State.State('WaitForServer', self.enterWaitForServer, self.exitWaitForServer, [
                'HasLocalToon',
                'NoLocalToon'])], 'WaitForServer', 'WaitForServer')
        self.localToonFsm.enterInitialState()
        self.adjustFsm = FSM.FSM('Adjust', [
            State.State('Adjusting', self.enterAdjusting, self.exitAdjusting, [
                'NotAdjusting']),
            State.State('NotAdjusting', self.enterNotAdjusting, self.exitNotAdjusting, [
                'Adjusting'])], 'NotAdjusting', 'NotAdjusting')
        self.adjustFsm.enterInitialState()

    
    def uniqueBattleName(self, name):
        DistributedBattleBase.id += 1
        return name + '-%d' % DistributedBattleBase.id

    
    def generate(self):
        self.notify.debug('generate(%s)' % self.doId)
        self.reparentTo(render)

    
    def _DistributedBattleBase__cleanupIntervals(self):
        for interval in self.activeIntervals.values():
            interval.finish()
        
        self.activeIntervals = { }

    
    def clearInterval(self, name, finish = 0):
        if self.activeIntervals.has_key(name):
            ival = self.activeIntervals[name]
            if finish:
                ival.finish()
            else:
                ival.pause()
            if self.activeIntervals.has_key(name):
                del self.activeIntervals[name]
            
        else:
            self.notify.debug('interval: %s already cleared' % name)

    
    def finishInterval(self, name):
        if self.activeIntervals.has_key(name):
            interval = self.activeIntervals[name]
            interval.finish()
        

    
    def disable(self):
        self.notify.debug('disable(%s)' % self.doId)
        self._DistributedBattleBase__cleanupIntervals()
        self.fsm.requestFinalState()
        if self.hasLocalToon():
            self.removeLocalToon()
            base.camLens.setFov(DefaultCameraFov)
        
        self.localToonFsm.request('WaitForServer')
        self.ignoreAll()
        for suit in self.suits:
            if suit.battleTrap != NO_TRAP:
                self.removeTrap(suit)
            
            del suit.battleTrap
            del suit.battleTrapProp
            del suit.battleTrapIsFresh
        
        self.suits = []
        self.pendingSuits = []
        self.joiningSuits = []
        self.activeSuits = []
        self.suitTraps = ''
        self.toons = []
        self.toonsKeep = None
        self.joiningToons = []
        self.pendingToons = []
        self.activeToons = []
        self.runningToons = []
        self._DistributedBattleBase__stopTimer()

    
    def delete(self):
        self.notify.debug('delete(%s)' % self.doId)
        self._DistributedBattleBase__cleanupIntervals()
        self.movie.battle = None
        del self.townBattle
        self.removeNode()
        self.fsm = None
        self.localToonFsm = None
        self.adjustFsm = None
        self._DistributedBattleBase__stopTimer()
        self.timer = None

    
    def loadTrap(self, suit, trapid):
        self.notify.debug('loadTrap() trap: %d suit: %d' % (trapid, suit.doId))
        trapName = AvProps[TRAP][trapid]
        trap = BattleProps.globalPropPool.getProp(trapName)
        suit.battleTrapProp = trap
        suit.battleTrap = trapid
        suit.battleTrapIsFresh = 0
        trap.wrtReparentTo(suit)
        distance = MovieUtil.SUIT_TRAP_DISTANCE
        if trapName == 'rake':
            distance = MovieUtil.SUIT_TRAP_RAKE_DISTANCE
            distance += MovieUtil.getSuitRakeOffset(suit)
            trap.setH(180)
            trap.setScale(0.69999999999999996)
        elif trapName == 'trapdoor' or trapName == 'quicksand':
            trap.setScale(1.7)
        elif trapName == 'marbles':
            distance = MovieUtil.SUIT_TRAP_MARBLES_DISTANCE
            trap.setH(94)
        elif trapName == 'tnt':
            trap.setP(90)
            tip = trap.find('**/joint-attachEmitter')
            sparks = BattleParticles.createParticleEffect(file = 'tnt')
            trap.sparksEffect = sparks
            sparks.start(tip)
        
        trap.setPos(0, distance, 0)
        if isinstance(trap, Actor.Actor):
            frame = trap.getNumFrames(trapName) - 1
            trap.pose(trapName, frame)
        

    
    def removeTrap(self, suit):
        self.notify.debug('removeTrap() from suit: %d' % suit.doId)
        if suit.battleTrapProp == None:
            suit.battleTrap = NO_TRAP
            return None
        
        if suit.battleTrap == 6:
            sparks = suit.battleTrap.sparksEffect
            sparks.cleanup()
        
        MovieUtil.removeProp(suit.battleTrapProp)
        suit.battleTrapProp = None
        suit.battleTrap = NO_TRAP
        suit.battleTrapIsFresh = 0

    
    def pause(self):
        self.timer.stop()

    
    def unpause(self):
        self.timer.resume()

    
    def findSuit(self, id):
        for s in self.suits:
            if s.doId == id:
                return s
            
        
        return None

    
    def findToon(self, id):
        toon = self.getToon(id)
        if toon == None:
            return None
        
        for t in self.toons:
            if t == toon:
                return t
            
        
        return None

    
    def isSuitLured(self, suit):
        if self.luredSuits.count(suit) != 0:
            return 1
        
        return 0

    
    def unlureSuit(self, suit):
        self.notify.debug('movie unluring suit %s' % suit.doId)
        if self.luredSuits.count(suit) != 0:
            self.luredSuits.remove(suit)
            self.needAdjustTownBattle = 1
        
        return None

    
    def lureSuit(self, suit):
        self.notify.debug('movie luring suit %s' % suit.doId)
        if self.luredSuits.count(suit) == 0:
            self.luredSuits.append(suit)
            self.needAdjustTownBattle = 1
        
        return None

    
    def getActorPosHpr(self, actor, actorList = []):
        if isinstance(actor, Suit.Suit):
            if actorList == []:
                actorList = self.activeSuits
            
            if actorList.count(actor) != 0:
                numSuits = len(actorList) - 1
                index = actorList.index(actor)
                point = self.suitPoints[numSuits][index]
                return (Point3(point[0]), VBase3(point[1], 0.0, 0.0))
            else:
                self.notify.warning('getActorPosHpr() - suit not active')
        elif actorList == []:
            actorList = self.activeToons
        
        if actorList.count(actor) != 0:
            numToons = len(actorList) - 1
            index = actorList.index(actor)
            point = self.toonPoints[numToons][index]
            return (Point3(point[0]), VBase3(point[1], 0.0, 0.0))
        else:
            self.notify.warning('getActorPosHpr() - toon not active')

    
    def setZoneId(self, zoneId):
        self.zoneId = zoneId

    
    def setBossBattle(self, value):
        self.bossBattle = value

    
    def setState(self, state, timestamp):
        self.notify.debug('setState(%s)' % state)
        self.fsm.request(state, [
            globalClockDelta.localElapsedTime(timestamp)])

    
    def setMembers(self, suits, suitsJoining, suitsPending, suitsActive, suitsLured, suitTraps, toons, toonsJoining, toonsPending, toonsActive, toonsRunning, timestamp):
        self.notify.debug('setMembers() - suits: %s suitsJoining: %s suitsPending: %s suitsActive: %s suitsLured: %s suitTraps: %s toons: %s toonsJoining: %s toonsPending: %s toonsActive: %s toonsRunning: %s' % (suits, suitsJoining, suitsPending, suitsActive, suitsLured, suitTraps, toons, toonsJoining, toonsPending, toonsActive, toonsRunning))
        ts = globalClockDelta.localElapsedTime(timestamp)
        oldsuits = self.suits
        self.suits = []
        suitGone = 0
        for s in suits:
            if self.cr.doId2do.has_key(s):
                suit = self.cr.doId2do[s]
                suit.setState('Battle')
                self.suits.append(suit)
                
                try:
                    pass
                except:
                    suit.battleTrap = NO_TRAP
                    suit.battleTrapProp = None
                    suit.battleTrapIsFresh = 0

            else:
                self.notify.warning('setMembers() - no suit in repository: %d' % s)
                self.suits.append(None)
                suitGone = 1
        
        for s in oldsuits:
            if self.suits.count(s) == 0:
                self._DistributedBattleBase__removeSuit(s)
            
        
        for s in suitsJoining:
            suit = self.suits[int(s)]
            if suit != None and self.joiningSuits.count(suit) == 0:
                self._DistributedBattleBase__makeSuitJoin(suit, ts)
            
        
        for s in suitsPending:
            suit = self.suits[int(s)]
            if suit != None and self.pendingSuits.count(suit) == 0:
                self._DistributedBattleBase__makeSuitPending(suit)
            
        
        activeSuits = []
        for s in suitsActive:
            suit = self.suits[int(s)]
            if suit != None and self.activeSuits.count(suit) == 0:
                activeSuits.append(suit)
            
        
        oldLuredSuits = self.luredSuits
        self.luredSuits = []
        for s in suitsLured:
            suit = self.suits[int(s)]
            if suit != None:
                self.luredSuits.append(suit)
                if oldLuredSuits.count(suit) == 0:
                    self.needAdjustTownBattle = 1
                
            
        
        if self.needAdjustTownBattle == 0:
            for s in oldLuredSuits:
                if self.luredSuits.count(s) == 0:
                    self.needAdjustTownBattle = 1
                
            
        
        index = 0
        oldSuitTraps = self.suitTraps
        self.suitTraps = suitTraps
        for s in suitTraps:
            trapid = int(s)
            if trapid == 9:
                trapid = -1
            
            suit = self.suits[index]
            index += 1
            if suit != None:
                if (trapid == NO_TRAP or trapid != suit.battleTrap) and suit.battleTrapProp != None:
                    self.removeTrap(suit)
                
                if trapid != NO_TRAP and suit.battleTrapProp == None:
                    if self.fsm.getCurrentState().getName() != 'PlayMovie':
                        self.loadTrap(suit, trapid)
                    
                
            
        
        if len(oldSuitTraps) != len(self.suitTraps):
            self.needAdjustTownBattle = 1
        else:
            for i in range(len(oldSuitTraps)):
                if oldSuitTraps[i] == '9' and self.suitTraps[i] != '9' and oldSuitTraps[i] != '9' and self.suitTraps[i] == '9':
                    self.needAdjustTownBattle = 1
                    break
                
            
        if suitGone:
            validSuits = []
            for s in self.suits:
                if s != None:
                    validSuits.append(s)
                
            
            self.suits = validSuits
            self.needAdjustTownBattle = 1
        
        oldtoons = self.toons
        self.toons = []
        toonGone = 0
        for t in toons:
            toon = self.getToon(t)
            if toon == None:
                self.notify.warning('setMembers() - toon not in tcr!')
                self.toons.append(None)
                toonGone = 1
                continue
            
            self.toons.append(toon)
            if oldtoons.count(toon) == 0:
                self.notify.debug('setMembers() - add toon: %d' % toon.doId)
                self._DistributedBattleBase__listenForUnexpectedExit(toon)
                toon.stopLookAround()
                toon.stopSmooth()
            
        
        for t in oldtoons:
            if self.toons.count(t) == 0:
                if self._DistributedBattleBase__removeToon(t) == 1:
                    self.notify.debug('setMembers() - local toon left battle')
                    return []
                
            
        
        for t in toonsJoining:
            toon = self.toons[int(t)]
            if toon != None and self.joiningToons.count(toon) == 0:
                self._DistributedBattleBase__makeToonJoin(toon, toonsPending, ts)
            
        
        for t in toonsPending:
            toon = self.toons[int(t)]
            if toon != None and self.pendingToons.count(toon) == 0:
                self._DistributedBattleBase__makeToonPending(toon, ts)
            
        
        for t in toonsRunning:
            toon = self.toons[int(t)]
            if toon != None and self.runningToons.count(toon) == 0:
                self._DistributedBattleBase__makeToonRun(toon, ts)
            
        
        activeToons = []
        for t in toonsActive:
            toon = self.toons[int(t)]
            if toon != None and self.activeToons.count(toon) == 0:
                activeToons.append(toon)
            
        
        if len(activeSuits) > 0 or len(activeToons) > 0:
            self._DistributedBattleBase__makeAvsActive(activeSuits, activeToons)
        
        if toonGone == 1:
            validToons = []
            for toon in self.toons:
                if toon != None:
                    validToons.append(toon)
                
            
            self.toons = validToons
        
        if len(self.activeToons) > 0:
            self._DistributedBattleBase__requestAdjustTownBattle()
        
        currStateName = self.localToonFsm.getCurrentState().getName()
        if self.toons.count(toonbase.localToon):
            if oldtoons.count(toonbase.localToon) == 0:
                self.notify.debug('setMembers() - local toon just joined')
                if self.streetBattle == 1:
                    toonbase.tcr.playGame.getPlace().enterZone(self.zoneId)
                
                self.localToonJustJoined = 1
            
            if currStateName != 'HasLocalToon':
                self.localToonFsm.request('HasLocalToon')
            
        elif oldtoons.count(toonbase.localToon):
            self.notify.debug('setMembers() - local toon just ran')
        
        if currStateName != 'NoLocalToon':
            self.localToonFsm.request('NoLocalToon')
        
        return oldtoons

    
    def adjust(self, timestamp):
        self.notify.debug('adjust(%f) from server' % globalClockDelta.localElapsedTime(timestamp))
        self.adjustFsm.request('Adjusting', [
            globalClockDelta.localElapsedTime(timestamp)])

    
    def setMovie(self, active, toons, suits, id0, tr0, le0, tg0, hp0, ac0, hpb0, kbb0, died0, id1, tr1, le1, tg1, hp1, ac1, hpb1, kbb1, died1, id2, tr2, le2, tg2, hp2, ac2, hpb2, kbb2, died2, id3, tr3, le3, tg3, hp3, ac3, hpb3, kbb3, died3, sid0, at0, stg0, dm0, sd0, sb0, st0, sid1, at1, stg1, dm1, sd1, sb1, st1, sid2, at2, stg2, dm2, sd2, sb2, st2, sid3, at3, stg3, dm3, sd3, sb3, st3):
        self.notify.debug('setMovie()')
        if int(active) == 1:
            self.notify.debug('setMovie() - movie is active')
            self.movie.genAttackDicts(toons, suits, id0, tr0, le0, tg0, hp0, ac0, hpb0, kbb0, died0, id1, tr1, le1, tg1, hp1, ac1, hpb1, kbb1, died1, id2, tr2, le2, tg2, hp2, ac2, hpb2, kbb2, died2, id3, tr3, le3, tg3, hp3, ac3, hpb3, kbb3, died3, sid0, at0, stg0, dm0, sd0, sb0, st0, sid1, at1, stg1, dm1, sd1, sb1, st1, sid2, at2, stg2, dm2, sd2, sb2, st2, sid3, at3, stg3, dm3, sd3, sb3, st3)
        

    
    def setChosenToonAttacks(self, ids, tracks, levels, targets):
        self.notify.debug('setChosenToonAttacks() - (%s), (%s), (%s), (%s)' % (ids, tracks, levels, targets))
        toonIndices = []
        targetIndices = []
        unAttack = 0
        localToonInList = 0
        for i in range(len(ids)):
            track = tracks[i]
            level = levels[i]
            toon = self.findToon(ids[i])
            if toon == None:
                self.notify.warning('setChosenToonAttacks() - toon gone: %d!' % ids[i])
                continue
            
            if self.activeToons.count(toon) == 0:
                self.notify.warning('setChosenToonAttacks() - toon not in battle: %d!' % ids[i])
                continue
            
            if toon == toonbase.localToon:
                localToonInList = 1
            
            toonIndices.append(self.activeToons.index(toon))
            if track == SOS:
                targetIndex = -1
            elif track == PASS:
                targetIndex = -1
                tracks[i] = NO_ATTACK
            elif attackAffectsGroup(track, level):
                targetIndex = -1
            elif track == HEAL:
                target = self.findToon(targets[i])
                targetIndex = self.activeToons.index(target)
            elif track == UN_ATTACK:
                targetIndex = -1
                tracks[i] = NO_ATTACK
                if toon == toonbase.localToon:
                    unAttack = 1
                    self.choseAttackAlready = 0
                
            elif track == NO_ATTACK:
                targetIndex = -1
            else:
                target = self.findSuit(targets[i])
                if target != None and self.activeSuits.count(target) != 0:
                    targetIndex = self.activeSuits.index(target)
                else:
                    targetIndex = -1
            targetIndices.append(targetIndex)
        
        for i in range(4 - len(ids)):
            toonIndices.append(-1)
            tracks.append(-1)
            levels.append(-1)
            targetIndices.append(-1)
        
        self.townBattleAttacks = (toonIndices, tracks, levels, targetIndices)
        if self.localToonActive() and localToonInList == 1:
            if unAttack == 1 and self.fsm.getCurrentState().getName() == 'WaitForInput':
                if self.townBattle.fsm.getCurrentState().getName() != 'Attack':
                    self.townBattle.setState('Attack')
                
            
            self.townBattle.updateChosenAttacks(self.townBattleAttacks[0], self.townBattleAttacks[1], self.townBattleAttacks[2], self.townBattleAttacks[3])
        

    
    def setBattleExperience(self, id0, origExp0, earnedExp0, items0, missedItems0, id1, origExp1, earnedExp1, items1, missedItems1, id2, origExp2, earnedExp2, items2, missedItems2, id3, origExp3, earnedExp3, items3, missedItems3, deathList):
        self.movie.genRewardDicts(id0, origExp0, earnedExp0, items0, missedItems0, id1, origExp1, earnedExp1, items1, missedItems1, id2, origExp2, earnedExp2, items2, missedItems2, id3, origExp3, earnedExp3, items3, missedItems3, deathList)

    
    def _DistributedBattleBase__listenForUnexpectedExit(self, toon):
        self.accept(toon.uniqueName('disable'), self._DistributedBattleBase__handleUnexpectedExit, extraArgs = [
            toon])

    
    def _DistributedBattleBase__handleUnexpectedExit(self, toon):
        self.notify.warning('handleUnexpectedExit() - toon: %d' % toon.doId)
        self._DistributedBattleBase__removeToon(toon, unexpected = 1)

    
    def delayDeleteToons(self):
        toonsKeep = []
        for t in self.toons:
            toonsKeep.append(DelayDelete.DelayDelete(t))
        
        self.toonsKeep = toonsKeep

    
    def _DistributedBattleBase__removeSuit(self, suit):
        self.notify.debug('__removeSuit(%d)' % suit.doId)
        if self.suits.count(suit) != 0:
            self.suits.remove(suit)
        
        if self.joiningSuits.count(suit) != 0:
            self.joiningSuits.remove(suit)
        
        if self.pendingSuits.count(suit) != 0:
            self.pendingSuits.remove(suit)
        
        if self.activeSuits.count(suit) != 0:
            self.activeSuits.remove(suit)
        
        self.suitGone = 1
        if suit.battleTrap != NO_TRAP:
            self.removeTrap(suit)
        
        del suit.battleTrap
        del suit.battleTrapProp
        del suit.battleTrapIsFresh

    
    def _DistributedBattleBase__removeToon(self, toon, unexpected = 0):
        self.notify.debug('__removeToon(%d)' % toon.doId)
        self.exitedToons.append(toon)
        if self.toons.count(toon) != 0:
            self.toons.remove(toon)
        
        if self.joiningToons.count(toon) != 0:
            self.clearInterval(self.taskName('to-pending-toon-%d' % toon.doId))
            self.joiningToons.remove(toon)
        
        if self.pendingToons.count(toon) != 0:
            self.pendingToons.remove(toon)
        
        if self.activeToons.count(toon) != 0:
            self.activeToons.remove(toon)
        
        if self.runningToons.count(toon) != 0:
            self.clearInterval(self.taskName('running-%d' % toon.doId), finish = 1)
            self.runningToons.remove(toon)
        
        self.ignore(toon.uniqueName('disable'))
        self.toonGone = 1
        if toon == toonbase.localToon:
            self.removeLocalToon()
            self._DistributedBattleBase__teleportToSafeZone(toon)
            return 1
        
        return 0

    
    def removeLocalToon(self):
        if toonbase.tcr.playGame.getPlace() != None:
            toonbase.tcr.playGame.getPlace().setState('walk')
        
        self.localToonFsm.request('NoLocalToon')

    
    def removeInactiveLocalToon(self, toon):
        self.notify.debug('removeInactiveLocalToon(%d)' % toon.doId)
        self.exitedToons.append(toon)
        if self.toons.count(toon) != 0:
            self.toons.remove(toon)
        
        if self.joiningToons.count(toon) != 0:
            self.clearInterval(self.taskName('to-pending-toon-%d' % toon.doId), finish = 1)
            self.joiningToons.remove(toon)
        
        if self.pendingToons.count(toon) != 0:
            self.pendingToons.remove(toon)
        
        self.ignore(toon.uniqueName('disable'))
        toonbase.tcr.playGame.getPlace().setState('walk')
        self.localToonFsm.request('WaitForServer')

    
    def _DistributedBattleBase__createJoinInterval(self, av, destPos, destHpr, name, ts, callback, toon = 0):
        joinIvals = []
        joinIvals.append(Func(Emote.DisableAll, av, 'dbattlebase, createJoinInterval'))
        avPos = av.getPos(self)
        plist = self.buildJoinPointList(avPos, destPos, toon)
        if len(plist) == 0:
            joinIvals.append(FunctionInterval(av.headsUp, extraArgs = [
                self,
                destPos]))
            if toon == 0:
                timeToDest = self.calcSuitMoveTime(avPos, destPos)
                joinIvals.append(FunctionInterval(av.loop, extraArgs = [
                    'walk']))
            else:
                timeToDest = self.calcToonMoveTime(avPos, destPos)
                joinIvals.append(FunctionInterval(av.loop, extraArgs = [
                    'run']))
            if timeToDest > BATTLE_SMALL_VALUE:
                joinIvals.append(LerpPosInterval(av, timeToDest, destPos, other = self))
                totalTime = timeToDest
            else:
                totalTime = 0
        else:
            timeToPerimeter = 0
            if toon == 0:
                timeToPerimeter = self.calcSuitMoveTime(plist[0], avPos)
                timePerSegment = 10.0 / BattleBase.suitSpeed
                timeToDest = self.calcSuitMoveTime(BattleBase.posA, destPos)
            else:
                timeToPerimeter = self.calcToonMoveTime(plist[0], avPos)
                timePerSegment = 10.0 / BattleBase.toonSpeed
                timeToDest = self.calcToonMoveTime(BattleBase.posE, destPos)
            totalTime = timeToPerimeter + (len(plist) - 1) * timePerSegment + timeToDest
            if totalTime > MAX_JOIN_T:
                self.notify.warning('__createJoinInterval() - time: %f' % totalTime)
            
            joinIvals.append(FunctionInterval(av.headsUp, extraArgs = [
                self,
                plist[0]]))
            if toon == 0:
                joinIvals.append(FunctionInterval(av.loop, extraArgs = [
                    'walk']))
            else:
                joinIvals.append(FunctionInterval(av.loop, extraArgs = [
                    'run']))
            joinIvals.append(LerpPosInterval(av, timeToPerimeter, plist[0], other = self))
            for p in plist[1:]:
                joinIvals.append(FunctionInterval(av.headsUp, extraArgs = [
                    self,
                    p]))
                joinIvals.append(LerpPosInterval(av, timePerSegment, p, other = self))
            
            joinIvals.append(FunctionInterval(av.headsUp, extraArgs = [
                self,
                destPos]))
            joinIvals.append(LerpPosInterval(av, timeToDest, destPos, other = self))
        joinIvals.append(FunctionInterval(av.loop, extraArgs = [
            'neutral']))
        joinIvals.append(FunctionInterval(av.headsUp, extraArgs = [
            self,
            Point3(0, 0, 0)]))
        tval = totalTime - ts
        if tval < 0:
            tval = totalTime
        
        joinIvals.append(Func(Emote.ReleaseAll, av, 'dbattlebase, createJoinInterval'))
        joinIvals.append(FunctionInterval(callback, extraArgs = [
            av,
            tval]))
        if av == toonbase.localToon:
            camIvals = []
            
            def setCamFov(fov):
                base.camLens.setFov(fov)

            camIvals.append(FunctionInterval(setCamFov, extraArgs = [
                self.camFov]))
            camIvals.append(FunctionInterval(camera.wrtReparentTo, extraArgs = [
                self]))
            camIvals.append(FunctionInterval(camera.setPos, extraArgs = [
                self.camJoinPos]))
            camIvals.append(FunctionInterval(camera.setHpr, extraArgs = [
                self.camJoinHpr]))
            camTrack = Track(camIvals)
            joinTrack = Track(joinIvals)
            return MultiTrack([
                joinTrack,
                camTrack], name = name)
        else:
            return Track(joinIvals, name = name)

    
    def _DistributedBattleBase__makeSuitJoin(self, suit, ts):
        self.notify.debug('__makeSuitJoin(%d)' % suit.doId)
        spotIndex = len(self.pendingSuits) + len(self.joiningSuits)
        self.joiningSuits.append(suit)
        suit.setState('Battle')
        openSpot = self.suitPendingPoints[spotIndex]
        pos = openSpot[0]
        hpr = VBase3(openSpot[1], 0.0, 0.0)
        trackName = self.taskName('to-pending-suit-%d' % suit.doId)
        track = self._DistributedBattleBase__createJoinInterval(suit, pos, hpr, trackName, ts, self._DistributedBattleBase__handleSuitJoinDone)
        track.start(ts)
        self.activeIntervals[trackName] = track

    
    def _DistributedBattleBase__handleSuitJoinDone(self, suit, ts):
        self.notify.debug('suit: %d is now pending' % suit.doId)
        if self.hasLocalToon():
            self.d_joinDone(toonbase.localToon.doId, suit.doId)
        

    
    def _DistributedBattleBase__makeSuitPending(self, suit):
        self.notify.debug('__makeSuitPending(%d)' % suit.doId)
        self.clearInterval(self.taskName('to-pending-suit-%d' % suit.doId), finish = 1)
        if self.joiningSuits.count(suit):
            self.joiningSuits.remove(suit)
        
        self.pendingSuits.append(suit)

    
    def _DistributedBattleBase__teleportToSafeZone(self, toon):
        self.notify.debug('teleportToSafeZone(%d)' % toon.doId)
        target_sz = ZoneUtil.getHoodId(self.zoneId)
        if toonbase.localToon.safeZonesVisited.count(target_sz) == 0:
            target_sz = toonbase.localToon.defaultZone
        
        toonbase.tcr.playGame.getPlace().fsm.request('teleportOut', [
            {
                'loader': ZoneUtil.getLoaderName(target_sz),
                'where': ZoneUtil.getWhereName(target_sz, 1),
                'how': 'teleportIn',
                'hoodId': target_sz,
                'zoneId': target_sz,
                'shardId': None,
                'avId': -1,
                'battle': 1 }])

    
    def _DistributedBattleBase__makeToonJoin(self, toon, pendingToons, ts):
        self.notify.debug('__makeToonJoin(%d)' % toon.doId)
        spotIndex = len(pendingToons) + len(self.joiningToons)
        self.joiningToons.append(toon)
        openSpot = self.toonPendingPoints[spotIndex]
        pos = openSpot[0]
        hpr = VBase3(openSpot[1], 0.0, 0.0)
        trackName = self.taskName('to-pending-toon-%d' % toon.doId)
        track = self._DistributedBattleBase__createJoinInterval(toon, pos, hpr, trackName, ts, self._DistributedBattleBase__handleToonJoinDone, toon = 1)
        if toon != toonbase.localToon:
            toon.animFSM.request('off')
        
        track.start(ts)
        self.activeIntervals[trackName] = track

    
    def _DistributedBattleBase__handleToonJoinDone(self, toon, ts):
        self.notify.debug('__handleToonJoinDone() - pending: %d' % toon.doId)
        if self.hasLocalToon():
            self.d_joinDone(toonbase.localToon.doId, toon.doId)
        

    
    def _DistributedBattleBase__makeToonPending(self, toon, ts):
        self.notify.debug('__makeToonPending(%d)' % toon.doId)
        self.clearInterval(self.taskName('to-pending-toon-%d' % toon.doId), finish = 1)
        if self.joiningToons.count(toon):
            self.joiningToons.remove(toon)
        
        self.pendingToons.append(toon)
        if toonbase.localToon == toon:
            currStateName = self.fsm.getCurrentState().getName()
        

    
    def _DistributedBattleBase__makeAvsActive(self, suits, toons):
        self.notify.debug('__makeAvsActive()')
        self._DistributedBattleBase__stopAdjusting()
        for s in suits:
            if self.joiningSuits.count(s):
                self.notify.warning('suit: %d was in joining list!' % s.doId)
                self.joiningSuits.remove(s)
            
            if self.pendingSuits.count(s):
                self.pendingSuits.remove(s)
            
            self.notify.debug('__makeAvsActive() - suit: %d' % s.doId)
            self.activeSuits.append(s)
        
        if len(self.activeSuits) >= 1:
            for suit in self.activeSuits:
                (suitPos, suitHpr) = self.getActorPosHpr(suit)
                if self.isSuitLured(suit) == 0:
                    suit.setPosHpr(self, suitPos, suitHpr)
                else:
                    spos = Point3(suitPos[0], suitPos[1] - MovieUtil.SUIT_LURE_DISTANCE, suitPos[2])
                    suit.setPosHpr(self, spos, suitHpr)
                suit.loop('neutral')
            
        
        for toon in toons:
            if self.joiningToons.count(toon):
                self.notify.warning('toon: %d was in joining list!' % toon.doId)
                self.joiningToons.remove(toon)
            
            if self.pendingToons.count(toon):
                self.pendingToons.remove(toon)
            
            self.notify.debug('__makeAvsActive() - toon: %d' % toon.doId)
            if self.activeToons.count(toon) == 0:
                self.activeToons.append(toon)
            else:
                self.notify.warning('makeAvsActive() - toon: %d is active!' % toon.doId)
        
        if len(self.activeToons) >= 1:
            for toon in self.activeToons:
                (toonPos, toonHpr) = self.getActorPosHpr(toon)
                toon.setPosHpr(self, toonPos, toonHpr)
                toon.loop('neutral')
            
        
        if self.fsm.getCurrentState().getName() == 'WaitForInput' and self.localToonActive() and self.localToonJustJoined == 1:
            self.notify.debug('makeAvsActive() - local toon just joined')
            self._DistributedBattleBase__enterLocalToonWaitForInput()
            self.localToonJustJoined = 0
            self.startTimer()
        

    
    def _DistributedBattleBase__makeToonRun(self, toon, ts):
        self.notify.debug('__makeToonRun(%d)' % toon.doId)
        if self.activeToons.count(toon):
            self.activeToons.remove(toon)
        
        self.runningToons.append(toon)
        self.toonGone = 1
        self._DistributedBattleBase__stopTimer()
        if self.localToonRunning():
            self.townBattle.setState('Off')
        
        runMTrack = MovieUtil.getToonTeleportOutInterval(toon)
        runName = self.taskName('running-%d' % toon.doId)
        self.notify.debug('duration: %f' % runMTrack.getDuration())
        runMTrack.start(ts)
        self.activeIntervals[runName] = runMTrack

    
    def getToon(self, toonId):
        if self.cr.doId2do.has_key(toonId):
            return self.cr.doId2do[toonId]
        else:
            self.notify.warning('getToon() - toon: %d not in repository!' % toonId)
            return None

    
    def d_toonRequestJoin(self, toonId, pos):
        self.notify.debug('network:toonRequestJoin()')
        self.sendUpdate('toonRequestJoin', [
            pos[0],
            pos[1],
            pos[2]])

    
    def d_toonRequestRun(self, toonId):
        self.notify.debug('network:toonRequestRun()')
        self.sendUpdate('toonRequestRun', [])

    
    def d_faceOffDone(self, toonId):
        self.notify.debug('network:faceOffDone()')
        self.sendUpdate('faceOffDone', [])

    
    def d_adjustDone(self, toonId):
        self.notify.debug('network:adjustDone()')
        self.sendUpdate('adjustDone', [])

    
    def d_timeout(self, toonId):
        self.notify.debug('network:timeout()')
        self.sendUpdate('timeout', [])

    
    def d_movieDone(self, toonId):
        self.notify.debug('network:movieDone()')
        self.sendUpdate('movieDone', [])

    
    def d_rewardDone(self, toonId):
        self.notify.debug('network:rewardDone()')
        self.sendUpdate('rewardDone', [])

    
    def d_joinDone(self, toonId, avId):
        self.notify.debug('network:joinDone(%d)' % avId)
        self.sendUpdate('joinDone', [
            avId])

    
    def d_requestAttack(self, toonId, track, level, av):
        self.notify.debug('network:requestAttack(%d, %d, %d)' % (track, level, av))
        self.sendUpdate('requestAttack', [
            track,
            level,
            av])

    
    def enterOff(self, ts = 0):
        return None

    
    def exitOff(self):
        return None

    
    def enterWaitForJoin(self, ts = 0):
        self.notify.debug('enterWaitForJoin()')
        return None

    
    def exitWaitForJoin(self):
        return None

    
    def _DistributedBattleBase__enterLocalToonWaitForInput(self):
        self.notify.debug('enterLocalToonWaitForInput()')
        camera.setPosHpr(self.camPos, self.camHpr)
        base.camLens.setFov(self.camMenuFov)
        NametagGlobals.setMasterArrowsOn(0)
        self.townBattle.setState('Attack')
        self.accept(self.localToonBattleEvent, self._DistributedBattleBase__handleLocalToonBattleEvent)

    
    def startTimer(self, ts = 0):
        self.notify.debug('startTimer()')
        if ts >= CLIENT_INPUT_TIMEOUT:
            self.notify.warning('startTimer() - ts: %f timeout: %f' % (ts, CLIENT_INPUT_TIMEOUT))
            self._DistributedBattleBase__timedOut()
            return None
        
        self.timer.startCallback(CLIENT_INPUT_TIMEOUT - ts, self._DistributedBattleBase__timedOut)
        timeTask = Task.loop(Task.Task(self._DistributedBattleBase__countdown), Task.pause(0.20000000000000001))
        taskMgr.add(timeTask, self.timerCountdownTaskName)

    
    def _DistributedBattleBase__stopTimer(self):
        self.notify.debug('__stopTimer()')
        self.timer.stop()
        taskMgr.remove(self.timerCountdownTaskName)

    
    def _DistributedBattleBase__countdown(self, task):
        self.townBattle.updateTimer(int(self.timer.getT()))
        return Task.done

    
    def enterWaitForInput(self, ts = 0):
        self.notify.debug('enterWaitForInput()')
        self.choseAttackAlready = 0
        if self.localToonActive():
            self._DistributedBattleBase__enterLocalToonWaitForInput()
            self.startTimer(ts)
        
        if self.needAdjustTownBattle == 1:
            self._DistributedBattleBase__adjustTownBattle()
        
        return None

    
    def exitWaitForInput(self):
        self.notify.debug('exitWaitForInput()')
        if self.localToonActive():
            self.townBattle.setState('Off')
            base.camLens.setFov(self.camFov)
            self.ignore(self.localToonBattleEvent)
            self._DistributedBattleBase__stopTimer()
        
        return None

    
    def _DistributedBattleBase__handleLocalToonBattleEvent(self, response):
        mode = response['mode']
        noAttack = 0
        if mode == 'Attack':
            self.notify.debug('got an attack')
            track = response['track']
            level = response['level']
            target = response['target']
            targetId = target
            if track == HEAL and not levelAffectsGroup(level):
                if target >= 0 and target < len(self.activeToons):
                    targetId = self.activeToons[target].doId
                else:
                    self.notify.warning('invalid toon target: %d' % target)
                    track = -1
                    level = -1
                    targetId = -1
            elif track == HEAL and len(self.activeToons) == 1:
                self.notify.warning('invalid group target for heal')
                track = -1
                level = -1
            elif not attackAffectsGroup(track, level):
                if target >= 0 and target < len(self.activeSuits):
                    targetId = self.activeSuits[target].doId
                else:
                    target = -1
            
            if len(self.luredSuits) > 0:
                if track == TRAP and track == LURE and not levelAffectsGroup(level):
                    if target != -1:
                        suit = self.findSuit(targetId)
                        if self.luredSuits.count(suit) != 0:
                            self.notify.warning('Suit: %d was lured!' % targetId)
                            track = -1
                            level = -1
                            targetId = -1
                        
                    
                elif track == LURE:
                    if levelAffectsGroup(level) and len(self.activeSuits) == len(self.luredSuits):
                        self.notify.warning('All suits are lured!')
                        track = -1
                        level = -1
                        targetId = -1
                    
                
            
            if track == TRAP:
                if target != -1:
                    suit = self.findSuit(targetId)
                    if suit.battleTrap != NO_TRAP:
                        self.notify.warning('Suit: %d was already trapped!' % targetId)
                        track = -1
                        level = -1
                        targetId = -1
                    
                
            
            self.d_requestAttack(toonbase.localToon.doId, track, level, targetId)
        elif mode == 'Run':
            self.notify.debug('got a run')
            self.d_toonRequestRun(toonbase.localToon.doId)
        elif mode == 'SOS':
            targetId = response['id']
            self.notify.debug('got an SOS for friend: %d' % targetId)
            self.d_requestAttack(toonbase.localToon.doId, SOS, -1, targetId)
        elif mode == 'Pass':
            targetId = response['id']
            self.notify.debug('got a Pass')
            self.d_requestAttack(toonbase.localToon.doId, PASS, -1, -1)
        elif mode == 'UnAttack':
            self.d_requestAttack(toonbase.localToon.doId, UN_ATTACK, -1, -1)
            noAttack = 1
        else:
            self.notify.warning('unknown battle response')
            return None
        if noAttack == 1:
            self.choseAttackAlready = 0
        else:
            self.choseAttackAlready = 1

    
    def _DistributedBattleBase__timedOut(self):
        if self.choseAttackAlready == 1:
            return None
        
        self.notify.debug('WaitForInput timed out')
        if self.localToonActive():
            self.notify.debug('battle timed out')
            self.d_timeout(toonbase.localToon.doId)
        

    
    def enterMakeMovie(self, ts = 0):
        self.notify.debug('enterMakeMovie()')
        return None

    
    def exitMakeMovie(self):
        return None

    
    def enterPlayMovie(self, ts):
        self.notify.debug('enterPlayMovie()')
        self.delayDeleteToons()
        if self.hasLocalToon():
            NametagGlobals.setMasterArrowsOn(0)
        
        self.movie.play(ts, self._DistributedBattleBase__handleMovieDone)
        return None

    
    def _DistributedBattleBase__handleMovieDone(self):
        self.notify.debug('__handleMovieDone()')
        if self.hasLocalToon():
            self.d_movieDone(toonbase.localToon.doId)
        
        self.movie.reset()

    
    def exitPlayMovie(self):
        self.notify.debug('exitPlayMovie()')
        self.toonsKeep = None
        self.movie.reset(finish = 1)
        self.townBattleAttacks = ([
            -1,
            -1,
            -1,
            -1], [
            -1,
            -1,
            -1,
            -1], [
            -1,
            -1,
            -1,
            -1], [
            0,
            0,
            0,
            0])
        return None

    
    def hasLocalToon(self):
        return self.toons.count(toonbase.localToon) > 0

    
    def localToonPendingOrActive(self):
        if not self.pendingToons.count(toonbase.localToon) > 0:
            pass
        return self.activeToons.count(toonbase.localToon) > 0

    
    def localToonActive(self):
        return self.activeToons.count(toonbase.localToon) > 0

    
    def localToonActiveOrRunning(self):
        if not self.activeToons.count(toonbase.localToon) > 0:
            pass
        return self.runningToons.count(toonbase.localToon) > 0

    
    def localToonRunning(self):
        return self.runningToons.count(toonbase.localToon) > 0

    
    def enterHasLocalToon(self):
        self.notify.debug('enterHasLocalToon()')
        toonbase.tcr.playGame.getPlace().setState('battle', self.localToonBattleEvent)
        camera.wrtReparentTo(self)
        base.camLens.setFov(self.camFov)
        return None

    
    def exitHasLocalToon(self):
        self.ignore(self.localToonBattleEvent)
        self._DistributedBattleBase__stopTimer()
        camera.wrtReparentTo(toonbase.localToon)
        base.camLens.setFov(DefaultCameraFov)
        return None

    
    def enterNoLocalToon(self):
        self.notify.debug('enterNoLocalToon()')
        return None

    
    def exitNoLocalToon(self):
        return None

    
    def enterWaitForServer(self):
        self.notify.debug('enterWaitForServer()')
        return None

    
    def exitWaitForServer(self):
        return None

    
    def createAdjustInterval(self, av, destPos, destHpr, toon = 0, run = 0):
        if run == 1:
            adjustTime = self.calcToonMoveTime(destPos, av.getPos(self))
        else:
            adjustTime = self.calcSuitMoveTime(destPos, av.getPos(self))
        self.notify.debug('creating adjust interval for: %d' % av.doId)
        adjustIvals = []
        if run == 1:
            adjustIvals.append(FunctionInterval(av.loop, extraArgs = [
                'run']))
        else:
            adjustIvals.append(FunctionInterval(av.loop, extraArgs = [
                'walk']))
        adjustIvals.append(FunctionInterval(av.headsUp, extraArgs = [
            self,
            destPos]))
        adjustIvals.append(LerpPosInterval(av, adjustTime, destPos, other = self))
        adjustIvals.append(FunctionInterval(av.setHpr, extraArgs = [
            self,
            destHpr]))
        adjustIvals.append(FunctionInterval(av.loop, extraArgs = [
            'neutral']))
        return Track(adjustIvals)

    
    def _DistributedBattleBase__adjust(self, ts, callback):
        self.notify.debug('__adjust(%f)' % ts)
        adjustIvals = []
        if len(self.pendingSuits) > 0 or self.suitGone == 1:
            self.suitGone = 0
            numSuits = len(self.pendingSuits) + len(self.activeSuits) - 1
            index = 0
            for suit in self.activeSuits:
                point = self.suitPoints[numSuits][index]
                pos = suit.getPos(self)
                destPos = point[0]
                if self.isSuitLured(suit) == 1:
                    destPos = Point3(destPos[0], destPos[1] - MovieUtil.SUIT_LURE_DISTANCE, destPos[2])
                
                if pos != destPos:
                    destHpr = VBase3(point[1], 0.0, 0.0)
                    adjustIvals.append(self.createAdjustInterval(suit, destPos, destHpr))
                
                index += 1
            
            for suit in self.pendingSuits:
                point = self.suitPoints[numSuits][index]
                destPos = point[0]
                destHpr = VBase3(point[1], 0.0, 0.0)
                adjustIvals.append(self.createAdjustInterval(suit, destPos, destHpr))
                index += 1
            
        
        if len(self.pendingToons) > 0 or self.toonGone == 1:
            self.toonGone = 0
            numToons = len(self.pendingToons) + len(self.activeToons) - 1
            index = 0
            for toon in self.activeToons:
                point = self.toonPoints[numToons][index]
                pos = toon.getPos(self)
                destPos = point[0]
                if pos != destPos:
                    destHpr = VBase3(point[1], 0.0, 0.0)
                    adjustIvals.append(self.createAdjustInterval(toon, destPos, destHpr))
                
                index += 1
            
            for toon in self.pendingToons:
                point = self.toonPoints[numToons][index]
                destPos = point[0]
                destHpr = VBase3(point[1], 0.0, 0.0)
                adjustIvals.append(self.createAdjustInterval(toon, destPos, destHpr))
                index += 1
            
        
        if len(adjustIvals) > 0:
            self.notify.debug('creating adjust multitrack')
            mtrack = MultiTrack(adjustIvals)
            e = FunctionInterval(self._DistributedBattleBase__handleAdjustDone)
            track = Track([
                mtrack,
                e], self.adjustName)
            self.activeIntervals[self.adjustName] = track
            track.start(ts)
        else:
            self.notify.warning('adjust() - nobody needed adjusting')
            self._DistributedBattleBase__adjustDone()

    
    def _DistributedBattleBase__handleAdjustDone(self):
        self.notify.debug('__handleAdjustDone() - client adjust finished')
        self.clearInterval(self.adjustName)
        self._DistributedBattleBase__adjustDone()

    
    def _DistributedBattleBase__stopAdjusting(self):
        self.notify.debug('__stopAdjusting()')
        self.clearInterval(self.adjustName)
        if self.adjustFsm.getCurrentState().getName() == 'Adjusting':
            self.adjustFsm.request('NotAdjusting')
        

    
    def _DistributedBattleBase__requestAdjustTownBattle(self):
        self.notify.debug('__requestAdjustTownBattle()')
        if self.fsm.getCurrentState().getName() == 'WaitForInput':
            self._DistributedBattleBase__adjustTownBattle()
        else:
            self.needAdjustTownBattle = 1

    
    def _DistributedBattleBase__adjustTownBattle(self):
        self.notify.debug('__adjustTownBattle()')
        if self.localToonActive() and len(self.activeSuits) > 0:
            self.notify.debug('__adjustTownBattle() - adjusting town battle')
            luredSuits = []
            for suit in self.luredSuits:
                luredSuits.append(self.activeSuits.index(suit))
            
            trappedSuits = []
            for suit in self.activeSuits:
                if suit.battleTrap != NO_TRAP:
                    trappedSuits.append(self.activeSuits.index(suit))
                
            
            self.townBattle.adjustCogsAndToons(self.activeSuits, luredSuits, trappedSuits, self.activeToons)
            if hasattr(self, 'townBattleAttacks'):
                self.townBattle.updateChosenAttacks(self.townBattleAttacks[0], self.townBattleAttacks[1], self.townBattleAttacks[2], self.townBattleAttacks[3])
            
        
        self.needAdjustTownBattle = 0

    
    def _DistributedBattleBase__adjustDone(self):
        self.notify.debug('__adjustDone()')
        if self.hasLocalToon():
            self.d_adjustDone(toonbase.localToon.doId)
        
        self.adjustFsm.request('NotAdjusting')

    
    def enterAdjusting(self, ts):
        self.notify.debug('enterAdjusting()')
        if self.localToonActive():
            self._DistributedBattleBase__stopTimer()
        
        self.delayDeleteToons()
        self._DistributedBattleBase__adjust(ts, self._DistributedBattleBase__handleAdjustDone)
        return None

    
    def exitAdjusting(self):
        self.notify.debug('exitAdjusting()')
        self.toonsKeep = None
        self.finishInterval(self.adjustName)
        currStateName = self.fsm.getCurrentState().getName()
        if currStateName == 'WaitForInput' and self.localToonActive():
            self.startTimer()
        
        return None

    
    def enterNotAdjusting(self):
        self.notify.debug('enterNotAdjusting()')
        return None

    
    def exitNotAdjusting(self):
        return None

    
    def visualize(self):
        
        try:
            pass
        except:
            self.isVisualized = 0

        if self.isVisualized:
            self.vis.removeNode()
            del self.vis
            self.reparentTo(hidden)
            self.isVisualized = 0
        else:
            lsegs = LineSegs()
            lsegs.setColor(0.5, 0.5, 1, 1)
            lsegs.moveTo(0, 0, 0)
            for p in BattleBase.allPoints:
                lsegs.drawTo(p[0], p[1], p[2])
            
            p = BattleBase.allPoints[0]
            lsegs.drawTo(p[0], p[1], p[2])
            self.vis = self.attachNewNode(lsegs.create())
            self.reparentTo(render)
            self.isVisualized = 1


