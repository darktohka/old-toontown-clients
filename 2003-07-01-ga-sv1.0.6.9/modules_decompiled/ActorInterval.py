# File: A (Python 2.2)

from PandaModules import *
from DirectNotifyGlobal import *
import Interval
import math
import LerpBlendHelpers

class ActorInterval(Interval.Interval):
    notify = directNotify.newCategory('ActorInterval')
    animNum = 1
    
    def __init__(self, actor, animName, loop = 0, duration = 0.0, startTime = 0.0, endTime = None, playRate = 1.0, name = None):
        id = 'Actor-%d' % ActorInterval.animNum
        ActorInterval.animNum += 1
        self.actor = actor
        self.animName = animName
        self.controls = self.actor.getAnimControls(self.animName)
        self.loopAnim = loop
        self.frameRate = self.controls[0].getAnim().getBaseFrameRate() * playRate
        self.numFrames = self.controls[0].getNumFrames()
        self.startTime = startTime
        if name == None:
            name = id
        
        self.reverse = 0
        if duration == 0.0:
            if endTime == None:
                duration = max(self.actor.getDuration(self.animName) - startTime, 0.0)
            else:
                duration = endTime - startTime
                if duration < 0.0:
                    duration = -duration
                
        
        if endTime == None:
            self.finishTime = self.startTime + duration
        else:
            self.finishTime = endTime
        if self.startTime > self.finishTime:
            self.reverse = 1
        
        Interval.Interval.__init__(self, name, duration)

    
    def calcFrame(self, t):
        segmentLength = abs(self.finishTime - self.startTime)
        if segmentLength == 0:
            offset = 0
        else:
            offset = t % segmentLength
        if t == self.getDuration() and offset < 0.0001:
            offset = segmentLength
        
        if self.reverse == 0:
            floatFrame = self.frameRate * (self.startTime + offset)
        else:
            negOffset = self.startTime - self.finishTime - offset
            floatFrame = self.frameRate * (self.finishTime + negOffset)
        frame = max(0, int(math.ceil(floatFrame)) - 1)
        return frame % self.numFrames

    
    def goToT(self, t):
        frame = self.calcFrame(t)
        for control in self.controls:
            control.pose(frame)
        
        return frame

    
    def privInitialize(self, t):
        self.state = CInterval.SStarted
        self.goToT(t)
        if self.loopAnim:
            self.actor.loop(self.animName, restart = 0)
        
        self.currT = t

    
    def privFinalize(self):
        if self.loopAnim:
            self.actor.stop()
        else:
            self.goToT(self.getDuration())
        self.currT = self.getDuration()
        self.state = CInterval.SFinal

    
    def privStep(self, t):
        if not (self.loopAnim):
            self.goToT(t)
        
        self.state = CInterval.SStarted
        self.currT = t

    
    def privInterrupt(self):
        if self.loopAnim:
            pass
        1



class LerpAnimInterval(CLerpAnimEffectInterval):
    lerpAnimNum = 1
    
    def __init__(self, actor, duration, startAnim, endAnim, startWeight = 0.0, endWeight = 1.0, blendType = 'noBlend', name = None):
        if name == None:
            name = 'LerpAnimInterval-%d' % LerpAnimInterval.lerpAnimNum
            LerpAnimInterval.lerpAnimNum += 1
        
        blendType = self.stringBlendType(blendType)
        CLerpAnimEffectInterval.__init__(self, name, duration, blendType)
        if startAnim != None:
            controls = actor.getAnimControls(startAnim)
            for control in controls:
                self.addControl(control, startAnim, 1.0 - startWeight, 1.0 - endWeight)
            
        
        if endAnim != None:
            controls = actor.getAnimControls(endAnim)
            for control in controls:
                self.addControl(control, endAnim, startWeight, endWeight)
            
        


