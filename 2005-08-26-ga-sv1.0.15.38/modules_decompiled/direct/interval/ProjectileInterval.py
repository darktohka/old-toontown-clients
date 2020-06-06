# File: P (Python 2.2)

from direct.showbase.DirectObject import *
from pandac.PandaModules import *
from Interval import Interval
from direct.showbase.PythonUtil import lerp
from direct.showbase import PythonUtil

class ProjectileInterval(Interval):
    notify = directNotify.newCategory('ProjectileInterval')
    projectileIntervalNum = 1
    gravity = 32.0
    
    def __init__(self, node, startPos = None, endPos = None, duration = None, startVel = None, endZ = None, wayPoint = None, timeToWayPoint = None, gravityMult = None, name = None):
        self.node = node
        if name == None:
            name = '%s-%s' % (self.__class__.__name__, self.projectileIntervalNum)
            ProjectileInterval.projectileIntervalNum += 1
        
        args = (startPos, endPos, duration, startVel, endZ, wayPoint, timeToWayPoint, gravityMult)
        self.implicitStartPos = 0
        if startPos is None:
            if duration is None:
                self.notify.error('must provide either startPos or duration')
            
            self.duration = duration
            self.trajectoryArgs = args
            self.implicitStartPos = 1
        else:
            self._ProjectileInterval__calcTrajectory(*args)
        Interval.__init__(self, name, self.duration)

    
    def _ProjectileInterval__calcTrajectory(self, startPos = None, endPos = None, duration = None, startVel = None, endZ = None, wayPoint = None, timeToWayPoint = None, gravityMult = None):
        if startPos is None:
            startPos = self.node.getPos()
        
        
        def doIndirections(*items):
            result = []
            for item in items:
                if callable(item):
                    item = item()
                
                result.append(item)
            
            return result

        (startPos, endPos, startVel, endZ, gravityMult, wayPoint, timeToWayPoint) = doIndirections(startPos, endPos, startVel, endZ, gravityMult, wayPoint, timeToWayPoint)
        self.startPos = startPos
        self.zAcc = -(self.gravity)
        if gravityMult:
            self.zAcc *= gravityMult
        
        
        def calcStartVel(startPos, endPos, duration, zAccel):
            t = duration
            return Point3((endPos[0] - startPos[0]) / duration, (endPos[1] - startPos[1]) / duration, (endPos[2] - startPos[2] - 0.5 * zAccel * t * t) / t)

        
        def calcTimeOfImpactOnPlane(startHeight, endHeight, startVel, accel):
            return PythonUtil.solveQuadratic(accel * 0.5, startVel, startHeight - endHeight)

        
        def calcTimeOfLastImpactOnPlane(startHeight, endHeight, startVel, accel):
            time = calcTimeOfImpactOnPlane(startHeight, endHeight, startVel, accel)
            if not time:
                return None
            
            if type(time) == type([]):
                self.notify.debug('projectile hits plane twice at times: %s' % time)
                time = max(*time)
            else:
                self.notify.debug('projectile hits plane once at time: %s' % time)
            return time

        if None not in (endPos, duration):
            self.duration = duration
            self.endPos = endPos
            self.startVel = calcStartVel(self.startPos, self.endPos, self.duration, self.zAcc)
        elif None not in (startVel, duration):
            self.duration = duration
            self.startVel = startVel
            self.endPos = self._ProjectileInterval__calcPos(self.duration)
        elif None not in (startVel, endZ):
            self.startVel = startVel
            time = calcTimeOfLastImpactOnPlane(self.startPos[2], endZ, self.startVel[2], self.zAcc)
            if time is None:
                self.notify.error('projectile never reaches plane Z=%s' % endZ)
            
            self.duration = time
            self.endPos = self._ProjectileInterval__calcPos(self.duration)
        elif None not in (wayPoint, timeToWayPoint, endZ):
            self.startVel = calcStartVel(self.startPos, wayPoint, timeToWayPoint, self.zAcc)
            self.duration = calcTimeOfLastImpactOnPlane(self.startPos[2], endZ, self.startVel[2], self.zAcc)
            self.endPos = self._ProjectileInterval__calcPos(self.duration)
        else:
            self.notify.error('invalid set of inputs to ProjectileInterval')
        self.notify.debug('startPos: %s' % `self.startPos`)
        self.notify.debug('endPos:   %s' % `self.endPos`)
        self.notify.debug('duration: %s' % self.duration)
        self.notify.debug('startVel: %s' % `self.startVel`)
        self.notify.debug('z-accel:  %s' % self.zAcc)

    
    def _ProjectileInterval__initialize(self):
        if self.implicitStartPos:
            self._ProjectileInterval__calcTrajectory(*self.trajectoryArgs)
        

    
    def privInitialize(self, t):
        self._ProjectileInterval__initialize()
        Interval.privInitialize(self, t)

    
    def privInstant(self):
        self._ProjectileInterval__initialize()
        Interval.privInstant(self)

    
    def _ProjectileInterval__calcPos(self, t):
        return Point3(self.startPos[0] + self.startVel[0] * t, self.startPos[1] + self.startVel[1] * t, self.startPos[2] + self.startVel[2] * t + 0.5 * self.zAcc * t * t)

    
    def privStep(self, t):
        self.node.setFluidPos(self._ProjectileInterval__calcPos(t))
        Interval.privStep(self, t)


