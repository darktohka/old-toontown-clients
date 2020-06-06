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
STAND_OUTSIDE_DOOR = 2.5
BATTLE_IGNORE_TIME = 6
BATTLE_WAIT_TIME = 3
CATCHUP_SPEED_MULTIPLIER = 3
ALLOW_BATTLE_DETECT = 1

class DistributedSuit(DistributedAvatar.DistributedAvatar, Suit.Suit, SuitBase.SuitBase):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedSuit')
    ENABLE_EXPANDED_NAME = 0
    STREET_HEIGHT_OFFSET = -0.5
    
    def __init__(self, cr):
        
        try:
            pass
        except:
            self.DistributedSuit_initialized = 1
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
            self.spDoId = None
            self.sp = None
            self.pathEndpointStart = 0
            self.pathEndpointEnd = 0
            self.pathPositionIndex = 0
            self.pathPositionTimestamp = 0.0
            self.pathState = 0
            self.path = None
            self.localPathState = 0
            self.currentLeg = -1
            self.pathStartTime = 0.0
            self.legList = None
            self.prop = None
            self.propInSound = None
            self.propOutSound = None
            self.initState = None
            self.finalState = None
            self.reparentTo(hidden)
            self.loop('neutral')
            self.buildingSuit = 0
            self.fsm = FSM.FSM('DistributedSuit', [
                State.State('Off', self.enterOff, self.exitOff, [
                    'FromSky',
                    'FromSuitBuilding',
                    'Bellicose',
                    'TutorialBellicose',
                    'Battle',
                    'Door',
                    'ToToonBuilding',
                    'ToSuitBuilding',
                    'ToSky',
                    'FlyAway',
                    'DanceThenFlyAway',
                    'WalkToStreet',
                    'WalkFromStreet']),
                State.State('FromSky', self.enterFromSky, self.exitFromSky, [
                    'Bellicose',
                    'Battle',
                    'Door',
                    'ToSky',
                    'WalkFromStreet']),
                State.State('FromSuitBuilding', self.enterFromSuitBuilding, self.exitFromSuitBuilding, [
                    'WalkToStreet',
                    'Bellicose',
                    'Battle',
                    'Door',
                    'ToSky']),
                State.State('WalkToStreet', self.enterWalkToStreet, self.exitWalkToStreet, [
                    'Bellicose',
                    'Battle',
                    'Door',
                    'ToSky',
                    'ToToonBuilding',
                    'ToSuitBuilding',
                    'WalkFromStreet']),
                State.State('WalkFromStreet', self.enterWalkFromStreet, self.exitWalkFromStreet, [
                    'ToToonBuilding',
                    'ToSuitBuilding',
                    'Battle',
                    'Door',
                    'ToSky']),
                State.State('Bellicose', self.enterBellicose, self.exitBellicose, [
                    'WaitForBattle',
                    'Battle',
                    'Door',
                    'WalkFromStreet',
                    'ToSky',
                    'Bellicose']),
                State.State('TutorialBellicose', self.enterTutorialBellicose, self.exitTutorialBellicose, [
                    'WaitForBattle',
                    'Battle']),
                State.State('Battle', self.enterBattle, self.exitBattle, [
                    'Bellicose',
                    'ToToonBuilding',
                    'ToSuitBuilding',
                    'ToSky']),
                State.State('Door', self.enterDoor, self.exitDoor, []),
                State.State('WaitForBattle', self.enterWaitForBattle, self.exitWaitForBattle, [
                    'Battle',
                    'Door',
                    'Bellicose',
                    'WalkToStreet',
                    'WalkFromStreet',
                    'ToToonBuilding',
                    'ToSuitBuilding',
                    'ToSky']),
                State.State('ToToonBuilding', self.enterToToonBuilding, self.exitToToonBuilding, [
                    'Door',
                    'Battle']),
                State.State('ToSuitBuilding', self.enterToSuitBuilding, self.exitToSuitBuilding, [
                    'Door',
                    'Battle']),
                State.State('ToSky', self.enterToSky, self.exitToSky, [
                    'Battle']),
                State.State('FlyAway', self.enterFlyAway, self.exitFlyAway, []),
                State.State('DanceThenFlyAway', self.enterDanceThenFlyAway, self.exitDanceThenFlyAway, [])], 'Off', 'Off')
            self.fsm.enterInitialState()

        return None

    
    def generate(self):
        if self.notify.getDebug():
            self.notify.debug('DistributedSuit %d: generating' % self.getDoId())
        
        DistributedAvatar.DistributedAvatar.generate(self)

    
    def disable(self):
        self.notify.debug('DistributedSuit %d: disabling' % self.getDoId())
        self.resumePath(0)
        self.stopPathNow()
        self.setState('Off')
        DistributedAvatar.DistributedAvatar.disable(self)
        self.ignoreAll()
        self._DistributedSuit__removeCollisionData()
        self.cleanupLoseActor()
        self.stop()
        taskMgr.remove(self.uniqueName('blink-task'))
        return None

    
    def delete(self):
        
        try:
            pass
        except:
            self.DistributedSuit_deleted = 1
            self.notify.debug('DistributedSuit %d: deleting' % self.getDoId())
            del self.fsm
            del self.dna
            del self.sp
            DistributedAvatar.DistributedAvatar.delete(self)
            Suit.Suit.delete(self)
            SuitBase.SuitBase.delete(self)

        return None

    
    def playDialogue(self, *args):
        Suit.Suit.playDialogue(self, *args)

    
    def _DistributedSuit__removeCollisionData(self):
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
            if self.notify.getDebug():
                self.notify.debug('setting dna string for %d...' % self.getDoId())
            
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

    
    def setPathEndpoints(self, start, end):
        if self.pathEndpointStart == start and self.pathEndpointEnd == end and self.path != None:
            return None
        
        self.pathEndpointStart = start
        self.pathEndpointEnd = end
        self.path = None
        self.pathLength = 0
        self.currentLeg = -1
        self.legList = None
        if self.pathEndpointStart == self.pathEndpointEnd:
            return None
        
        if not self.verifySuitPlanner():
            return None
        
        self.startPoint = self.sp.pointIndexes[self.pathEndpointStart]
        self.endPoint = self.sp.pointIndexes[self.pathEndpointEnd]
        path = self.sp.genPath(self.startPoint, self.endPoint)
        self.setPath(path)
        self.makeLegList()
        return None

    
    def verifySuitPlanner(self):
        if self.sp == None and self.spDoId != 0:
            self.notify.warning('Suit %d does not have a suit planner!  Expected SP doId %s.' % (self.doId, self.spDoId))
            self.sp = self.cr.doId2do.get(self.spDoId, None)
        
        if self.sp == None:
            self.notify.warning('Cannot create path for suit %d' % self.doId)
            return 0
        
        return 1

    
    def setPathPosition(self, index, timestamp):
        if not self.verifySuitPlanner():
            return None
        
        if self.path == None:
            self.setPathEndpoints(self.pathEndpointStart, self.pathEndpointEnd)
        
        self.pathPositionIndex = index
        self.pathPositionTimestamp = globalClockDelta.networkToLocalTime(timestamp)
        if self.legList != None:
            self.pathStartTime = self.pathPositionTimestamp - self.legList.getStartTime(self.pathPositionIndex)
        

    
    def setPathState(self, state):
        self.pathState = state
        self.resumePath(state)

    
    def debugSuitPosition(self, elapsed, currentLeg, x, y, timestamp):
        now = globalClock.getFrameTime()
        chug = globalClock.getRealTime() - now
        messageAge = now - globalClockDelta.networkToLocalTime(timestamp, now)
        if messageAge < -(chug + 0.5) or messageAge > chug + 1.0:
            print 'Apparently out of sync with AI by %0.2f seconds.  Suggest resync!' % messageAge
            return None
        
        localElapsed = now - self.pathStartTime
        timeDiff = localElapsed - elapsed + messageAge
        if abs(timeDiff) > 0.20000000000000001:
            print "%s (%d) appears to be %0.2f seconds out of sync along its path.  Suggest '~cogs sync'." % (self.getName(), self.getDoId(), timeDiff)
            return None
        
        if self.legList == None:
            print "%s (%d) doesn't have a legList yet." % (self.getName(), self.getDoId())
            return None
        
        netPos = Point3(x, y, 0.0)
        leg = self.legList.getLeg(currentLeg)
        calcPos = leg.getPosAtTime(elapsed - leg.getStartTime())
        calcPos.setZ(0.0)
        calcDelta = Vec3(netPos - calcPos)
        diff = calcDelta.length()
        if diff > 4.0:
            print '%s (%d) is %0.2f feet from the AI computed path!' % (self.getName(), self.getDoId(), diff)
            print 'Probably your DNA files are out of sync.'
            return None
        
        localPos = Point3(self.getX(), self.getY(), 0.0)
        localDelta = Vec3(netPos - localPos)
        diff = localDelta.length()
        if diff > 10.0:
            print '%s (%d) in state %s is %0.2f feet from its correct position!' % (self.getName(), self.getDoId(), self.fsm.getCurrentState().getName(), diff)
            print 'Should be at (%0.2f, %0.2f), but is at (%0.2f, %0.2f).' % (x, y, localPos[0], localPos[1])
            return None
        
        print '%s (%d) is in the correct position.' % (self.getName(), self.getDoId())

    
    def resumePath(self, state):
        if self.localPathState != state:
            self.localPathState = state
            if state == 0:
                self.stopPathNow()
            elif state == 1:
                self.moveToNextLeg(None)
            elif state == 2:
                self.stopPathNow()
                self.setState('Off')
                if self.sp != None:
                    self.setState('FlyAway')
                
            elif state == 3:
                self.setState('TutorialBellicose')
            elif state == 4:
                self.stopPathNow()
                self.setState('Off')
                if self.sp != None:
                    self.setState('DanceThenFlyAway')
                
            else:
                self.notify.error('No such state as: ' + str(state))
        

    
    def moveToNextLeg(self, task):
        if self.legList == None:
            self.notify.warning('Suit %d does not have a path!')
            return Task.done
        
        now = globalClock.getFrameTime()
        elapsed = now - self.pathStartTime
        nextLeg = self.legList.getLegIndexAtTime(elapsed, self.currentLeg)
        numLegs = self.legList.getNumLegs()
        if self.currentLeg != nextLeg:
            self.currentLeg = nextLeg
            self.doPathLeg(self.legList[nextLeg], elapsed - self.legList.getStartTime(nextLeg))
            self.notify.debug('Suit %d reached leg %d of %d.' % (self.getDoId(), nextLeg, numLegs - 1))
        
        nextLeg += 1
        if nextLeg < numLegs:
            nextTime = self.legList.getStartTime(nextLeg)
            delay = nextTime - elapsed
            name = self.taskName('move')
            taskMgr.remove(name)
            taskMgr.doMethodLater(delay, self.moveToNextLeg, name)
        
        return Task.done

    
    def doPathLeg(self, leg, time):
        self.fsm.request(SuitLeg.getTypeName(leg.getType()), [
            leg,
            time])
        return 0

    
    def stopPathNow(self):
        name = self.taskName('move')
        taskMgr.remove(name)
        self.currentLeg = -1

    
    def calculateHeading(self, a, b):
        xdelta = b[0] - a[0]
        ydelta = b[1] - a[1]
        if ydelta == 0:
            if xdelta > 0:
                return -90
            else:
                return 90
        elif xdelta == 0:
            if ydelta > 0:
                return 0
            else:
                return 180
        else:
            angle = math.atan2(ydelta, xdelta)
            return rad2Deg(angle) - 90

    
    def beginBuildingMove(self, moveIn, doneEvent, suit = 0):
        doorPt = Point3(0)
        buildingPt = Point3(0)
        streetPt = Point3(0)
        if self.virtualPos:
            doorPt.assign(self.virtualPos)
        else:
            doorPt.assign(self.getPos())
        if moveIn:
            streetPt = self.prevPointPos()
        else:
            streetPt = self.currPointPos()
        dx = doorPt[0] - streetPt[0]
        dy = doorPt[1] - streetPt[1]
        buildingPt = Point3(doorPt[0] + dx, doorPt[1] + dy, doorPt[2])
        if moveIn:
            if suit:
                moveTime = SuitTimings.toSuitBuilding
            else:
                moveTime = SuitTimings.toToonBuilding
            return self.beginMove(doneEvent, buildingPt, time = moveTime)
        else:
            return self.beginMove(doneEvent, doorPt, buildingPt, time = SuitTimings.fromSuitBuilding)
        return None

    
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

    
    def enableBattleDetect(self, name):
        if not ALLOW_BATTLE_DETECT:
            self.notify.debug('not allowing battle detection')
            return Task.done
        
        if self.bSphereNodePath:
            self.bSphereNodePath.removeNode()
            self.bSphereNodePath = None
        
        if self.bSphere:
            self.bSphereName = self.taskName(name)
            self.bSphereNode = CollisionNode(self.bSphereName)
            self.bSphereNode.addSolid(self.bSphere)
            self.bSphereNodePath = self.attachNewNode(self.bSphereNode)
            self.bSphereNode.setCollideMask(ToontownGlobals.WallBitmask)
            self.accept('enter' + self.bSphereName, self._DistributedSuit__handleToonCollision)
        
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

    
    def setState(self, state):
        debug = self.notify.getDebug()
        if self.fsm.getCurrentState().getName() == state:
            if debug:
                self.notify.debug('State change ignored, already in ' + 'state' + str(state))
            
            return 0
        
        if debug:
            self.notify.debug('DistributedSuit: entering state: %s from %s' % (state, self.fsm.getCurrentState().getName()))
        
        return self.fsm.request(state)

    
    def setSPDoId(self, doId):
        self.spDoId = doId
        self.sp = self.cr.doId2do.get(doId, None)
        if self.sp == None and self.spDoId != 0:
            self.notify.warning('Suit %s created before its suit planner, %d' % (self.doId, self.spDoId))
        

    
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

    
    def denyBattle(self):
        self.notify.debug('denyBattle()')
        self.cr.playGame.getPlace().setState('walk')
        self.resumePath(self.pathState)

    
    def _DistributedSuit__handleToonCollision(self, collEntry):
        toonId = toonbase.localToon.getDoId()
        self.notify.debug('Distributed suit: requesting a Battle with ' + 'toon: %d' % toonId)
        self.d_requestBattle(self.getPos(), self.getHpr())
        self.setState('WaitForBattle')
        return None

    
    def enterOff(self, *args):
        self.hideNametag3d()
        self.hideNametag2d()
        self.notify.debug('enterOff()')
        self.setParent(ToontownGlobals.SPHidden)
        self.loop('neutral', 0)

    
    def exitOff(self):
        self.setParent(ToontownGlobals.SPRender)
        self.showNametag3d()
        self.showNametag2d()

    
    def enterFromSky(self, leg, time):
        self.enableBattleDetect('fromSky')
        self.loop('neutral', 0)
        if not self.verifySuitPlanner():
            return None
        
        a = leg.getPosA()
        b = leg.getPosB()
        a.setZ(self.STREET_HEIGHT_OFFSET)
        h = self.calculateHeading(a, b)
        self.setPosHprScale(a[0], a[1], a[2], h, 0.0, 0.0, 1.0, 1.0, 1.0)
        self.mtrack = self.beginSupaFlyMove(a, 1, 'fromSky')
        self.mtrack.start(time)

    
    def exitFromSky(self):
        self.disableBattleDetect()
        self.mtrack.finish()
        del self.mtrack
        self.detachPropeller()
        self.dropShadows[0].reparentTo(self.getShadowJoints()[0])
        self.dropShadows[0].clearMat()

    
    def enterWalkToStreet(self, leg, time):
        self.enableBattleDetect('walkToStreet')
        self.loop('walk', 0)
        a = leg.getPosA()
        b = leg.getPosB()
        b.setZ(self.STREET_HEIGHT_OFFSET)
        delta = Vec3(b - a)
        length = delta.length()
        delta *= (length - STAND_OUTSIDE_DOOR) / length
        a1 = Point3(b - delta)
        self.enableRaycast(1)
        h = self.calculateHeading(a, b)
        self.setHprScale(h, 0.0, 0.0, 1.0, 1.0, 1.0)
        self.mtrack = Sequence(LerpPosInterval(self, leg.getLegTime(), b, startPos = a1), name = self.taskName('walkToStreet'))
        self.mtrack.start(time)

    
    def exitWalkToStreet(self):
        self.disableBattleDetect()
        self.enableRaycast(0)
        self.mtrack.finish()
        del self.mtrack

    
    def enterWalkFromStreet(self, leg, time):
        self.enableBattleDetect('walkFromStreet')
        self.loop('walk', 0)
        a = leg.getPosA()
        b = leg.getPosB()
        a.setZ(self.STREET_HEIGHT_OFFSET)
        delta = Vec3(b - a)
        length = delta.length()
        delta *= (length - STAND_OUTSIDE_DOOR) / length
        b1 = Point3(a + delta)
        self.enableRaycast(1)
        h = self.calculateHeading(a, b)
        self.setHprScale(h, 0.0, 0.0, 1.0, 1.0, 1.0)
        self.mtrack = Sequence(LerpPosInterval(self, leg.getLegTime(), b1, startPos = a), name = self.taskName('walkFromStreet'))
        self.mtrack.start(time)

    
    def exitWalkFromStreet(self):
        self.disableBattleDetect()
        self.enableRaycast(0)
        self.mtrack.finish()
        del self.mtrack

    
    def enterBellicose(self, leg, time):
        self.enableBattleDetect('bellicose')
        self.loop('walk', 0)
        a = leg.getPosA()
        b = leg.getPosB()
        a.setZ(self.STREET_HEIGHT_OFFSET)
        b.setZ(self.STREET_HEIGHT_OFFSET)
        h = self.calculateHeading(a, b)
        pos = leg.getPosAtTime(time)
        self.setPosHprScale(pos[0], pos[1], self.STREET_HEIGHT_OFFSET, h, 0.0, 0.0, 1.0, 1.0, 1.0)
        self.mtrack = Sequence(LerpPosInterval(self, leg.getLegTime(), b, startPos = a), name = self.taskName('bellicose'))
        self.mtrack.start(time)

    
    def exitBellicose(self):
        self.disableBattleDetect()
        self.mtrack.pause()
        del self.mtrack

    
    def enterTutorialBellicose(self):
        self.enableBattleDetect('tutorialBellicose')
        self.loop('walk', 0)
        pathPoints = [
            Vec3(50, 15, 0),
            Vec3(50, 25, 0),
            Vec3(20, 25, 0),
            Vec3(20, 15, 0),
            Vec3(50, 15, 0)]
        self.tutWalkTrack = self.makePathTrack(self, pathPoints, 4.5, 'tutFlunkyWalk')
        self.tutWalkTrack.loop()

    
    def exitTutorialBellicose(self):
        self.disableBattleDetect()
        self.tutWalkTrack.pause()
        self.tutWalkTrack = None
        return None

    
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

    
    def enterToSky(self, leg, time):
        self.enableBattleDetect('toSky')
        if not self.verifySuitPlanner():
            return None
        
        a = leg.getPosA()
        b = leg.getPosB()
        b.setZ(self.STREET_HEIGHT_OFFSET)
        h = self.calculateHeading(a, b)
        self.setPosHprScale(b[0], b[1], b[2], h, 0.0, 0.0, 1.0, 1.0, 1.0)
        self.mtrack = self.beginSupaFlyMove(b, 0, 'toSky')
        self.mtrack.start(time)

    
    def exitToSky(self):
        self.disableBattleDetect()
        self.mtrack.finish()
        del self.mtrack
        self.detachPropeller()
        self.dropShadows[0].reparentTo(self.getShadowJoints()[0])
        self.dropShadows[0].clearMat()

    
    def enterFromSuitBuilding(self, leg, time):
        self.enableBattleDetect('fromSuitBuilding')
        self.loop('walk', 0)
        if not self.verifySuitPlanner():
            return None
        
        a = leg.getPosA()
        b = leg.getPosB()
        b.setZ(self.STREET_HEIGHT_OFFSET)
        delta = Vec3(b - a)
        length = delta.length()
        delta2 = delta * self.sp.suitWalkSpeed * leg.getLegTime() / length
        delta *= (length - STAND_OUTSIDE_DOOR) / length
        b1 = Point3(b - delta)
        a1 = Point3(b1 - delta2)
        self.enableRaycast(1)
        h = self.calculateHeading(a, b)
        self.setHprScale(h, 0.0, 0.0, 1.0, 1.0, 1.0)
        self.mtrack = Sequence(LerpPosInterval(self, leg.getLegTime(), b1, startPos = a1), name = self.taskName('fromSuitBuilding'))
        self.mtrack.start(time)

    
    def exitFromSuitBuilding(self):
        self.disableBattleDetect()
        self.mtrack.finish()
        del self.mtrack

    
    def enterToToonBuilding(self, leg, time):
        self.loop('neutral', 0)

    
    def exitToToonBuilding(self):
        return None

    
    def enterToSuitBuilding(self, leg, time):
        self.loop('walk', 0)
        if not self.verifySuitPlanner():
            return None
        
        a = leg.getPosA()
        b = leg.getPosB()
        a.setZ(self.STREET_HEIGHT_OFFSET)
        delta = Vec3(b - a)
        length = delta.length()
        delta2 = delta * self.sp.suitWalkSpeed * leg.getLegTime() / length
        delta *= (length - STAND_OUTSIDE_DOOR) / length
        a1 = Point3(a + delta)
        b1 = Point3(a1 + delta2)
        self.enableRaycast(1)
        h = self.calculateHeading(a, b)
        self.setHprScale(h, 0.0, 0.0, 1.0, 1.0, 1.0)
        self.mtrack = Sequence(LerpPosInterval(self, leg.getLegTime(), b1, startPos = a1), name = self.taskName('toSuitBuilding'))
        self.mtrack.start(time)

    
    def exitToSuitBuilding(self):
        self.mtrack.finish()
        del self.mtrack

    
    def enterBattle(self):
        self.notify.debug('DistributedSuit: entering a Battle')
        self.resumePath(0)
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

    
    def enterDoor(self):
        self.notify.debug('DistributedSuit: entering a Door')
        self.resumePath(0)
        self.loop('neutral', 0)

    
    def exitDoor(self):
        return None

    
    def enterWaitForBattle(self):
        self.resumePath(0)
        self.loop('neutral', 0)
        return None

    
    def exitWaitForBattle(self):
        return None

    
    def enterFlyAway(self):
        self.enableBattleDetect('flyAway')
        if not self.verifySuitPlanner():
            return None
        
        b = Point3(self.getPos())
        self.mtrack = self.beginSupaFlyMove(b, 0, 'flyAway')
        self.mtrack.start()
        return None

    
    def exitFlyAway(self):
        self.disableBattleDetect()
        self.mtrack.finish()
        del self.mtrack
        self.detachPropeller()
        self.dropShadows[0].reparentTo(self.getShadowJoints()[0])
        self.dropShadows[0].clearMat()
        return None

    
    def enterDanceThenFlyAway(self):
        self.enableBattleDetect('danceThenFlyAway')
        if not self.verifySuitPlanner():
            return None
        
        danceTrack = self.actorInterval('victory')
        b = Point3(self.getPos())
        flyMtrack = self.beginSupaFlyMove(b, 0, 'flyAway')
        self.mtrack = Sequence(danceTrack, flyMtrack, name = self.taskName('danceThenFlyAway'))
        self.mtrack.start()
        return None

    
    def exitDanceThenFlyAway(self):
        self.disableBattleDetect()
        self.mtrack.finish()
        del self.mtrack
        self.detachPropeller()
        self.dropShadows[0].reparentTo(self.getShadowJoints()[0])
        self.dropShadows[0].clearMat()
        return None


