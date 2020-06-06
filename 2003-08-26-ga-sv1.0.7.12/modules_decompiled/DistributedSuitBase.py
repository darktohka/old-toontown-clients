# File: D (Python 2.2)

from ShowBaseGlobal import *
from IntervalGlobal import *
from ClockDelta import *
from DirectGeometry import CLAMP
import DistributedAvatar
import Suit
import ToontownGlobals
import DistributedBattle
import FSM
import State
import SuitTimings
import SuitBase
import DistributedSuitPlanner
import AvatarDNA
import DirectNotifyGlobal
import SuitDialog
import BattleProps
import math
import copy
BATTLE_READY_RADIUS_EASY = 4.0
BATTLE_READY_RADIUS_MEDIUM = 8.0
BATTLE_READY_RADIUS_HARD = 16.0

class DistributedSuitBase(DistributedAvatar.DistributedAvatar, Suit.Suit, SuitBase.SuitBase):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedSuitBase')
    
    def __init__(self, cr):
        
        try:
            pass
        except:
            self.DistributedSuitBase_initialized = 1
            DistributedAvatar.DistributedAvatar.__init__(self, cr)
            Suit.Suit.__init__(self)
            SuitBase.SuitBase.__init__(self)
            self.cSphere = None
            self.cSphereNode = None
            self.cSphereNodePath = None
            self.cSphereBitMask = None
            self.bSphereName = None
            self.bSphere = None
            self.bSphereNode = None
            self.bSphereNodePath = None
            self.cRay = None
            self.cRayNode = None
            self.cRayNodePath = None
            self.cRayBitMask = None
            self.lifter = None
            self.cTrav = None
            self.sp = None
            self.fsm = None
            self.prop = None
            self.propInSound = None
            self.propOutSound = None
            self.reparentTo(hidden)
            self.loop('neutral')

        return None

    
    def generate(self):
        DistributedAvatar.DistributedAvatar.generate(self)

    
    def disable(self):
        self.notify.debug('DistributedSuit %d: disabling' % self.getDoId())
        DistributedAvatar.DistributedAvatar.disable(self)
        self.ignoreAll()
        self._DistributedSuitBase__removeCollisionData()
        self.cleanupLoseActor()
        self.stop()
        taskMgr.remove(self.uniqueName('blink-task'))
        return None

    
    def delete(self):
        
        try:
            pass
        except:
            self.DistributedSuitBase_deleted = 1
            self.notify.debug('DistributedSuit %d: deleting' % self.getDoId())
            del self.dna
            del self.sp
            DistributedAvatar.DistributedAvatar.delete(self)
            Suit.Suit.delete(self)
            SuitBase.SuitBase.delete(self)

        return None

    
    def playDialogue(self, *args):
        Suit.Suit.playDialogue(self, *args)

    
    def _DistributedSuitBase__removeCollisionData(self):
        self.enableRaycast(0)
        self.cSphere = None
        self.cSphereNodePath = None
        self.cSphereNode = None
        self.bSphere = None
        self.bSphereNode = None
        self.bSphereNodePath = None
        self.cRay = None
        self.cRayNode = None
        self.cRayNodePath = None
        self.lifter = None
        self.cTrav = None

    
    def setDNAString(self, dnaString):
        if not (self.dna):
            self.dna = AvatarDNA.AvatarDNA()
            self.dna.makeFromNetString(dnaString)
            self.setDNA(self.dna)
        
        return None

    
    def setHeight(self, height):
        Suit.Suit.setHeight(self, height)
        return None

    
    def setLevelDist(self, level):
        if self.notify.getDebug():
            self.notify.debug('Got level %d from server for suit %d' % (level, self.getDoId()))
        
        self.setLevel(level)

    
    def attachPropeller(self):
        if self.prop == None:
            self.prop = BattleProps.globalPropPool.getProp('propeller')
        
        if self.propInSound == None:
            self.propInSound = base.loadSfx('phase_5/audio/sfx/ENC_propeller_in.mp3')
        
        if self.propOutSound == None:
            self.propOutSound = base.loadSfx('phase_5/audio/sfx/ENC_propeller_out.mp3')
        
        head = self.find('**/joint-head')
        self.prop.reparentTo(head)

    
    def detachPropeller(self):
        if self.prop:
            self.prop.removeNode()
            self.prop = None
        
        if self.propInSound:
            self.propInSound = None
        
        if self.propOutSound:
            self.propOutSound = None
        

    
    def beginSupaFlyMove(self, pos, moveIn, trackName):
        skyPos = Point3(pos)
        if moveIn:
            skyPos.setZ(pos.getZ() + SuitTimings.fromSky * self.sp.suitWalkSpeed)
        else:
            skyPos.setZ(pos.getZ() + SuitTimings.toSky * self.sp.suitWalkSpeed)
        groundF = 28
        dur = self.getDuration('landing')
        fr = self.getFrameRate('landing')
        animTimeInAir = groundF / fr
        impactLength = dur - animTimeInAir
        timeTillLanding = SuitTimings.fromSky - impactLength
        waitTime = timeTillLanding - animTimeInAir
        if self.prop == None:
            self.prop = BattleProps.globalPropPool.getProp('propeller')
        
        propDur = self.prop.getDuration('propeller')
        lastSpinFrame = 8
        fr = self.prop.getFrameRate('propeller')
        spinTime = lastSpinFrame / fr
        openTime = (lastSpinFrame + 1) / fr
        if moveIn:
            lerpPosTrack = Sequence(Func(self.dropShadows[0].wrtReparentTo, render), LerpPosInterval(self, timeTillLanding, pos, startPos = skyPos), Wait(impactLength))
            shadowScaleInt = LerpScaleInterval(self.dropShadows[0], timeTillLanding, Point3(1, 1, 1), startScale = Point3(0.01, 0.01, 0.01))
            shadowFuncInt2 = Func(self.dropShadows[0].wrtReparentTo, self.getGeomNode())
            shadowFuncInt3 = Func(self.dropShadows[0].setPos, Point3(0, 0, 0))
            funcIntPose = Func(self.pose, 'landing', 0)
            waitInt = Wait(waitTime)
            actInt = ActorInterval(self, 'landing', loop = 0, duration = dur)
            funcIntWalk = Func(self.loop, 'walk')
            self.attachPropeller()
            funcIntProp2 = FunctionInterval(base.playSfx, openEnded = 1, extraArgs = [
                self.propInSound,
                0,
                1,
                None,
                0.0,
                self])
            actIntProp1 = ActorInterval(self.prop, 'propeller', loop = 0, duration = waitTime + spinTime, startTime = 0.0, endTime = spinTime)
            actIntProp2 = ActorInterval(self.prop, 'propeller', loop = 0, duration = propDur - openTime, startTime = openTime)
            funcIntProp3 = FunctionInterval(self.propInSound.stop, openEnded = 1)
            funcIntProp4 = FunctionInterval(self.detachPropeller, openEnded = 1)
            return Parallel(lerpPosTrack, Sequence(shadowScaleInt, shadowFuncInt2, shadowFuncInt3), Sequence(funcIntPose, waitInt, actInt, funcIntWalk), Sequence(funcIntProp2, actIntProp1, actIntProp2, funcIntProp3, funcIntProp4), name = self.taskName('trackName'))
        else:
            lerpPosTrack = Sequence(Func(self.dropShadows[0].wrtReparentTo, render), Wait(impactLength), LerpPosInterval(self, timeTillLanding, skyPos, startPos = pos))
            lerpWaitInt2 = Wait(impactLength)
            shadowScaleInt = LerpScaleInterval(self.dropShadows[0], timeTillLanding, Point3(0.01, 0.01, 0.01), startScale = Point3(1, 1, 1))
            shadowFuncInt2 = Func(self.dropShadows[0].reparentTo, self.getGeomNode())
            shadowFuncInt3 = Func(self.dropShadows[0].setPos, Point3(0, 0, 0))
            actInt = ActorInterval(self, 'landing', loop = 0, startTime = dur, endTime = 0.0)
            self.attachPropeller()
            self.prop.hide()
            funcIntProp1 = FunctionInterval(self.prop.show, openEnded = 1)
            funcIntProp2 = FunctionInterval(base.playSfx, openEnded = 1, extraArgs = [
                self.propOutSound,
                0,
                1,
                1.0,
                0.0,
                self])
            actIntProp1 = ActorInterval(self.prop, 'propeller', loop = 0, endTime = openTime, startTime = propDur)
            actIntProp2 = ActorInterval(self.prop, 'propeller', loop = 0, duration = propDur - openTime, startTime = spinTime, endTime = 0.0)
            funcIntProp3 = FunctionInterval(self.propOutSound.stop, openEnded = 1)
            funcIntProp4 = FunctionInterval(self.detachPropeller, openEnded = 1)
            return Parallel(lerpPosTrack, Sequence(lerpWaitInt2, shadowScaleInt, shadowFuncInt2, shadowFuncInt3), actInt, Sequence(funcIntProp1, funcIntProp2, actIntProp1, actIntProp2, funcIntProp3, funcIntProp4), name = self.taskName('trackName'))
        return None

    
    def enableBattleDetect(self, name, handler):
        if self.bSphereNodePath:
            self.bSphereNodePath.removeNode()
            self.bSphereNodePath = None
        
        if self.bSphere:
            self.bSphereName = self.taskName(name)
            self.bSphereNode = CollisionNode(self.bSphereName)
            self.bSphereNode.addSolid(self.bSphere)
            self.bSphereNodePath = self.attachNewNode(self.bSphereNode)
            self.bSphereNode.setCollideMask(ToontownGlobals.WallBitmask)
            self.accept('enter' + self.bSphereName, handler)
        
        return Task.done

    
    def disableBattleDetect(self):
        if self.bSphereName:
            self.ignore('enter' + self.bSphereName)
        
        if self.bSphereNodePath:
            self.bSphereNodePath.removeNode()
            self.bSphereNodePath = None
        

    
    def enableRaycast(self, enable = 1):
        if not (self.cTrav) and not hasattr(self, 'cRayNode') or not (self.cRayNode):
            return None
        
        self.cTrav.removeCollider(self.cRayNode)
        if enable:
            if self.notify.getDebug():
                self.notify.debug('enabling raycast')
            
            self.cTrav.addCollider(self.cRayNode, self.lifter)
        elif self.notify.getDebug():
            self.notify.debug('disabling raycast')
        
        return None

    
    def b_setBrushOff(self, index):
        self.setBrushOff(index)
        self.d_setBrushOff(index)
        return None

    
    def d_setBrushOff(self, index):
        self.sendUpdate('setBrushOff', [
            index])

    
    def setBrushOff(self, index):
        self.setChatAbsolute(SuitDialog.getBrushOffText(self.getStyleName(), index), CFSpeech | CFTimeout)

    
    def initializeBodyCollisions(self, collIdStr):
        self.cSphere = CollisionSphere(0.0, 0.0, 0.0, 1.0)
        self.cSphereNode = CollisionNode(self.taskName('barrierSphere'))
        self.cSphereNode.addSolid(self.cSphere)
        self.cSphereNodePath = self.attachNewNode(self.cSphereNode)
        self.cSphereNodePath.hide()
        self.cSphereBitMask = ToontownGlobals.WallBitmask
        self.cSphereNode.setCollideMask(self.cSphereBitMask)
        self.cSphere.setTangible(1)
        self.bSphere = CollisionSphere(0.0, 0.0, 0.0, BATTLE_READY_RADIUS_EASY)
        self.bSphere.setTangible(0)
        self.cRay = CollisionRay(0.0, 0.0, 6.0, 0.0, 0.0, -1.0)
        self.cRayNode = CollisionNode(self.taskName('cRay'))
        self.cRayNode.addSolid(self.cRay)
        self.cRayNodePath = self.attachNewNode(self.cRayNode)
        self.cRayNodePath.hide()
        self.cRayBitMask = ToontownGlobals.FloorBitmask
        self.cRayNode.setFromCollideMask(self.cRayBitMask)
        self.cRayNode.setIntoCollideMask(BitMask32.allOff())
        self.lifter = CollisionHandlerFloor()
        self.lifter.setOffset(ToontownGlobals.FloorOffset)
        self.lifter.setMaxVelocity(8.0)
        self.lifter.addColliderNode(self.cRayNode, self.node())
        self.cTrav = toonbase.localToon.cTrav
        return None

    
    def disableBodyCollisions(self):
        self.disableBattleDetect()
        self.enableRaycast(0)
        if self.cRayNodePath:
            self.cRayNodePath.removeNode()
        
        del self.cRayNode
        del self.cRay
        del self.bSphereNode
        del self.bSphere
        if self.cSphereNodePath:
            self.cSphereNodePath.removeNode()
        
        del self.cSphereNode
        del self.cSphere
        del self.lifter

    
    def denyBattle(self):
        self.notify.debug('denyBattle()')
        self.cr.playGame.getPlace().setState('walk')
        self.resumePath(self.pathState)

    
    def makePathTrack(self, nodePath, posPoints, velocity, name):
        track = Sequence(name = name)
        restOfPosPoints = posPoints[1:]
        for pointIndex in range(len(posPoints) - 1):
            startPoint = posPoints[pointIndex]
            endPoint = posPoints[pointIndex + 1]
            track.append(Func(nodePath.headsUp, endPoint[0], endPoint[1], endPoint[2]))
            distance = Vec3(endPoint - startPoint).length()
            duration = distance / velocity
            track.append(LerpPosInterval(nodePath, duration = duration, pos = Point3(endPoint), startPos = Point3(startPoint)))
        
        return track

    
    def setState(self, state):
        if self.fsm == None:
            return 0
        
        if self.fsm.getCurrentState().getName() == state:
            return 0
        
        return self.fsm.request(state)

    
    def enterOff(self, *args):
        self.hideNametag3d()
        self.hideNametag2d()
        self.setParent(ToontownGlobals.SPHidden)

    
    def exitOff(self):
        self.setParent(ToontownGlobals.SPRender)
        self.showNametag3d()
        self.showNametag2d()
        self.loop('neutral', 0)

    
    def enterBattle(self):
        self.loop('neutral', 0)
        self.disableBattleDetect()
        self.corpMedallion.hide()
        self.healthBar.show()
        self.currHP = self.maxHP

    
    def exitBattle(self):
        self.healthBar.hide()
        self.corpMedallion.show()
        self.currHP = self.maxHP
        return None

    
    def enterWaitForBattle(self):
        self.loop('neutral', 0)
        return None

    
    def exitWaitForBattle(self):
        return None


