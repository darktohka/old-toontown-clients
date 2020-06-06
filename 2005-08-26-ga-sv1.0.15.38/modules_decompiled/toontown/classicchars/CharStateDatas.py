# File: C (Python 2.2)

from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from direct.distributed.ClockDelta import *
from direct.fsm import StateData
from direct.directnotify import DirectNotifyGlobal
import CCharPaths
from toontown.toonbase import ToontownGlobals

class CharNeutralState(StateData.StateData):
    notify = DirectNotifyGlobal.directNotify.newCategory('CharNeutralState')
    
    def __init__(self, doneEvent, character):
        StateData.StateData.__init__(self, doneEvent)
        self._CharNeutralState__doneEvent = doneEvent
        self.character = character

    
    def enter(self, startTrack = None, playRate = None):
        StateData.StateData.enter(self)
        self.notify.debug('Neutral ' + self.character.getName() + '...')
        self._CharNeutralState__neutralTrack = Sequence(name = self.character.getName() + '-neutral')
        if startTrack:
            self._CharNeutralState__neutralTrack.append(startTrack)
        
        if playRate:
            self._CharNeutralState__neutralTrack.append(Func(self.character.setPlayRate, playRate, 'neutral'))
        
        self._CharNeutralState__neutralTrack.append(Func(self.character.loop, 'neutral'))
        self._CharNeutralState__neutralTrack.start()

    
    def exit(self):
        StateData.StateData.exit(self)
        self._CharNeutralState__neutralTrack.finish()

    
    def _CharNeutralState__doneHandler(self):
        doneStatus = { }
        doneStatus['state'] = 'walk'
        doneStatus['status'] = 'done'
        messenger.send(self._CharNeutralState__doneEvent, [
            doneStatus])
        return Task.done



class CharWalkState(StateData.StateData):
    notify = DirectNotifyGlobal.directNotify.newCategory('CharWalkState')
    
    def __init__(self, doneEvent, character):
        StateData.StateData.__init__(self, doneEvent)
        self._CharWalkState__doneEvent = doneEvent
        self.character = character
        self.paths = CCharPaths.getPaths(character.getName())
        self.speed = character.walkSpeed()

    
    def enter(self, startTrack = None, playRate = None):
        StateData.StateData.enter(self)
        self.notify.debug('Walking ' + self.character.getName() + '... from ' + str(self._CharWalkState__walkInfo[0]) + ' to ' + str(self._CharWalkState__walkInfo[1]))
        posPoints = CCharPaths.getPointsFromTo(self._CharWalkState__walkInfo[0], self._CharWalkState__walkInfo[1], self.paths)
        self._CharWalkState__walkTrack = Sequence(name = self.character.getName() + '-walk')
        if startTrack:
            self._CharWalkState__walkTrack.append(startTrack)
        
        self.character.setPos(posPoints[0])
        raycast = CCharPaths.getRaycastFlag(self._CharWalkState__walkInfo[0], self._CharWalkState__walkInfo[1], self.paths)
        moveTrack = self._CharWalkState__makePathTrack(self.character, posPoints, self.speed, raycast)
        if playRate:
            self._CharWalkState__walkTrack.append(Func(self.character.setPlayRate, playRate, 'walk'))
        
        self._CharWalkState__walkTrack.append(Func(self.character.loop, 'walk'))
        self._CharWalkState__walkTrack.append(moveTrack)
        doneEventName = self.character.getName() + 'WalkDone'
        self._CharWalkState__walkTrack.append(Func(messenger.send, doneEventName))
        ts = globalClockDelta.localElapsedTime(self._CharWalkState__walkInfo[2])
        self.accept(doneEventName, self._CharWalkState__doneHandler)
        self.notify.debug('walkTrack.start(%s)' % ts)
        self._CharWalkState__walkTrack.start(ts)

    
    def _CharWalkState__makePathTrack(self, nodePath, posPoints, velocity, raycast = 0):
        track = Sequence()
        if raycast:
            track.append(Func(nodePath.enableRaycast, 1))
        
        startHpr = nodePath.getHpr()
        for pointIndex in range(len(posPoints) - 1):
            startPoint = posPoints[pointIndex]
            endPoint = posPoints[pointIndex + 1]
            track.append(Func(nodePath.setPos, startPoint))
            distance = Vec3(endPoint - startPoint).length()
            duration = distance / velocity
            curHpr = nodePath.getHpr()
            nodePath.headsUp(endPoint[0], endPoint[1], endPoint[2])
            destHpr = nodePath.getHpr()
            reducedCurH = reduceAngle(curHpr[0])
            reducedCurHpr = Vec3(reducedCurH, curHpr[1], curHpr[2])
            reducedDestH = reduceAngle(destHpr[0])
            shortestAngle = closestDestAngle(reducedCurH, reducedDestH)
            shortestHpr = Vec3(shortestAngle, destHpr[1], destHpr[2])
            turnTime = abs(shortestAngle) / 270.0
            nodePath.setHpr(shortestHpr)
            if duration - turnTime > 0.01:
                track.append(Parallel(Func(nodePath.loop, 'walk'), LerpHprInterval(nodePath, turnTime, shortestHpr, startHpr = reducedCurHpr, name = 'lerp' + nodePath.getName() + 'Hpr'), LerpPosInterval(nodePath, duration = duration - turnTime, pos = Point3(endPoint), startPos = Point3(startPoint), fluid = 1)))
            
        
        nodePath.setHpr(startHpr)
        if raycast:
            track.append(Func(nodePath.enableRaycast, 0))
        
        return track

    
    def _CharWalkState__doneHandler(self):
        doneStatus = { }
        doneStatus['state'] = 'walk'
        doneStatus['status'] = 'done'
        messenger.send(self._CharWalkState__doneEvent, [
            doneStatus])
        return Task.done

    
    def exit(self):
        StateData.StateData.exit(self)
        self.ignore(self.character.getName() + 'WalkDone')
        self._CharWalkState__walkTrack.finish()

    
    def setWalk(self, srcNode, destNode, timestamp):
        self._CharWalkState__walkInfo = (srcNode, destNode, timestamp)


