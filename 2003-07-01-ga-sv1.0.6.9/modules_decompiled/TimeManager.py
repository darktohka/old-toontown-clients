# File: T (Python 2.2)

from ShowBaseGlobal import *
from PandaObject import *
from ClockDelta import *
import DistributedObject
import DirectNotifyGlobal
import ToontownGlobals
import PythonUtil

class TimeManager(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('TimeManager')
    neverDisable = 1
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.updateFreq = base.config.GetFloat('time-manager-freq', 1800)
        self.minWait = base.config.GetFloat('time-manager-min-wait', 10)
        self.maxLatency = base.config.GetFloat('time-manager-max-latency', 2)
        self.maxAttempts = base.config.GetInt('time-manager-max-attempts', 5)
        self.extraSkew = base.config.GetInt('time-manager-extra-skew', 0)
        if self.extraSkew != 0:
            self.notify.info('Simulating clock skew of %0.3f s' % self.extraSkew)
        
        self.talkResult = 0
        self.thisContext = -1
        self.nextContext = 0
        self.attemptCount = 0
        self.start = 0
        self.lastAttempt = -(self.minWait)
        self.gotSync = 0
        return None

    
    def generate(self):
        if toonbase.tcr.timeManager != None:
            toonbase.tcr.timeManager.delete()
        
        toonbase.tcr.timeManager = self
        DistributedObject.DistributedObject.generate(self)
        self.accept(ToontownGlobals.SynchronizeHotkey, self.handleHotkey)
        if self.updateFreq > 0:
            self.startTask()
        

    
    def disable(self):
        self.ignore(ToontownGlobals.SynchronizeHotkey)
        self.stopTask()
        self.gotSync = 0
        toonbase.tcr.timeManager = None
        DistributedObject.DistributedObject.disable(self)

    
    def delete(self):
        self.ignore(ToontownGlobals.SynchronizeHotkey)
        self.stopTask()
        self.gotSync = 0
        toonbase.tcr.timeManager = None
        DistributedObject.DistributedObject.delete(self)

    
    def startTask(self):
        self.stopTask()
        taskMgr.doMethodLater(self.updateFreq, self.doUpdate, 'timeMgrTask')

    
    def stopTask(self):
        taskMgr.remove('timeMgrTask')

    
    def doUpdate(self, task):
        self.synchronize('timer')
        taskMgr.doMethodLater(self.updateFreq, self.doUpdate, 'timeMgrTask')
        return Task.done

    
    def handleHotkey(self):
        self.lastAttempt = -(self.minWait)
        if self.synchronize('user hotkey'):
            self.talkResult = 1
        else:
            toonbase.localToon.setChatAbsolute('Too soon.', CFSpeech | CFTimeout)
        return None

    
    def synchronize(self, description):
        now = globalClock.getRealTime()
        if now - self.lastAttempt < self.minWait:
            self.notify.debug('Not resyncing (too soon): %s' % description)
            return 0
        
        self.talkResult = 0
        self.thisContext = self.nextContext
        self.attemptCount = 0
        self.nextContext = self.nextContext + 1 & 255
        self.notify.info('Clock sync: %s' % description)
        self.start = now
        self.lastAttempt = now
        self.sendUpdate('requestServerTime', [
            self.thisContext])
        return 1

    
    def serverTime(self, context, timestamp, timeOfDay):
        end = globalClock.getRealTime()
        now = int(time.time())
        aiTimeDelta = timeOfDay - now
        aiTimeSkew = aiTimeDelta - self.cr.getServerDelta()
        if context != self.thisContext:
            self.notify.info('Ignoring TimeManager response for old context %d' % context)
            return None
        
        elapsed = end - self.start
        self.attemptCount += 1
        self.notify.info('Clock sync roundtrip took %0.3f ms' % elapsed * 1000.0)
        self.notify.info('AI time delta is %s from server delta' % PythonUtil.formatElapsedSeconds(aiTimeSkew))
        if elapsed > self.maxLatency:
            if self.attemptCount < self.maxAttempts:
                self.notify.info('Latency is too high, trying again.')
                self.start = globalClock.getRealTime()
                self.sendUpdate('requestServerTime', [
                    self.thisContext])
                return None
            
            self.notify.info('Giving up on latency requirement.')
        
        average = (self.start + end) / 2.0 - self.extraSkew
        change = globalClockDelta.resynchronize(average, timestamp)
        self.notify.info('Clock delta changed by %.3f s' % change)
        if self.talkResult:
            toonbase.localToon.setChatAbsolute('latency %0.0f ms, clock adjusted %.1f s' % (elapsed * 1000.0, change), CFSpeech | CFTimeout)
        
        self.gotSync = 1
        messenger.send('gotTimeSync')

    
    def setDisconnectReason(self, disconnectCode):
        self.notify.info('Client disconnect reason %s.' % disconnectCode)
        self.sendUpdate('setDisconnectReason', [
            disconnectCode])


