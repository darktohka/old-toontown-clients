# File: C (Python 2.2)

from pandac.PandaModules import *
from direct.directnotify import DirectNotifyGlobal
from direct.showbase import DirectObject
import math
NetworkTimeBits = 16
NetworkTimePrecision = 100.0
NetworkTimeMask = (1 << NetworkTimeBits) - 1
NetworkTimeTopBits = 32 - NetworkTimeBits
MaxTimeDelta = NetworkTimeMask / 2.0 / NetworkTimePrecision
ClockDriftPerHour = 1.0
ClockDriftPerSecond = ClockDriftPerHour / 3600.0
P2PResyncDelay = 10.0

class ClockDelta(DirectObject.DirectObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('ClockDelta')
    
    def __init__(self):
        self.globalClock = ClockObject.getGlobalClock()
        self.delta = 0
        self.uncertainty = None
        self.lastResync = 0.0
        self.accept('resetClock', self._ClockDelta__resetClock)

    
    def getDelta(self):
        return self.delta

    
    def getUncertainty(self):
        if self.uncertainty == None:
            return None
        
        now = self.globalClock.getRealTime()
        elapsed = now - self.lastResync
        return self.uncertainty + elapsed * ClockDriftPerSecond

    
    def getLastResync(self):
        return self.lastResync

    
    def _ClockDelta__resetClock(self, timeDelta):
        self.delta += timeDelta

    
    def clear(self):
        self.delta = 0
        self.uncertainty = None
        self.lastResync = 0.0

    
    def resynchronize(self, localTime, networkTime, newUncertainty, trustNew = 1):
        newDelta = float(localTime) - float(networkTime) / NetworkTimePrecision
        self.newDelta(localTime, newDelta, newUncertainty)

    
    def peerToPeerResync(self, avId, timestamp, serverTime, uncertainty):
        now = self.globalClock.getRealTime()
        if now - self.lastResync < P2PResyncDelay:
            return -1
        
        local = self.networkToLocalTime(timestamp, now)
        elapsed = now - local
        delta = (local + now) / 2.0 - serverTime
        gotSync = 0
        if elapsed <= 0 or elapsed > P2PResyncDelay:
            self.notify.info('Ignoring old request for resync from %s.' % avId)
        else:
            self.notify.info('Got sync +/- %.3f s, elapsed %.3f s, from %s.' % (uncertainty, elapsed, avId))
            delta -= elapsed / 2.0
            uncertainty += elapsed / 2.0
            gotSync = self.newDelta(local, delta, uncertainty, trustNew = 0)
        return gotSync

    
    def newDelta(self, localTime, newDelta, newUncertainty, trustNew = 1):
        oldUncertainty = self.getUncertainty()
        if oldUncertainty != None:
            oldLow = self.delta - oldUncertainty
            oldHigh = self.delta + oldUncertainty
            newLow = newDelta - newUncertainty
            newHigh = newDelta + newUncertainty
            low = max(oldLow, newLow)
            high = min(oldHigh, newHigh)
            if low > high:
                if not trustNew:
                    self.notify.info('discarding new delta.')
                    return 0
                
                self.notify.info('discarding previous delta.')
            else:
                newDelta = (low + high) / 2.0
                newUncertainty = (high - low) / 2.0
        
        self.delta = newDelta
        self.uncertainty = newUncertainty
        self.lastResync = localTime
        return 1

    
    def networkToLocalTime(self, networkTime, now = None, bits = 16, ticksPerSec = NetworkTimePrecision):
        if now == None:
            now = self.globalClock.getRealTime()
        
        if self.globalClock.getMode() == ClockObject.MNonRealTime:
            return now
        
        ntime = int(math.floor((now - self.delta) * ticksPerSec + 0.5))
        if bits == 16:
            diff = self._ClockDelta__signExtend(networkTime - ntime)
        else:
            diff = networkTime - ntime
        return now + float(diff) / ticksPerSec

    
    def localToNetworkTime(self, localTime, bits = 16, ticksPerSec = NetworkTimePrecision):
        ntime = int(math.floor((localTime - self.delta) * ticksPerSec + 0.5))
        if bits == 16:
            return self._ClockDelta__signExtend(ntime)
        else:
            return ntime

    
    def getRealNetworkTime(self, bits = 16, ticksPerSec = NetworkTimePrecision):
        return self.localToNetworkTime(self.globalClock.getRealTime(), bits = bits, ticksPerSec = ticksPerSec)

    
    def getFrameNetworkTime(self, bits = 16, ticksPerSec = NetworkTimePrecision):
        return self.localToNetworkTime(self.globalClock.getFrameTime(), bits = bits, ticksPerSec = ticksPerSec)

    
    def localElapsedTime(self, networkTime, bits = 16, ticksPerSec = NetworkTimePrecision):
        now = self.globalClock.getFrameTime()
        dt = now - self.networkToLocalTime(networkTime, now, bits = bits, ticksPerSec = ticksPerSec)
        return max(dt, 0.0)

    
    def _ClockDelta__signExtend(self, networkTime):
        return (networkTime & NetworkTimeMask) << NetworkTimeTopBits >> NetworkTimeTopBits


globalClockDelta = ClockDelta()
