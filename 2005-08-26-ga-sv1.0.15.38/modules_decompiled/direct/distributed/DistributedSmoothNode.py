# File: D (Python 2.2)

from pandac.PandaModules import *
from ClockDelta import *
import DistributedNode
import DistributedSmoothNodeBase
from direct.task import Task
MaxFuture = base.config.GetFloat('smooth-max-future', 0.20000000000000001)
MinSuggestResync = base.config.GetFloat('smooth-min-suggest-resync', 15)
EnableSmoothing = base.config.GetBool('smooth-enable-smoothing', 1)
EnablePrediction = base.config.GetBool('smooth-enable-prediction', 1)
Lag = base.config.GetDouble('smooth-lag', 0.20000000000000001)
PredictionLag = base.config.GetDouble('smooth-prediction-lag', 0.0)

def activateSmoothing(smoothing, prediction):
    if smoothing and EnableSmoothing:
        if prediction and EnablePrediction:
            SmoothMover.setSmoothMode(SmoothMover.SMOn)
            SmoothMover.setPredictionMode(SmoothMover.PMOn)
            SmoothMover.setDelay(PredictionLag)
        else:
            SmoothMover.setSmoothMode(SmoothMover.SMOn)
            SmoothMover.setPredictionMode(SmoothMover.PMOff)
            SmoothMover.setDelay(Lag)
    else:
        SmoothMover.setSmoothMode(SmoothMover.SMOff)
        SmoothMover.setPredictionMode(SmoothMover.PMOff)
        SmoothMover.setDelay(0.0)


