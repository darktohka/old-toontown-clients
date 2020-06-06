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
import DistributedSuitBase
STAND_OUTSIDE_DOOR = 2.5
BATTLE_IGNORE_TIME = 6
BATTLE_WAIT_TIME = 3
CATCHUP_SPEED_MULTIPLIER = 3
ALLOW_BATTLE_DETECT = 1

class DistributedSuit(DistributedSuitBase.DistributedSuitBase):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedSuit')
    ENABLE_EXPANDED_NAME = 0
    STREET_HEIGHT_OFFSET = -0.5
    
    def __init__(self, cr):
        
        try:
            pass
        except:
            self.DistributedSuit_initialized = 1
            DistributedSuitBase.DistributedSuitBase.__init__(self, cr)
            self.spDoId = None
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
            self.initState = None
            self.finalState = None
            self.buildingSuit = 0
            self.fsm = FSM.FSM('DistributedSuit', [
                State.State('Off', self.enterOff, self.exitOff, [
                    'FromSky',
                    'FromSuitBuilding',
                    'Walk',
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
                    'Walk',
                    'Battle',
                    'Door',
                    'ToSky',
                    'WalkFromStreet']),
                State.State('FromSuitBuilding', self.enterFromSuitBuilding, self.exitFromSuitBuilding, [
                    'WalkToStreet',
                    'Walk',
                    'Battle',
                    'Door',
                    'ToSky']),
                State.State('WalkToStreet', self.enterWalkToStreet, self.exitWalkToStreet, [
                    'Walk',
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
                State.State('Walk', self.enterWalk, self.exitWalk, [
                    'WaitForBattle',
                    'Battle',
                    'Door',
                    'WalkFromStreet',
                    'ToSky',
                    'Walk']),
                State.State('Battle', self.enterBattle, self.exitBattle, [
                    'Walk',
                    'ToToonBuilding',
                    'ToSuitBuilding',
                    'ToSky']),
                State.State('Door', self.enterDoor, self.exitDoor, []),
                State.State('WaitForBattle', self.enterWaitForBattle, self.exitWaitForBattle, [
                    'Battle',
                    'Door',
                    'Walk',
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
        DistributedSuitBase.DistributedSuitBase.generate(self)

    
    def disable(self):
        self.notify.debug('DistributedSuit %d: disabling' % self.getDoId())
        self.resumePath(0)
        self.stopPathNow()
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
                pass
            elif state == 4:
                self.stopPathNow()
                self.setState('Off')
                if self.sp != None:
                    self.setState('DanceThenFlyAway')
                
            else:
                self.notify.error('No such state as: ' + str(state))
        

    
    def moveToNextLeg(self, task):
        if self.legList == None:
            self.notify.warning('Suit %d does not have a path!' % self.getDoId())
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

    
    def setSPDoId(self, doId):
        self.spDoId = doId
        self.sp = self.cr.doId2do.get(doId, None)
        if self.sp == None and self.spDoId != 0:
            self.notify.warning('Suit %s created before its suit planner, %d' % (self.doId, self.spDoId))
        

    
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

    
    def _DistributedSuit__handleToonCollision(self, collEntry):
        toonId = toonbase.localToon.getDoId()
        self.notify.debug('Distributed suit: requesting a Battle with ' + 'toon: %d' % toonId)
        self.d_requestBattle(self.getPos(), self.getHpr())
        self.setState('WaitForBattle')
        return None

    
    def enterFromSky(self, leg, time):
        self.enableBattleDetect('fromSky', self._DistributedSuit__handleToonCollision)
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
        self.enableBattleDetect('walkToStreet', self._DistributedSuit__handleToonCollision)
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
        self.enableBattleDetect('walkFromStreet', self._DistributedSuit__handleToonCollision)
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

    
    def enterWalk(self, leg, time):
        self.enableBattleDetect('bellicose', self._DistributedSuit__handleToonCollision)
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

    
    def exitWalk(self):
        self.disableBattleDetect()
        self.mtrack.pause()
        del self.mtrack

    
    def enterToSky(self, leg, time):
        self.enableBattleDetect('toSky', self._DistributedSuit__handleToonCollision)
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
        self.enableBattleDetect('fromSuitBuilding', self._DistributedSuit__handleToonCollision)
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
        DistributedSuitBase.DistributedSuitBase.enterBattle(self)
        self.resumePath(0)

    
    def enterDoor(self):
        self.notify.debug('DistributedSuit: entering a Door')
        self.resumePath(0)
        self.loop('neutral', 0)

    
    def exitDoor(self):
        return None

    
    def enterWaitForBattle(self):
        DistributedSuitBase.DistributedSuitBase.enterWaitForBattle(self)
        self.resumePath(0)

    
    def enterFlyAway(self):
        self.enableBattleDetect('flyAway', self._DistributedSuit__handleToonCollision)
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
        self.enableBattleDetect('danceThenFlyAway', self._DistributedSuit__handleToonCollision)
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


