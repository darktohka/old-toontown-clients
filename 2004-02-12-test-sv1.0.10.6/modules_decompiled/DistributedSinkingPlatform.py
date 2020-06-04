# File: D (Python 2.2)

from PandaModules import *
from ClockDelta import *
from IntervalGlobal import *
import FSM
import State
import BasicEntities
import MovingPlatform
import DistributedObject
import SinkingPlatformGlobals
import DirectNotifyGlobal

class DistributedSinkingPlatform(BasicEntities.DistributedNodePathEntity):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedSinkingPlatform')
    
    def __init__(self, cr):
        BasicEntities.DistributedNodePathEntity.__init__(self, cr)
        self.moveIval = None

    
    def generateInit(self):
        self.notify.debug('generateInit')
        BasicEntities.DistributedNodePathEntity.generateInit(self)
        self.fsm = FSM.FSM('DistributedSinkingPlatform', [
            State.State('off', self.enterOff, self.exitOff, [
                'sinking']),
            State.State('sinking', self.enterSinking, self.exitSinking, [
                'rising']),
            State.State('rising', self.enterRising, self.exitRising, [
                'sinking',
                'off'])], 'off', 'off')
        self.fsm.enterInitialState()

    
    def generate(self):
        self.notify.debug('generate')
        BasicEntities.DistributedNodePathEntity.generate(self)

    
    def announceGenerate(self):
        self.notify.debug('announceGenerate')
        BasicEntities.DistributedNodePathEntity.announceGenerate(self)
        self.loadModel()
        self.accept(self.platform.getEnterEvent(), self.localToonEntered)
        self.accept(self.platform.getExitEvent(), self.localToonLeft)

    
    def disable(self):
        self.notify.debug('disable')
        self.ignoreAll()
        self.fsm.requestFinalState()
        BasicEntities.DistributedNodePathEntity.disable(self)

    
    def delete(self):
        self.notify.debug('delete')
        self.ignoreAll()
        if self.moveIval:
            self.moveIval.pause()
            del self.moveIval
        
        self.platform.destroy()
        del self.platform
        BasicEntities.DistributedNodePathEntity.delete(self)

    
    def loadModel(self):
        self.notify.debug('loadModel')
        model = loader.loadModelCopy('phase_9/models/cogHQ/platform1')
        self.platform = MovingPlatform.MovingPlatform()
        self.platform.setupCopyModel(self.entId, model, 'platformcollision')
        self.platform.reparentTo(self)
        self.highPos = self.startPos
        self.lowPos = self.startPos - Vec3(0, 0, self.verticalRange)
        self.setPos(self.highPos)

    
    def localToonEntered(self):
        ts = globalClockDelta.localToNetworkTime(globalClock.getFrameTime(), bits = 32)
        self.sendUpdate('setOnOff', [
            1,
            ts])

    
    def localToonLeft(self):
        ts = globalClockDelta.localToNetworkTime(globalClock.getFrameTime(), bits = 32)
        self.sendUpdate('setOnOff', [
            0,
            ts])

    
    def enterOff(self):
        self.notify.debug('enterOff')

    
    def exitOff(self):
        self.notify.debug('exitOff')

    
    def enterSinking(self, ts = 0):
        self.notify.debug('enterSinking')
        self.startMoving(SinkingPlatformGlobals.SINKING, ts)

    
    def exitSinking(self):
        self.notify.debug('exitSinking')
        if self.moveIval:
            self.moveIval.pause()
            del self.moveIval
            self.moveIval = None
        

    
    def enterRising(self, ts = 0):
        self.notify.debug('enterRising')
        self.startMoving(SinkingPlatformGlobals.RISING, ts)

    
    def exitRising(self):
        self.notify.debug('exitRising')
        if self.moveIval:
            self.moveIval.pause()
            del self.moveIval
            self.moveIval = None
        

    
    def setSinkMode(self, avId, mode, ts):
        self.notify.debug('setSinkMode %s' % mode)
        if mode == SinkingPlatformGlobals.OFF:
            self.fsm.requestInitialState()
        elif mode == SinkingPlatformGlobals.RISING:
            self.fsm.request('rising', [
                ts])
        elif mode == SinkingPlatformGlobals.SINKING:
            self.fsm.request('sinking', [
                ts])
        

    
    def startMoving(self, direction, ts):
        if direction == SinkingPlatformGlobals.RISING:
            endPos = self.highPos
            duration = Vec3(self.getPos() - self.highPos).length() / self.riseRate
        else:
            endPos = self.lowPos
            duration = Vec3(self.getPos() - self.lowPos).length() / self.sinkRate
        if duration > 0.0:
            startT = globalClockDelta.networkToLocalTime(ts, bits = 32)
            curT = globalClock.getFrameTime()
            ivalTime = curT - startT
            if ivalTime < 0:
                ivalTime = 0
            elif ivalTime > duration:
                ivalTime = duration
            
            duration = duration - ivalTime
            print 'ivalTime = %s' % ivalTime
            self.moveIval = Sequence(LerpPosInterval(self, duration, endPos, startPos = self.getPos(), blendType = 'easeInOut', name = '%s-move' % self.platform.name, fluid = 1))
            self.moveIval.start()
        