class DistributedSmoothNode(DistributedNode.DistributedNode, DistributedSmoothNodeBase.DistributedSmoothNodeBase):
    
    def __init__(self, cr):
        
        try:
            pass
        except:
            self.DistributedSmoothNode_initialized = 1
            DistributedNode.DistributedNode.__init__(self, cr)
            DistributedSmoothNodeBase.DistributedSmoothNodeBase.__init__(self)
            self.cnode.setRepository(cr, 0, 0)
            self.smoother = SmoothMover()
            self.smoothStarted = 0
            self.lastSuggestResync = 0


    
    def delete(self):
        DistributedSmoothNodeBase.DistributedSmoothNodeBase.delete(self)
        DistributedNode.DistributedNode.delete(self)

    
    def smoothPosition(self):
        self.smoother.computeAndApplySmoothMat(self)

    
    def doSmoothTask(self, task):
        self.smoothPosition()
        return Task.cont

    
    def wantsSmoothing(self):
        return 1

    
    def startSmooth(self):
        if not self.wantsSmoothing() and self.isDisabled() or self.isLocal():
            return None
        
        if not (self.smoothStarted):
            taskName = self.taskName('smooth')
            taskMgr.remove(taskName)
            self.reloadPosition()
            taskMgr.add(self.doSmoothTask, taskName)
            self.smoothStarted = 1
        

    
    def stopSmooth(self):
        if self.smoothStarted:
            taskName = self.taskName('smooth')
            taskMgr.remove(taskName)
            self.forceToTruePosition()
            self.smoothStarted = 0
        

    
    def forceToTruePosition(self):
        if not self.isLocal() and self.smoother.getLatestPosition():
            self.smoother.applySmoothMat(self)
        
        self.smoother.clearPositions(1)

    
    def reloadPosition(self):
        self.smoother.clearPositions(0)
        self.smoother.setMat(self.getMat())
        self.smoother.setPhonyTimestamp()
        self.smoother.markPosition()

    
    def setSmStop(self, timestamp):
        self.setComponentTLive(timestamp)

    
    def setSmH(self, h, timestamp):
        self.setComponentH(h)
        self.setComponentTLive(timestamp)

    
    def setSmZ(self, z, timestamp):
        self.setComponentZ(z)
        self.setComponentTLive(timestamp)

    
    def setSmXY(self, x, y, timestamp):
        self.setComponentX(x)
        self.setComponentY(y)
        self.setComponentTLive(timestamp)

    
    def setSmXZ(self, x, z, timestamp):
        self.setComponentX(x)
        self.setComponentZ(z)
        self.setComponentTLive(timestamp)

    
    def setSmPos(self, x, y, z, timestamp):
        self.setComponentX(x)
        self.setComponentY(y)
        self.setComponentZ(z)
        self.setComponentTLive(timestamp)

    
    def setSmHpr(self, h, p, r, timestamp):
        self.setComponentH(h)
        self.setComponentP(p)
        self.setComponentR(r)
        self.setComponentTLive(timestamp)

    
    def setSmXYH(self, x, y, h, timestamp):
        self.setComponentX(x)
        self.setComponentY(y)
        self.setComponentH(h)
        self.setComponentTLive(timestamp)

    
    def setSmXYZH(self, x, y, z, h, timestamp):
        self.setComponentX(x)
        self.setComponentY(y)
        self.setComponentZ(z)
        self.setComponentH(h)
        self.setComponentTLive(timestamp)

    
    def setSmPosHpr(self, x, y, z, h, p, r, timestamp):
        self.setComponentX(x)
        self.setComponentY(y)
        self.setComponentZ(z)
        self.setComponentH(h)
        self.setComponentP(p)
        self.setComponentR(r)
        self.setComponentTLive(timestamp)
        return None

    
    def setComponentX(self, x):
        self.smoother.setX(x)

    
    def setComponentY(self, y):
        self.smoother.setY(y)

    
    def setComponentZ(self, z):
        self.smoother.setZ(z)

    
    def setComponentH(self, h):
        self.smoother.setH(h)

    
    def setComponentP(self, p):
        self.smoother.setP(p)

    
    def setComponentR(self, r):
        self.smoother.setR(r)

    
    def setComponentT(self, timestamp):
        self.smoother.setPhonyTimestamp()
        self.smoother.clearPositions(1)
        self.smoother.markPosition()
        self.forceToTruePosition()

    
    def setComponentTLive(self, timestamp):
        now = globalClock.getFrameTime()
        local = globalClockDelta.networkToLocalTime(timestamp, now)
        realTime = globalClock.getRealTime()
        chug = realTime - now
        howFarFuture = local - now
        if howFarFuture - chug >= MaxFuture:
            if globalClockDelta.getUncertainty() != None and realTime - self.lastSuggestResync >= MinSuggestResync:
                self.lastSuggestResync = realTime
                timestampB = globalClockDelta.localToNetworkTime(realTime)
                serverTime = realTime - globalClockDelta.getDelta()
                self.notify.info('Suggesting resync for %s, with discrepency %s; local time is %s and server time is %s.' % (self.doId, howFarFuture - chug, realTime, serverTime))
                self.d_suggestResync(self.cr.localAvatarDoId, timestamp, timestampB, serverTime, globalClockDelta.getUncertainty())
            
        
        self.smoother.setTimestamp(local)
        self.smoother.markPosition()

    
    def clearSmoothing(self, bogus = None):
        self.smoother.clearPositions(1)

    
    def wrtReparentTo(self, parent):
        if self.smoothStarted:
            self.forceToTruePosition()
            NodePath.wrtReparentTo(self, parent)
            self.reloadPosition()
        else:
            NodePath.wrtReparentTo(self, parent)

    
    def d_setParent(self, parentToken):
        DistributedNode.DistributedNode.d_setParent(self, parentToken)
        self.forceToTruePosition()
        self.sendCurrentPosition()

    
    def sendCurrentPosition(self):
        self.cnode.initialize(self, self.dclass, self.doId)
        self.cnode.sendEverything()

    
    def d_suggestResync(self, avId, timestampA, timestampB, serverTime, uncertainty):
        serverTimeSec = math.floor(serverTime)
        serverTimeUSec = (serverTime - serverTimeSec) * 10000.0
        self.sendUpdate('suggestResync', [
            avId,
            timestampA,
            timestampB,
            serverTimeSec,
            serverTimeUSec,
            uncertainty])

    
    def suggestResync(self, avId, timestampA, timestampB, serverTimeSec, serverTimeUSec, uncertainty):
        serverTime = float(serverTimeSec) + float(serverTimeUSec) / 10000.0
        result = self.peerToPeerResync(avId, timestampA, serverTime, uncertainty)
        if result >= 0 and globalClockDelta.getUncertainty() != None:
            other = self.cr.doId2do.get(avId)
            if not other:
                self.notify.info("Warning: couldn't find the avatar %d" % avId)
            elif hasattr(other, 'd_returnResync'):
                realTime = globalClock.getRealTime()
                serverTime = realTime - globalClockDelta.getDelta()
                self.notify.info('Returning resync for %s; local time is %s and server time is %s.' % (self.doId, realTime, serverTime))
                other.d_returnResync(self.cr.localAvatarDoId, timestampB, serverTime, globalClockDelta.getUncertainty())
            
        

    
    def d_returnResync(self, avId, timestampB, serverTime, uncertainty):
        serverTimeSec = math.floor(serverTime)
        serverTimeUSec = (serverTime - serverTimeSec) * 10000.0
        self.sendUpdate('returnResync', [
            avId,
            timestampB,
            serverTimeSec,
            serverTimeUSec,
            uncertainty])

    
    def returnResync(self, avId, timestampB, serverTimeSec, serverTimeUSec, uncertainty):
        serverTime = float(serverTimeSec) + float(serverTimeUSec) / 10000.0
        self.peerToPeerResync(avId, timestampB, serverTime, uncertainty)

    
    def peerToPeerResync(self, avId, timestamp, serverTime, uncertainty):
        gotSync = globalClockDelta.peerToPeerResync(avId, timestamp, serverTime, uncertainty)
        if not gotSync:
            if self.cr.timeManager != None:
                self.cr.timeManager.synchronize('suggested by %d' % avId)
            
        
        return gotSync


