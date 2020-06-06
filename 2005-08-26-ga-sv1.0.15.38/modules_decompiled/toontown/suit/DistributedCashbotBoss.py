# File: D (Python 2.2)

from direct.interval.IntervalGlobal import *
from direct.task.TaskManagerGlobal import *
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import TTLocalizer
import DistributedBossCog
import DistributedCashbotBossGoon
import SuitDNA
from toontown.toon import Toon
from toontown.toon import ToonDNA
from direct.fsm import FSM
from toontown.toonbase import ToontownGlobals
from otp.otpbase import OTPGlobals
from toontown.building import ElevatorUtils
from toontown.building import ElevatorConstants
from toontown.battle import MovieToonVictory
from toontown.battle import RewardPanel
from direct.distributed import DelayDelete
from toontown.chat import ResistanceChat
from toontown.coghq import CogDisguiseGlobals
from pandac.PandaModules import *
OneBossCog = None
TTL = TTLocalizer

class DistributedCashbotBoss(DistributedBossCog.DistributedBossCog, FSM.FSM):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedCashbotBoss')
    numFakeGoons = 3
    
    def __init__(self, cr):
        DistributedBossCog.DistributedBossCog.__init__(self, cr)
        FSM.FSM.__init__(self, 'DistributedSellbotBoss')
        self.resistanceToon = None
        self.resistanceToonOnstage = 0
        self.cranes = { }
        self.safes = { }
        self.goons = []
        self.bossMaxDamage = ToontownGlobals.CashbotBossMaxDamage
        self.elevatorType = ElevatorConstants.ELEVATOR_CFO
        base.boss = self

    
    def announceGenerate(self):
        global OneBossCog
        DistributedBossCog.DistributedBossCog.announceGenerate(self)
        self.setName(TTLocalizer.CashbotBossName)
        nameInfo = TTLocalizer.BossCogNameWithDept % {
            'name': self.name,
            'dept': SuitDNA.getDeptFullname(self.style.dept) }
        self.setDisplayName(nameInfo)
        target = CollisionSphere(2, 0, 0, 3)
        targetNode = CollisionNode('headTarget')
        targetNode.addSolid(target)
        targetNode.setCollideMask(OTPGlobals.PieBitmask)
        self.headTarget = self.neck.attachNewNode(targetNode)
        shield = CollisionSphere(0, 0, 0.80000000000000004, 7)
        shieldNode = CollisionNode('shield')
        shieldNode.addSolid(shield)
        shieldNode.setCollideMask(OTPGlobals.PieBitmask)
        shieldNodePath = self.pelvis.attachNewNode(shieldNode)
        self.heldObject = None
        self.bossDamage = 0
        self.loadEnvironment()
        self._DistributedCashbotBoss__makeResistanceToon()
        self.physicsMgr = PhysicsManager()
        integrator = LinearEulerIntegrator()
        self.physicsMgr.attachLinearIntegrator(integrator)
        fn = ForceNode('gravity')
        self.fnp = self.geom.attachNewNode(fn)
        gravity = LinearVectorForce(0, 0, -32)
        fn.addForce(gravity)
        self.physicsMgr.addLinearForce(gravity)
        localAvatar.chatMgr.chatInputSpeedChat.addCFOMenu()
        if OneBossCog != None:
            self.notify.warning('Multiple BossCogs visible.')
        
        OneBossCog = self

    
    def disable(self):
        global OneBossCog
        DistributedBossCog.DistributedBossCog.disable(self)
        self.demand('Off')
        self.unloadEnvironment()
        self._DistributedCashbotBoss__cleanupResistanceToon()
        self.fnp.removeNode()
        self.physicsMgr.clearLinearForces()
        self.battleThreeMusic.stop()
        self.epilogueMusic.stop()
        localAvatar.chatMgr.chatInputSpeedChat.removeCFOMenu()
        if OneBossCog == self:
            OneBossCog = None
        

    
    def _DistributedCashbotBoss__makeResistanceToon(self):
        if self.resistanceToon:
            return None
        
        npc = Toon.Toon()
        npc.setName(TTLocalizer.ResistanceToonName)
        npc.setPickable(0)
        npc.setPlayerType(NametagGroup.CCNonPlayer)
        dna = ToonDNA.ToonDNA()
        dna.newToonRandom(11237, 'f', 1)
        dna.head = 'pls'
        npc.setDNAString(dna.makeNetString())
        npc.animFSM.request('neutral')
        self.resistanceToon = npc
        self.resistanceToon.setPosHpr(*ToontownGlobals.CashbotRTBattleOneStartPosHpr)
        state = random.getstate()
        random.seed(self.doId)
        self.resistanceToon.suitType = SuitDNA.getRandomSuitByDept('m')
        random.setstate(state)
        self.fakeGoons = []
        for i in range(self.numFakeGoons):
            goon = DistributedCashbotBossGoon.DistributedCashbotBossGoon(base.cr)
            goon.doId = -1 - i
            goon.setBossCogId(self.doId)
            goon.announceGenerate()
            self.fakeGoons.append(goon)
        
        self._DistributedCashbotBoss__hideFakeGoons()

    
    def _DistributedCashbotBoss__cleanupResistanceToon(self):
        self._DistributedCashbotBoss__hideResistanceToon()
        if self.resistanceToon:
            self.resistanceToon.removeActive()
            self.resistanceToon.delete()
            self.resistanceToon = None
            for i in range(self.numFakeGoons):
                self.fakeGoons[i].disable()
                self.fakeGoons[i].delete()
                self.fakeGoons[i] = None
            
        

    
    def _DistributedCashbotBoss__showResistanceToon(self, withSuit):
        if not (self.resistanceToonOnstage):
            self.resistanceToon.addActive()
            self.resistanceToon.reparentTo(self.geom)
            self.resistanceToonOnstage = 1
        
        if withSuit:
            suit = self.resistanceToon.suitType
            self.resistanceToon.putOnSuit(suit, False)
        else:
            self.resistanceToon.takeOffSuit()

    
    def _DistributedCashbotBoss__hideResistanceToon(self):
        if self.resistanceToonOnstage:
            self.resistanceToon.removeActive()
            self.resistanceToon.detachNode()
            self.resistanceToonOnstage = 0
        

    
    def _DistributedCashbotBoss__hideFakeGoons(self):
        if self.fakeGoons:
            for goon in self.fakeGoons:
                goon.request('Off')
            
        

    
    def _DistributedCashbotBoss__showFakeGoons(self, state):
        print self.fakeGoons
        if self.fakeGoons:
            for goon in self.fakeGoons:
                goon.request(state)
            
        

    
    def loadEnvironment(self):
        DistributedBossCog.DistributedBossCog.loadEnvironment(self)
        self.midVault = loader.loadModel('phase_10/models/cogHQ/MidVault.bam')
        self.endVault = loader.loadModel('phase_10/models/cogHQ/EndVault.bam')
        self.lightning = loader.loadModel('phase_10/models/cogHQ/CBLightning.bam')
        self.magnet = loader.loadModel('phase_10/models/cogHQ/CBMagnet.bam')
        self.craneArm = loader.loadModel('phase_10/models/cogHQ/CBCraneArm.bam')
        self.controls = loader.loadModel('phase_10/models/cogHQ/CBCraneControls.bam')
        self.stick = loader.loadModel('phase_10/models/cogHQ/CBCraneStick.bam')
        self.safe = loader.loadModel('phase_10/models/cogHQ/CBSafe.bam')
        self.eyes = loader.loadModel('phase_10/models/cogHQ/CashBotBossEyes.bam')
        self.cableTex = self.craneArm.findTexture('MagnetControl')
        self.eyes.setPosHprScale(4.5, 0, -2.5, 90, 90, 0, 0.40000000000000002, 0.40000000000000002, 0.40000000000000002)
        self.eyes.reparentTo(self.neck)
        self.eyes.hide()
        self.midVault.setPos(0, -222, -70.700000000000003)
        self.endVault.setPos(84, -201, -6)
        self.geom = NodePath('geom')
        self.midVault.reparentTo(self.geom)
        self.endVault.reparentTo(self.geom)
        self.endVault.findAllMatches('**/MagnetArms').detach()
        self.endVault.findAllMatches('**/Safes').detach()
        self.endVault.findAllMatches('**/MagnetControlsAll').detach()
        cn = self.endVault.find('**/wallsCollision').node()
        cn.setIntoCollideMask(OTPGlobals.WallBitmask | OTPGlobals.PieBitmask | BitMask32.lowerOn(3) << 21)
        self.door1 = self.midVault.find('**/SlidingDoor1/')
        self.door2 = self.midVault.find('**/SlidingDoor/')
        self.door3 = self.endVault.find('**/SlidingDoor/')
        elevatorModel = loader.loadModelCopy('phase_10/models/cogHQ/CFOElevator')
        elevatorOrigin = self.midVault.find('**/elevator_origin')
        elevatorOrigin.setScale(1)
        elevatorModel.reparentTo(elevatorOrigin)
        leftDoor = elevatorModel.find('**/left_door')
        leftDoor.setName('left-door')
        rightDoor = elevatorModel.find('**/right_door')
        rightDoor.setName('right-door')
        self.setupElevator(elevatorOrigin)
        ElevatorUtils.closeDoors(leftDoor, rightDoor, ElevatorConstants.ELEVATOR_CFO)
        walls = self.endVault.find('**/RollUpFrameCillison')
        walls.detachNode()
        self.evWalls = self.replaceCollisionPolysWithPlanes(walls)
        self.evWalls.reparentTo(self.endVault)
        self.evWalls.stash()
        floor = self.endVault.find('**/EndVaultFloorCollision')
        floor.detachNode()
        self.evFloor = self.replaceCollisionPolysWithPlanes(floor)
        self.evFloor.reparentTo(self.endVault)
        self.evFloor.setName('floor')
        plane = CollisionPlane(Plane(Vec3(0, 0, 1), Point3(0, 0, -50)))
        planeNode = CollisionNode('dropPlane')
        planeNode.addSolid(plane)
        planeNode.setCollideMask(OTPGlobals.PieBitmask)
        self.geom.attachNewNode(planeNode)
        self.geom.reparentTo(render)

    
    def unloadEnvironment(self):
        DistributedBossCog.DistributedBossCog.unloadEnvironment(self)
        self.geom.removeNode()

    
    def replaceCollisionPolysWithPlanes(self, model):
        newCollisionNode = CollisionNode('collisions')
        newCollideMask = BitMask32(0)
        planes = []
        collList = model.findAllMatches('**/+CollisionNode').asList()
        if not collList:
            collList = [
                model]
        
        for cnp in collList:
            cn = cnp.node()
            if not isinstance(cn, CollisionNode):
                self.notify.warning('Not a collision node: %s' % repr(cnp))
                break
            
            newCollideMask = newCollideMask | cn.getIntoCollideMask()
            for i in range(cn.getNumSolids()):
                solid = cn.getSolid(i)
                if isinstance(solid, CollisionPolygon):
                    plane = Plane(solid.getPlane())
                    planes.append(plane)
                else:
                    self.notify.warning('Unexpected collision solid: %s' % repr(solid))
                    newCollisionNode.addSolid(plane)
            
        
        newCollisionNode.setIntoCollideMask(newCollideMask)
        threshold = 0.10000000000000001
        planes.sort(lambda p1, p2: p1.compareTo(p2, threshold))
        lastPlane = None
        for plane in planes:
            if lastPlane == None or plane.compareTo(lastPlane, threshold) != 0:
                cp = CollisionPlane(plane)
                newCollisionNode.addSolid(cp)
                lastPlane = plane
            
        
        return NodePath(newCollisionNode)

    
    def _DistributedCashbotBoss__makeGoonMovieForIntro(self):
        goonTrack = Parallel()
        goon = self.fakeGoons[0]
        goonTrack.append(Sequence(goon.posHprInterval(0, Point3(111, -287, 0), VBase3(165, 0, 0)), goon.posHprInterval(9, Point3(101, -323, 0), VBase3(165, 0, 0)), goon.hprInterval(1, VBase3(345, 0, 0)), goon.posHprInterval(9, Point3(111, -287, 0), VBase3(345, 0, 0)), goon.hprInterval(1, VBase3(165, 0, 0)), goon.posHprInterval(9.5, Point3(104, -316, 0), VBase3(165, 0, 0)), Func(goon.request, 'Stunned'), Wait(1)))
        goon = self.fakeGoons[1]
        goonTrack.append(Sequence(goon.posHprInterval(0, Point3(119, -315, 0), VBase3(357, 0, 0)), goon.posHprInterval(9, Point3(121, -280, 0), VBase3(357, 0, 0)), goon.hprInterval(1, VBase3(177, 0, 0)), goon.posHprInterval(9, Point3(119, -315, 0), VBase3(177, 0, 0)), goon.hprInterval(1, VBase3(357, 0, 0)), goon.posHprInterval(9, Point3(121, -280, 0), VBase3(357, 0, 0))))
        goon = self.fakeGoons[2]
        goonTrack.append(Sequence(goon.posHprInterval(0, Point3(102, -320, 0), VBase3(231, 0, 0)), goon.posHprInterval(9, Point3(127, -337, 0), VBase3(231, 0, 0)), goon.hprInterval(1, VBase3(51, 0, 0)), goon.posHprInterval(9, Point3(102, -320, 0), VBase3(51, 0, 0)), goon.hprInterval(1, VBase3(231, 0, 0)), goon.posHprInterval(9, Point3(127, -337, 0), VBase3(231, 0, 0))))
        return Sequence(Func(self._DistributedCashbotBoss__showFakeGoons, 'Walk'), goonTrack, Func(self._DistributedCashbotBoss__hideFakeGoons))

    
    def makeIntroductionMovie(self, delayDeletes):
        for toonId in self.involvedToons:
            toon = self.cr.doId2do.get(toonId)
            if toon:
                delayDeletes.append(DelayDelete.DelayDelete(toon))
            
        
        rtTrack = Sequence()
        startPos = Point3(ToontownGlobals.CashbotBossOffstagePosHpr[0], ToontownGlobals.CashbotBossOffstagePosHpr[1], ToontownGlobals.CashbotBossOffstagePosHpr[2])
        battlePos = Point3(ToontownGlobals.CashbotBossBattleOnePosHpr[0], ToontownGlobals.CashbotBossBattleOnePosHpr[1], ToontownGlobals.CashbotBossBattleOnePosHpr[2])
        battleHpr = VBase3(ToontownGlobals.CashbotBossBattleOnePosHpr[3], ToontownGlobals.CashbotBossBattleOnePosHpr[4], ToontownGlobals.CashbotBossBattleOnePosHpr[5])
        bossTrack = Sequence()
        bossTrack.append(Func(self.reparentTo, render))
        bossTrack.append(Func(self.getGeomNode().setH, 180))
        bossTrack.append(Func(self.pelvis.setHpr, self.pelvisForwardHpr))
        bossTrack.append(Func(self.loop, 'Ff_neutral'))
        (track, hpr) = self.rollBossToPoint(startPos, None, battlePos, None, 0)
        bossTrack.append(track)
        (track, hpr) = self.rollBossToPoint(battlePos, hpr, battlePos, battleHpr, 0)
        bossTrack.append(track)
        bossTrack.append(Func(self.getGeomNode().setH, 0))
        bossTrack.append(Func(self.pelvis.setHpr, self.pelvisReversedHpr))
        goonTrack = self._DistributedCashbotBoss__makeGoonMovieForIntro()
        attackToons = TTL.CashbotBossCogAttack
        rToon = self.resistanceToon
        rToon.setPosHpr(*ToontownGlobals.CashbotRTBattleOneStartPosHpr)
        track = Sequence(Func(camera.setPosHpr, 82, -219, 5, 267, 0, 0), Func(rToon.setChatAbsolute, TTL.ResistanceToonWelcome, CFSpeech), Wait(3), Sequence(goonTrack, duration = 0), Parallel(camera.posHprInterval(4, Point3(108, -244, 4), VBase3(211.5, 0, 0)), Sequence(Func(rToon.suit.setPlayRate, 1.3999999999999999, 'walk'), Func(rToon.suit.loop, 'walk'), Parallel(rToon.hprInterval(1, VBase3(180, 0, 0)), rToon.posInterval(3, VBase3(120, -255, 0)), Sequence(Wait(2), Func(rToon.clearChat))), Func(rToon.suit.loop, 'neutral'), self.door2.posInterval(3, VBase3(0, 0, 30)))), Func(rToon.setHpr, 0, 0, 0), Func(rToon.setChatAbsolute, TTL.ResistanceToonTooLate, CFSpeech), Func(camera.reparentTo, render), Func(camera.setPosHpr, 61.100000000000001, -228.80000000000001, 10.199999999999999, -90, 0, 0), self.door1.posInterval(2, VBase3(0, 0, 30)), Parallel(bossTrack, Sequence(Wait(3), Func(rToon.clearChat), self.door1.posInterval(3, VBase3(0, 0, 0)))), Func(self.setChatAbsolute, TTL.CashbotBossDiscoverToons1, CFSpeech), camera.posHprInterval(1.5, Point3(93.299999999999997, -230, 0.69999999999999996), VBase3(-92.900000000000006, 39.700000000000003, 8.3000000000000007)), Func(self.setChatAbsolute, TTL.CashbotBossDiscoverToons2, CFSpeech), Wait(4), Func(self.clearChat), self.loseCogSuits(self.toonsA + self.toonsB, render, (113, -228, 10, 90, 0, 0)), Wait(1), Func(rToon.setHpr, 0, 0, 0), self.loseCogSuits([
            rToon], render, (133, -243, 5, 143, 0, 0), True), Func(rToon.setChatAbsolute, TTL.ResistanceToonKeepHimBusy, CFSpeech), Wait(1), Func(self._DistributedCashbotBoss__showResistanceToon, False), Sequence(Func(rToon.animFSM.request, 'run'), rToon.hprInterval(1, VBase3(180, 0, 0)), Parallel(Sequence(rToon.posInterval(1.5, VBase3(109, -294, 0)), Parallel(Func(rToon.animFSM.request, 'jump')), rToon.posInterval(1.5, VBase3(93.935000000000002, -341.065, 2))), self.door2.posInterval(3, VBase3(0, 0, 0))), Func(rToon.animFSM.request, 'neutral')), self.toonNormalEyes(self.involvedToons), self.toonNormalEyes([
            self.resistanceToon], True), Func(rToon.clearChat), Func(camera.setPosHpr, 93.299999999999997, -230, 0.69999999999999996, -92.900000000000006, 39.700000000000003, 8.3000000000000007), Func(self.setChatAbsolute, attackToons, CFSpeech), Wait(2), Func(self.clearChat))
        return Sequence(Func(camera.reparentTo, render), track)

    
    def _DistributedCashbotBoss__makeGoonMovieForBattleThree(self):
        goonPosHprs = [
            [
                Point3(111, -287, 0),
                VBase3(165, 0, 0),
                Point3(101, -323, 0),
                VBase3(165, 0, 0)],
            [
                Point3(119, -315, 0),
                VBase3(357, 0, 0),
                Point3(121, -280, 0),
                VBase3(357, 0, 0)],
            [
                Point3(102, -320, 0),
                VBase3(231, 0, 0),
                Point3(127, -337, 0),
                VBase3(231, 0, 0)]]
        mainGoon = self.fakeGoons[0]
        goonLoop = Parallel()
        print self.fakeGoons
        for i in range(1, self.numFakeGoons):
            print i
            goon = self.fakeGoons[i]
            goonLoop.append(Sequence(goon.posHprInterval(8, goonPosHprs[i][0], goonPosHprs[i][1]), goon.posHprInterval(8, goonPosHprs[i][2], goonPosHprs[i][3])))
        
        goonTrack = Sequence(Func(self._DistributedCashbotBoss__showFakeGoons, 'Walk'), Func(mainGoon.request, 'Stunned'), Func(goonLoop.loop), Wait(20))
        return goonTrack

    
    def makePrepareBattleThreeMovie(self, delayDeletes, crane, safe):
        for toonId in self.involvedToons:
            toon = self.cr.doId2do.get(toonId)
            if toon:
                delayDeletes.append(DelayDelete.DelayDelete(toon))
            
        
        startPos = Point3(ToontownGlobals.CashbotBossBattleOnePosHpr[0], ToontownGlobals.CashbotBossBattleOnePosHpr[1], ToontownGlobals.CashbotBossBattleOnePosHpr[2])
        battlePos = Point3(ToontownGlobals.CashbotBossBattleThreePosHpr[0], ToontownGlobals.CashbotBossBattleThreePosHpr[1], ToontownGlobals.CashbotBossBattleThreePosHpr[2])
        startHpr = Point3(ToontownGlobals.CashbotBossBattleOnePosHpr[3], ToontownGlobals.CashbotBossBattleOnePosHpr[4], ToontownGlobals.CashbotBossBattleOnePosHpr[5])
        battleHpr = VBase3(ToontownGlobals.CashbotBossBattleThreePosHpr[3], ToontownGlobals.CashbotBossBattleThreePosHpr[4], ToontownGlobals.CashbotBossBattleThreePosHpr[5])
        finalHpr = VBase3(135, 0, 0)
        bossTrack = Sequence()
        bossTrack.append(Func(self.reparentTo, render))
        bossTrack.append(Func(self.getGeomNode().setH, 180))
        bossTrack.append(Func(self.pelvis.setHpr, self.pelvisForwardHpr))
        bossTrack.append(Func(self.loop, 'Ff_neutral'))
        (track, hpr) = self.rollBossToPoint(startPos, startHpr, startPos, battleHpr, 0)
        bossTrack.append(track)
        (track, hpr) = self.rollBossToPoint(startPos, None, battlePos, None, 0)
        bossTrack.append(track)
        (track, hpr) = self.rollBossToPoint(battlePos, battleHpr, battlePos, finalHpr, 0)
        bossTrack.append(track)
        rToon = self.resistanceToon
        rToon.setPosHpr(93.935000000000002, -341.065, 0, -45, 0, 0)
        goon = self.fakeGoons[0]
        crane = self.cranes[0]
        track = Sequence(Func(self._DistributedCashbotBoss__hideToons), Func(crane.request, 'Movie'), Func(crane.accomodateToon, rToon), Func(goon.request, 'Stunned'), Func(goon.setPosHpr, 104, -316, 0, 165, 0, 0), Parallel(self.door2.posInterval(4.5, VBase3(0, 0, 30)), self.door3.posInterval(4.5, VBase3(0, 0, 30)), bossTrack), Func(rToon.loop, 'leverNeutral'), Func(camera.reparentTo, self.geom), Func(camera.setPosHpr, 105, -326, 5, 136.30000000000001, 0, 0), Func(rToon.setChatAbsolute, TTL.ResistanceToonWatchThis, CFSpeech), Wait(2), Func(rToon.clearChat), Func(camera.setPosHpr, 105, -326, 20, -45.299999999999997, 11, 0), Func(self.setChatAbsolute, TTL.CashbotBossGetAwayFromThat, CFSpeech), Wait(2), Func(self.clearChat), camera.posHprInterval(1.5, Point3(105, -326, 5), Point3(136.30000000000001, 0, 0), blendType = 'easeInOut'), Func(rToon.setChatAbsolute, TTL.ResistanceToonCraneInstructions1, CFSpeech), Wait(4), Func(rToon.setChatAbsolute, TTL.ResistanceToonCraneInstructions2, CFSpeech), Wait(4), Func(rToon.setChatAbsolute, TTL.ResistanceToonCraneInstructions3, CFSpeech), Wait(4), Func(rToon.setChatAbsolute, TTL.ResistanceToonCraneInstructions4, CFSpeech), Wait(4), Func(rToon.clearChat), Func(camera.setPosHpr, 102, -323.60000000000002, 0.90000000000000002, -10.6, 14, 0), Func(goon.request, 'Recovery'), Wait(2), Func(camera.setPosHpr, 95.400000000000006, -332.60000000000002, 4.2000000000000002, 167.09999999999999, -13.199999999999999, 0), Func(rToon.setChatAbsolute, TTL.ResistanceToonGetaway, CFSpeech), Func(rToon.animFSM.request, 'jump'), Wait(1.8), Func(rToon.clearChat), Func(camera.setPosHpr, 109.09999999999999, -300.69999999999999, 13.9, -15.6, -13.6, 0), Func(rToon.animFSM.request, 'run'), Func(goon.request, 'Walk'), Parallel(self.door3.posInterval(3, VBase3(0, 0, 0)), rToon.posHprInterval(3, Point3(136, -212.90000000000001, 0), VBase3(-14, 0, 0), startPos = Point3(110.8, -292.69999999999999, 0), startHpr = VBase3(-14, 0, 0)), goon.posHprInterval(3, Point3(125.2, -243.5, 0), VBase3(-14, 0, 0), startPos = Point3(104.8, -309.5, 0), startHpr = VBase3(-14, 0, 0))), Func(self._DistributedCashbotBoss__hideFakeGoons), Func(crane.request, 'Free'), Func(self.getGeomNode().setH, 0), self.moveToonsToBattleThreePos(self.involvedToons), Func(self._DistributedCashbotBoss__showToons))
        return Sequence(Func(camera.reparentTo, self), Func(camera.setPosHpr, 0, -27, 25, 0, -18, 0), track)

    
    def moveToonsToBattleThreePos(self, toons):
        track = Parallel()
        for i in range(len(toons)):
            toon = base.cr.doId2do.get(toons[i])
            if toon:
                posHpr = ToontownGlobals.CashbotToonsBattleThreeStartPosHpr[i]
                pos = Point3(*posHpr[0:3])
                hpr = VBase3(*posHpr[3:6])
                track.append(toon.posHprInterval(0.20000000000000001, pos, hpr))
            
        
        return track

    
    def makeBossFleeMovie(self):
        hadEnough = TTLocalizer.CashbotBossHadEnough
        outtaHere = TTLocalizer.CashbotBossOuttaHere
        loco = loader.loadModelCopy('phase_10/models/cogHQ/CashBotLocomotive')
        car1 = loader.loadModelCopy('phase_10/models/cogHQ/CashBotBoxCar')
        car2 = loader.loadModelCopy('phase_10/models/cogHQ/CashBotTankCar')
        trainPassingSfx = base.loadSfx('phase_10/audio/sfx/CBHQ_TRAIN_trainpass.mp3')
        boomSfx = loader.loadSfx('phase_3.5/audio/sfx/ENC_cogfall_apart.mp3')
        rollThroughDoor = self.rollBossToPoint(fromPos = Point3(120, -280, 0), fromHpr = None, toPos = Point3(120, -250, 0), toHpr = None, reverse = 0)
        rollTrack = Sequence(Func(self.getGeomNode().setH, 180), rollThroughDoor[0], Func(self.getGeomNode().setH, 0))
        g = 80.0 / 300.0
        trainTrack = Track((0 * g, loco.posInterval(0.5, Point3(0, -242, 0), startPos = Point3(150, -242, 0))), (1 * g, car2.posInterval(0.5, Point3(0, -242, 0), startPos = Point3(150, -242, 0))), (2 * g, car1.posInterval(0.5, Point3(0, -242, 0), startPos = Point3(150, -242, 0))), (3 * g, car2.posInterval(0.5, Point3(0, -242, 0), startPos = Point3(150, -242, 0))), (4 * g, car1.posInterval(0.5, Point3(0, -242, 0), startPos = Point3(150, -242, 0))), (5 * g, car2.posInterval(0.5, Point3(0, -242, 0), startPos = Point3(150, -242, 0))), (6 * g, car1.posInterval(0.5, Point3(0, -242, 0), startPos = Point3(150, -242, 0))), (7 * g, car2.posInterval(0.5, Point3(0, -242, 0), startPos = Point3(150, -242, 0))), (8 * g, car1.posInterval(0.5, Point3(0, -242, 0), startPos = Point3(150, -242, 0))), (9 * g, car2.posInterval(0.5, Point3(0, -242, 0), startPos = Point3(150, -242, 0))), (10 * g, car1.posInterval(0.5, Point3(0, -242, 0), startPos = Point3(150, -242, 0))), (11 * g, car2.posInterval(0.5, Point3(0, -242, 0), startPos = Point3(150, -242, 0))), (12 * g, car1.posInterval(0.5, Point3(0, -242, 0), startPos = Point3(150, -242, 0))), (13 * g, car2.posInterval(0.5, Point3(0, -242, 0), startPos = Point3(150, -242, 0))), (14 * g, car1.posInterval(0.5, Point3(0, -242, 0), startPos = Point3(150, -242, 0))))
        bossTrack = Track((0.0, Sequence(Func(camera.reparentTo, render), Func(camera.setPosHpr, 105, -280, 20, -158, -3, 0), Func(self.reparentTo, render), Func(self.show), Func(self.clearChat), Func(self.setPosHpr, *ToontownGlobals.CashbotBossBattleThreePosHpr), Func(self.reverseHead), ActorInterval(self, 'Fb_firstHit'), ActorInterval(self, 'Fb_down2Up'))), (1.0, Func(self.setChatAbsolute, hadEnough, CFSpeech)), (5.5, Parallel(Func(camera.setPosHpr, 100, -315, 16, -20, 0, 0), Func(self.hideBattleThreeObjects), Func(self.forwardHead), Func(self.loop, 'Ff_neutral'), rollTrack, self.door3.posInterval(2.5, Point3(0, 0, 25), startPos = Point3(0, 0, 18)))), (5.5, Func(self.setChatAbsolute, outtaHere, CFSpeech)), (5.5, SoundInterval(trainPassingSfx)), (8.0999999999999996, Func(self.clearChat)), (9.4000000000000004, Sequence(Func(loco.reparentTo, render), Func(car1.reparentTo, render), Func(car2.reparentTo, render), trainTrack, Func(loco.detachNode), Func(car1.detachNode), Func(car2.detachNode), Wait(2))), (9.5, SoundInterval(boomSfx)), (9.5, Sequence(self.posInterval(0.40000000000000002, Point3(0, -250, 0)), Func(self.stash))))
        return bossTrack

    
    def grabObject(self, obj):
        obj.wrtReparentTo(self.neck)
        obj.hideShadows()
        obj.stashCollisions()
        if obj.lerpInterval:
            obj.lerpInterval.finish()
        
        obj.lerpInterval = Parallel(obj.posInterval(ToontownGlobals.CashbotBossToMagnetTime, Point3(-1, 0, 0.20000000000000001)), obj.quatInterval(ToontownGlobals.CashbotBossToMagnetTime, VBase3(0, -90, 90)), Sequence(Wait(ToontownGlobals.CashbotBossToMagnetTime), ShowInterval(self.eyes)), obj.toMagnetSoundInterval)
        obj.lerpInterval.start()
        self.heldObject = obj

    
    def dropObject(self, obj):
        if obj.lerpInterval:
            obj.lerpInterval.finish()
            obj.lerpInterval = None
        
        obj = self.heldObject
        obj.wrtReparentTo(render)
        obj.setHpr(obj.getH(), 0, 0)
        self.eyes.hide()
        obj.showShadows()
        obj.unstashCollisions()
        self.heldObject = None

    
    def setBossDamage(self, bossDamage):
        if bossDamage > self.bossDamage:
            delta = bossDamage - self.bossDamage
            self.flashRed()
            self.doAnimate('hit', now = 1)
            self.showHpText(-delta, scale = 5)
        
        self.bossDamage = bossDamage
        self.updateHealthBar()

    
    def setRewardId(self, rewardId):
        self.rewardId = rewardId

    
    def d_applyReward(self):
        self.sendUpdate('applyReward', [])

    
    def stunAllGoons(self):
        for goon in self.goons:
            if goon.state == 'Walk' or goon.state == 'Battle':
                goon.demand('Stunned')
                goon.sendUpdate('requestStunned', [
                    0])
            
        

    
    def destroyAllGoons(self):
        for goon in self.goons:
            if goon.state != 'Off' and not (goon.isDead):
                goon.b_destroyGoon()
            
        

    
    def deactivateCranes(self):
        for crane in self.cranes.values():
            crane.demand('Free')
        

    
    def hideBattleThreeObjects(self):
        for goon in self.goons:
            goon.demand('Off')
        
        for safe in self.safes.values():
            safe.demand('Off')
        
        for crane in self.cranes.values():
            crane.demand('Off')
        

    
    def _DistributedCashbotBoss__doPhysics(self, task):
        dt = globalClock.getDt()
        self.physicsMgr.doPhysics(dt)
        return Task.cont

    
    def _DistributedCashbotBoss__hideToons(self):
        for toonId in self.involvedToons:
            toon = self.cr.doId2do.get(toonId)
            if toon:
                toon.hide()
            
        

    
    def _DistributedCashbotBoss__showToons(self):
        for toonId in self.involvedToons:
            toon = self.cr.doId2do.get(toonId)
            if toon:
                toon.show()
            
        

    
    def _DistributedCashbotBoss__arrangeToonsAroundResistanceToon(self):
        radius = 7
        numToons = len(self.involvedToons)
        center = (numToons - 1) / 2.0
        for i in range(numToons):
            toon = self.cr.doId2do.get(self.involvedToons[i])
            if toon:
                angle = 90 - 15 * (i - center)
                radians = angle * math.pi / 180.0
                x = math.cos(radians) * radius
                y = math.sin(radians) * radius
                toon.setPos(self.resistanceToon, x, y, 0)
                toon.headsUp(self.resistanceToon)
                toon.loop('neutral')
                toon.show()
            
        

    
    def _DistributedCashbotBoss__talkAboutPromotion(self, speech):
        if self.prevCogSuitLevel < ToontownGlobals.MaxCogSuitLevel:
            newCogSuitLevel = localAvatar.getCogLevels()[CogDisguiseGlobals.dept2deptIndex(self.style.dept)]
            if newCogSuitLevel == ToontownGlobals.MaxCogSuitLevel:
                speech += TTLocalizer.ResistanceToonLastPromotion % (ToontownGlobals.MaxCogSuitLevel + 1)
            
            if newCogSuitLevel in ToontownGlobals.CogSuitHPLevels:
                speech += TTLocalizer.ResistanceToonHPBoost
            
        else:
            speech += TTLocalizer.ResistanceToonMaxed % (ToontownGlobals.MaxCogSuitLevel + 1)
        return speech

    
    def enterOff(self):
        DistributedBossCog.DistributedBossCog.enterOff(self)
        if self.resistanceToon:
            self.resistanceToon.clearChat()
        

    
    def enterWaitForToons(self):
        DistributedBossCog.DistributedBossCog.enterWaitForToons(self)
        self.detachNode()
        self.geom.hide()
        self.resistanceToon.removeActive()

    
    def exitWaitForToons(self):
        DistributedBossCog.DistributedBossCog.exitWaitForToons(self)
        self.geom.show()
        self.resistanceToon.addActive()

    
    def enterElevator(self):
        DistributedBossCog.DistributedBossCog.enterElevator(self)
        self.detachNode()
        self.resistanceToon.removeActive()
        self.endVault.stash()
        self.midVault.unstash()
        self._DistributedCashbotBoss__showResistanceToon(True)

    
    def exitElevator(self):
        DistributedBossCog.DistributedBossCog.exitElevator(self)
        self.resistanceToon.addActive()

    
    def enterIntroduction(self):
        self.detachNode()
        self.stopAnimate()
        self.endVault.unstash()
        self.evWalls.stash()
        self.midVault.unstash()
        self._DistributedCashbotBoss__showResistanceToon(True)
        base.playMusic(self.stingMusic, looping = 1, volume = 0.90000000000000002)
        DistributedBossCog.DistributedBossCog.enterIntroduction(self)

    
    def exitIntroduction(self):
        DistributedBossCog.DistributedBossCog.exitIntroduction(self)
        self.stingMusic.stop()

    
    def enterBattleOne(self):
        DistributedBossCog.DistributedBossCog.enterBattleOne(self)
        self.reparentTo(render)
        self.setPosHpr(*ToontownGlobals.CashbotBossBattleOnePosHpr)
        self.show()
        self.pelvis.setHpr(self.pelvisReversedHpr)
        self.doAnimate()
        self.endVault.stash()
        self.midVault.unstash()
        self._DistributedCashbotBoss__hideResistanceToon()

    
    def exitBattleOne(self):
        DistributedBossCog.DistributedBossCog.exitBattleOne(self)

    
    def enterPrepareBattleThree(self):
        self.controlToons()
        NametagGlobals.setMasterArrowsOn(0)
        intervalName = 'PrepareBattleThreeMovie'
        delayDeletes = []
        self.movieCrane = self.cranes[0]
        self.movieSafe = self.safes[1]
        self.movieCrane.request('Movie')
        seq = Sequence(self.makePrepareBattleThreeMovie(delayDeletes, self.movieCrane, self.movieSafe), Func(self._DistributedCashbotBoss__beginBattleThree), name = intervalName)
        seq.delayDeletes = delayDeletes
        seq.start()
        self.activeIntervals[intervalName] = seq
        self.endVault.unstash()
        self.evWalls.stash()
        self.midVault.unstash()
        self._DistributedCashbotBoss__showResistanceToon(False)
        taskMgr.add(self._DistributedCashbotBoss__doPhysics, self.uniqueName('physics'), priority = 25)

    
    def _DistributedCashbotBoss__beginBattleThree(self):
        intervalName = 'PrepareBattleThreeMovie'
        self.clearInterval(intervalName)
        self.doneBarrier('PrepareBattleThree')

    
    def exitPrepareBattleThree(self):
        intervalName = 'PrepareBattleThreeMovie'
        self.clearInterval(intervalName)
        self.unstickToons()
        self.releaseToons()
        if self.newState == 'BattleThree':
            self.movieCrane.request('Free')
            self.movieSafe.request('Initial')
        
        NametagGlobals.setMasterArrowsOn(1)
        ElevatorUtils.closeDoors(self.leftDoor, self.rightDoor, ElevatorConstants.ELEVATOR_CFO)
        taskMgr.remove(self.uniqueName('physics'))

    
    def enterBattleThree(self):
        self.cleanupIntervals()
        self.releaseToons(finalBattle = 1)
        self.clearChat()
        self.resistanceToon.clearChat()
        self.reparentTo(render)
        self.setPosHpr(*ToontownGlobals.CashbotBossBattleThreePosHpr)
        self.happy = 1
        self.raised = 1
        self.forward = 1
        self.doAnimate()
        self.endVault.unstash()
        self.evWalls.unstash()
        self.midVault.stash()
        self._DistributedCashbotBoss__hideResistanceToon()
        localAvatar.setCameraFov(ToontownGlobals.BossBattleCameraFov)
        self.generateHealthBar()
        self.updateHealthBar()
        base.playMusic(self.battleThreeMusic, looping = 1, volume = 0.90000000000000002)
        taskMgr.add(self._DistributedCashbotBoss__doPhysics, self.uniqueName('physics'), priority = 25)

    
    def exitBattleThree(self):
        bossDoneEventName = self.uniqueName('DestroyedBoss')
        self.ignore(bossDoneEventName)
        self.stopAnimate()
        self.cleanupAttacks()
        self.setDizzy(0)
        self.removeHealthBar()
        localAvatar.setCameraFov(ToontownGlobals.CogHQCameraFov)
        if self.newState != 'Victory':
            self.battleThreeMusic.stop()
        
        taskMgr.remove(self.uniqueName('physics'))

    
    def enterVictory(self):
        self.cleanupIntervals()
        self.reparentTo(render)
        self.setPosHpr(*ToontownGlobals.CashbotBossBattleThreePosHpr)
        self.stopAnimate()
        self.endVault.unstash()
        self.evWalls.unstash()
        self.midVault.unstash()
        self._DistributedCashbotBoss__hideResistanceToon()
        self._DistributedCashbotBoss__hideToons()
        self.clearChat()
        self.resistanceToon.clearChat()
        self.deactivateCranes()
        if self.cranes:
            self.cranes[1].demand('Off')
        
        self.releaseToons(finalBattle = 1)
        if self.hasLocalToon():
            self.toMovieMode()
        
        intervalName = 'VictoryMovie'
        seq = Sequence(self.makeBossFleeMovie(), Func(self._DistributedCashbotBoss__continueVictory), name = intervalName)
        seq.start()
        self.activeIntervals[intervalName] = seq
        if self.oldState != 'BattleThree':
            base.playMusic(self.battleThreeMusic, looping = 1, volume = 0.90000000000000002)
        

    
    def _DistributedCashbotBoss__continueVictory(self):
        self.doneBarrier('Victory')

    
    def exitVictory(self):
        self.cleanupIntervals()
        if self.newState != 'Reward':
            if self.hasLocalToon():
                self.toWalkMode()
            
        
        self._DistributedCashbotBoss__showToons()
        self.door3.setPos(0, 0, 0)
        if self.newState != 'Reward':
            self.battleThreeMusic.stop()
        

    
    def enterReward(self):
        self.cleanupIntervals()
        self.clearChat()
        self.resistanceToon.clearChat()
        self.stash()
        self.stopAnimate()
        self.controlToons()
        panelName = self.uniqueName('reward')
        self.rewardPanel = RewardPanel.RewardPanel(panelName)
        (victory, camVictory) = MovieToonVictory.doToonVictory(1, self.involvedToons, self.toonRewardIds, self.toonRewardDicts, self.deathList, self.rewardPanel, allowGroupShot = 0)
        ival = Sequence(Parallel(victory, camVictory), Func(self._DistributedCashbotBoss__doneReward))
        intervalName = 'RewardMovie'
        delayDeletes = []
        for toonId in self.involvedToons:
            toon = self.cr.doId2do.get(toonId)
            if toon:
                delayDeletes.append(DelayDelete.DelayDelete(toon))
            
        
        ival.delayDeletes = delayDeletes
        ival.start()
        self.activeIntervals[intervalName] = ival
        if self.oldState != 'Victory':
            base.playMusic(self.battleThreeMusic, looping = 1, volume = 0.90000000000000002)
        

    
    def _DistributedCashbotBoss__doneReward(self):
        self.doneBarrier('Reward')
        self.toWalkMode()

    
    def exitReward(self):
        intervalName = 'RewardMovie'
        self.clearInterval(intervalName)
        if self.newState != 'Epilogue':
            self.releaseToons()
        
        self.unstash()
        self.rewardPanel.destroy()
        del self.rewardPanel
        self.battleThreeMusic.stop()

    
    def enterEpilogue(self):
        self.cleanupIntervals()
        self.clearChat()
        self.resistanceToon.clearChat()
        self.stash()
        self.stopAnimate()
        self.controlToons()
        self._DistributedCashbotBoss__showResistanceToon(False)
        self.resistanceToon.setPosHpr(*ToontownGlobals.CashbotBossBattleThreePosHpr)
        self.resistanceToon.loop('neutral')
        self._DistributedCashbotBoss__arrangeToonsAroundResistanceToon()
        camera.reparentTo(render)
        camera.setPos(self.resistanceToon, -9, 12, 6)
        camera.lookAt(self.resistanceToon, 0, 0, 3)
        intervalName = 'EpilogueMovie'
        text = ResistanceChat.getChatText(self.rewardId)
        (menuIndex, itemIndex) = ResistanceChat.decodeId(self.rewardId)
        value = ResistanceChat.getItemValue(self.rewardId)
        if menuIndex == ResistanceChat.RESISTANCE_TOONUP:
            if value == -1:
                instructions = TTLocalizer.ResistanceToonToonupAllInstructions
            else:
                instructions = TTLocalizer.ResistanceToonToonupInstructions % value
        elif menuIndex == ResistanceChat.RESISTANCE_MONEY:
            if value == -1:
                instructions = TTLocalizer.ResistanceToonMoneyAllInstructions
            else:
                instructions = TTLocalizer.ResistanceToonMoneyInstructions % value
        elif menuIndex == ResistanceChat.RESISTANCE_RESTOCK:
            if value == -1:
                instructions = TTLocalizer.ResistanceToonRestockAllInstructions
            else:
                trackName = TTLocalizer.BattleGlobalTracks[value]
                instructions = TTLocalizer.ResistanceToonRestockInstructions % trackName
        
        speech = TTLocalizer.ResistanceToonCongratulations % (text, instructions)
        speech = self._DistributedCashbotBoss__talkAboutPromotion(speech)
        self.resistanceToon.setLocalPageChat(speech, 0)
        self.accept('nextChatPage', self._DistributedCashbotBoss__epilogueChatNext)
        self.accept('doneChatPage', self._DistributedCashbotBoss__epilogueChatDone)
        base.playMusic(self.epilogueMusic, looping = 1, volume = 0.90000000000000002)

    
    def _DistributedCashbotBoss__epilogueChatNext(self, pageNumber, elapsed):
        if pageNumber == 1:
            toon = self.resistanceToon
            playRate = 0.75
            track = Sequence(ActorInterval(toon, 'victory', playRate = playRate, startFrame = 0, endFrame = 9), ActorInterval(toon, 'victory', playRate = playRate, startFrame = 9, endFrame = 0), Func(self.resistanceToon.loop, 'neutral'))
            intervalName = 'EpilogueMovieToonAnim'
            self.activeIntervals[intervalName] = track
            track.start()
        elif pageNumber == 3:
            self.d_applyReward()
            ResistanceChat.doEffect(self.rewardId, self.resistanceToon, self.involvedToons)
        

    
    def _DistributedCashbotBoss__epilogueChatDone(self, elapsed):
        self.resistanceToon.setChatAbsolute(TTLocalizer.CagedToonGoodbye, CFSpeech)
        self.ignore('nextChatPage')
        self.ignore('doneChatPage')
        intervalName = 'EpilogueMovieToonAnim'
        self.clearInterval(intervalName)
        track = Parallel(Sequence(ActorInterval(self.resistanceToon, 'wave'), Func(self.resistanceToon.loop, 'neutral')), Sequence(Wait(0.5), Func(self.localToonToSafeZone)))
        self.activeIntervals[intervalName] = track
        track.start()

    
    def exitEpilogue(self):
        self.clearInterval('EpilogueMovieToonAnim')
        self.unstash()
        self.epilogueMusic.stop()

    
    def enterFrolic(self):
        DistributedBossCog.DistributedBossCog.enterFrolic(self)
        self.setPosHpr(*ToontownGlobals.CashbotBossBattleOnePosHpr)
        self.releaseToons()
        if self.hasLocalToon():
            self.toWalkMode()
        
        self.door3.setZ(25)
        self.door2.setZ(25)
        self.endVault.unstash()
        self.evWalls.stash()
        self.midVault.unstash()
        self._DistributedCashbotBoss__hideResistanceToon()

    
    def exitFrolic(self):
        self.door3.setZ(0)
        self.door2.setZ(0)


