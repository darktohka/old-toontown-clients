# File: D (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from direct.interval.IntervalGlobal import *
from direct.distributed.ClockDelta import *
from direct.directtools.DirectGeometry import CLAMP
from otp.avatar import DistributedAvatar
import Suit
from toontown.toonbase import ToontownGlobals
from toontown.battle import DistributedBattle
from direct.fsm import ClassicFSM
from direct.fsm import State
import SuitTimings
import SuitBase
import DistributedSuitPlanner
import SuitDNA
from direct.directnotify import DirectNotifyGlobal
import SuitDialog
from toontown.battle import BattleProps
import math
import copy

class DistributedSuitBase(DistributedAvatar.DistributedAvatar, Suit.Suit, SuitBase.SuitBase):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedSuitBase')
    
    def __init__(self, cr):
        
        try:
            return None
        except:
            self.DistributedSuitBase_initialized = 1

        DistributedAvatar.DistributedAvatar.__init__(self, cr)
        Suit.Suit.__init__(self)
        SuitBase.SuitBase.__init__(self)
        self.activeShadow = 0
        self.battleDetectName = None
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


    
    def setDNAString(self, dnaString):
        Suit.Suit.setDNAString(self, dnaString)

    
    def setDNA(self, dna):
        Suit.Suit.setDNA(self, dna)

    
    def getDialogueArray(self, *args):
        return Suit.Suit.getDialogueArray(self, *args)

    
    def _DistributedSuitBase__removeCollisionData(self):
        self.enableRaycast(0)
        self.cRay = None
        self.cRayNode = None
        self.cRayNodePath = None
        self.lifter = None
        self.cTrav = None

    
    def setHeight(self, height):
        Suit.Suit.setHeight(self, height)

    
    def getRadius(self):
        return Suit.Suit.getRadius(self)

    
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
            skyPos.setZ(pos.getZ() + SuitTimings.fromSky * ToontownGlobals.SuitWalkSpeed)
        else:
            skyPos.setZ(pos.getZ() + SuitTimings.toSky * ToontownGlobals.SuitWalkSpeed)
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
            lerpPosTrack = Sequence(self.posInterval(timeTillLanding, pos, startPos = skyPos), Wait(impactLength))
            shadowScale = self.dropShadow.getScale()
            shadowTrack = Sequence(Func(self.dropShadow.reparentTo, render), Func(self.dropShadow.setPos, pos), self.dropShadow.scaleInterval(timeTillLanding, self.scale, startScale = 0.01), Func(self.dropShadow.reparentTo, self.getShadowJoint()), Func(self.dropShadow.setPos, 0, 0, 0), Func(self.dropShadow.setScale, shadowScale))
            fadeInTrack = Sequence(Func(self.setTransparency, 1), self.colorScaleInterval(1, colorScale = VBase4(1, 1, 1, 1), startColorScale = VBase4(1, 1, 1, 0)), Func(self.clearColorScale), Func(self.clearTransparency))
            animTrack = Sequence(Func(self.pose, 'landing', 0), Wait(waitTime), ActorInterval(self, 'landing', duration = dur), Func(self.loop, 'walk'))
            self.attachPropeller()
            propTrack = Parallel(SoundInterval(self.propInSound, duration = waitTime + dur, node = self), Sequence(ActorInterval(self.prop, 'propeller', constrainedLoop = 1, duration = waitTime + spinTime, startTime = 0.0, endTime = spinTime), ActorInterval(self.prop, 'propeller', duration = propDur - openTime, startTime = openTime), Func(self.detachPropeller)))
            return Parallel(lerpPosTrack, shadowTrack, fadeInTrack, animTrack, propTrack, name = self.taskName('trackName'))
        else:
            lerpPosTrack = Sequence(Wait(impactLength), LerpPosInterval(self, timeTillLanding, skyPos, startPos = pos))
            shadowTrack = Sequence(Func(self.dropShadow.reparentTo, render), Func(self.dropShadow.setPos, pos), self.dropShadow.scaleInterval(timeTillLanding, 0.01, startScale = self.scale), Func(self.dropShadow.reparentTo, self.getShadowJoint()), Func(self.dropShadow.setPos, 0, 0, 0))
            fadeOutTrack = Sequence(Func(self.setTransparency, 1), self.colorScaleInterval(1, colorScale = VBase4(1, 1, 1, 0), startColorScale = VBase4(1, 1, 1, 1)), Func(self.clearColorScale), Func(self.clearTransparency), Func(self.reparentTo, hidden))
            actInt = ActorInterval(self, 'landing', loop = 0, startTime = dur, endTime = 0.0)
            self.attachPropeller()
            self.prop.hide()
            propTrack = Parallel(SoundInterval(self.propOutSound, duration = waitTime + dur, node = self), Sequence(Func(self.prop.show), ActorInterval(self.prop, 'propeller', endTime = openTime, startTime = propDur), ActorInterval(self.prop, 'propeller', constrainedLoop = 1, duration = propDur - openTime, startTime = spinTime, endTime = 0.0), Func(self.detachPropeller)))
            return Parallel(ParallelEndTogether(lerpPosTrack, shadowTrack, fadeOutTrack), actInt, propTrack, name = self.taskName('trackName'))

    
    def enableBattleDetect(self, name, handler):
        if self.collTube:
            self.battleDetectName = self.taskName(name)
            self.collNode = CollisionNode(self.battleDetectName)
            self.collNode.addSolid(self.collTube)
            self.collNodePath = self.attachNewNode(self.collNode)
            self.collNode.setCollideMask(ToontownGlobals.WallBitmask)
            self.accept('enter' + self.battleDetectName, handler)
        
        return Task.done

    
    def disableBattleDetect(self):
        if self.battleDetectName:
            self.ignore('enter' + self.battleDetectName)
            self.battleDetectName = None
        
        if self.collNodePath:
            self.collNodePath.removeNode()
            self.collNodePath = None
        

    
    def enableRaycast(self, enable = 1):
        if not (self.cTrav) and not hasattr(self, 'cRayNode') or not (self.cRayNode):
            return None
        
        self.cTrav.removeCollider(self.cRayNodePath)
        if enable:
            if self.notify.getDebug():
                self.notify.debug('enabling raycast')
            
            self.cTrav.addCollider(self.cRayNodePath, self.lifter)
        elif self.notify.getDebug():
            self.notify.debug('disabling raycast')
        

    
    def b_setBrushOff(self, index):
        self.setBrushOff(index)
        self.d_setBrushOff(index)

    
    def d_setBrushOff(self, index):
        self.sendUpdate('setBrushOff', [
            index])

    
    def setBrushOff(self, index):
        self.setChatAbsolute(SuitDialog.getBrushOffText(self.getStyleName(), index), CFSpeech | CFTimeout)

    
    def initializeBodyCollisions(self, collIdStr):
        DistributedAvatar.DistributedAvatar.initializeBodyCollisions(self, collIdStr)
        self.cRay = CollisionRay(0.0, 0.0, CollisionHandlerRayStart, 0.0, 0.0, -1.0)
        self.cRayNode = CollisionNode(self.taskName('cRay'))
        self.cRayNode.addSolid(self.cRay)
        self.cRayNodePath = self.attachNewNode(self.cRayNode)
        self.cRayNodePath.hide()
        self.cRayBitMask = ToontownGlobals.FloorBitmask
        self.cRayNode.setFromCollideMask(self.cRayBitMask)
        self.cRayNode.setIntoCollideMask(BitMask32.allOff())
        self.lifter = CollisionHandlerFloor()
        self.lifter.setOffset(ToontownGlobals.FloorOffset)
        self.lifter.setReach(6.0)
        self.lifter.setMaxVelocity(8.0)
        self.lifter.addCollider(self.cRayNodePath, self)
        self.cTrav = base.cTrav

    
    def disableBodyCollisions(self):
        self.disableBattleDetect()
        self.enableRaycast(0)
        if self.cRayNodePath:
            self.cRayNodePath.removeNode()
        
        del self.cRayNode
        del self.cRay
        del self.lifter

    
    def denyBattle(self):
        self.notify.debug('denyBattle()')
        place = self.cr.playGame.getPlace()
        if place.fsm.getCurrentState().getName() == 'WaitForBattle':
            place.setState('walk')
        
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

    
    def subclassManagesParent(self):
        return 0

    
    def enterOff(self, *args):
        self.hideNametag3d()
        self.hideNametag2d()
        if not self.subclassManagesParent():
            self.setParent(ToontownGlobals.SPHidden)
        

    
    def exitOff(self):
        if not self.subclassManagesParent():
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

    
    def enterWaitForBattle(self):
        self.loop('neutral', 0)

    
    def exitWaitForBattle(self):
        pass

    
    def setSkelecog(self, flag):
        SuitBase.SuitBase.setSkelecog(self, flag)
        if flag:
            Suit.Suit.makeSkeleton(self)
        


