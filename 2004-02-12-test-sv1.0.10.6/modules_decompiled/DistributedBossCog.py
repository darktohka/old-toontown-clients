# File: D (Python 2.2)

from ShowBaseGlobal import *
from IntervalGlobal import *
from BattleProps import *
from ClockDelta import *
from PythonUtil import Functor
from DirectGui import *
import FSM
import State
import DirectNotifyGlobal
import BattleExperience
import ToontownGlobals
import ToontownBattleGlobals
import BossCog
import DistributedAvatar
import Localizer
import AvatarDNA
import Toon
import BattleBase
import Mopath
import DelayDelete
import DustCloud
import Rope
import ZoneUtil
import MovieToonVictory
import ElevatorUtils
import ElevatorConstants
import RewardPanel
import NPCToons
import Transitions
import Task
import random
import math
OneBossCog = None

class DistributedBossCog(DistributedAvatar.DistributedAvatar, BossCog.BossCog):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedBossCog')
    cageHeights = [
        100,
        81,
        63,
        44,
        25,
        18]
    
    def __init__(self, cr):
        DistributedAvatar.DistributedAvatar.__init__(self, cr)
        BossCog.BossCog.__init__(self)
        self.cagedToonNpcId = None
        self.gotAllToons = 0
        self.toonsA = []
        self.toonsB = []
        self.involvedToons = []
        self.toonRequest = None
        self.doobers = []
        self.dooberRequest = None
        self.battleNumber = 0
        self.battleAId = None
        self.battleBId = None
        self.battleA = None
        self.battleB = None
        self.battleRequest = None
        self.arenaSide = 0
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
        self._DistributedBossCog__toonsStuckToFloor = []
        self.rays = None
        self.ray1 = None
        self.ray2 = None
        self.ray3 = None
        self.e1 = None
        self.e2 = None
        self.e3 = None
        self.toonSphere = None
        self.battleANode = self.attachNewNode('battleA')
        self.battleBNode = self.attachNewNode('battleB')
        self.battleANode.setPosHpr(*ToontownGlobals.BossCogBattleAPosHpr)
        self.battleBNode.setPosHpr(*ToontownGlobals.BossCogBattleBPosHpr)
        self.activeIntervals = { }
        self.flashInterval = None
        self.strafeInterval = None
        self.onscreenMessage = None
        self.fsm = FSM.FSM('DistributedBossCog', [
            State.State('WaitForToons', self.enterWaitForToons, self.exitWaitForToons),
            State.State('Elevator', self.enterElevator, self.exitElevator),
            State.State('Introduction', self.enterIntroduction, self.exitIntroduction),
            State.State('BattleOne', self.enterBattleOne, self.exitBattleOne),
            State.State('RollToBattleTwo', self.enterRollToBattleTwo, self.exitRollToBattleTwo),
            State.State('PrepareBattleTwo', self.enterPrepareBattleTwo, self.exitPrepareBattleTwo),
            State.State('BattleTwo', self.enterBattleTwo, self.exitBattleTwo),
            State.State('PrepareBattleThree', self.enterPrepareBattleThree, self.exitPrepareBattleThree),
            State.State('BattleThree', self.enterBattleThree, self.exitBattleThree),
            State.State('NearVictory', self.enterNearVictory, self.exitNearVictory),
            State.State('Victory', self.enterVictory, self.exitVictory),
            State.State('Reward', self.enterReward, self.exitReward),
            State.State('Epilogue', self.enterEpilogue, self.exitEpilogue),
            State.State('Frolic', self.enterFrolic, self.exitFrolic),
            State.State('Off', self.enterOff, self.exitOff)], 'Off', 'Off')
        self.fsm.enterInitialState()

    
    def announceGenerate(self):
        global OneBossCog
        DistributedAvatar.DistributedAvatar.announceGenerate(self)
        self.setName(Localizer.BossCogName)
        nameInfo = Localizer.BossCogNameWithDept % {
            'name': self.name,
            'dept': AvatarDNA.getDeptFullname(self.style.dept) }
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
        nearBubble = CollisionSphere(0, 0, 0, 50)
        nearBubble.setTangible(0)
        nearBubbleNode = CollisionNode('NearBoss')
        nearBubbleNode.setCollideMask(ToontownGlobals.WallBitmask)
        nearBubbleNode.addSolid(nearBubble)
        self.attachNewNode(nearBubbleNode)
        self.accept('enterNearBoss', self._DistributedBossCog__avatarNearEnter)
        self.accept('exitNearBoss', self._DistributedBossCog__avatarNearExit)
        self.collNode.removeSolid(0)
        tube1 = CollisionTube(6.5, -7.5, 2, 6.5, 7.5, 2, 2.5)
        tube2 = CollisionTube(-6.5, -7.5, 2, -6.5, 7.5, 2, 2.5)
        roof = CollisionPolygon(Point3(-4.4000000000000004, 7.0999999999999996, 5.5), Point3(-4.4000000000000004, -7.0999999999999996, 5.5), Point3(4.4000000000000004, -7.0999999999999996, 5.5), Point3(4.4000000000000004, 7.0999999999999996, 5.5))
        side1 = CollisionPolygon(Point3(-4.4000000000000004, -7.0999999999999996, 5.5), Point3(-4.4000000000000004, 7.0999999999999996, 5.5), Point3(-4.4000000000000004, 7.0999999999999996, 0), Point3(-4.4000000000000004, -7.0999999999999996, 0))
        side2 = CollisionPolygon(Point3(4.4000000000000004, 7.0999999999999996, 5.5), Point3(4.4000000000000004, -7.0999999999999996, 5.5), Point3(4.4000000000000004, -7.0999999999999996, 0), Point3(4.4000000000000004, 7.0999999999999996, 0))
        front1 = CollisionPolygon(Point3(4.4000000000000004, -7.0999999999999996, 5.5), Point3(-4.4000000000000004, -7.0999999999999996, 5.5), Point3(-4.4000000000000004, -7.0999999999999996, 5.2000000000000002), Point3(4.4000000000000004, -7.0999999999999996, 5.2000000000000002))
        back1 = CollisionPolygon(Point3(-4.4000000000000004, 7.0999999999999996, 5.5), Point3(4.4000000000000004, 7.0999999999999996, 5.5), Point3(4.4000000000000004, 7.0999999999999996, 5.2000000000000002), Point3(-4.4000000000000004, 7.0999999999999996, 5.2000000000000002))
        self.collNode.addSolid(tube1)
        self.collNode.addSolid(tube2)
        self.collNode.addSolid(roof)
        self.collNode.addSolid(side1)
        self.collNode.addSolid(side2)
        self.collNode.addSolid(front1)
        self.collNode.addSolid(back1)
        self.collNodePath.reparentTo(self.axle)
        self.collNode.setCollideMask(ToontownGlobals.PieBitmask | ToontownGlobals.WallBitmask)
        self.collNode.setName('BossZap')
        self.setTag('attackCode', str(ToontownGlobals.BossCogElectricFence))
        self.accept('enterBossZap', self._DistributedBossCog__touchedBoss)
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
        bubbleL = CollisionSphere(10, -5, 0, 10)
        bubbleL.setTangible(0)
        bubbleLNode = CollisionNode('BossZap')
        bubbleLNode.setCollideMask(ToontownGlobals.WallBitmask)
        bubbleLNode.addSolid(bubbleL)
        self.bubbleL = self.axle.attachNewNode(bubbleLNode)
        self.bubbleL.setTag('attackCode', str(ToontownGlobals.BossCogSwatLeft))
        self.bubbleL.stash()
        bubbleR = CollisionSphere(-10, -5, 0, 10)
        bubbleR.setTangible(0)
        bubbleRNode = CollisionNode('BossZap')
        bubbleRNode.setCollideMask(ToontownGlobals.WallBitmask)
        bubbleRNode.addSolid(bubbleR)
        self.bubbleR = self.axle.attachNewNode(bubbleRNode)
        self.bubbleR.setTag('attackCode', str(ToontownGlobals.BossCogSwatRight))
        self.bubbleR.stash()
        bubbleF = CollisionSphere(0, -25, 0, 12)
        bubbleF.setTangible(0)
        bubbleFNode = CollisionNode('BossZap')
        bubbleFNode.setCollideMask(ToontownGlobals.WallBitmask)
        bubbleFNode.addSolid(bubbleF)
        self.bubbleF = self.rotateNode.attachNewNode(bubbleFNode)
        self.bubbleF.setTag('attackCode', str(ToontownGlobals.BossCogFrontAttack))
        self.bubbleF.stash()
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
        disk = loader.loadModel('phase_9/models/char/sellbotBoss-gearCollide')
        disk.find('**/+CollisionNode').setName('BossZap')
        disk.reparentTo(self.pelvis)
        disk.setZ(0.80000000000000004)
        self._DistributedBossCog__loadEnvironment()
        self._DistributedBossCog__makeCagedToon()
        self._DistributedBossCog__loadMopaths()
        if OneBossCog != None:
            self.notify.warning('Multiple BossCogs visible.')
        
        OneBossCog = self

    
    def getDialogueArray(self, *args):
        return BossCog.BossCog.getDialogueArray(self, *args)

    
    def _DistributedBossCog__cleanupIntervals(self):
        for interval in self.activeIntervals.values():
            interval.finish()
        
        self.activeIntervals = { }

    
    def clearInterval(self, name, finish = 1):
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
        global OneBossCog
        DistributedAvatar.DistributedAvatar.disable(self)
        self.fsm.requestFinalState()
        self._DistributedBossCog__unloadEnvironment()
        self._DistributedBossCog__unloadMopaths()
        self._DistributedBossCog__cleanupIntervals()
        self._DistributedBossCog__cleanupCagedToon()
        self._DistributedBossCog__clearOnscreenMessage()
        taskMgr.remove(self.uniqueName('PieAdvice'))
        self.stopAnimate()
        self._DistributedBossCog__cleanupFlash()
        self._DistributedBossCog__cleanupStrafe()
        self._DistributedBossCog__disableLocalToonSimpleCollisions()
        render.clearTag('pieCode')
        self.targetNodePath.detachNode()
        self.battleAId = None
        self.battleBId = None
        self.battleA = None
        self.battleB = None
        self.cr.relatedObjectMgr.abortRequest(self.toonRequest)
        self.toonRequest = None
        self.cr.relatedObjectMgr.abortRequest(self.battleRequest)
        self.battleRequest = None
        self.cr.relatedObjectMgr.abortRequest(self.dooberRequest)
        self.dooberRequest = None
        self.ignoreAll()
        if OneBossCog == self:
            OneBossCog = None
        

    
    def delete(self):
        
        try:
            pass
        except:
            self.DistributedBossCog_deleted = 1
            self.ignoreAll()
            DistributedAvatar.DistributedAvatar.delete(self)
            BossCog.BossCog.delete(self)

        return None

    
    def d_hitBoss(self, bossDamage):
        self.sendUpdate('hitBoss', [
            bossDamage])

    
    def d_hitBossInsides(self):
        self.sendUpdate('hitBossInsides', [])

    
    def d_hitToon(self, toonId):
        self.sendUpdate('hitToon', [
            toonId])

    
    def d_avatarEnter(self):
        self.sendUpdate('avatarEnter', [])

    
    def d_avatarExit(self):
        self.sendUpdate('avatarExit', [])

    
    def _DistributedBossCog__avatarNearEnter(self, entry):
        self.sendUpdate('avatarNearEnter', [])

    
    def _DistributedBossCog__avatarNearExit(self, entry):
        self.sendUpdate('avatarNearExit', [])

    
    def hasLocalToon(self):
        doId = toonbase.localToon.doId
        if not doId in self.toonsA:
            pass
        return doId in self.toonsB

    
    def setBattleExperience(self, id0, origExp0, earnedExp0, items0, missedItems0, origMerits0, merits0, parts0, id1, origExp1, earnedExp1, items1, missedItems1, origMerits1, merits1, parts1, id2, origExp2, earnedExp2, items2, missedItems2, origMerits2, merits2, parts2, id3, origExp3, earnedExp3, items3, missedItems3, origMerits3, merits3, parts3, id4, origExp4, earnedExp4, items4, missedItems4, origMerits4, merits4, parts4, id5, origExp5, earnedExp5, items5, missedItems5, origMerits5, merits5, parts5, id6, origExp6, earnedExp6, items6, missedItems6, origMerits6, merits6, parts6, id7, origExp7, earnedExp7, items7, missedItems7, origMerits7, merits7, parts7, deathList):
        self.deathList = deathList
        entries = ((id0, origExp0, earnedExp0, items0, missedItems0, origMerits0, merits0, parts0), (id1, origExp1, earnedExp1, items1, missedItems1, origMerits1, merits1, parts1), (id2, origExp2, earnedExp2, items2, missedItems2, origMerits2, merits2, parts2), (id3, origExp3, earnedExp3, items3, missedItems3, origMerits3, merits3, parts3), (id4, origExp4, earnedExp4, items4, missedItems4, origMerits4, merits4, parts4), (id5, origExp5, earnedExp5, items5, missedItems5, origMerits5, merits5, parts5), (id6, origExp6, earnedExp6, items6, missedItems6, origMerits6, merits6, parts6), (id7, origExp7, earnedExp7, items7, missedItems7, origMerits7, merits7, parts7))
        self.toonRewardDicts = BattleExperience.genRewardDicts(entries)

    
    def setState(self, state):
        self.fsm.forceTransition(state)

    
    def setCagedToonNpcId(self, npcId):
        self.cagedToonNpcId = npcId

    
    def setToonIds(self, involvedToons, toonsA, toonsB):
        self.involvedToons = involvedToons
        self.toonsA = toonsA
        self.toonsB = toonsB
        self.cr.relatedObjectMgr.abortRequest(self.toonRequest)
        self.gotAllToons = 0
        self.toonRequest = self.cr.relatedObjectMgr.requestObjects(self.involvedToons, allCallback = self._DistributedBossCog__gotAllToons, eachCallback = self._DistributedBossCog__gotToon)

    
    def _DistributedBossCog__gotToon(self, toon):
        stateName = self.fsm.getCurrentState().getName()
        if stateName == 'Elevator':
            self._DistributedBossCog__placeToonInElevator(toon)
        

    
    def _DistributedBossCog__gotAllToons(self, toons):
        self.gotAllToons = 1
        messenger.send('gotAllToons')

    
    def setArenaSide(self, arenaSide):
        self.arenaSide = arenaSide

    
    def setDooberIds(self, dooberIds):
        self.doobers = []
        self.cr.relatedObjectMgr.abortRequest(self.dooberRequest)
        self.dooberRequest = self.cr.relatedObjectMgr.requestObjects(dooberIds, allCallback = self._DistributedBossCog__gotDoobers)

    
    def _DistributedBossCog__gotDoobers(self, doobers):
        self.dooberRequest = None
        self.doobers = doobers

    
    def setBattleIds(self, battleNumber, battleAId, battleBId):
        self.battleNumber = battleNumber
        self.battleAId = battleAId
        self.battleBId = battleBId
        self.cr.relatedObjectMgr.abortRequest(self.battleRequest)
        self.battleRequest = self.cr.relatedObjectMgr.requestObjects([
            self.battleAId,
            self.battleBId], allCallback = self._DistributedBossCog__gotBattles)

    
    def _DistributedBossCog__gotBattles(self, battles):
        self.battleRequest = None
        if self.battleA and self.battleA != battles[0]:
            self.battleA.cleanupBattle()
        
        if self.battleB and self.battleB != battles[1]:
            self.battleB.cleanupBattle()
        
        self.battleA = battles[0]
        self.battleB = battles[1]

    
    def _DistributedBossCog__cleanupBattles(self):
        if self.battleA:
            self.battleA.cleanupBattle()
        
        if self.battleB:
            self.battleB.cleanupBattle()
        

    
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
                    taskMgr.add(self._DistributedBossCog__recoverBossDamage, taskName)
                
        

    
    def getBossDamage(self):
        now = globalClock.getFrameTime()
        elapsed = now - self.recoverStartTime
        return max(self.bossDamage - self.recoverRate * elapsed / 60.0, 0)

    
    def _DistributedBossCog__recoverBossDamage(self, task):
        self.bossDamageMovie.setT(self.getBossDamage() * self.bossDamageToMovie)
        return Task.cont

    
    def _DistributedBossCog__makeCagedToon(self):
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

    
    def _DistributedBossCog__cleanupCagedToon(self):
        if self.cagedToon:
            self.cagedToon.removeActive()
            self.cagedToon.delete()
            self.cagedToon = None
        

    
    def _DistributedBossCog__controlToons(self):
        for toonId in self.involvedToons:
            toon = self.cr.doId2do.get(toonId)
            if toon:
                toon.stopLookAround()
                toon.stopSmooth()
            
        
        if self.hasLocalToon():
            self._DistributedBossCog__toMovieMode()
        

    
    def _DistributedBossCog__enableLocalToonSimpleCollisions(self):
        if not (self.toonSphere):
            sphere = CollisionSphere(0, 0, 1, 1)
            
            try:
                sphere.setRespectEffectiveNormal(0)
            except:
                pass

            sphereNode = CollisionNode('SimpleCollisions')
            sphereNode.setFromCollideMask(ToontownGlobals.WallBitmask | ToontownGlobals.FloorBitmask)
            sphereNode.setIntoCollideMask(BitMask32.allOff())
            sphereNode.addSolid(sphere)
            self.toonSphere = NodePath(sphereNode)
            self.toonSphereHandler = CollisionHandlerPusher()
            self.toonSphereHandler.addCollider(self.toonSphere, toonbase.localToon)
        
        self.toonSphere.reparentTo(toonbase.localToon)
        base.cTrav.addCollider(self.toonSphere, self.toonSphereHandler)

    
    def _DistributedBossCog__disableLocalToonSimpleCollisions(self):
        if self.toonSphere:
            base.cTrav.removeCollider(self.toonSphere)
            self.toonSphere.detachNode()
        

    
    def _DistributedBossCog__toOuchMode(self):
        place = self.cr.playGame.getPlace()
        if place and hasattr(place, 'fsm'):
            place.setState('ouch')
        

    
    def _DistributedBossCog__toMovieMode(self):
        place = self.cr.playGame.getPlace()
        if place and hasattr(place, 'fsm'):
            place.setState('movie')
        

    
    def _DistributedBossCog__toWalkMode(self):
        place = self.cr.playGame.getPlace()
        if place and hasattr(place, 'fsm'):
            place.setState('walk')
        

    
    def _DistributedBossCog__toFinalBattleMode(self):
        place = self.cr.playGame.getPlace()
        if place and hasattr(place, 'fsm'):
            place.setState('finalBattle')
        

    
    def _DistributedBossCog__releaseToons(self, finalBattle = 0):
        for toonId in self.involvedToons:
            toon = self.cr.doId2do.get(toonId)
            if toon:
                if self.battleA and toon in self.battleA.toons:
                    pass
                1
                if self.battleB and toon in self.battleB.toons:
                    pass
                1
                toon.startLookAround()
                toon.startSmooth()
                toon.wrtReparentTo(render)
                if toon == toonbase.localToon:
                    if finalBattle:
                        self._DistributedBossCog__toFinalBattleMode()
                    else:
                        self._DistributedBossCog__toWalkMode()
                
            
        

    
    def _DistributedBossCog__stickToonsToFloor(self):
        self._DistributedBossCog__unstickToons()
        rayNode = CollisionNode('stickToonsToFloor')
        rayNode.addSolid(CollisionRay(0.0, 0.0, 10.0, 0.0, 0.0, -1.0))
        rayNode.setFromCollideMask(ToontownGlobals.FloorBitmask)
        rayNode.setIntoCollideMask(BitMask32.allOff())
        ray = NodePath(rayNode)
        lifter = CollisionHandlerFloor()
        lifter.setOffset(ToontownGlobals.FloorOffset)
        for toonId in self.involvedToons:
            toon = toonbase.tcr.doId2do.get(toonId)
            if toon:
                toonRay = ray.instanceTo(toon)
                lifter.addCollider(toonRay, toon)
                base.cTrav.addCollider(toonRay, lifter)
                self._DistributedBossCog__toonsStuckToFloor.append(toonRay)
            
        

    
    def _DistributedBossCog__unstickToons(self):
        for toonRay in self._DistributedBossCog__toonsStuckToFloor:
            base.cTrav.removeCollider(toonRay)
            toonRay.removeNode()
        
        self._DistributedBossCog__toonsStuckToFloor = []

    
    def _DistributedBossCog__stickBossToFloor(self):
        self._DistributedBossCog__unstickBoss()
        self.ray1 = CollisionRay(0.0, 10.0, 20.0, 0.0, 0.0, -1.0)
        self.ray2 = CollisionRay(0.0, 0.0, 20.0, 0.0, 0.0, -1.0)
        self.ray3 = CollisionRay(0.0, -10.0, 20.0, 0.0, 0.0, -1.0)
        rayNode = CollisionNode('stickBossToFloor')
        rayNode.addSolid(self.ray1)
        rayNode.addSolid(self.ray2)
        rayNode.addSolid(self.ray3)
        rayNode.setFromCollideMask(ToontownGlobals.FloorBitmask)
        rayNode.setIntoCollideMask(BitMask32.allOff())
        self.rays = self.attachNewNode(rayNode)
        self.cqueue = CollisionHandlerQueue()
        base.cTrav.addCollider(self.rays, self.cqueue)

    
    def _DistributedBossCog__rollBoss(self, t, fromPos, deltaPos):
        self.setPos(fromPos + deltaPos * t)
        self.cqueue.sortEntries()
        numEntries = self.cqueue.getNumEntries()
        if numEntries != 0:
            for i in range(self.cqueue.getNumEntries() - 1, -1, -1):
                entry = self.cqueue.getEntry(i)
                solid = entry.getFrom()
                if solid == self.ray1:
                    self.e1 = entry
                elif solid == self.ray2:
                    self.e2 = entry
                elif solid == self.ray3:
                    self.e3 = entry
                else:
                    self.notify.warning('Unexpected ray in __liftBoss')
                    return None
            
            self.cqueue.clearEntries()
        
        if self.e1 and self.e2:
            pass
        if not (self.e3):
            self.notify.debug('Some points missed in __liftBoss')
            return None
        
        p1 = self.e1.getSurfacePoint(self)
        p2 = self.e2.getSurfacePoint(self)
        p3 = self.e3.getSurfacePoint(self)
        p2a = (p1 + p3) / 2
        if p2a[2] > p2[2]:
            center = p2a
        else:
            center = p2
        self.setZ(self, center[2])
        if p1[2] > p2[2] + 0.01 or p3[2] > p2[2] + 0.01:
            mat = Mat4()
            if abs(p3[2] - center[2]) < abs(p1[2] - center[2]):
                lookAt(mat, Vec3(p1 - center), CSDefault)
            else:
                lookAt(mat, Vec3(center - p3), CSDefault)
            self.rotateNode.setMat(mat)
        else:
            self.rotateNode.clearTransform()

    
    def _DistributedBossCog__unstickBoss(self):
        if self.rays:
            base.cTrav.removeCollider(self.rays)
            self.rays.removeNode()
        
        self.rays = None
        self.ray1 = None
        self.ray2 = None
        self.ray3 = None
        self.e1 = None
        self.e2 = None
        self.e3 = None
        self.rotateNode.clearTransform()

    
    def _DistributedBossCog__walkToonToPromotion(self, toonId, delay, mopath, track, delayDeletes):
        toon = toonbase.tcr.doId2do.get(toonId)
        if toon:
            destPos = toon.getPos()
            self._DistributedBossCog__placeToonInElevator(toon)
            toon.wrtReparentTo(render)
            ival = Sequence(Wait(delay), Func(toon.suit.setPlayRate, 1, 'walk'), Func(toon.suit.loop, 'walk'), toon.posInterval(1, Point3(0, 90, 20)), ParallelEndTogether(MopathInterval(mopath, toon), toon.posInterval(2, destPos, blendType = 'noBlend')), Func(toon.suit.loop, 'neutral'))
            track.append(ival)
            delayDeletes.append(DelayDelete.DelayDelete(toon))
        

    
    def _DistributedBossCog__loseCogSuits(self, toons, battleNode):
        seq = Sequence()
        if not toons:
            return seq
        
        seq.append(Func(camera.setPosHpr, battleNode, 0, 18, 5, -180, 0, 0))
        suitsOff = Parallel()
        for toonId in toons:
            toon = toonbase.tcr.doId2do.get(toonId)
            if toon:
                dustCloud = DustCloud.DustCloud()
                dustCloud.setPos(0, 2, 3)
                dustCloud.setScale(0.5)
                dustCloud.setDepthWrite(0)
                dustCloud.setBin('fixed', 0)
                dustCloud.createTrack()
                suitsOff.append(Sequence(Func(dustCloud.reparentTo, toon), Parallel(dustCloud.track, Sequence(Wait(0.29999999999999999), Func(toon.takeOffSuit), Func(toon.sadEyes), Func(toon.blinkEyes), Func(toon.play, 'slip-backward'), Wait(0.69999999999999996))), Func(dustCloud.detachNode)))
            
        
        seq.append(suitsOff)
        return seq

    
    def _DistributedBossCog__toonNormalEyes(self, toons):
        seq = Sequence()
        for toonId in toons:
            toon = toonbase.tcr.doId2do.get(toonId)
            if toon:
                seq.append(Func(toon.normalEyes))
                seq.append(Func(toon.blinkEyes))
            
        
        return seq

    
    def _DistributedBossCog__walkDoober(self, suit, delay, turnPos, track, delayDeletes):
        turnPos = Point3(*turnPos)
        turnPosDown = Point3(*ToontownGlobals.BossCogDooberTurnPosDown)
        flyPos = Point3(*ToontownGlobals.BossCogDooberFlyPos)
        seq = Sequence(Func(suit.headsUp, turnPos), Wait(delay), Func(suit.loop, 'walk', 0), self._DistributedBossCog__walkSuitToPoint(suit, suit.getPos(), turnPos), self._DistributedBossCog__walkSuitToPoint(suit, turnPos, turnPosDown), self._DistributedBossCog__walkSuitToPoint(suit, turnPosDown, flyPos), suit.beginSupaFlyMove(flyPos, 0, 'flyAway'), Func(suit.fsm.request, 'Off'))
        track.append(seq)
        delayDeletes.append(DelayDelete.DelayDelete(suit))

    
    def _DistributedBossCog__walkSuitToPoint(self, node, fromPos, toPos):
        vector = Vec3(toPos - fromPos)
        distance = vector.length()
        time = distance / ToontownGlobals.SuitWalkSpeed * 1.8
        return Sequence(Func(node.setPos, fromPos), Func(node.headsUp, toPos), node.posInterval(time, toPos))

    
    def _DistributedBossCog__rollBossToPoint(self, fromPos, fromHpr, toPos, toHpr, reverse):
        vector = Vec3(toPos - fromPos)
        distance = vector.length()
        if toHpr == None:
            mat = Mat3()
            headsUp(mat, vector, CSDefault)
            scale = VBase3()
            shear = VBase3()
            toHpr = VBase3()
            decomposeMatrix(mat, scale, shear, toHpr, CSDefault)
        
        if fromHpr:
            newH = PythonUtil.fitDestAngle2Src(fromHpr[0], toHpr[0])
            toHpr = VBase3(newH, 0, 0)
        else:
            fromHpr = toHpr
        turnTime = abs(toHpr[0] - fromHpr[0]) / ToontownGlobals.BossCogTurnSpeed
        if toHpr[0] < fromHpr[0]:
            leftRate = ToontownGlobals.BossCogTreadSpeed
        else:
            leftRate = -(ToontownGlobals.BossCogTreadSpeed)
        if reverse:
            rollTreadRate = -(ToontownGlobals.BossCogTreadSpeed)
        else:
            rollTreadRate = ToontownGlobals.BossCogTreadSpeed
        rollTime = distance / ToontownGlobals.BossCogRollSpeed
        deltaPos = toPos - fromPos
        track = Sequence(Func(self.setPos, fromPos), Func(self.headsUp, toPos), Parallel(self.hprInterval(turnTime, toHpr, fromHpr), self.rollLeftTreads(turnTime, leftRate), self.rollRightTreads(turnTime, -leftRate)), Parallel(LerpFunctionInterval(self._DistributedBossCog__rollBoss, duration = rollTime, extraArgs = [
            fromPos,
            deltaPos]), self.rollLeftTreads(rollTime, rollTreadRate), self.rollRightTreads(rollTime, rollTreadRate)))
        return (track, toHpr)

    
    def _DistributedBossCog__makeIntroductionMovie(self, delayDeletes):
        track = Parallel()
        camera.reparentTo(render)
        camera.setPosHpr(0, 25, 30, 0, 0, 0)
        base.camLens.setFov(ToontownGlobals.CogHQCameraFov)
        dooberTrack = Parallel()
        if self.doobers:
            self._DistributedBossCog__doobersToPromotionPosition(self.doobers[:4], self.battleANode)
            self._DistributedBossCog__doobersToPromotionPosition(self.doobers[4:], self.battleBNode)
            turnPosA = ToontownGlobals.BossCogDooberTurnPosA
            turnPosB = ToontownGlobals.BossCogDooberTurnPosB
            self._DistributedBossCog__walkDoober(self.doobers[0], 0, turnPosA, dooberTrack, delayDeletes)
            self._DistributedBossCog__walkDoober(self.doobers[1], 4, turnPosA, dooberTrack, delayDeletes)
            self._DistributedBossCog__walkDoober(self.doobers[2], 8, turnPosA, dooberTrack, delayDeletes)
            self._DistributedBossCog__walkDoober(self.doobers[3], 12, turnPosA, dooberTrack, delayDeletes)
            self._DistributedBossCog__walkDoober(self.doobers[7], 2, turnPosB, dooberTrack, delayDeletes)
            self._DistributedBossCog__walkDoober(self.doobers[6], 6, turnPosB, dooberTrack, delayDeletes)
            self._DistributedBossCog__walkDoober(self.doobers[5], 10, turnPosB, dooberTrack, delayDeletes)
            self._DistributedBossCog__walkDoober(self.doobers[4], 14, turnPosB, dooberTrack, delayDeletes)
        
        toonTrack = Parallel()
        self._DistributedBossCog__toonsToPromotionPosition(self.toonsA, self.battleANode)
        self._DistributedBossCog__toonsToPromotionPosition(self.toonsB, self.battleBNode)
        delay = 0
        for toonId in self.toonsA:
            self._DistributedBossCog__walkToonToPromotion(toonId, delay, self.toonsEnterA, toonTrack, delayDeletes)
            delay += 1
        
        for toonId in self.toonsB:
            self._DistributedBossCog__walkToonToPromotion(toonId, delay, self.toonsEnterB, toonTrack, delayDeletes)
            delay += 1
        
        toonTrack.append(Sequence(Wait(delay), self.closeDoors))
        self.rampA.request('extended')
        self.rampB.request('extended')
        self.rampC.request('retracted')
        self.clearChat()
        self.cagedToon.clearChat()
        promoteDoobers = Localizer.BossCogPromoteDoobers % AvatarDNA.getDeptFullnameP(self.style.dept)
        doobersAway = Localizer.BossCogDoobersAway[self.style.dept]
        welcomeToons = Localizer.BossCogWelcomeToons
        promoteToons = Localizer.BossCogPromoteToons % AvatarDNA.getDeptFullnameP(self.style.dept)
        discoverToons = Localizer.BossCogDiscoverToons
        attackToons = Localizer.BossCogAttackToons
        interruptBoss = Localizer.CagedToonInterruptBoss
        rescueQuery = Localizer.CagedToonRescueQuery
        bossAnimTrack = Sequence(ActorInterval(self, 'Ff_speech', startTime = 2, duration = 10, loop = 1), ActorInterval(self, 'ltTurn2Wave', duration = 2), ActorInterval(self, 'wave', duration = 4, loop = 1), ActorInterval(self, 'ltTurn2Wave', startTime = 2, endTime = 0), ActorInterval(self, 'Ff_speech', duration = 7, loop = 1))
        track.append(bossAnimTrack)
        dialogTrack = Track((0, Parallel(camera.posHprInterval(8, Point3(-22, -100, 35), Point3(-10, -13, 0), blendType = 'easeInOut'), IndirectInterval(toonTrack, 0, 18))), (5.5999999999999996, Func(self.setChatAbsolute, promoteDoobers, CFSpeech)), (9, IndirectInterval(dooberTrack, 0, 9)), (10, Sequence(Func(self.clearChat), Func(camera.setPosHpr, -23.100000000000001, 15.699999999999999, 17.199999999999999, -160, -2.3999999999999999, 0))), (12, Func(self.setChatAbsolute, doobersAway, CFSpeech)), (16, Parallel(Func(self.clearChat), Func(camera.setPosHpr, -25, -99, 10, -14, 10, 0), IndirectInterval(dooberTrack, 14), IndirectInterval(toonTrack, 30))), (18, Func(self.setChatAbsolute, welcomeToons, CFSpeech)), (22, Func(self.setChatAbsolute, promoteToons, CFSpeech)), (22.199999999999999, Sequence(Func(self.cagedToon.nametag3d.setScale, 2), Func(self.cagedToon.setChatAbsolute, interruptBoss, CFSpeech), ActorInterval(self.cagedToon, 'wave'), Func(self.cagedToon.loop, 'neutral'))), (25, Sequence(Func(self.clearChat), Func(self.cagedToon.clearChat), Func(camera.setPosHpr, -12, -15, 27, -151, -15, 0), ActorInterval(self, 'Ff_lookRt'))), (27, Sequence(Func(self.cagedToon.setChatAbsolute, rescueQuery, CFSpeech), Func(camera.setPosHpr, -12, 48, 94, -26, 20, 0), ActorInterval(self.cagedToon, 'wave'), Func(self.cagedToon.loop, 'neutral'))), (31, Sequence(Func(camera.setPosHpr, -20, -35, 10, -88, 25, 0), Func(self.setChatAbsolute, discoverToons, CFSpeech), Func(self.cagedToon.nametag3d.setScale, 1), Func(self.cagedToon.clearChat), ActorInterval(self, 'turn2Fb'))), (34, Sequence(Func(self.clearChat), self._DistributedBossCog__loseCogSuits(self.toonsA, self.battleANode), self._DistributedBossCog__loseCogSuits(self.toonsB, self.battleBNode))), (37, Sequence(self._DistributedBossCog__toonNormalEyes(self.involvedToons), Func(camera.setPosHpr, -23.399999999999999, -145.59999999999999, 44.0, -10.0, -12.5, 0), Func(self.loop, 'Fb_neutral'), Func(self.rampA.request, 'retract'), Func(self.rampB.request, 'retract'), Parallel(self._DistributedBossCog__backupToonsToBattlePosition(self.toonsA, self.battleANode), self._DistributedBossCog__backupToonsToBattlePosition(self.toonsB, self.battleBNode), Sequence(Wait(2), Func(self.setChatAbsolute, attackToons, CFSpeech))))))
        track.append(dialogTrack)
        return Sequence(Func(self._DistributedBossCog__stickToonsToFloor), track, Func(self._DistributedBossCog__unstickToons), name = self.uniqueName('Introduction'))

    
    def _DistributedBossCog__makeRollToBattleTwoMovie(self):
        startPos = Point3(ToontownGlobals.BossCogBattleOnePosHpr[0], ToontownGlobals.BossCogBattleOnePosHpr[1], ToontownGlobals.BossCogBattleOnePosHpr[2])
        if self.arenaSide:
            topRampPos = Point3(*ToontownGlobals.BossCogTopRampPosB)
            topRampTurnPos = Point3(*ToontownGlobals.BossCogTopRampTurnPosB)
            p3Pos = Point3(*ToontownGlobals.BossCogP3PosB)
        else:
            topRampPos = Point3(*ToontownGlobals.BossCogTopRampPosA)
            topRampTurnPos = Point3(*ToontownGlobals.BossCogTopRampTurnPosA)
            p3Pos = Point3(*ToontownGlobals.BossCogP3PosA)
        battlePos = Point3(ToontownGlobals.BossCogBattleTwoPosHpr[0], ToontownGlobals.BossCogBattleTwoPosHpr[1], ToontownGlobals.BossCogBattleTwoPosHpr[2])
        battleHpr = VBase3(ToontownGlobals.BossCogBattleTwoPosHpr[3], ToontownGlobals.BossCogBattleTwoPosHpr[4], ToontownGlobals.BossCogBattleTwoPosHpr[5])
        bossTrack = Sequence()
        bossTrack.append(Func(self.getGeomNode().setH, 180))
        bossTrack.append(Func(self.loop, 'Fb_neutral'))
        (track, hpr) = self._DistributedBossCog__rollBossToPoint(startPos, None, topRampPos, None, 0)
        bossTrack.append(track)
        (track, hpr) = self._DistributedBossCog__rollBossToPoint(topRampPos, hpr, topRampTurnPos, None, 0)
        bossTrack.append(track)
        (track, hpr) = self._DistributedBossCog__rollBossToPoint(topRampTurnPos, hpr, p3Pos, None, 0)
        bossTrack.append(track)
        (track, hpr) = self._DistributedBossCog__rollBossToPoint(p3Pos, hpr, battlePos, None, 0)
        bossTrack.append(track)
        return Sequence(bossTrack, Func(self.getGeomNode().setH, 0), name = self.uniqueName('BattleTwo'))

    
    def makeCageDropMovie(self, hasLocalToon):
        name = self.uniqueName('CageDrop')
        seq = Sequence(name = name)
        seq.append(Func(self.cage.setPos, self.cagePos[self.cageIndex]))
        if hasLocalToon:
            seq += [
                Func(camera.reparentTo, render),
                Func(camera.setPosHpr, self.cage, 0, -50, 0, 0, 0, 0),
                Func(base.camLens.setFov, ToontownGlobals.CogHQCameraFov),
                Func(self.hide)]
        
        seq += [
            Wait(0.5),
            Parallel(self.cage.posInterval(1, self.cagePos[self.cageIndex + 1], blendType = 'easeInOut'), SoundInterval(self.cageLowerSfx, duration = 1)),
            Func(self.cagedToon.nametag3d.setScale, 2),
            Func(self.cagedToon.setChatAbsolute, Localizer.CagedToonDrop[self.cageIndex], CFSpeech),
            Wait(3),
            Func(self.cagedToon.nametag3d.setScale, 1),
            Func(self.cagedToon.clearChat)]
        if hasLocalToon:
            seq += [
                Func(self.show),
                Func(camera.reparentTo, toonbase.localToon),
                Func(camera.setPos, toonbase.localToon.cameraPositions[0][0]),
                Func(camera.setHpr, 0, 0, 0)]
        
        self.cageIndex += 1
        return seq

    
    def _DistributedBossCog__makeBossDamageMovie(self):
        startPos = Point3(ToontownGlobals.BossCogBattleTwoPosHpr[0], ToontownGlobals.BossCogBattleTwoPosHpr[1], ToontownGlobals.BossCogBattleTwoPosHpr[2])
        startHpr = Point3(*ToontownGlobals.BossCogBattleThreeHpr)
        bottomPos = Point3(*ToontownGlobals.BossCogBottomPos)
        deathPos = Point3(*ToontownGlobals.BossCogDeathPos)
        self.setPosHpr(startPos, startHpr)
        bossTrack = Sequence()
        bossTrack.append(Func(self.loop, 'Fb_neutral'))
        (track, hpr) = self._DistributedBossCog__rollBossToPoint(startPos, startHpr, bottomPos, None, 1)
        bossTrack.append(track)
        (track, hpr) = self._DistributedBossCog__rollBossToPoint(bottomPos, startHpr, deathPos, None, 1)
        bossTrack.append(track)
        duration = bossTrack.getDuration()
        return bossTrack

    
    def _DistributedBossCog__makeCageOpenMovie(self):
        name = self.uniqueName('CageOpen')
        seq = Sequence(Func(self.cage.setPos, self.cagePos[4]), Func(self.cageDoor.setHpr, VBase3(0, 0, 0)), Func(self.cagedToon.setPos, Point3(0, -2, 0)), Parallel(self.cage.posInterval(0.5, self.cagePos[5], blendType = 'easeOut'), SoundInterval(self.cageLowerSfx, duration = 0.5)), Parallel(self.cageDoor.hprInterval(0.5, VBase3(0, 90, 0), blendType = 'easeOut'), Sequence(SoundInterval(self.cageDoorSfx), duration = 0)), Wait(0.20000000000000001), Func(self.cagedToon.loop, 'walk'), self.cagedToon.posInterval(0.80000000000000004, Point3(0, -6, 0)), Func(self.cagedToon.setChatAbsolute, Localizer.CagedToonYippee, CFSpeech), ActorInterval(self.cagedToon, 'jump'), Func(self.cagedToon.loop, 'neutral'), Func(self.cagedToon.headsUp, toonbase.localToon), Func(self.cagedToon.setLocalPageChat, Localizer.CagedToonThankYou, 0), Func(camera.reparentTo, toonbase.localToon), Func(camera.setPos, 0, -9, 9), Func(camera.lookAt, self.cagedToon, Point3(0, 0, 2)), name = name)
        return seq

    
    def _DistributedBossCog__showOnscreenMessage(self, text):
        if self.onscreenMessage:
            self.onscreenMessage.destroy()
            self.onscreenMessage = None
        
        self.onscreenMessage = DirectLabel(text = text, text_fg = VBase4(1, 1, 1, 1), text_align = TextNode.ACenter, relief = None, pos = (0, 0, 0.34999999999999998), scale = 0.10000000000000001)

    
    def _DistributedBossCog__clearOnscreenMessage(self):
        if self.onscreenMessage:
            self.onscreenMessage.destroy()
            self.onscreenMessage = None
        

    
    def _DistributedBossCog__showWaitingMessage(self, task):
        self._DistributedBossCog__showOnscreenMessage(Localizer.BuildingWaitingForVictors)

    
    def _DistributedBossCog__placeCageShadow(self):
        if self.cageShadow == None:
            self.cageShadow = loader.loadModel('phase_3/models/props/drop_shadow')
            self.cageShadow.setPos(0, 77.900000000000006, 18)
            self.cageShadow.setColorScale(1, 1, 1, 0.59999999999999998)
        
        self.cageShadow.reparentTo(render)

    
    def _DistributedBossCog__removeCageShadow(self):
        if self.cageShadow != None:
            self.cageShadow.detachNode()
        

    
    def setCageIndex(self, cageIndex):
        self.cageIndex = cageIndex
        self.cage.setPos(self.cagePos[self.cageIndex])
        if self.cageIndex >= 4:
            self._DistributedBossCog__placeCageShadow()
        else:
            self._DistributedBossCog__removeCageShadow()

    
    def _DistributedBossCog__loadEnvironment(self):
        self.geom = loader.loadModel('phase_9/models/cogHQ/BossRoomHQ')
        self.rampA = self._DistributedBossCog__findRamp('rampA', '**/west_ramp2')
        self.rampB = self._DistributedBossCog__findRamp('rampB', '**/west_ramp')
        self.rampC = self._DistributedBossCog__findRamp('rampC', '**/west_ramp1')
        self.cage = self.geom.find('**/cage')
        self._DistributedBossCog__setupElevator()
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
        self.rope.ropeNode.setUvScale(VBase2(1 / 0.80000000000000004, 0.80000000000000004))
        self.rope.setTexture(self.cage.findTexture('hq_chain'))
        self.rope.setTransparency(1)
        self.elevatorMusic = base.loadMusic('phase_7/audio/bgm/tt_elevator.mid')
        self.stingMusic = base.loadMusic('phase_7/audio/bgm/encntr_suit_winning_indoor.mid')
        self.promotionMusic = base.loadMusic('phase_7/audio/bgm/encntr_suit_winning_indoor.mid')
        self.battleOneMusic = base.loadMusic('phase_3.5/audio/bgm/encntr_general_bg.mid')
        self.betweenBattleMusic = base.loadMusic('phase_9/audio/bgm/encntr_toon_winning.mid')
        self.battleTwoMusic = base.loadMusic('phase_7/audio/bgm/encntr_suit_winning_indoor.mid')
        self.battleThreeMusic = base.loadMusic('phase_7/audio/bgm/encntr_suit_winning_indoor.mid')
        self.epilogueMusic = base.loadMusic('phase_9/audio/bgm/encntr_hall_of_fame.mid')
        self.geom.reparentTo(render)

    
    def _DistributedBossCog__setupElevator(self):
        elevatorEntrance = self.geom.find('**/elevatorEntrance')
        elevatorEntrance.getChildren().detach()
        elevatorEntrance.setScale(1)
        self.elevatorModel = loader.loadModelCopy('phase_9/models/cogHQ/cogHQ_elevator')
        self.elevatorModel.reparentTo(elevatorEntrance)
        self.leftDoor = self.elevatorModel.find('**/left-door')
        self.rightDoor = self.elevatorModel.find('**/right-door')
        self.openSfx = base.loadSfx('phase_9/audio/sfx/CHQ_FACT_door_open_sliding.mp3')
        self.finalOpenSfx = base.loadSfx('phase_9/audio/sfx/CHQ_FACT_door_open_final.mp3')
        self.closeSfx = base.loadSfx('phase_9/audio/sfx/CHQ_FACT_door_open_sliding.mp3')
        self.finalCloseSfx = base.loadSfx('phase_9/audio/sfx/CHQ_FACT_door_open_final.mp3')
        self.openDoors = ElevatorUtils.getOpenInterval(self, self.leftDoor, self.rightDoor, self.openSfx, self.finalOpenSfx, 1)
        self.closeDoors = ElevatorUtils.getCloseInterval(self, self.leftDoor, self.rightDoor, self.closeSfx, self.finalCloseSfx, 1)
        self.closeDoors.start()
        self.closeDoors.finish()

    
    def _DistributedBossCog__putToonInCogSuit(self, toon):
        if not (toon.isDisguised):
            deptIndex = AvatarDNA.suitDepts.index(self.style.dept)
            toon.setCogIndex(deptIndex)
        
        toon.getGeomNode().hide()

    
    def _DistributedBossCog__placeToonInElevator(self, toon):
        self._DistributedBossCog__putToonInCogSuit(toon)
        toonIndex = self.involvedToons.index(toon.doId)
        toon.reparentTo(self.elevatorModel)
        toon.setPos(*ElevatorConstants.BigElevatorPoints[toonIndex])
        toon.setHpr(180, 0, 0)
        toon.suit.loop('neutral')

    
    def _DistributedBossCog__unloadEnvironment(self):
        self.geom.removeNode()
        del self.geom
        del self.cage
        self.rampA.requestFinalState()
        self.rampB.requestFinalState()
        self.rampC.requestFinalState()
        del self.rampA
        del self.rampB
        del self.rampC

    
    def _DistributedBossCog__loadMopaths(self):
        self.toonsEnterA = Mopath.Mopath()
        self.toonsEnterA.loadFile('phase_9/paths/bossBattle-toonsEnterA')
        self.toonsEnterA.fFaceForward = 1
        self.toonsEnterA.timeScale = 35
        self.toonsEnterB = Mopath.Mopath()
        self.toonsEnterB.loadFile('phase_9/paths/bossBattle-toonsEnterB')
        self.toonsEnterB.fFaceForward = 1
        self.toonsEnterB.timeScale = 35

    
    def _DistributedBossCog__unloadMopaths(self):
        self.toonsEnterA.reset()
        self.toonsEnterB.reset()

    
    def _DistributedBossCog__findRamp(self, name, path):
        ramp = self.geom.find(path)
        children = ramp.getChildren()
        animate = ramp.attachNewNode(name)
        children.reparentTo(animate)
        fsm = FSM.FSM(name, [
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
            State.State('off', Functor(self.enterRampOff, animate), Functor(self.exitRampOff, animate))], 'off', 'off', onUndefTransition = FSM.FSM.DISALLOW)
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
        self._DistributedBossCog__cleanupIntervals()
        self.hide()
        self.clearChat()
        if self.cagedToon:
            self.cagedToon.clearChat()
        
        if self.rampA:
            self.rampA.request('off')
        
        if self.rampB:
            self.rampB.request('off')
        
        if self.rampC:
            self.rampC.request('off')
        
        self._DistributedBossCog__toWalkMode()

    
    def exitOff(self):
        self.show()

    
    def enterWaitForToons(self):
        self._DistributedBossCog__cleanupIntervals()
        self.hide()
        self.geom.hide()
        if self.gotAllToons:
            self._DistributedBossCog__doneWaitForToons()
        else:
            self.accept('gotAllToons', self._DistributedBossCog__doneWaitForToons)
        self.cagedToon.removeActive()
        self.transitions = Transitions.Transitions(loader)
        self.transitions.IrisModelName = 'phase_3/models/misc/iris'
        self.transitions.FadeModelName = 'phase_3/models/misc/fade'
        self.transitions.fadeScreen(alpha = 1)
        NametagGlobals.setMasterArrowsOn(0)

    
    def _DistributedBossCog__doneWaitForToons(self):
        self.doneBarrier()

    
    def exitWaitForToons(self):
        self.show()
        self.geom.show()
        self.cagedToon.addActive()
        self.transitions.noFade()
        del self.transitions
        NametagGlobals.setMasterArrowsOn(1)

    
    def enterElevator(self):
        self.rampA.request('extended')
        self.rampB.request('extended')
        self.rampC.request('retracted')
        self.setCageIndex(0)
        self.reparentTo(render)
        self.setPosHpr(*ToontownGlobals.BossCogBattleOnePosHpr)
        self.happy = 1
        self.raised = 1
        self.forward = 1
        self.doAnimate()
        self.cagedToon.removeActive()
        for toonId in self.involvedToons:
            toon = self.cr.doId2do.get(toonId)
            if toon:
                toon.stopLookAround()
                toon.stopSmooth()
                self._DistributedBossCog__placeToonInElevator(toon)
            
        
        self._DistributedBossCog__toMovieMode()
        camera.reparentTo(self.elevatorModel)
        camera.setH(180)
        camera.setPos(0, 30, 8)
        base.playMusic(self.elevatorMusic, looping = 1, volume = 1.0)
        ival = Sequence(ElevatorUtils.getRideElevatorInterval(big = 1), ElevatorUtils.getRideElevatorInterval(big = 1), self.openDoors, Func(camera.wrtReparentTo, render), Func(self._DistributedBossCog__doneElevator))
        intervalName = 'ElevatorMovie'
        ival.start()
        self.activeIntervals[intervalName] = ival

    
    def _DistributedBossCog__doneElevator(self):
        self.doneBarrier()

    
    def exitElevator(self):
        intervalName = 'ElevatorMovie'
        self.clearInterval(intervalName)
        self.elevatorMusic.stop()
        self.cagedToon.addActive()
        ElevatorUtils.closeDoors(self.leftDoor, self.rightDoor, big = 1)

    
    def enterIntroduction(self):
        self._DistributedBossCog__controlToons()
        ElevatorUtils.openDoors(self.leftDoor, self.rightDoor, big = 1)
        self.rampA.request('extended')
        self.rampB.request('extended')
        self.rampC.request('retracted')
        self.setCageIndex(0)
        self.reparentTo(render)
        self.setPosHpr(*ToontownGlobals.BossCogBattleOnePosHpr)
        self.stopAnimate()
        NametagGlobals.setMasterArrowsOn(0)
        intervalName = 'IntroductionMovie'
        delayDeletes = []
        seq = Sequence(self._DistributedBossCog__makeIntroductionMovie(delayDeletes), Func(self._DistributedBossCog__beginBattleOne), name = intervalName)
        seq.delayDeletes = delayDeletes
        seq.start()
        self.activeIntervals[intervalName] = seq
        base.playMusic(self.promotionMusic, looping = 1, volume = 0.90000000000000002)

    
    def _DistributedBossCog__beginBattleOne(self):
        intervalName = 'IntroductionMovie'
        self.clearInterval(intervalName)
        self.doneBarrier()

    
    def exitIntroduction(self):
        intervalName = 'IntroductionMovie'
        self.clearInterval(intervalName)
        self._DistributedBossCog__unstickToons()
        self._DistributedBossCog__releaseToons()
        NametagGlobals.setMasterArrowsOn(1)
        ElevatorUtils.closeDoors(self.leftDoor, self.rightDoor, big = 1)
        self.promotionMusic.stop()

    
    def enterBattleOne(self):
        self._DistributedBossCog__cleanupIntervals()
        mult = ToontownBattleGlobals.getBossBattleCreditMultiplier(1)
        toonbase.localToon.inventory.setBattleCreditMultiplier(mult)
        self.reparentTo(render)
        self.setPosHpr(*ToontownGlobals.BossCogBattleOnePosHpr)
        self.clearChat()
        self.cagedToon.clearChat()
        self.rampA.request('retract')
        self.rampB.request('retract')
        self.rampC.request('retract')
        self._DistributedBossCog__toonsToBattlePosition(self.toonsA, self.battleANode)
        self._DistributedBossCog__toonsToBattlePosition(self.toonsB, self.battleBNode)
        if self.battleA == None or self.battleB == None:
            cageIndex = 1
        else:
            cageIndex = 0
        self.setCageIndex(cageIndex)
        self._DistributedBossCog__releaseToons()
        base.playMusic(self.battleOneMusic, looping = 1, volume = 0.90000000000000002)

    
    def exitBattleOne(self):
        self._DistributedBossCog__cleanupBattles()
        self.battleOneMusic.stop()
        toonbase.localToon.inventory.setBattleCreditMultiplier(1)

    
    def enterRollToBattleTwo(self):
        self._DistributedBossCog__releaseToons()
        if self.arenaSide:
            self.rampA.request('retract')
            self.rampB.request('extend')
        else:
            self.rampA.request('extend')
            self.rampB.request('retract')
        self.rampC.request('retract')
        self.reparentTo(render)
        self.setCageIndex(2)
        self._DistributedBossCog__stickBossToFloor()
        intervalName = 'RollToBattleTwo'
        seq = Sequence(self._DistributedBossCog__makeRollToBattleTwoMovie(), Func(self._DistributedBossCog__onToPrepareBattleTwo), name = intervalName)
        seq.start()
        self.activeIntervals[intervalName] = seq
        base.playMusic(self.betweenBattleMusic, looping = 1, volume = 0.90000000000000002)

    
    def _DistributedBossCog__onToPrepareBattleTwo(self):
        self._DistributedBossCog__unstickBoss()
        self.setPosHpr(*ToontownGlobals.BossCogBattleTwoPosHpr)
        self.doneBarrier()

    
    def exitRollToBattleTwo(self):
        self._DistributedBossCog__unstickBoss()
        intervalName = 'RollToBattleTwo'
        self.clearInterval(intervalName)
        self.betweenBattleMusic.stop()

    
    def enterPrepareBattleTwo(self):
        self._DistributedBossCog__cleanupIntervals()
        self._DistributedBossCog__controlToons()
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
        (base.camLens.setFov(ToontownGlobals.CogHQCameraFov),)
        self.hide()
        self.acceptOnce('doneChatPage', self._DistributedBossCog__onToBattleTwo)
        self.cagedToon.setLocalPageChat(Localizer.CagedToonPrepareBattleTwo, 1)
        base.playMusic(self.stingMusic, looping = 0, volume = 1.0)

    
    def _DistributedBossCog__onToBattleTwo(self, elapsed):
        self.doneBarrier()
        taskMgr.doMethodLater(1, self._DistributedBossCog__showWaitingMessage, self.uniqueName('WaitingMessage'))

    
    def exitPrepareBattleTwo(self):
        self.show()
        taskMgr.remove(self.uniqueName('WaitingMessage'))
        self.ignore('doneChatPage')
        self._DistributedBossCog__clearOnscreenMessage()
        self.stingMusic.stop()

    
    def enterBattleTwo(self):
        self._DistributedBossCog__cleanupIntervals()
        mult = ToontownBattleGlobals.getBossBattleCreditMultiplier(2)
        toonbase.localToon.inventory.setBattleCreditMultiplier(mult)
        self.reparentTo(render)
        self.setPosHpr(*ToontownGlobals.BossCogBattleTwoPosHpr)
        self.clearChat()
        self.cagedToon.clearChat()
        self.rampA.request('retract')
        self.rampB.request('retract')
        self.rampC.request('retract')
        self._DistributedBossCog__releaseToons()
        self._DistributedBossCog__toonsToBattlePosition(self.toonsA, self.battleANode)
        self._DistributedBossCog__toonsToBattlePosition(self.toonsB, self.battleBNode)
        if self.battleA == None or self.battleB == None:
            cageIndex = 3
        else:
            cageIndex = 2
        self.setCageIndex(cageIndex)
        base.playMusic(self.battleTwoMusic, looping = 1, volume = 0.90000000000000002)

    
    def exitBattleTwo(self):
        intervalName = self.uniqueName('cageDrop')
        self.clearInterval(intervalName)
        self._DistributedBossCog__cleanupBattles()
        self.battleTwoMusic.stop()
        toonbase.localToon.inventory.setBattleCreditMultiplier(1)

    
    def enterPrepareBattleThree(self):
        self._DistributedBossCog__cleanupIntervals()
        self._DistributedBossCog__controlToons()
        self.clearChat()
        self.cagedToon.clearChat()
        self.reparentTo(render)
        self.rampA.request('retract')
        self.rampB.request('retract')
        self.rampC.request('extend')
        self.setCageIndex(4)
        camera.reparentTo(render)
        camera.setPosHpr(self.cage, 0, -17, 3.2999999999999998, 0, 0, 0)
        (base.camLens.setFov(ToontownGlobals.CogHQCameraFov),)
        self.hide()
        self.acceptOnce('doneChatPage', self._DistributedBossCog__onToBattleThree)
        self.cagedToon.setLocalPageChat(Localizer.CagedToonPrepareBattleThree, 1)
        base.playMusic(self.betweenBattleMusic, looping = 1, volume = 0.90000000000000002)

    
    def _DistributedBossCog__onToBattleThree(self, elapsed):
        self.doneBarrier()
        taskMgr.doMethodLater(1, self._DistributedBossCog__showWaitingMessage, self.uniqueName('WaitingMessage'))

    
    def exitPrepareBattleThree(self):
        self.show()
        taskMgr.remove(self.uniqueName('WaitingMessage'))
        self.ignore('doneChatPage')
        intervalName = 'PrepareBattleThree'
        self.clearInterval(intervalName)
        self._DistributedBossCog__clearOnscreenMessage()
        self.betweenBattleMusic.stop()

    
    def enterBattleThree(self):
        self._DistributedBossCog__cleanupIntervals()
        self._DistributedBossCog__releaseToons(finalBattle = 1)
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
        self.accept('enterCage', self._DistributedBossCog__touchedCage)
        self.accept('pieSplat', self._DistributedBossCog__pieSplat)
        self.accept('localPieSplat', self._DistributedBossCog__localPieSplat)
        self.accept('outOfPies', self._DistributedBossCog__outOfPies)
        self.accept('begin-pie', self._DistributedBossCog__foundPieButton)
        base.camLens.setFov(ToontownGlobals.BossBattleCameraFov)
        taskMgr.doMethodLater(30, self._DistributedBossCog__howToGetPies, self.uniqueName('PieAdvice'))
        self._DistributedBossCog__stickBossToFloor()
        self.bossDamageMovie = self._DistributedBossCog__makeBossDamageMovie()
        bossDoneEventName = self.uniqueName('DestroyedBoss')
        self.bossDamageMovie.setDoneEvent(bossDoneEventName)
        self.acceptOnce(bossDoneEventName, self._DistributedBossCog__doneBattleThree)
        self.bossMaxDamage = ToontownGlobals.BossCogMaxDamage
        self.bossDamageToMovie = self.bossDamageMovie.getDuration() / self.bossMaxDamage
        self.bossDamageMovie.setT(self.bossDamage * self.bossDamageToMovie)
        base.playMusic(self.battleThreeMusic, looping = 1, volume = 0.90000000000000002)

    
    def _DistributedBossCog__doneBattleThree(self):
        self.setState('NearVictory')
        self._DistributedBossCog__unstickBoss()

    
    def exitBattleThree(self):
        bossDoneEventName = self.uniqueName('DestroyedBoss')
        self.ignore(bossDoneEventName)
        taskMgr.remove(self.uniqueName('StandUp'))
        self.ignore('enterCage')
        self.ignore('pieSplat')
        self.ignore('localPieSplat')
        self.ignore('outOfPies')
        self.ignore('begin-pie')
        self._DistributedBossCog__clearOnscreenMessage()
        taskMgr.remove(self.uniqueName('PieAdvice'))
        base.camLens.setFov(ToontownGlobals.CogHQCameraFov)
        self._DistributedBossCog__removeCageShadow()
        self.bossDamageMovie.finish()
        self.bossDamageMovie = None
        self._DistributedBossCog__unstickBoss()
        taskName = 'RecoverBossDamage'
        taskMgr.remove(taskName)
        self.battleThreeMusicTime = self.battleThreeMusic.getTime()
        self.battleThreeMusic.stop()

    
    def enterNearVictory(self):
        self._DistributedBossCog__cleanupIntervals()
        self.reparentTo(render)
        self.setPos(*ToontownGlobals.BossCogDeathPos)
        self.setHpr(*ToontownGlobals.BossCogBattleThreeHpr)
        self.clearChat()
        self.cagedToon.clearChat()
        self.setCageIndex(4)
        self._DistributedBossCog__releaseToons(finalBattle = 1)
        self.rampA.request('retract')
        self.rampB.request('retract')
        self.rampC.request('extend')
        self.accept('enterCage', self._DistributedBossCog__touchedCage)
        self.accept('pieSplat', self._DistributedBossCog__finalPieSplat)
        self.accept('localPieSplat', self._DistributedBossCog__localPieSplat)
        self.accept('outOfPies', self._DistributedBossCog__outOfPies)
        base.camLens.setFov(ToontownGlobals.BossBattleCameraFov)
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
        self._DistributedBossCog__clearOnscreenMessage()
        taskMgr.remove(self.uniqueName('PieAdvice'))
        base.camLens.setFov(ToontownGlobals.CogHQCameraFov)
        self._DistributedBossCog__removeCageShadow()
        self.setDizzy(0)
        self.battleThreeMusicTime = self.battleThreeMusic.getTime()
        self.battleThreeMusic.stop()

    
    def enterVictory(self):
        self._DistributedBossCog__cleanupIntervals()
        base.camLens.setFov(ToontownGlobals.BossBattleCameraFov)
        self.reparentTo(render)
        self.setPos(*ToontownGlobals.BossCogDeathPos)
        self.setHpr(*ToontownGlobals.BossCogBattleThreeHpr)
        self.clearChat()
        self.cagedToon.clearChat()
        self.setCageIndex(4)
        self._DistributedBossCog__releaseToons(finalBattle = 1)
        self.rampA.request('retract')
        self.rampB.request('retract')
        self.rampC.request('extend')
        self.happy = 0
        self.raised = 0
        self.forward = 1
        self.doAnimate('Fb_fall', now = 1)
        self.acceptOnce(self.animDoneEvent, self._DistributedBossCog__continueVictory)
        base.playMusic(self.battleThreeMusic, looping = 1, volume = 0.90000000000000002, time = self.battleThreeMusicTime)

    
    def _DistributedBossCog__continueVictory(self):
        self.stopAnimate()
        self.stash()
        self.doneBarrier()

    
    def exitVictory(self):
        self.stopAnimate()
        self.unstash()
        self._DistributedBossCog__removeCageShadow()
        base.camLens.setFov(ToontownGlobals.CogHQCameraFov)
        self.battleThreeMusicTime = self.battleThreeMusic.getTime()
        self.battleThreeMusic.stop()

    
    def enterReward(self):
        self._DistributedBossCog__cleanupIntervals()
        self.clearChat()
        self.cagedToon.clearChat()
        self.stash()
        self.stopAnimate()
        self.setCageIndex(4)
        self._DistributedBossCog__releaseToons(finalBattle = 1)
        self._DistributedBossCog__toMovieMode()
        self.rampA.request('retract')
        self.rampB.request('retract')
        self.rampC.request('extend')
        panelName = self.uniqueName('reward')
        self.rewardPanel = RewardPanel.RewardPanel(panelName)
        (victory, camVictory) = MovieToonVictory.doToonVictory(1, self.involvedToons, self.toonRewardDicts, self.deathList, self.rewardPanel)
        ival = Sequence(Parallel(victory, camVictory), Func(self._DistributedBossCog__doneReward))
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

    
    def _DistributedBossCog__doneReward(self):
        self.doneBarrier()
        self._DistributedBossCog__toWalkMode()

    
    def exitReward(self):
        intervalName = 'RewardMovie'
        self.clearInterval(intervalName)
        self.unstash()
        self.rewardPanel.destroy()
        del self.rewardPanel
        self._DistributedBossCog__removeCageShadow()
        self.battleThreeMusicTime = 0
        self.battleThreeMusic.stop()

    
    def enterEpilogue(self):
        self._DistributedBossCog__cleanupIntervals()
        self.clearChat()
        self.cagedToon.clearChat()
        self.stash()
        self.stopAnimate()
        self.setCageIndex(4)
        self._DistributedBossCog__controlToons()
        self.rampA.request('retract')
        self.rampB.request('retract')
        self.rampC.request('extend')
        self._DistributedBossCog__arrangeToonsAroundCage()
        camera.reparentTo(render)
        camera.setPosHpr(-24, 52, 27.5, -53, -13, 0)
        intervalName = 'EpilogueMovie'
        seq = Sequence(self._DistributedBossCog__makeCageOpenMovie(), name = intervalName)
        seq.start()
        self.activeIntervals[intervalName] = seq
        self.accept('nextChatPage', self._DistributedBossCog__epilogueChatNext)
        self.accept('doneChatPage', self._DistributedBossCog__epilogueChatDone)
        base.playMusic(self.epilogueMusic, looping = 1, volume = 0.90000000000000002)

    
    def _DistributedBossCog__epilogueChatNext(self, pageNumber, elapsed):
        if pageNumber == 2:
            if self.cagedToon.style.torso[1] == 'd':
                track = ActorInterval(self.cagedToon, 'curtsy')
            else:
                track = ActorInterval(self.cagedToon, 'bow')
            track = Sequence(track, Func(self.cagedToon.loop, 'neutral'))
            intervalName = 'EpilogueMovieToonAnim'
            self.activeIntervals[intervalName] = track
            track.start()
        

    
    def _DistributedBossCog__epilogueChatDone(self, elapsed):
        self.cagedToon.setChatAbsolute(Localizer.CagedToonGoodbye, CFSpeech)
        self.ignore('nextChatPage')
        self.ignore('doneChatPage')
        intervalName = 'EpilogueMovieToonAnim'
        self.clearInterval(intervalName)
        track = Parallel(Sequence(ActorInterval(self.cagedToon, 'wave'), Func(self.cagedToon.loop, 'neutral')), Sequence(Wait(0.5), Func(self._DistributedBossCog__localToonToSafeZone)))
        self.activeIntervals[intervalName] = track
        track.start()

    
    def exitEpilogue(self):
        self.clearInterval('EpilogueMovieToonAnim')
        self.unstash()
        self._DistributedBossCog__removeCageShadow()
        self.epilogueMusic.stop()

    
    def _DistributedBossCog__arrangeToonsAroundCage(self):
        radius = 15
        numToons = len(self.involvedToons)
        center = (numToons - 1) / 2.0
        for i in range(numToons):
            toon = toonbase.tcr.doId2do.get(self.involvedToons[i])
            if toon:
                angle = 270 - 15 * (i - center)
                radians = angle * math.pi / 180.0
                x = math.cos(radians) * radius
                y = math.sin(radians) * radius
                toon.setPos(self.cage, x, y, 0)
                toon.setZ(18.0)
                toon.headsUp(self.cage)
            
        

    
    def enterFrolic(self):
        self._DistributedBossCog__cleanupIntervals()
        self.clearChat()
        self.cagedToon.clearChat()
        self.reparentTo(render)
        self.setPosHpr(*ToontownGlobals.BossCogBattleOnePosHpr)
        self.stopAnimate()
        self.pose('Ff_neutral', 0)
        self.cage.setPos(self.cagePos[0])
        self.rampA.request('extend')
        self.rampB.request('extend')
        self.rampC.request('extend')
        self._DistributedBossCog__releaseToons()

    
    def exitFrolic(self):
        pass

    
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
        

    
    def _DistributedBossCog__toonsToBattlePosition(self, toonIds, battleNode):
        points = BattleBase.BattleBase.toonPoints[len(toonIds) - 1]
        for i in range(len(toonIds)):
            toon = toonbase.tcr.doId2do.get(toonIds[i])
            if toon:
                toon.reparentTo(render)
                (pos, h) = points[i]
                toon.setPosHpr(battleNode, pos[0], pos[1], pos[2], h, 0, 0)
            
        

    
    def _DistributedBossCog__backupToonsToBattlePosition(self, toonIds, battleNode):
        ival = Parallel()
        points = BattleBase.BattleBase.toonPoints[len(toonIds) - 1]
        for i in range(len(toonIds)):
            toon = toonbase.tcr.doId2do.get(toonIds[i])
            if toon:
                (pos, h) = points[i]
                pos = render.getRelativePoint(battleNode, pos)
                ival.append(Sequence(Func(toon.setPlayRate, -0.80000000000000004, 'walk'), Func(toon.loop, 'walk'), toon.posInterval(3, pos), Func(toon.setPlayRate, 1, 'walk'), Func(toon.loop, 'neutral')))
            
        
        return ival

    
    def _DistributedBossCog__toonsToPromotionPosition(self, toonIds, battleNode):
        points = BattleBase.BattleBase.toonPoints[len(toonIds) - 1]
        for i in range(len(toonIds)):
            toon = toonbase.tcr.doId2do.get(toonIds[i])
            if toon:
                toon.reparentTo(render)
                (pos, h) = points[i]
                toon.setPosHpr(battleNode, pos[0], pos[1] + 10, pos[2], h, 0, 0)
            
        

    
    def _DistributedBossCog__doobersToPromotionPosition(self, doobers, battleNode):
        points = BattleBase.BattleBase.toonPoints[len(doobers) - 1]
        for i in range(len(doobers)):
            suit = doobers[i]
            suit.fsm.request('neutral')
            suit.loop('neutral')
            (pos, h) = points[i]
            suit.setPosHpr(battleNode, pos[0], pos[1] + 10, pos[2], h, 0, 0)
        

    
    def _DistributedBossCog__touchedCage(self, entry):
        self.sendUpdate('touchCage', [])
        self._DistributedBossCog__clearOnscreenMessage()
        taskMgr.remove(self.uniqueName('PieAdvice'))
        base.playSfx(self.piesRestockSfx)
        if not (self.everThrownPie):
            taskMgr.doMethodLater(30, self._DistributedBossCog__howToThrowPies, self.uniqueName('PieAdvice'))
        

    
    def _DistributedBossCog__outOfPies(self):
        self._DistributedBossCog__showOnscreenMessage(Localizer.BossBattleNeedMorePies)
        taskMgr.doMethodLater(20, self._DistributedBossCog__howToGetPies, self.uniqueName('PieAdvice'))

    
    def _DistributedBossCog__howToGetPies(self, task):
        self._DistributedBossCog__showOnscreenMessage(Localizer.BossBattleHowToGetPies)

    
    def _DistributedBossCog__howToThrowPies(self, task):
        self._DistributedBossCog__showOnscreenMessage(Localizer.BossBattleHowToThrowPies)

    
    def _DistributedBossCog__foundPieButton(self):
        self.everThrownPie = 1
        self._DistributedBossCog__clearOnscreenMessage()
        taskMgr.remove(self.uniqueName('PieAdvice'))

    
    def _DistributedBossCog__pieSplat(self, toon, pieCode):
        if pieCode == ToontownGlobals.PieCodeBossInsides:
            if toon == toonbase.localToon:
                self.d_hitBossInsides()
            
            self._DistributedBossCog__flashRed()
        elif pieCode == ToontownGlobals.PieCodeBossCog:
            if toon == toonbase.localToon:
                self.d_hitBoss(1)
            
            if self.dizzy:
                self._DistributedBossCog__flashRed()
                self.doAnimate('hit', now = 1)
            
        

    
    def _DistributedBossCog__cleanupFlash(self):
        if self.flashInterval:
            self.flashInterval.finish()
            self.flashInterval = None
        

    
    def _DistributedBossCog__flashRed(self):
        self._DistributedBossCog__cleanupFlash()
        self.setColorScale(1, 1, 1, 1)
        i = Sequence(self.colorScaleInterval(0.10000000000000001, colorScale = VBase4(1, 0, 0, 1)), self.colorScaleInterval(0.29999999999999999, colorScale = VBase4(1, 1, 1, 1)))
        self.flashInterval = i
        i.start()

    
    def _DistributedBossCog__localPieSplat(self, pieCode, entry):
        if pieCode != ToontownGlobals.PieCodeToon:
            return None
        
        avatarDoId = entry.getIntoNodePath().getNetTag('avatarDoId')
        if avatarDoId == '':
            self.notify.warning('Toon %s has no avatarDoId tag.' % repr(entry.getIntoNodePath()))
            return None
        
        doId = int(avatarDoId)
        if doId != toonbase.localToon.doId:
            self.d_hitToon(doId)
        

    
    def _DistributedBossCog__finalPieSplat(self, toon, pieCode):
        if pieCode != ToontownGlobals.PieCodeBossCog:
            return None
        
        self.sendUpdate('finalPieSplat', [])
        self.ignore('pieSplat')

    
    def _DistributedBossCog__touchedBoss(self, entry):
        attackCodeStr = entry.getIntoNodePath().getNetTag('attackCode')
        if attackCodeStr == '':
            self.notify.warning('Node %s has no attackCode tag.' % repr(entry.getIntoNodePath()))
            return None
        
        attackCode = int(attackCodeStr)
        self._DistributedBossCog__zapLocalToon(attackCode)

    
    def _DistributedBossCog__zapLocalToon(self, attackCode):
        messenger.send('interrupt-pie')
        place = self.cr.playGame.getPlace()
        currentState = None
        if place:
            currentState = place.fsm.getCurrentState().getName()
        
        if currentState != 'walk' and currentState != 'finalBattle':
            return None
        
        toon = toonbase.localToon
        fling = 1
        shake = 0
        if attackCode == ToontownGlobals.BossCogAreaAttack:
            fling = 0
            shake = 1
        
        if fling:
            camera.wrtReparentTo(render)
            toon.headsUp(self)
            camera.wrtReparentTo(toon)
        
        bossRelativePos = toon.getPos(self.getGeomNode())
        bp2d = Vec2(bossRelativePos[0], bossRelativePos[1])
        bp2d.normalize()
        pos = toon.getPos()
        hpr = toon.getHpr()
        timestamp = globalClockDelta.getFrameNetworkTime()
        self.sendUpdate('zapToon', [
            pos[0],
            pos[1],
            pos[2],
            hpr[0],
            hpr[1],
            hpr[2],
            bp2d[0],
            bp2d[1],
            attackCode,
            timestamp])
        self._DistributedBossCog__doZapToon(toon, fling = fling, shake = shake)

    
    def showZapToon(self, toonId, x, y, z, h, p, r, attackCode, timestamp):
        if toonId == toonbase.localToon.doId:
            return None
        
        ts = globalClockDelta.localElapsedTime(timestamp)
        pos = Point3(x, y, z)
        hpr = VBase3(h, p, r)
        fling = 1
        if attackCode == ToontownGlobals.BossCogAreaAttack:
            pos = None
            hpr = None
            fling = 0
        else:
            ts -= SmoothMover.getDelay()
        toon = self.cr.doId2do.get(toonId)
        if toon:
            self._DistributedBossCog__doZapToon(toon, pos = pos, hpr = hpr, ts = ts, fling = fling)
        

    
    def _DistributedBossCog__doZapToon(self, toon, pos = None, hpr = None, ts = 0, fling = 1, shake = 1):
        zapName = toon.uniqueName('zap')
        self.clearInterval(zapName)
        zapTrack = Sequence(name = zapName)
        if toon == toonbase.localToon:
            self._DistributedBossCog__toOuchMode()
            messenger.send('interrupt-pie')
            self._DistributedBossCog__enableLocalToonSimpleCollisions()
        else:
            zapTrack.append(Func(toon.stopSmooth))
        
        def getSlideToPos(toon = toon):
            return render.getRelativePoint(toon, Point3(0, -5, 0))

        if pos != None and hpr != None:
            (zapTrack.append(Func(toon.setPosHpr, pos, hpr)),)
        
        toonTrack = Parallel()
        if shake and toon == toonbase.localToon:
            toonTrack.append(Sequence(Func(camera.setZ, camera, 1), Wait(0.14999999999999999), Func(camera.setZ, camera, -2), Wait(0.14999999999999999), Func(camera.setZ, camera, 1)))
        
        if fling:
            toonTrack += [
                ActorInterval(toon, 'slip-backward'),
                toon.posInterval(0.5, getSlideToPos, fluid = 1)]
        else:
            toonTrack += [
                ActorInterval(toon, 'slip-forward')]
        zapTrack.append(toonTrack)
        if toon == toonbase.localToon:
            zapTrack.append(Func(self._DistributedBossCog__disableLocalToonSimpleCollisions))
            currentState = self.fsm.getCurrentState().getName()
            if currentState == 'BattleThree':
                zapTrack.append(Func(self._DistributedBossCog__toFinalBattleMode))
            else:
                zapTrack.append(Func(self._DistributedBossCog__toWalkMode))
        else:
            zapTrack.append(Func(toon.startSmooth))
        if ts > 0:
            startTime = ts
        else:
            zapTrack = Sequence(Wait(-ts), zapTrack)
            startTime = 0
        zapTrack.delayDelete = DelayDelete.DelayDelete(toon)
        zapTrack.start(startTime)
        self.activeIntervals[zapName] = zapTrack

    
    def setAttackCode(self, attackCode, avId = 0):
        self.attackCode = attackCode
        self.attackAvId = avId
        isDizzy = attackCode == ToontownGlobals.BossCogDizzy
        self.setDizzy(isDizzy)
        self.stopAnimate()
        if isDizzy:
            self._DistributedBossCog__cleanupStrafe()
            self.doAnimate(None, raised = 0, happy = 1)
        elif attackCode == ToontownGlobals.BossCogSwatLeft:
            self.doAnimate('ltSwing')
        elif attackCode == ToontownGlobals.BossCogSwatRight:
            self.doAnimate('rtSwing')
        elif attackCode == ToontownGlobals.BossCogAreaAttack:
            self.doAnimate('areaAttack')
        elif attackCode == ToontownGlobals.BossCogFrontAttack:
            self.doAnimate('frontAttack')
        elif attackCode == ToontownGlobals.BossCogRecoverDizzyAttack:
            self.doAnimate('frontAttack')
        elif attackCode == ToontownGlobals.BossCogDirectedAttack:
            self.doDirectedAttack(avId)
        

    
    def getGearFrisbee(self):
        return loader.loadModelCopy('phase_9/models/char/gearProp')

    
    def doDirectedAttack(self, avId):
        toon = toonbase.tcr.doId2do.get(avId)
        if toon:
            gearRoot = self.rotateNode.attachNewNode('gearRoot')
            gearRoot.setZ(10)
            gearRoot.setTag('attackCode', str(ToontownGlobals.BossCogDirectedAttack))
            gearModel = self.getGearFrisbee()
            gearModel.setScale(0.20000000000000001)
            gearRoot.headsUp(toon)
            toToonH = PythonUtil.fitDestAngle2Src(0, gearRoot.getH() + 180)
            gearRoot.lookAt(toon)
            gearTrack = Parallel()
            for i in range(4):
                node = gearRoot.attachNewNode(str(i))
                node.hide()
                node.setPos(0, 5.8499999999999996, 4.0)
                gear = gearModel.instanceTo(node)
                x = random.uniform(-5, 5)
                z = random.uniform(-3, 3)
                h = random.uniform(-720, 720)
                gearTrack.append(Sequence(Wait(i * 0.14999999999999999), Func(node.show), Parallel(node.posInterval(1, Point3(x, 50, z), fluid = 1), node.hprInterval(1, VBase3(h, 0, 0), fluid = 1)), Func(node.detachNode)))
            
            if not (self.raised):
                neutral1Anim = self.getAnim('down2Up')
                self.raised = 1
            else:
                neutral1Anim = ActorInterval(self, 'Fb_neutral', startFrame = 48)
            throwAnim = self.getAnim('throw')
            neutral2Anim = self.getAnim(None)
            seq = Sequence(ParallelEndTogether(self.pelvis.hprInterval(1, VBase3(toToonH, 0, 0)), neutral1Anim), Parallel(Sequence(Wait(0.19), gearTrack, Func(gearRoot.detachNode), self.pelvis.hprInterval(0.20000000000000001, VBase3(0, 0, 0))), Sequence(throwAnim, neutral2Anim)))
            self.doAnimate(seq)
        

    
    def announceAreaAttack(self):
        if not (toonbase.localToon.controlManager.walkControls.isAirborne):
            self._DistributedBossCog__zapLocalToon(ToontownGlobals.BossCogAreaAttack)
        

    
    def _DistributedBossCog__cleanupStrafe(self):
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
        self._DistributedBossCog__cleanupStrafe()
        self.strafeInterval = seq
        seq.start()

    
    def toonDied(self, avId):
        if avId == toonbase.localToon.doId:
            self._DistributedBossCog__localToonDied()
        

    
    def cagedToonBattleThree(self, index, avId):
        str = Localizer.CagedToonBattleThree.get(index)
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

    
    def _DistributedBossCog__localToonToSafeZone(self):
        target_sz = ZoneUtil.getSafeZoneId(toonbase.localToon.defaultZone)
        place = self.cr.playGame.getPlace()
        place.fsm.request('teleportOut', [
            {
                'loader': ZoneUtil.getLoaderName(target_sz),
                'where': ZoneUtil.getWhereName(target_sz, 1),
                'how': 'teleportIn',
                'hoodId': target_sz,
                'zoneId': target_sz,
                'shardId': None,
                'avId': -1,
                'battle': 1 }])

    
    def _DistributedBossCog__localToonDied(self):
        target_sz = ZoneUtil.getSafeZoneId(toonbase.localToon.defaultZone)
        place = self.cr.playGame.getPlace()
        place.fsm.request('died', [
            {
                'loader': ZoneUtil.getLoaderName(target_sz),
                'where': ZoneUtil.getWhereName(target_sz, 1),
                'how': 'teleportIn',
                'hoodId': target_sz,
                'zoneId': target_sz,
                'shardId': None,
                'avId': -1,
                'battle': 1 }])


