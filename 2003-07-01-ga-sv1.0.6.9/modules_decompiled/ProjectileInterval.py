# File: P (Python 2.2)

from DirectObject import *
from PandaModules import *
from Interval import Interval
from PythonUtil import lerp
import PythonUtil

class ProjectileInterval(Interval):
    notify = directNotify.newCategory('ProjectileInterval')
    projectileIntervalNum = 1
    gravity = 32.0
    
    def __init__(self, node, startPos = None, endPos = None, duration = None, startVel = None, endZ = None, gravityMult = None, name = None):
        self.node = node
        if name == None:
            name = '%s-%s' % (self.__class__.__name__, self.projectileIntervalNum)
            ProjectileInterval.projectileIntervalNum += 1
        
        args = (startPos, endPos, duration, startVel, endZ, gravityMult)
        self.needToCalcTraj = 0
        if startPos is None:
            self.trajectoryArgs = args
            self.needToCalcTraj = 1
        else:
            self._ProjectileInterval__calcTrajectory(*args)
        Interval.__init__(self, name, duration)

    
    def _ProjectileInterval__calcTrajectory(self, startPos = None, endPos = None, duration = None, startVel = None, endZ = None, gravityMult = None):
        self.needToCalcTraj = 0
        if not startPos:
            startPos = self.node.getPos()
        
        
        def doIndirections(*items):
            result = []
            for item in items:
                if callable(item):
                    item = item()
                
                result.append(item)
            
            return result

        (startPos, endPos, startVel, endZ, gravityMult) = doIndirections(startPos, endPos, startVel, endZ, gravityMult)
        self.startPos = startPos
        self.zAcc = -(self.gravity)
        if gravityMult:
            self.zAcc *= gravityMult
        
        
        def calcStartVel(startPos, endPos, duration, zAccel):
            t = duration
            return Point3((endPos[0] - startPos[0]) / duration, (endPos[1] - startPos[1]) / duration, (endPos[2] - startPos[2] - 0.5 * zAccel * t * t) / t)

        
        def calcTimeOfImpactOnPlane(startHeight, endHeight, startVel, accel):
            return PythonUtil.solveQuadratic(accel * 0.5, startVel, startHeight - endHeight)

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
            time = calcTimeOfImpactOnPlane(self.startPos[2], endZ, self.startVel[2], self.zAcc)
            if not time:
                self.notify.error('projectile never reaches plane Z=%s' % endZ)
            
            if type(time) == type([]):
                self.notify.debug('projectile hits plane twice at times: %s' % time)
                time = max(*time)
            else:
                self.notify.debug('projectile hits plane once at time: %s' % time)
            self.duration = time
            self.endPos = self._ProjectileInterval__calcPos(self.duration)
        else:
            self.notify.error('invalid set of inputs')
        self.notify.debug('startPos: %s' % `self.startPos`)
        self.notify.debug('endPos:   %s' % `self.endPos`)
        self.notify.debug('duration: %s' % self.duration)
        self.notify.debug('startVel: %s' % `self.startVel`)
        self.notify.debug('z-accel:  %s' % self.zAcc)

    
    def _ProjectileInterval__initialize(self):
        if self.needToCalcTraj:
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
        self.node.setPos(self._ProjectileInterval__calcPos(t))
        Interval.privStep(self, t)


