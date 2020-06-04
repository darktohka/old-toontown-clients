# File: D (Python 2.2)

from PandaModules import *
from IntervalGlobal import *
from BattleBase import *
import DistributedBattle
import DirectNotifyGlobal
import Emote
import SuitBattleGlobals
import whrandom
import AvatarDNA
import State
import FSM
import ToontownGlobals

class DistributedBattleFactory(DistributedBattle.DistributedBattle):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedBattleFactory')
    
    def __init__(self, cr):
        DistributedBattle.DistributedBattle.__init__(self, cr)
        self.factoryRequest = None
        self.factoryBattle = 1
        self.fsm.addState(State.State('FactoryReward', self.enterFactoryReward, self.exitFactoryReward, [
            'Resume']))
        offState = self.fsm.getStateNamed('Off')
        offState.addTransition('FactoryReward')
        playMovieState = self.fsm.getStateNamed('PlayMovie')
        playMovieState.addTransition('FactoryReward')

    
    def setFactoryDoId(self, factoryDoId):
        self.factoryDoId = factoryDoId

    
    def setBattleCellId(self, battleCellId):
        self.battleCellId = battleCellId
        
        def doPlacement(factoryList, self = self):
            self.factoryRequest = None
            self.factory = factoryList[0]
            spec = self.factory.getBattleCellSpec(self.battleCellId)
            self.factory.requestReparent(self, spec['parentEntId'])
            self.setPos(spec['pos'])
            print 'spec = %s' % spec
            print 'h = %s' % spec.get('h')
            self.wrtReparentTo(render)

        factory = toonbase.tcr.doId2do.get(self.factoryDoId)
        if factory is None:
            self.notify.warning('factory %s not in doId2do yet, battle %s will be mispositioned.' % self.factoryDoId, self.doId)
            self.factoryRequest = self.cr.relatedObjectMgr.requestObjects([
                self.factoryDoId], doPlacement)
        else:
            doPlacement([
                factory])

    
    def setPosition(self, *args):
        pass

    
    def setInitialSuitPos(self, x, y, z):
        self.initialSuitPos = Point3(x, y, z)

    
    def announceGenerate(self):
        DistributedBattle.DistributedBattle.announceGenerate(self)

    
    def disable(self):
        if self.hasLocalToon():
            self.unlockFactoryViz()
        
        if self.factoryRequest is not None:
            self.cr.relatedObjectMgr.abortRequest(self.factoryRequest)
            self.factoryRequest = None
        
        DistributedBattle.DistributedBattle.disable(self)

    
    def delete(self):
        self.ignoreAll()
        DistributedBattle.DistributedBattle.delete(self)

    
    def handleBattleBlockerCollision(self):
        messenger.send(self.getCollisionName(), [
            None])

    
    def lockFactoryViz(self):
        factory = toonbase.tcr.doId2do.get(self.factoryDoId)
        if factory:
            factory.lockVisibility(zoneId = self.zoneId)
        else:
            self.notify.warning("lockFactoryViz: couldn't find factory %s" % self.factoryDoId)

    
    def unlockFactoryViz(self):
        factory = toonbase.tcr.doId2do.get(self.factoryDoId)
        if factory:
            factory.unlockVisibility()
        else:
            self.notify.warning("unlockFactoryViz: couldn't find factory %s" % self.factoryDoId)

    
    def onWaitingForJoin(self):
        self.lockFactoryViz()

    
    def _DistributedBattleFactory__faceOff(self, ts, name, callback):
        toon = self.toons[0]
        point = self.toonPoints[0][0]
        toonPos = point[0]
        toonHpr = VBase3(point[1], 0.0, 0.0)
        p = toon.getPos(self)
        toon.setPos(self, p[0], p[1], 0.0)
        toon.setShadowHeight(0)
        if len(self.suits) == 1:
            leaderIndex = 0
        elif self.bossBattle == 1:
            for suit in self.suits:
                if suit.boss:
                    leaderIndex = self.suits.index(suit)
                    break
                
            
        else:
            maxTypeNum = -1
            for suit in self.suits:
                suitTypeNum = AvatarDNA.getSuitType(suit.dna.name)
                if maxTypeNum < suitTypeNum:
                    maxTypeNum = suitTypeNum
                    leaderIndex = self.suits.index(suit)
                
            
        delay = FACEOFF_TAUNT_T
        suitTrack = Parallel()
        suitLeader = None
        for suit in self.suits:
            suit.setState('Battle')
            suitIsLeader = 0
            oneSuitTrack = Sequence()
            oneSuitTrack.append(Func(suit.loop, 'neutral'))
            oneSuitTrack.append(Func(suit.headsUp, toonPos))
            if self.suits.index(suit) == leaderIndex:
                suitLeader = suit
                suitIsLeader = 1
                if self.bossBattle == 1:
                    if suit.boss:
                        taunt = Localizer.FactoryBossTaunt
                    else:
                        taunt = Localizer.FactoryBossBattleTaunt
                else:
                    taunt = SuitBattleGlobals.getFaceoffTaunt(suit.getStyleName(), suit.doId)
                oneSuitTrack.append(Func(suit.setChatAbsolute, taunt, CFSpeech | CFTimeout))
            
            (destPos, destHpr) = self.getActorPosHpr(suit, self.suits)
            oneSuitTrack.append(Wait(delay))
            if suitIsLeader == 1:
                oneSuitTrack.append(Func(suit.clearChat))
            
            oneSuitTrack.append(self.createAdjustInterval(suit, destPos, destHpr))
            suitTrack.append(oneSuitTrack)
        
        suitHeight = suitLeader.getHeight()
        suitOffsetPnt = Point3(0, 0, suitHeight)
        toonTrack = Parallel()
        for toon in self.toons:
            oneToonTrack = Sequence()
            (destPos, destHpr) = self.getActorPosHpr(toon, self.toons)
            oneToonTrack.append(Wait(delay))
            oneToonTrack.append(self.createAdjustInterval(toon, destPos, destHpr, toon = 1, run = 1))
            toonTrack.append(oneToonTrack)
        
        if self.hasLocalToon():
            MidTauntCamHeight = suitHeight * 0.66000000000000003
            MidTauntCamHeightLim = suitHeight - 1.8
            if MidTauntCamHeight < MidTauntCamHeightLim:
                MidTauntCamHeight = MidTauntCamHeightLim
            
            TauntCamY = 18
            TauntCamX = 0
            TauntCamHeight = whrandom.choice((MidTauntCamHeight, 1, 11))
            camTrack = Sequence()
            camTrack.append(Func(camera.reparentTo, suitLeader))
            camTrack.append(Func(base.camLens.setFov, self.camFOFov))
            camTrack.append(Func(camera.setPos, TauntCamX, TauntCamY, TauntCamHeight))
            camTrack.append(Func(camera.lookAt, suitLeader, suitOffsetPnt))
            camTrack.append(Wait(delay))
            camTrack.append(Func(base.camLens.setFov, self.camFov))
            camTrack.append(Func(camera.wrtReparentTo, self))
            camTrack.append(Func(camera.setPos, self.camFOPos))
            camTrack.append(Func(camera.lookAt, suit))
        
        mtrack = Parallel(suitTrack, toonTrack)
        if self.hasLocalToon():
            NametagGlobals.setMasterArrowsOn(0)
            mtrack = Parallel(mtrack, camTrack)
        
        done = Func(callback)
        track = Sequence(mtrack, done, name = name)
        track.start(ts)
        self.activeIntervals[name] = track

    
    def enterFaceOff(self, ts):
        if len(self.toons) > 0 and toonbase.localToon == self.toons[0]:
            Emote.DisableAll(self.toons[0], 'dbattlebldg, enterFaceOff')
        
        self.delayDeleteMembers()
        self._DistributedBattleFactory__faceOff(ts, self.faceOffName, self._DistributedBattleFactory__handleFaceOffDone)

    
    def _DistributedBattleFactory__handleFaceOffDone(self):
        self.notify.debug('FaceOff done')
        self.d_faceOffDone(toonbase.localToon.doId)

    
    def exitFaceOff(self):
        self.notify.debug('exitFaceOff()')
        if len(self.toons) > 0 and toonbase.localToon == self.toons[0]:
            Emote.ReleaseAll(self.toons[0], 'dbattlebldg exitFaceOff')
        
        self.clearInterval(self.faceOffName)
        self.membersKeep = None

    
    def _DistributedBattleFactory__playReward(self, ts, callback):
        toonTracks = Parallel()
        for toon in self.toons:
            toonTracks.append(Sequence(Func(toon.loop, 'victory'), Wait(FLOOR_REWARD_TIMEOUT), Func(toon.loop, 'neutral')))
        
        name = self.uniqueName('floorReward')
        track = Sequence(toonTracks, Func(callback), name = name)
        camera.setPos(0, 0, 1)
        camera.setHpr(180, 10, 0)
        self.activeIntervals[name] = track
        track.start(ts)

    
    def enterReward(self, ts):
        self.notify.info('enterReward()')
        self.disableCollision()
        self.delayDeleteMembers()
        self._DistributedBattleFactory__playReward(ts, self._DistributedBattleFactory__handleFloorRewardDone)

    
    def _DistributedBattleFactory__handleFloorRewardDone(self):
        return None

    
    def exitReward(self):
        self.notify.info('exitReward()')
        self.clearInterval(self.uniqueName('floorReward'))
        self.membersKeep = None
        NametagGlobals.setMasterArrowsOn(1)
        for toon in self.toons:
            toon.startSmooth()
        

    
    def enterFactoryReward(self, ts):
        self.notify.info('enterFactoryReward()')
        self.disableCollision()
        self.delayDeleteMembers()
        if self.hasLocalToon():
            NametagGlobals.setMasterArrowsOn(0)
            if self.bossBattle:
                messenger.send('localToonConfrontedForeman')
            
        
        self.movie.playReward(ts, self.uniqueName('building-reward'), self._DistributedBattleFactory__handleFactoryRewardDone)

    
    def _DistributedBattleFactory__handleFactoryRewardDone(self):
        self.notify.info('Factory reward done')
        if self.hasLocalToon():
            self.d_rewardDone(toonbase.localToon.doId)
        
        self.movie.resetReward()
        self.fsm.request('Resume')

    
    def exitFactoryReward(self):
        self.notify.info('exitFactoryReward()')
        self.movie.resetReward(finish = 1)
        self.membersKeep = None
        NametagGlobals.setMasterArrowsOn(1)


