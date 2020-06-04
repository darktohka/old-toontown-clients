# File: O (Python 2.2)

from toontown.toonbase.ToonBaseGlobal import *
from direct.interval.IntervalGlobal import *
import ArrowKeys

class OrthoDrive:
    notify = DirectNotifyGlobal.directNotify.newCategory('OrthoDrive')
    TASK_NAME = 'OrthoDriveTask'
    SET_ATREST_HEADING_TASK = 'setAtRestHeadingTask'
    
    def __init__(self, speed, maxFrameMove = None, customCollisionCallback = None, priority = 0, setHeading = 1, upHeading = 0):
        self.speed = speed
        self.maxFrameMove = maxFrameMove
        self.customCollisionCallback = customCollisionCallback
        self.priority = priority
        self.setHeading = setHeading
        self.upHeading = upHeading
        self.arrowKeys = ArrowKeys.ArrowKeys()
        self.lt = base.localAvatar

    
    def destroy(self):
        self.arrowKeys.destroy()
        del self.arrowKeys
        del self.customCollisionCallback

    
    def start(self):
        self.notify.debug('start')
        self._OrthoDrive__placeToonHOG(self.lt.getPos())
        taskMgr.add(self._OrthoDrive__update, OrthoDrive.TASK_NAME, priority = self.priority)

    
    def _OrthoDrive__placeToonHOG(self, pos, h = None):
        if h == None:
            h = self.lt.getH()
        
        self.lt.setPos(pos)
        self.lt.setH(h)
        self.lastPos = pos
        self.atRestHeading = h
        self.lastXVel = 0
        self.lastYVel = 0

    
    def stop(self):
        self.notify.debug('stop')
        taskMgr.remove(OrthoDrive.TASK_NAME)
        taskMgr.remove(OrthoDrive.SET_ATREST_HEADING_TASK)
        if hasattr(self, 'turnLocalToonIval'):
            if self.turnLocalToonIval.isPlaying():
                self.turnLocalToonIval.pause()
            
            del self.turnLocalToonIval
        
        base.localAvatar.setSpeed(0, 0)

    
    def _OrthoDrive__update(self, task):
        vel = Vec3(0, 0, 0)
        xVel = 0
        yVel = 0
        if self.arrowKeys.upPressed():
            yVel += 1
        
        if self.arrowKeys.downPressed():
            yVel -= 1
        
        if self.arrowKeys.leftPressed():
            xVel -= 1
        
        if self.arrowKeys.rightPressed():
            xVel += 1
        
        vel.setX(xVel)
        vel.setY(yVel)
        vel.normalize()
        vel *= self.speed
        speed = vel.length()
        self.lt.setSpeed(speed, 0)
        if self.setHeading:
            self._OrthoDrive__handleHeading(xVel, yVel)
        
        toonPos = self.lt.getPos()
        dt = globalClock.getDt()
        posOffset = vel * dt
        posOffset += toonPos - self.lastPos
        toonPos = self.lastPos
        if self.maxFrameMove:
            posOffsetLen = posOffset.length()
            if posOffsetLen > self.maxFrameMove:
                posOffset *= self.maxFrameMove
                posOffset /= posOffsetLen
            
        
        if self.customCollisionCallback:
            toonPos = self.customCollisionCallback(toonPos, toonPos + posOffset)
        
        self.lt.setPos(toonPos)
        self.lastPos = toonPos
        return Task.cont

    
    def _OrthoDrive__handleHeading(self, xVel, yVel):
        
        def getHeading(xVel, yVel):
            angTab = [
                [
                    None,
                    0,
                    180],
                [
                    -90,
                    -45,
                    -135],
                [
                    90,
                    45,
                    135]]
            return angTab[xVel][yVel] + self.upHeading

        
        def orientToon(angle, self = self):
            startAngle = self.lt.getH()
            startAngle = fitSrcAngle2Dest(startAngle, angle)
            dur = 0.10000000000000001 * abs(startAngle - angle) / 90
            self.turnLocalToonIval = LerpHprInterval(self.lt, dur, Point3(angle, 0, 0), startHpr = Point3(startAngle, 0, 0), name = 'OrthoDriveLerpHpr')
            self.turnLocalToonIval.start()

        if xVel != self.lastXVel or yVel != self.lastYVel:
            taskMgr.remove(OrthoDrive.SET_ATREST_HEADING_TASK)
            if not xVel:
                pass
            if not yVel:
                orientToon(self.atRestHeading)
            else:
                curHeading = getHeading(xVel, yVel)
                if self.lastXVel and self.lastYVel:
                    if xVel:
                        pass
                    if not yVel:
                        
                        def setAtRestHeading(task, self = self, angle = curHeading):
                            self.atRestHeading = angle
                            return Task.done

                        taskMgr.doMethodLater(0.050000000000000003, setAtRestHeading, OrthoDrive.SET_ATREST_HEADING_TASK)
                    else:
                        self.atRestHeading = curHeading
                orientToon(curHeading)
        
        self.lastXVel = xVel
        self.lastYVel = yVel


