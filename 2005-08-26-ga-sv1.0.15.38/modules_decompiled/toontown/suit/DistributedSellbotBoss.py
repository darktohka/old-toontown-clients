# File: D (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from direct.interval.IntervalGlobal import *
from toontown.battle.BattleProps import *
from direct.distributed.ClockDelta import *
from direct.showbase.PythonUtil import Functor
from direct.gui.DirectGui import *
from direct.fsm import FSM
from direct.fsm import ClassicFSM
from direct.fsm import State
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import ToontownBattleGlobals
import DistributedBossCog
from toontown.toonbase import TTLocalizer
import SuitDNA
from toontown.toon import Toon
from toontown.battle import BattleBase
from direct.directutil import Mopath
from direct.distributed import DelayDelete
from direct.showutil import Rope
from toontown.battle import MovieToonVictory
from toontown.building import ElevatorUtils
from toontown.battle import RewardPanel
from toontown.toon import NPCToons
from direct.task import Task
import random
import math
from toontown.coghq import CogDisguiseGlobals
OneBossCog = None

class DistributedSellbotBoss(DistributedBossCog.DistributedBossCog, FSM.FSM):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedSellbotBoss')
    cageHeights = [
        100,
        81,
        63,
        44,
        25,
        18]
    
    def __init__(self, cr):
        DistributedBossCog.DistributedBossCog.__init__(self, cr)
        FSM.FSM.__init__(self, 'DistributedSellbotBoss')
        self.cagedToonNpcId = None
        self.doobers = []
        self.dooberRequest = None
        self.bossDamage = 0
        self.attackCode = None
        self.attackAvId = 0
        self.recoverRate = 0
        self.recoverStartTime = 0
        self.bossDamageMovie = None
        self.cagedToon = None
        self.cageShadow = None
        self.cageIndex = 0
        self.everThrownPie = 0
        self.battleThreeMusicTime = 0
        self.insidesANodePath = None
        self.insidesBNodePath = None
        self.rampA = None
        self.rampB = None
        self.rampC = None
        self.strafeInterval = None
        self.onscreenMessage = None
        self.bossMaxDamage = ToontownGlobals.SellbotBossMaxDamage

    
    def announceGenerate(self):
        global OneBossCog
        DistributedBossCog.DistributedBossCog.announceGenerate(self)
        self.setName(TTLocalizer.SellbotBossName)
        nameInfo = TTLocalizer.BossCogNameWithDept % {
            'name': self.name,
            'dept': SuitDNA.getDeptFullname(self.style.dept) }
        self.setDisplayName(nameInfo)
        self.cageDoorSfx = loader.loadSfx('phase_9/audio/sfx/CHQ_SOS_cage_door.mp3')
        self.cageLandSfx = loader.loadSfx('phase_9/audio/sfx/CHQ_SOS_cage_land.mp3')
        self.cageLowerSfx = loader.loadSfx('phase_9/audio/sfx/CHQ_SOS_cage_lower.mp3')
        self.piesRestockSfx = loader.loadSfx('phase_9/audio/sfx/CHQ_SOS_pies_restock.mp3')
        self.rampSlideSfx = loader.loadSfx('phase_9/audio/sfx/CHQ_VP_ramp_slide.mp3')
        self.strafeSfx = []
        for i in range(10):
            self.strafeSfx.append(loader.loadSfx('phase_3.5/audio/sfx/SA_shred.mp3'))
        
        render.setTag('pieCode', str(ToontownGlobals.PieCodeNotBossCog))
        insidesA = CollisionPolygon(Point3(4.0, -2.0, 5.0), Point3(-4.0, -2.0, 5.0), Point3(-4.0, -2.0, 0.5), Point3(4.0, -2.0, 0.5))
        insidesANode = CollisionNode('BossZap')
        insidesANode.addSolid(insidesA)
        insidesANode.setCollideMask(ToontownGlobals.PieBitmask | ToontownGlobals.WallBitmask)
        self.insidesANodePath = self.axle.attachNewNode(insidesANode)
        self.insidesANodePath.setTag('pieCode', str(ToontownGlobals.PieCodeBossInsides))
        self.insidesANodePath.stash()
        insidesB = CollisionPolygon(Point3(-4.0, 2.0, 5.0), Point3(4.0, 2.0, 5.0), Point3(4.0, 2.0, 0.5), Point3(-4.0, 2.0, 0.5))
        insidesBNode = CollisionNode('BossZap')
        insidesBNode.addSolid(insidesB)
        insidesBNode.setCollideMask(ToontownGlobals.PieBitmask | ToontownGlobals.WallBitmask)
        self.insidesBNodePath = self.axle.attachNewNode(insidesBNode)
        self.insidesBNodePath.setTag('pieCode', str(ToontownGlobals.PieCodeBossInsides))
        self.insidesBNodePath.stash()
        target = CollisionTube(0, -1, 4, 0, -1, 9, 3.5)
        targetNode = CollisionNode('BossZap')
        targetNode.addSolid(target)
        targetNode.setCollideMask(ToontownGlobals.PieBitmask)
        self.targetNodePath = self.pelvis.attachNewNode(targetNode)
        self.targetNodePath.setTag('pieCode', str(ToontownGlobals.PieCodeBossCog))
        shield = CollisionTube(0, 1, 4, 0, 1, 7, 3.5)
        shieldNode = CollisionNode('BossZap')
        shieldNode.addSolid(shield)
        shieldNode.setCollideMask(ToontownGlobals.PieBitmask | ToontownGlobals.CameraBitmask)
        shieldNodePath = self.pelvis.attachNewNode(shieldNode)
        disk = loader.loadModel('phase_9/models/char/bossCog-gearCollide')
        disk.find('**/+CollisionNode').setName('BossZap')
        disk.reparentTo(self.pelvis)
        disk.setZ(0.80000000000000004)
        self.loadEnvironment()
        self._DistributedSellbotBoss__makeCagedToon()
        self._DistributedSellbotBoss__loadMopaths()
        if OneBossCog != None:
            self.notify.warning('Multiple BossCogs visible.')
        
        OneBossCog = self

    
    def disable(self):
        global OneBossCog
        DistributedBossCog.DistributedBossCog.disable(self)
        self.request('Off')
        self.unloadEnvironment()
        self._DistributedSellbotBoss__unloadMopaths()
        self._DistributedSellbotBoss__cleanupCagedToon()
        self._DistributedSellbotBoss__clearOnscreenMessage()
        taskMgr.remove(self.uniqueName('PieAdvice'))
        self._DistributedSellbotBoss__cleanupStrafe()
        render.clearTag('pieCode')
        self.targetNodePath.detachNode()
        self.cr.relatedObjectMgr.abortRequest(self.dooberRequest)
        self.dooberRequest = None
        self.betweenBattleMusic.stop()
        self.promotionMusic.stop()
        self.stingMusic.stop()
        self.battleTwoMusic.stop()
        self.battleThreeMusic.stop()
        self.epilogueMusic.stop()
        if OneBossCog == self:
            OneBossCog = None
        

    
    def d_hitBoss(self, bossDamage):
        self.sendUpdate('hitBoss', [
            bossDamage])

    
    def d_hitBossInsides(self):
        self.sendUpdate('hitBossInsides', [])

    
    def d_hitToon(self, toonId):
        self.sendUpdate('hitToon', [
            toonId])

    
    def setCagedToonNpcId(self, npcId):
        self.cagedToonNpcId = npcId

    
    def gotToon(self, toon):
        stateName = self.state
        if stateName == 'Elevator':
            self.placeToonInElevator(toon)
        

    
    def setDooberIds(self, dooberIds):
        self.doobers = []
        self.cr.relatedObjectMgr.abortRequest(self.dooberRequest)
        self.dooberRequest = self.cr.relatedObjectMgr.requestObjects(dooberIds, allCallback = self._DistributedSellbotBoss__gotDoobers)

    
    def _DistributedSellbotBoss__gotDoobers(self, doobers):
        self.dooberRequest = None
        self.doobers = doobers

    
    def setBossDamage(self, bossDamage, recoverRate, timestamp):
        recoverStartTime = globalClockDelta.networkToLocalTime(timestamp)
        self.bossDamage = bossDamage
        self.recoverRate = recoverRate
        self.recoverStartTime = recoverStartTime
        taskName = 'RecoverBossDamage'
        taskMgr.remove(taskName)
        if self.bossDamageMovie:
            if self.bossDamage >= self.bossMaxDamage:
                self.bossDamageMovie.resumeUntil(self.bossDamageMovie.getDuration())
            else:
                self.bossDamageMovie.resumeUntil(self.bossDamage * self.bossDamageToMovie)
                if self.recoverRate:
                    taskMgr.add(self._DistributedSellbotBoss__recoverBossDamage, taskName)
                
        

    
    def getBossDamage(self):
        now = globalClock.getFrameTime()
        elapsed = now - self.recoverStartTime
        return max(self.bossDamage - self.recoverRate * elapsed / 60.0, 0)

    
    def _DistributedSellbotBoss__recoverBossDamage(self, task):
        self.bossDamageMovie.setT(self.getBossDamage() * self.bossDamageToMovie)
        return Task.cont

    
    def _DistributedSellbotBoss__makeCagedToon(self):
        if self.cagedToon:
            return None
        
        self.cagedToon = NPCToons.createLocalNPC(self.cagedToonNpcId)
        self.cagedToon.addActive()
        self.cagedToon.reparentTo(self.cage)
        self.cagedToon.setPosHpr(0, -2, 0, 180, 0, 0)
        self.cagedToon.loop('neutral')
        touch = CollisionPolygon(Point3(-3.0381999999999998, 3.0381999999999998, -1), Point3(3.0381999999999998, 3.0381999999999998, -1), Point3(3.0381999999999998, -3.0381999999999998, -1), Point3(-3.0381999999999998, -3.0381999999999998, -1))
        touchNode = CollisionNode('Cage')
        touchNode.setCollideMask(ToontownGlobals.WallBitmask)
        touchNode.addSolid(touch)
        self.cage.attachNewNode(touchNode)

    
    def _DistributedSellbotBoss__cleanupCagedToon(self):
        if self.cagedToon:
            self.cagedToon.removeActive()
            self.cagedToon.delete()
            self.cagedToon = None
        

    
    def _DistributedSellbotBoss__walkToonToPromotion(self, toonId, delay, mopath, track, delayDeletes):
        toon = base.cr.doId2do.get(toonId)
        if toon:
            destPos = toon.getPos()
            self.placeToonInElevator(toon)
            toon.wrtReparentTo(render)
            ival = Sequence(Wait(delay), Func(toon.suit.setPlayRate, 1, 'walk'), Func(toon.suit.loop, 'walk'), toon.posInterval(1, Point3(0, 90, 20)), ParallelEndTogether(MopathInterval(mopath, toon), toon.posInterval(2, destPos, blendType = 'noBlend')), Func(toon.suit.loop, 'neutral'))
            track.append(ival)
            delayDeletes.append(DelayDelete.DelayDelete(toon))
        

    
    def _DistributedSellbotBoss__walkDoober(self, suit, delay, turnPos, track, delayDeletes):
        turnPos = Point3(*turnPos)
        turnPosDown = Point3(*ToontownGlobals.SellbotBossDooberTurnPosDown)
        flyPos = Point3(*ToontownGlobals.SellbotBossDooberFlyPos)
        seq = Sequence(Func(suit.headsUp, turnPos), Wait(delay), Func(suit.loop, 'walk', 0), self._DistributedSellbotBoss__walkSuitToPoint(suit, suit.getPos(), turnPos), self._DistributedSellbotBoss__walkSuitToPoint(suit, turnPos, turnPosDown), self._DistributedSellbotBoss__walkSuitToPoint(suit, turnPosDown, flyPos), suit.beginSupaFlyMove(flyPos, 0, 'flyAway'), Func(suit.fsm.request, 'Off'))
        track.append(seq)
        delayDeletes.append(DelayDelete.DelayDelete(suit))

    
    def _DistributedSellbotBoss__walkSuitToPoint(self, node, fromPos, toPos):
        vector = Vec3(toPos - fromPos)
        distance = vector.length()
        time = distance / ToontownGlobals.SuitWalkSpeed * 1.8
        return Sequence(Func(node.setPos, fromPos), Func(node.headsUp, toPos), node.posInterval(time, toPos))

    
    def makeIntroductionMovie(self, delayDeletes):
        track = Parallel()
        camera.reparentTo(render)
        camera.setPosHpr(0, 25, 30, 0, 0, 0)
        localAvatar.setCameraFov(ToontownGlobals.CogHQCameraFov)
        dooberTrack = Parallel()
        if self.doobers:
            self._DistributedSellbotBoss__doobersToPromotionPosition(self.doobers[:4], self.battleANode)
            self._DistributedSellbotBoss__doobersToPromotionPosition(self.doobers[4:], self.battleBNode)
            turnPosA = ToontownGlobals.SellbotBossDooberTurnPosA
            turnPosB = ToontownGlobals.SellbotBossDooberTurnPosB
            self._DistributedSellbotBoss__walkDoober(self.doobers[0], 0, turnPosA, dooberTrack, delayDeletes)
            self._DistributedSellbotBoss__walkDoober(self.doobers[1], 4, turnPosA, dooberTrack, delayDeletes)
            self._DistributedSellbotBoss__walkDoober(self.doobers[2], 8, turnPosA, dooberTrack, delayDeletes)
            self._DistributedSellbotBoss__walkDoober(self.doobers[3], 12, turnPosA, dooberTrack, delayDeletes)
            self._DistributedSellbotBoss__walkDoober(self.doobers[7], 2, turnPosB, dooberTrack, delayDeletes)
            self._DistributedSellbotBoss__walkDoober(self.doobers[6], 6, turnPosB, dooberTrack, delayDeletes)
            self._DistributedSellbotBoss__walkDoober(self.doobers[5], 10, turnPosB, dooberTrack, delayDeletes)
            self._DistributedSellbotBoss__walkDoober(self.doobers[4], 14, turnPosB, dooberTrack, delayDeletes)
        
        toonTrack = Parallel()
        self._DistributedSellbotBoss__toonsToPromotionPosition(self.toonsA, self.battleANode)
        self._DistributedSellbotBoss__toonsToPromotionPosition(self.toonsB, self.battleBNode)
        delay = 0
        for toonId in self.toonsA:
            self._DistributedSellbotBoss__walkToonToPromotion(toonId, delay, self.toonsEnterA, toonTrack, delayDeletes)
            delay += 1
        
        for toonId in self.toonsB:
            self._DistributedSellbotBoss__walkToonToPromotion(toonId, delay, self.toonsEnterB, toonTrack, delayDeletes)
            delay += 1
        
        toonTrack.append(Sequence(Wait(delay), self.closeDoors))
        self.rampA.request('extended')
        self.rampB.request('extended')
        self.rampC.request('retracted')
        self.clearChat()
        self.cagedToon.clearChat()
        promoteDoobers = TTLocalizer.BossCogPromoteDoobers % SuitDNA.getDeptFullnameP(self.style.dept)
        doobersAway = TTLocalizer.BossCogDoobersAway[self.style.dept]
        welcomeToons = TTLocalizer.BossCogWelcomeToons
        promoteToons = TTLocalizer.BossCogPromoteToons % SuitDNA.getDeptFullnameP(self.style.dept)
        discoverToons = TTLocalizer.BossCogDiscoverToons
        attackToons = TTLocalizer.BossCogAttackToons
        interruptBoss = TTLocalizer.CagedToonInterruptBoss
        rescueQuery = TTLocalizer.CagedToonRescueQuery
        bossAnimTrack = Sequence(ActorInterval(self, 'Ff_speech', startTime = 2, duration = 10, loop = 1), ActorInterval(self, 'ltTurn2Wave', duration = 2), ActorInterval(self, 'wave', duration = 4, loop = 1), ActorInterval(self, 'ltTurn2Wave', startTime = 2, endTime = 0), ActorInterval(self, 'Ff_speech', duration = 7, loop = 1))
        track.append(bossAnimTrack)
        dialogTrack = Track((0, Parallel(camera.posHprInterval(8, Point3(-22, -100, 35), Point3(-10, -13, 0), blendType = 'easeInOut'), IndirectInterval(toonTrack, 0, 18))), (5.5999999999999996, Func(self.setChatAbsolute, promoteDoobers, CFSpeech)), (9, IndirectInterval(dooberTrack, 0, 9)), (10, Sequence(Func(self.clearChat), Func(camera.setPosHpr, -23.100000000000001, 15.699999999999999, 17.199999999999999, -160, -2.3999999999999999, 0))), (12, Func(self.setChatAbsolute, doobersAway, CFSpeech)), (16, Parallel(Func(self.clearChat), Func(camera.setPosHpr, -25, -99, 10, -14, 10, 0), IndirectInterval(dooberTrack, 14), IndirectInterval(toonTrack, 30))), (18, Func(self.setChatAbsolute, welcomeToons, CFSpeech)), (22, Func(self.setChatAbsolute, promoteToons, CFSpeech)), (22.199999999999999, Sequence(Func(self.cagedToon.nametag3d.setScale, 2), Func(self.cagedToon.setChatAbsolute, interruptBoss, CFSpeech), ActorInterval(self.cagedToon, 'wave'), Func(self.cagedToon.loop, 'neutral'))), (25, Sequence(Func(self.clearChat), Func(self.cagedToon.clearChat), Func(camera.setPosHpr, -12, -15, 27, -151, -15, 0), ActorInterval(self, 'Ff_lookRt'))), (27, Sequence(Func(self.cagedToon.setChatAbsolute, rescueQuery, CFSpeech), Func(camera.setPosHpr, -12, 48, 94, -26, 20, 0), ActorInterval(self.cagedToon, 'wave'), Func(self.cagedToon.loop, 'neutral'))), (31, Sequence(Func(camera.setPosHpr, -20, -35, 10, -88, 25, 0), Func(self.setChatAbsolute, discoverToons, CFSpeech), Func(self.cagedToon.nametag3d.setScale, 1), Func(self.cagedToon.clearChat), ActorInterval(self, 'turn2Fb'))), (34, Sequence(Func(self.clearChat), self.loseCogSuits(self.toonsA, self.battleANode, (0, 18, 5, -180, 0, 0)), self.loseCogSuits(self.toonsB, self.battleBNode, (0, 18, 5, -180, 0, 0)))), (37, Sequence(self.toonNormalEyes(self.involvedToons), Func(camera.setPosHpr, -23.399999999999999, -145.59999999999999, 44.0, -10.0, -12.5, 0), Func(self.loop, 'Fb_neutral'), Func(self.rampA.request, 'retract'), Func(self.rampB.request, 'retract'), Parallel(self.backupToonsToBattlePosition(self.toonsA, self.battleANode), self.backupToonsToBattlePosition(self.toonsB, self.battleBNode), Sequence(Wait(2), Func(self.setChatAbsolute, attackToons, CFSpeech))))))
        track.append(dialogTrack)
        return Sequence(Func(self.stickToonsToFloor), track, Func(self.unstickToons), name = self.uniqueName('Introduction'))

    
    def _DistributedSellbotBoss__makeRollToBattleTwoMovie(self):
        startPos = Point3(ToontownGlobals.SellbotBossBattleOnePosHpr[0], ToontownGlobals.SellbotBossBattleOnePosHpr[1], ToontownGlobals.SellbotBossBattleOnePosHpr[2])
        if self.arenaSide:
            topRampPos = Point3(*ToontownGlobals.SellbotBossTopRampPosB)
            topRampTurnPos = Point3(*ToontownGlobals.SellbotBossTopRampTurnPosB)
            p3Pos = Point3(*ToontownGlobals.SellbotBossP3PosB)
        else:
            topRampPos = Point3(*ToontownGlobals.SellbotBossTopRampPosA)
            topRampTurnPos = Point3(*ToontownGlobals.SellbotBossTopRampTurnPosA)
            p3Pos = Point3(*ToontownGlobals.SellbotBossP3PosA)
        battlePos = Point3(ToontownGlobals.SellbotBossBattleTwoPosHpr[0], ToontownGlobals.SellbotBossBattleTwoPosHpr[1], ToontownGlobals.SellbotBossBattleTwoPosHpr[2])
        battleHpr = VBase3(ToontownGlobals.SellbotBossBattleTwoPosHpr[3], ToontownGlobals.SellbotBossBattleTwoPosHpr[4], ToontownGlobals.SellbotBossBattleTwoPosHpr[5])
        bossTrack = Sequence()
        bossTrack.append(Func(self.getGeomNode().setH, 180))
        bossTrack.append(Func(self.loop, 'Fb_neutral'))
        (track, hpr) = self.rollBossToPoint(startPos, None, topRampPos, None, 0)
        bossTrack.append(track)
        (track, hpr) = self.rollBossToPoint(topRampPos, hpr, topRampTurnPos, None, 0)
        bossTrack.append(track)
        (track, hpr) = self.rollBossToPoint(topRampTurnPos, hpr, p3Pos, None, 0)
        bossTrack.append(track)
        (track, hpr) = self.rollBossToPoint(p3Pos, hpr, battlePos, None, 0)
        bossTrack.append(track)
        return Sequence(bossTrack, Func(self.getGeomNode().setH, 0), name = self.uniqueName('BattleTwo'))

    
    def makeEndOfBattleMovie(self, hasLocalToon):
        name = self.uniqueName('CageDrop')
        seq = Sequence(name = name)
        seq.append(Func(self.cage.setPos, self.cagePos[self.cageIndex]))
        if hasLocalToon:
            seq += [
                Func(camera.reparentTo, render),
                Func(camera.setPosHpr, self.cage, 0, -50, 0, 0, 0, 0),
                Func(localAvatar.setCameraFov, ToontownGlobals.CogHQCameraFov),
                Func(self.hide)]
        
        seq += [
            Wait(0.5),
            Parallel(self.cage.posInterval(1, self.cagePos[self.cageIndex + 1], blendType = 'easeInOut'), SoundInterval(self.cageLowerSfx, duration = 1)),
            Func(self.cagedToon.nametag3d.setScale, 2),
            Func(self.cagedToon.setChatAbsolute, TTLocalizer.CagedToonDrop[self.cageIndex], CFSpeech),
            Wait(3),
            Func(self.cagedToon.nametag3d.setScale, 1),
            Func(self.cagedToon.clearChat)]
        if hasLocalToon:
            seq += [
                Func(self.show),
                Func(camera.reparentTo, localAvatar),
                Func(camera.setPos, localAvatar.cameraPositions[0][0]),
                Func(camera.setHpr, 0, 0, 0)]
        
        self.cageIndex += 1
        return seq

    
    def _DistributedSellbotBoss__makeBossDamageMovie(self):
        startPos = Point3(ToontownGlobals.SellbotBossBattleTwoPosHpr[0], ToontownGlobals.SellbotBossBattleTwoPosHpr[1], ToontownGlobals.SellbotBossBattleTwoPosHpr[2])
        startHpr = Point3(*ToontownGlobals.SellbotBossBattleThreeHpr)
        bottomPos = Point3(*ToontownGlobals.SellbotBossBottomPos)
        deathPos = Point3(*ToontownGlobals.SellbotBossDeathPos)
        self.setPosHpr(startPos, startHpr)
        bossTrack = Sequence()
        bossTrack.append(Func(self.loop, 'Fb_neutral'))
        (track, hpr) = self.rollBossToPoint(startPos, startHpr, bottomPos, None, 1)
        bossTrack.append(track)
        (track, hpr) = self.rollBossToPoint(bottomPos, startHpr, deathPos, None, 1)
        bossTrack.append(track)
        duration = bossTrack.getDuration()
        return bossTrack

    
    def _DistributedSellbotBoss__talkAboutPromotion(self, speech):
        if self.prevCogSuitLevel < ToontownGlobals.MaxCogSuitLevel:
            speech += TTLocalizer.CagedToonPromotion
            newCogSuitLevel = localAvatar.getCogLevels()[CogDisguiseGlobals.dept2deptIndex(self.style.dept)]
            if newCogSuitLevel == ToontownGlobals.MaxCogSuitLevel:
                speech += TTLocalizer.CagedToonLastPromotion % (ToontownGlobals.MaxCogSuitLevel + 1)
            
            if newCogSuitLevel in ToontownGlobals.CogSuitHPLevels:
                speech += TTLocalizer.CagedToonHPBoost
            
        else:
            speech += TTLocalizer.CagedToonMaxed % (ToontownGlobals.MaxCogSuitLevel + 1)
        return speech

    
    def _DistributedSellbotBoss__makeCageOpenMovie(self):
        speech = TTLocalizer.CagedToonThankYou
        speech = self._DistributedSellbotBoss__talkAboutPromotion(speech)
        name = self.uniqueName('CageOpen')
        seq = Sequence(Func(self.cage.setPos, self.cagePos[4]), Func(self.cageDoor.setHpr, VBase3(0, 0, 0)), Func(self.cagedToon.setPos, Point3(0, -2, 0)), Parallel(self.cage.posInterval(0.5, self.cagePos[5], blendType = 'easeOut'), SoundInterval(self.cageLowerSfx, duration = 0.5)), Parallel(self.cageDoor.hprInterval(0.5, VBase3(0, 90, 0), blendType = 'easeOut'), Sequence(SoundInterval(self.cageDoorSfx), duration = 0)), Wait(0.20000000000000001), Func(self.cagedToon.loop, 'walk'), self.cagedToon.posInterval(0.80000000000000004, Point3(0, -6, 0)), Func(self.cagedToon.setChatAbsolute, TTLocalizer.CagedToonYippee, CFSpeech), ActorInterval(self.cagedToon, 'jump'), Func(self.cagedToon.loop, 'neutral'), Func(self.cagedToon.headsUp, localAvatar), Func(self.cagedToon.setLocalPageChat, speech, 0), Func(camera.reparentTo, localAvatar), Func(camera.setPos, 0, -9, 9), Func(camera.lookAt, self.cagedToon, Point3(0, 0, 2)), name = name)
        return seq

    
    def _DistributedSellbotBoss__showOnscreenMessage(self, text):
        if self.onscreenMessage:
            self.onscreenMessage.destroy()
            self.onscreenMessage = None
        
        self.onscreenMessage = DirectLabel(text = text, text_fg = VBase4(1, 1, 1, 1), text_align = TextNode.ACenter, relief = None, pos = (0, 0, 0.34999999999999998), scale = 0.10000000000000001)

    
    def _DistributedSellbotBoss__clearOnscreenMessage(self):
        if self.onscreenMessage:
            self.onscreenMessage.destroy()
            self.onscreenMessage = None
        

    
    def _DistributedSellbotBoss__showWaitingMessage(self, task):
        self._DistributedSellbotBoss__showOnscreenMessage(TTLocalizer.BuildingWaitingForVictors)

    
    def _DistributedSellbotBoss__placeCageShadow(self):
        if self.cageShadow == None:
            self.cageShadow = loader.loadModel('phase_3/models/props/drop_shadow')
            self.cageShadow.setPos(0, 77.900000000000006, 18)
            self.cageShadow.setColorScale(1, 1, 1, 0.59999999999999998)
        
        self.cageShadow.reparentTo(render)

    
    def _DistributedSellbotBoss__removeCageShadow(self):
        if self.cageShadow != None:
            self.cageShadow.detachNode()
        

    
    def setCageIndex(self, cageIndex):
        self.cageIndex = cageIndex
        self.cage.setPos(self.cagePos[self.cageIndex])
        if self.cageIndex >= 4:
            self._DistributedSellbotBoss__placeCageShadow()
        else:
            self._DistributedSellbotBoss__removeCageShadow()

    
    def loadEnvironment(self):
        DistributedBossCog.DistributedBossCog.loadEnvironment(self)
        self.geom = loader.loadModel('phase_9/models/cogHQ/BossRoomHQ')
        self.rampA = self._DistributedSellbotBoss__findRamp('rampA', '**/west_ramp2')
        self.rampB = self._DistributedSellbotBoss__findRamp('rampB', '**/west_ramp')
        self.rampC = self._DistributedSellbotBoss__findRamp('rampC', '**/west_ramp1')
        self.cage = self.geom.find('**/cage')
        elevatorEntrance = self.geom.find('**/elevatorEntrance')
        elevatorEntrance.getChildren().detach()
        elevatorEntrance.setScale(1)
        elevatorModel = loader.loadModelCopy('phase_9/models/cogHQ/cogHQ_elevator')
        elevatorModel.reparentTo(elevatorEntrance)
        self.setupElevator(elevatorModel)
        pos = self.cage.getPos()
        self.cagePos = []
        for height in self.cageHeights:
            self.cagePos.append(Point3(pos[0], pos[1], height))
        
        self.cageDoor = self.geom.find('**/cage_door')
        self.cage.setScale(1)
        self.rope = Rope.Rope(name = 'supportChain')
        self.rope.reparentTo(self.cage)
        self.rope.setup(2, ((self.cage, (0.14999999999999999, 0.13, 16)), (self.geom, (0.23000000000000001, 78, 120))))
        self.rope.ropeNode.setRenderMode(RopeNode.RMBillboard)
        self.rope.ropeNode.setUvMode(RopeNode.UVDistance)
        self.rope.ropeNode.setUvDirection(0)
        self.rope.ropeNode.setUvScale(0.80000000000000004)
        self.rope.setTexture(self.cage.findTexture('hq_chain'))
        self.rope.setTransparency(1)
        self.promotionMusic = base.loadMusic('phase_7/audio/bgm/encntr_suit_winning_indoor.mid')
        self.betweenBattleMusic = base.loadMusic('phase_9/audio/bgm/encntr_toon_winning.mid')
        self.battleTwoMusic = base.loadMusic('phase_7/audio/bgm/encntr_suit_winning_indoor.mid')
        self.geom.reparentTo(render)

    
    def unloadEnvironment(self):
        DistributedBossCog.DistributedBossCog.unloadEnvironment(self)
        self.geom.removeNode()
        del self.geom
        del self.cage
        self.rampA.requestFinalState()
        self.rampB.requestFinalState()
        self.rampC.requestFinalState()
        del self.rampA
        del self.rampB
        del self.rampC

    
    def _DistributedSellbotBoss__loadMopaths(self):
        self.toonsEnterA = Mopath.Mopath()
        self.toonsEnterA.loadFile('phase_9/paths/bossBattle-toonsEnterA')
        self.toonsEnterA.fFaceForward = 1
        self.toonsEnterA.timeScale = 35
        self.toonsEnterB = Mopath.Mopath()
        self.toonsEnterB.loadFile('phase_9/paths/bossBattle-toonsEnterB')
        self.toonsEnterB.fFaceForward = 1
        self.toonsEnterB.timeScale = 35

    
    def _DistributedSellbotBoss__unloadMopaths(self):
        self.toonsEnterA.reset()
        self.toonsEnterB.reset()

    
    def _DistributedSellbotBoss__findRamp(self, name, path):
        ramp = self.geom.find(path)
        children = ramp.getChildren()
        animate = ramp.attachNewNode(name)
        children.reparentTo(animate)
        fsm = ClassicFSM.ClassicFSM(name, [
            State.State('extend', Functor(self.enterRampExtend, animate), Functor(self.exitRampExtend, animate), [
                'extended',
                'retract',
                'retracted']),
            State.State('extended', Functor(self.enterRampExtended, animate), Functor(self.exitRampExtended, animate), [
                'retract',
                'retracted']),
            State.State('retract', Functor(self.enterRampRetract, animate), Functor(self.exitRampRetract, animate), [
                'extend',
                'extended',
                'retracted']),
            State.State('retracted', Functor(self.enterRampRetracted, animate), Functor(self.exitRampRetracted, animate), [
                'extend',
                'extended']),
            State.State('off', Functor(self.enterRampOff, animate), Functor(self.exitRampOff, animate))], 'off', 'off', onUndefTransition = ClassicFSM.ClassicFSM.DISALLOW)
        fsm.enterInitialState()
        return fsm

    
    def enterRampExtend(self, animate):
        intervalName = self.uniqueName('extend-%s' % animate.getName())
        adjustTime = 2.0 * animate.getX() / 18.0
        ival = Parallel(SoundInterval(self.rampSlideSfx, node = animate), animate.posInterval(adjustTime, Point3(0, 0, 0), blendType = 'easeInOut', name = intervalName))
        ival.start()
        self.activeIntervals[intervalName] = ival

    
    def exitRampExtend(self, animate):
        intervalName = self.uniqueName('extend-%s' % animate.getName())
        self.clearInterval(intervalName)

    
    def enterRampExtended(self, animate):
        animate.setPos(0, 0, 0)

    
    def exitRampExtended(self, animate):
        pass

    
    def enterRampRetract(self, animate):
        intervalName = self.uniqueName('retract-%s' % animate.getName())
        adjustTime = 2.0 * (18 - animate.getX()) / 18.0
        ival = Parallel(SoundInterval(self.rampSlideSfx, node = animate), animate.posInterval(adjustTime, Point3(18, 0, 0), blendType = 'easeInOut', name = intervalName))
        ival.start()
        self.activeIntervals[intervalName] = ival

    
    def exitRampRetract(self, animate):
        intervalName = self.uniqueName('retract-%s' % animate.getName())
        self.clearInterval(intervalName)

    
    def enterRampRetracted(self, animate):
        animate.setPos(18, 0, 0)

    
    def exitRampRetracted(self, animate):
        pass

    
    def enterRampOff(self, animate):
        pass

    
    def exitRampOff(self, animate):
        pass

    
    def enterOff(self):
        DistributedBossCog.DistributedBossCog.enterOff(self)
        if self.cagedToon:
            self.cagedToon.clearChat()
        
        if self.rampA:
            self.rampA.request('off')
        
        if self.rampB:
            self.rampB.request('off')
        
        if self.rampC:
            self.rampC.request('off')
        

    
    def enterWaitForToons(self):
        DistributedBossCog.DistributedBossCog.enterWaitForToons(self)
        self.geom.hide()
        self.cagedToon.removeActive()

    
    def exitWaitForToons(self):
        DistributedBossCog.DistributedBossCog.exitWaitForToons(self)
        self.geom.show()
        self.cagedToon.addActive()

    
    def enterElevator(self):
        DistributedBossCog.DistributedBossCog.enterElevator(self)
        self.rampA.request('extended')
        self.rampB.request('extended')
        self.rampC.request('retracted')
        self.setCageIndex(0)
        self.reparentTo(render)
        self.setPosHpr(*ToontownGlobals.SellbotBossBattleOnePosHpr)
        self.happy = 1
        self.raised = 1
        self.forward = 1
        self.doAnimate()
        self.cagedToon.removeActive()

    
    def exitElevator(self):
        DistributedBossCog.DistributedBossCog.exitElevator(self)
        self.cagedToon.addActive()

    
    def enterIntroduction(self):
        self.reparentTo(render)
        self.setPosHpr(*ToontownGlobals.SellbotBossBattleOnePosHpr)
        self.stopAnimate()
        DistributedBossCog.DistributedBossCog.enterIntroduction(self)
        self.rampA.request('extended')
        self.rampB.request('extended')
        self.rampC.request('retracted')
        self.setCageIndex(0)
        base.playMusic(self.promotionMusic, looping = 1, volume = 0.90000000000000002)

    
    def exitIntroduction(self):
        DistributedBossCog.DistributedBossCog.exitIntroduction(self)
        self.promotionMusic.stop()

    
    def enterBattleOne(self):
        DistributedBossCog.DistributedBossCog.enterBattleOne(self)
        self.reparentTo(render)
        self.setPosHpr(*ToontownGlobals.SellbotBossBattleOnePosHpr)
        self.clearChat()
        self.cagedToon.clearChat()
        self.rampA.request('retract')
        self.rampB.request('retract')
        self.rampC.request('retract')
        if self.battleA == None or self.battleB == None:
            cageIndex = 1
        else:
            cageIndex = 0
        self.setCageIndex(cageIndex)

    
    def exitBattleOne(self):
        DistributedBossCog.DistributedBossCog.exitBattleOne(self)

    
    def enterRollToBattleTwo(self):
        self.releaseToons()
        if self.arenaSide:
            self.rampA.request('retract')
            self.rampB.request('extend')
        else:
            self.rampA.request('extend')
            self.rampB.request('retract')
        self.rampC.request('retract')
        self.reparentTo(render)
        self.setCageIndex(2)
        self.stickBossToFloor()
        intervalName = 'RollToBattleTwo'
        seq = Sequence(self._DistributedSellbotBoss__makeRollToBattleTwoMovie(), Func(self._DistributedSellbotBoss__onToPrepareBattleTwo), name = intervalName)
        seq.start()
        self.activeIntervals[intervalName] = seq
        base.playMusic(self.betweenBattleMusic, looping = 1, volume = 0.90000000000000002)

    
    def _DistributedSellbotBoss__onToPrepareBattleTwo(self):
        self.unstickBoss()
        self.setPosHpr(*ToontownGlobals.SellbotBossBattleTwoPosHpr)
        self.doneBarrier('RollToBattleTwo')

    
    def exitRollToBattleTwo(self):
        self.unstickBoss()
        intervalName = 'RollToBattleTwo'
        self.clearInterval(intervalName)
        self.betweenBattleMusic.stop()

    
    def enterPrepareBattleTwo(self):
        self.cleanupIntervals()
        self.controlToons()
        self.clearChat()
        self.cagedToon.clearChat()
        self.reparentTo(render)
        if self.arenaSide:
            self.rampA.request('retract')
            self.rampB.request('extend')
        else:
            self.rampA.request('extend')
            self.rampB.request('retract')
        self.rampC.request('retract')
        self.reparentTo(render)
        self.setCageIndex(2)
        camera.reparentTo(render)
        camera.setPosHpr(self.cage, 0, -17, 3.2999999999999998, 0, 0, 0)
        (localAvatar.setCameraFov(ToontownGlobals.CogHQCameraFov),)
        self.hide()
        self.acceptOnce('doneChatPage', self._DistributedSellbotBoss__onToBattleTwo)
        self.cagedToon.setLocalPageChat(TTLocalizer.CagedToonPrepareBattleTwo, 1)
        base.playMusic(self.stingMusic, looping = 0, volume = 1.0)

    
    def _DistributedSellbotBoss__onToBattleTwo(self, elapsed):
        self.doneBarrier('PrepareBattleTwo')
        taskMgr.doMethodLater(1, self._DistributedSellbotBoss__showWaitingMessage, self.uniqueName('WaitingMessage'))

    
    def exitPrepareBattleTwo(self):
        self.show()
        taskMgr.remove(self.uniqueName('WaitingMessage'))
        self.ignore('doneChatPage')
        self._DistributedSellbotBoss__clearOnscreenMessage()
        self.stingMusic.stop()

    
    def enterBattleTwo(self):
        self.cleanupIntervals()
        mult = ToontownBattleGlobals.getBossBattleCreditMultiplier(2)
        localAvatar.inventory.setBattleCreditMultiplier(mult)
        self.reparentTo(render)
        self.setPosHpr(*ToontownGlobals.SellbotBossBattleTwoPosHpr)
        self.clearChat()
        self.cagedToon.clearChat()
        self.rampA.request('retract')
        self.rampB.request('retract')
        self.rampC.request('retract')
        self.releaseToons()
        self.toonsToBattlePosition(self.toonsA, self.battleANode)
        self.toonsToBattlePosition(self.toonsB, self.battleBNode)
        if self.battleA == None or self.battleB == None:
            cageIndex = 3
        else:
            cageIndex = 2
        self.setCageIndex(cageIndex)
        base.playMusic(self.battleTwoMusic, looping = 1, volume = 0.90000000000000002)

    
    def exitBattleTwo(self):
        intervalName = self.uniqueName('cageDrop')
        self.clearInterval(intervalName)
        self.cleanupBattles()
        self.battleTwoMusic.stop()
        localAvatar.inventory.setBattleCreditMultiplier(1)

    
    def enterPrepareBattleThree(self):
        self.cleanupIntervals()
        self.controlToons()
        self.clearChat()
        self.cagedToon.clearChat()
        self.reparentTo(render)
        self.rampA.request('retract')
        self.rampB.request('retract')
        self.rampC.request('extend')
        self.setCageIndex(4)
        camera.reparentTo(render)
        camera.setPosHpr(self.cage, 0, -17, 3.2999999999999998, 0, 0, 0)
        (localAvatar.setCameraFov(ToontownGlobals.CogHQCameraFov),)
        self.hide()
        self.acceptOnce('doneChatPage', self._DistributedSellbotBoss__onToBattleThree)
        self.cagedToon.setLocalPageChat(TTLocalizer.CagedToonPrepareBattleThree, 1)
        base.playMusic(self.betweenBattleMusic, looping = 1, volume = 0.90000000000000002)

    
    def _DistributedSellbotBoss__onToBattleThree(self, elapsed):
        self.doneBarrier('PrepareBattleThree')
        taskMgr.doMethodLater(1, self._DistributedSellbotBoss__showWaitingMessage, self.uniqueName('WaitingMessage'))

    
    def exitPrepareBattleThree(self):
        self.show()
        taskMgr.remove(self.uniqueName('WaitingMessage'))
        self.ignore('doneChatPage')
        intervalName = 'PrepareBattleThree'
        self.clearInterval(intervalName)
        self._DistributedSellbotBoss__clearOnscreenMessage()
        self.betweenBattleMusic.stop()

    
    def enterBattleThree(self):
        self.cleanupIntervals()
        self.releaseToons(finalBattle = 1)
        self.clearChat()
        self.cagedToon.clearChat()
        self.reparentTo(render)
        self.rampA.request('retract')
        self.rampB.request('retract')
        self.rampC.request('extend')
        self.setCageIndex(4)
        self.happy = 0
        self.raised = 1
        self.forward = 1
        self.doAnimate()
        self.accept('enterCage', self._DistributedSellbotBoss__touchedCage)
        self.accept('pieSplat', self._DistributedSellbotBoss__pieSplat)
        self.accept('localPieSplat', self._DistributedSellbotBoss__localPieSplat)
        self.accept('outOfPies', self._DistributedSellbotBoss__outOfPies)
        self.accept('begin-pie', self._DistributedSellbotBoss__foundPieButton)
        localAvatar.setCameraFov(ToontownGlobals.BossBattleCameraFov)
        taskMgr.doMethodLater(30, self._DistributedSellbotBoss__howToGetPies, self.uniqueName('PieAdvice'))
        self.stickBossToFloor()
        self.bossDamageMovie = self._DistributedSellbotBoss__makeBossDamageMovie()
        bossDoneEventName = self.uniqueName('DestroyedBoss')
        self.bossDamageMovie.setDoneEvent(bossDoneEventName)
        self.acceptOnce(bossDoneEventName, self._DistributedSellbotBoss__doneBattleThree)
        self.bossMaxDamage = ToontownGlobals.SellbotBossMaxDamage
        self.bossDamageToMovie = self.bossDamageMovie.getDuration() / self.bossMaxDamage
        self.bossDamageMovie.setT(self.bossDamage * self.bossDamageToMovie)
        base.playMusic(self.battleThreeMusic, looping = 1, volume = 0.90000000000000002)

    
    def _DistributedSellbotBoss__doneBattleThree(self):
        self.setState('NearVictory')
        self.unstickBoss()

    
    def exitBattleThree(self):
        bossDoneEventName = self.uniqueName('DestroyedBoss')
        self.ignore(bossDoneEventName)
        taskMgr.remove(self.uniqueName('StandUp'))
        self.ignore('enterCage')
        self.ignore('pieSplat')
        self.ignore('localPieSplat')
        self.ignore('outOfPies')
        self.ignore('begin-pie')
        self._DistributedSellbotBoss__clearOnscreenMessage()
        taskMgr.remove(self.uniqueName('PieAdvice'))
        localAvatar.setCameraFov(ToontownGlobals.CogHQCameraFov)
        self._DistributedSellbotBoss__removeCageShadow()
        self.bossDamageMovie.finish()
        self.bossDamageMovie = None
        self.unstickBoss()
        taskName = 'RecoverBossDamage'
        taskMgr.remove(taskName)
        self.battleThreeMusicTime = self.battleThreeMusic.getTime()
        self.battleThreeMusic.stop()

    
    def enterNearVictory(self):
        self.cleanupIntervals()
        self.reparentTo(render)
        self.setPos(*ToontownGlobals.SellbotBossDeathPos)
        self.setHpr(*ToontownGlobals.SellbotBossBattleThreeHpr)
        self.clearChat()
        self.cagedToon.clearChat()
        self.setCageIndex(4)
        self.releaseToons(finalBattle = 1)
        self.rampA.request('retract')
        self.rampB.request('retract')
        self.rampC.request('extend')
        self.accept('enterCage', self._DistributedSellbotBoss__touchedCage)
        self.accept('pieSplat', self._DistributedSellbotBoss__finalPieSplat)
        self.accept('localPieSplat', self._DistributedSellbotBoss__localPieSplat)
        self.accept('outOfPies', self._DistributedSellbotBoss__outOfPies)
        localAvatar.setCameraFov(ToontownGlobals.BossBattleCameraFov)
        self.happy = 0
        self.raised = 0
        self.forward = 1
        self.doAnimate()
        self.setDizzy(1)
        base.playMusic(self.battleThreeMusic, looping = 1, volume = 0.90000000000000002, time = self.battleThreeMusicTime)

    
    def exitNearVictory(self):
        self.ignore('enterCage')
        self.ignore('pieSplat')
        self.ignore('localPieSplat')
        self.ignore('outOfPies')
        self._DistributedSellbotBoss__clearOnscreenMessage()
        taskMgr.remove(self.uniqueName('PieAdvice'))
        localAvatar.setCameraFov(ToontownGlobals.CogHQCameraFov)
        self._DistributedSellbotBoss__removeCageShadow()
        self.setDizzy(0)
        self.battleThreeMusicTime = self.battleThreeMusic.getTime()
        self.battleThreeMusic.stop()

    
    def enterVictory(self):
        self.cleanupIntervals()
        localAvatar.setCameraFov(ToontownGlobals.BossBattleCameraFov)
        self.reparentTo(render)
        self.setPos(*ToontownGlobals.SellbotBossDeathPos)
        self.setHpr(*ToontownGlobals.SellbotBossBattleThreeHpr)
        self.clearChat()
        self.cagedToon.clearChat()
        self.setCageIndex(4)
        self.releaseToons(finalBattle = 1)
        self.rampA.request('retract')
        self.rampB.request('retract')
        self.rampC.request('extend')
        self.happy = 0
        self.raised = 0
        self.forward = 1
        self.doAnimate('Fb_fall', now = 1)
        self.acceptOnce(self.animDoneEvent, self._DistributedSellbotBoss__continueVictory)
        base.playMusic(self.battleThreeMusic, looping = 1, volume = 0.90000000000000002, time = self.battleThreeMusicTime)

    
    def _DistributedSellbotBoss__continueVictory(self):
        self.stopAnimate()
        self.stash()
        self.doneBarrier('Victory')

    
    def exitVictory(self):
        self.stopAnimate()
        self.unstash()
        self._DistributedSellbotBoss__removeCageShadow()
        localAvatar.setCameraFov(ToontownGlobals.CogHQCameraFov)
        self.battleThreeMusicTime = self.battleThreeMusic.getTime()
        self.battleThreeMusic.stop()

    
    def enterReward(self):
        self.cleanupIntervals()
        self.clearChat()
        self.cagedToon.clearChat()
        self.stash()
        self.stopAnimate()
        self.setCageIndex(4)
        self.releaseToons(finalBattle = 1)
        self.toMovieMode()
        self.rampA.request('retract')
        self.rampB.request('retract')
        self.rampC.request('extend')
        panelName = self.uniqueName('reward')
        self.rewardPanel = RewardPanel.RewardPanel(panelName)
        (victory, camVictory) = MovieToonVictory.doToonVictory(1, self.involvedToons, self.toonRewardIds, self.toonRewardDicts, self.deathList, self.rewardPanel, allowGroupShot = 0)
        ival = Sequence(Parallel(victory, camVictory), Func(self._DistributedSellbotBoss__doneReward))
        intervalName = 'RewardMovie'
        delayDeletes = []
        for toonId in self.involvedToons:
            toon = self.cr.doId2do.get(toonId)
            if toon:
                delayDeletes.append(DelayDelete.DelayDelete(toon))
            
        
        ival.delayDeletes = delayDeletes
        ival.start()
        self.activeIntervals[intervalName] = ival
        base.playMusic(self.battleThreeMusic, looping = 1, volume = 0.90000000000000002, time = self.battleThreeMusicTime)

    
    def _DistributedSellbotBoss__doneReward(self):
        self.doneBarrier('Reward')
        self.toWalkMode()

    
    def exitReward(self):
        intervalName = 'RewardMovie'
        self.clearInterval(intervalName)
        self.unstash()
        self.rewardPanel.destroy()
        del self.rewardPanel
        self._DistributedSellbotBoss__removeCageShadow()
        self.battleThreeMusicTime = 0
        self.battleThreeMusic.stop()

    
    def enterEpilogue(self):
        self.cleanupIntervals()
        self.clearChat()
        self.cagedToon.clearChat()
        self.stash()
        self.stopAnimate()
        self.setCageIndex(4)
        self.controlToons()
        self.rampA.request('retract')
        self.rampB.request('retract')
        self.rampC.request('extend')
        self._DistributedSellbotBoss__arrangeToonsAroundCage()
        camera.reparentTo(render)
        camera.setPosHpr(-24, 52, 27.5, -53, -13, 0)
        intervalName = 'EpilogueMovie'
        seq = Sequence(self._DistributedSellbotBoss__makeCageOpenMovie(), name = intervalName)
        seq.start()
        self.activeIntervals[intervalName] = seq
        self.accept('nextChatPage', self._DistributedSellbotBoss__epilogueChatNext)
        self.accept('doneChatPage', self._DistributedSellbotBoss__epilogueChatDone)
        base.playMusic(self.epilogueMusic, looping = 1, volume = 0.90000000000000002)

    
    def _DistributedSellbotBoss__epilogueChatNext(self, pageNumber, elapsed):
        if pageNumber == 2:
            if self.cagedToon.style.torso[1] == 'd':
                track = ActorInterval(self.cagedToon, 'curtsy')
            else:
                track = ActorInterval(self.cagedToon, 'bow')
            track = Sequence(track, Func(self.cagedToon.loop, 'neutral'))
            intervalName = 'EpilogueMovieToonAnim'
            self.activeIntervals[intervalName] = track
            track.start()
        

    
    def _DistributedSellbotBoss__epilogueChatDone(self, elapsed):
        self.cagedToon.setChatAbsolute(TTLocalizer.CagedToonGoodbye, CFSpeech)
        self.ignore('nextChatPage')
        self.ignore('doneChatPage')
        intervalName = 'EpilogueMovieToonAnim'
        self.clearInterval(intervalName)
        track = Parallel(Sequence(ActorInterval(self.cagedToon, 'wave'), Func(self.cagedToon.loop, 'neutral')), Sequence(Wait(0.5), Func(self.localToonToSafeZone)))
        self.activeIntervals[intervalName] = track
        track.start()

    
    def exitEpilogue(self):
        self.clearInterval('EpilogueMovieToonAnim')
        self.unstash()
        self._DistributedSellbotBoss__removeCageShadow()
        self.epilogueMusic.stop()

    
    def _DistributedSellbotBoss__arrangeToonsAroundCage(self):
        radius = 15
        numToons = len(self.involvedToons)
        center = (numToons - 1) / 2.0
        for i in range(numToons):
            toon = base.cr.doId2do.get(self.involvedToons[i])
            if toon:
                angle = 270 - 15 * (i - center)
                radians = angle * math.pi / 180.0
                x = math.cos(radians) * radius
                y = math.sin(radians) * radius
                toon.setPos(self.cage, x, y, 0)
                toon.setZ(18.0)
                toon.headsUp(self.cage)
            
        

    
    def enterFrolic(self):
        DistributedBossCog.DistributedBossCog.enterFrolic(self)
        self.setPosHpr(*ToontownGlobals.SellbotBossBattleOnePosHpr)

    
    def doorACallback(self, isOpen):
        if self.insidesANodePath:
            if isOpen:
                self.insidesANodePath.unstash()
            else:
                self.insidesANodePath.stash()
        

    
    def doorBCallback(self, isOpen):
        if self.insidesBNodePath:
            if isOpen:
                self.insidesBNodePath.unstash()
            else:
                self.insidesBNodePath.stash()
        

    
    def _DistributedSellbotBoss__toonsToPromotionPosition(self, toonIds, battleNode):
        points = BattleBase.BattleBase.toonPoints[len(toonIds) - 1]
        for i in range(len(toonIds)):
            toon = base.cr.doId2do.get(toonIds[i])
            if toon:
                toon.reparentTo(render)
                (pos, h) = points[i]
                toon.setPosHpr(battleNode, pos[0], pos[1] + 10, pos[2], h, 0, 0)
            
        

    
    def _DistributedSellbotBoss__doobersToPromotionPosition(self, doobers, battleNode):
        points = BattleBase.BattleBase.toonPoints[len(doobers) - 1]
        for i in range(len(doobers)):
            suit = doobers[i]
            suit.fsm.request('neutral')
            suit.loop('neutral')
            (pos, h) = points[i]
            suit.setPosHpr(battleNode, pos[0], pos[1] + 10, pos[2], h, 0, 0)
        

    
    def _DistributedSellbotBoss__touchedCage(self, entry):
        self.sendUpdate('touchCage', [])
        self._DistributedSellbotBoss__clearOnscreenMessage()
        taskMgr.remove(self.uniqueName('PieAdvice'))
        base.playSfx(self.piesRestockSfx)
        if not (self.everThrownPie):
            taskMgr.doMethodLater(30, self._DistributedSellbotBoss__howToThrowPies, self.uniqueName('PieAdvice'))
        

    
    def _DistributedSellbotBoss__outOfPies(self):
        self._DistributedSellbotBoss__showOnscreenMessage(TTLocalizer.BossBattleNeedMorePies)
        taskMgr.doMethodLater(20, self._DistributedSellbotBoss__howToGetPies, self.uniqueName('PieAdvice'))

    
    def _DistributedSellbotBoss__howToGetPies(self, task):
        self._DistributedSellbotBoss__showOnscreenMessage(TTLocalizer.BossBattleHowToGetPies)

    
    def _DistributedSellbotBoss__howToThrowPies(self, task):
        self._DistributedSellbotBoss__showOnscreenMessage(TTLocalizer.BossBattleHowToThrowPies)

    
    def _DistributedSellbotBoss__foundPieButton(self):
        self.everThrownPie = 1
        self._DistributedSellbotBoss__clearOnscreenMessage()
        taskMgr.remove(self.uniqueName('PieAdvice'))

    
    def _DistributedSellbotBoss__pieSplat(self, toon, pieCode):
        if pieCode == ToontownGlobals.PieCodeBossInsides:
            if toon == localAvatar:
                self.d_hitBossInsides()
            
            self.flashRed()
        elif pieCode == ToontownGlobals.PieCodeBossCog:
            if toon == localAvatar:
                self.d_hitBoss(1)
            
            if self.dizzy:
                self.flashRed()
                self.doAnimate('hit', now = 1)
            
        

    
    def _DistributedSellbotBoss__localPieSplat(self, pieCode, entry):
        if pieCode != ToontownGlobals.PieCodeToon:
            return None
        
        avatarDoId = entry.getIntoNodePath().getNetTag('avatarDoId')
        if avatarDoId == '':
            self.notify.warning('Toon %s has no avatarDoId tag.' % repr(entry.getIntoNodePath()))
            return None
        
        doId = int(avatarDoId)
        if doId != localAvatar.doId:
            self.d_hitToon(doId)
        

    
    def _DistributedSellbotBoss__finalPieSplat(self, toon, pieCode):
        if pieCode != ToontownGlobals.PieCodeBossCog:
            return None
        
        self.sendUpdate('finalPieSplat', [])
        self.ignore('pieSplat')

    
    def cagedToonBattleThree(self, index, avId):
        str = TTLocalizer.CagedToonBattleThree.get(index)
        if str:
            toonName = ''
            if avId:
                toon = self.cr.doId2do.get(avId)
                if not toon:
                    self.cagedToon.clearChat()
                    return None
                
                toonName = toon.getName()
            
            text = str % {
                'toon': toonName }
            self.cagedToon.setChatAbsolute(text, CFSpeech | CFTimeout)
        else:
            self.cagedToon.clearChat()

    
    def cleanupAttacks(self):
        self._DistributedSellbotBoss__cleanupStrafe()

    
    def _DistributedSellbotBoss__cleanupStrafe(self):
        if self.strafeInterval:
            self.strafeInterval.finish()
            self.strafeInterval = None
        

    
    def doStrafe(self, side, direction):
        gearRoot = self.rotateNode.attachNewNode('gearRoot')
        if side == 0:
            gearRoot.setPos(0, -7, 3)
            gearRoot.setHpr(180, 0, 0)
            door = self.doorA
        else:
            gearRoot.setPos(0, 7, 3)
            door = self.doorB
        gearRoot.setTag('attackCode', str(ToontownGlobals.BossCogStrafeAttack))
        gearModel = self.getGearFrisbee()
        gearModel.setScale(0.10000000000000001)
        t = self.getBossDamage() / 100.0
        gearTrack = Parallel()
        numGears = int(4 + 6 * t + 0.5)
        time = 5.0 - 4.0 * t
        spread = 60 * math.pi / 180.0
        if direction == 1:
            spread = -spread
        
        dist = 50
        rate = time / numGears
        for i in range(numGears):
            node = gearRoot.attachNewNode(str(i))
            node.hide()
            node.setPos(0, 0, 0)
            gear = gearModel.instanceTo(node)
            angle = (float(i) / (numGears - 1) - 0.5) * spread
            x = dist * math.sin(angle)
            y = dist * math.cos(angle)
            h = random.uniform(-720, 720)
            gearTrack.append(Sequence(Wait(i * rate), Func(node.show), Parallel(node.posInterval(1, Point3(x, y, 0), fluid = 1), node.hprInterval(1, VBase3(h, 0, 0), fluid = 1), Sequence(SoundInterval(self.strafeSfx[i], volume = 0.20000000000000001, node = self), duration = 0)), Func(node.detachNode)))
        
        seq = Sequence(Func(door.request, 'open'), Wait(0.69999999999999996), gearTrack, Func(door.request, 'close'))
        self._DistributedSellbotBoss__cleanupStrafe()
        self.strafeInterval = seq
        seq.start()


