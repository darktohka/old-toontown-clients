# File: O (Python 2.2)

from toontown.toonbase.ToonBaseGlobal import *
from direct.interval.IntervalGlobal import *
from OrthoDrive import *

class OrthoWalk:
    notify = DirectNotifyGlobal.directNotify.newCategory('OrthoWalk')
    BROADCAST_POS_TASK = 'OrthoWalkBroadcastPos'
    
    def __init__(self, orthoDrive, collisions = 1, broadcast = 1, broadcastPeriod = 0.10000000000000001):
        self.orthoDrive = orthoDrive
        self.collisions = collisions
        self.broadcast = broadcast
        self.broadcastPeriod = broadcastPeriod
        self.priority = self.orthoDrive.priority + 1
        self.lt = base.localAvatar

    
    def destroy(self):
        self.orthoDrive.destroy()
        del self.orthoDrive

    
    def start(self):
        self.notify.debug('start')
        self.orthoDrive.start()
        if self.collisions:
            self._OrthoWalk__initCollisions()
        
        if self.broadcast:
            self._OrthoWalk__initBroadcast()
        

    
    def stop(self):
        self.notify.debug('stop')
        self._OrthoWalk__shutdownCollisions()
        self._OrthoWalk__shutdownBroadcast()
        self.orthoDrive.stop()

    
    def _OrthoWalk__initCollisions(self):
        self.notify.debug('initCollisions')
        lt = base.localAvatar
        lt.collisionsOn()
        self._OrthoWalk__collisionsOn = 1

    
    def _OrthoWalk__shutdownCollisions(self):
        if not hasattr(self, '_OrthoWalk__collisionsOn'):
            return None
        
        del self._OrthoWalk__collisionsOn
        self.notify.debug('shutdownCollisions')
        lt = base.localAvatar
        lt.collisionsOff()

    
    def _OrthoWalk__initBroadcast(self):
        self.notify.debug('initBroadcast')
        self._OrthoWalk__timeSinceLastPosBroadcast = 0.0
        self._OrthoWalk__lastPosBroadcast = self.lt.getPos()
        self._OrthoWalk__lastHprBroadcast = self.lt.getHpr()
        self._OrthoWalk__storeStop = 0
        lt = self.lt
        lt.d_clearSmoothing()
        lt.sendCurrentPosition()
        taskMgr.add(self._OrthoWalk__doBroadcast, self.BROADCAST_POS_TASK, priority = self.priority)

    
    def _OrthoWalk__shutdownBroadcast(self):
        self.notify.debug('shutdownBroadcast')
        taskMgr.remove(self.BROADCAST_POS_TASK)

    
    def _OrthoWalk__doBroadcast(self, task):
        dt = globalClock.getDt()
        self._OrthoWalk__timeSinceLastPosBroadcast += dt
        if self._OrthoWalk__timeSinceLastPosBroadcast >= self.broadcastPeriod:
            self._OrthoWalk__timeSinceLastPosBroadcast = 0
            self.lt.cnode.broadcastPosHprXyh()
        
        return Task.cont


