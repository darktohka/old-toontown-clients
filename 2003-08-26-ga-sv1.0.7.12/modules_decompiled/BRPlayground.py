# File: B (Python 2.2)

from ShowBaseGlobal import *
import Playground
import whrandom
import Place
import ToontownGlobals

class BRPlayground(Playground.Playground):
    STILL = 1
    RUN = 2
    ROTATE = 3
    stillPos = Point3(0, 20, 8)
    runPos = Point3(0, 60, 8)
    rotatePos = Point3(0, 0, 8)
    timeFromStill = 1.0
    timeFromRotate = 2.0
    
    def __init__(self, loader, parentFSM, doneEvent):
        Playground.Playground.__init__(self, loader, parentFSM, doneEvent)

    
    def load(self):
        Playground.Playground.load(self)

    
    def unload(self):
        Playground.Playground.unload(self)

    
    def enter(self, requestStatus):
        Playground.Playground.enter(self, requestStatus)
        self.nextWindTime = 0
        taskMgr.add(self._BRPlayground__windTask, 'br-wind')
        self.state = 0
        taskMgr.add(self._BRPlayground__snowTask, 'br-snow')

    
    def exit(self):
        taskMgr.remove('br-wind')
        taskMgr.remove('br-snow')
        taskMgr.remove('lerp-snow')
        Playground.Playground.exit(self)

    
    def enterTunnelOut(self, requestStatus):
        Place.Place.enterTunnelOut(self, requestStatus)

    
    def _BRPlayground__windTask(self, task):
        now = globalClock.getFrameTime()
        if now < self.nextWindTime:
            return Task.cont
        
        randNum = whrandom.random()
        wind = int(randNum * 100) % 3 + 1
        if wind == 1:
            base.playSfx(self.loader.wind1Sound)
        elif wind == 2:
            base.playSfx(self.loader.wind2Sound)
        elif wind == 3:
            base.playSfx(self.loader.wind3Sound)
        
        self.nextWindTime = now + randNum * 8.0
        return Task.cont

    
    def _BRPlayground__snowTask(self, task):
        speed = base.mouseInterfaceNode.getSpeed()
        rotSpeed = base.mouseInterfaceNode.getRotSpeed()
        if speed > 0.0:
            if self.state != self.RUN:
                if self.state == self.STILL:
                    time = self.timeFromStill
                else:
                    time = self.timeFromRotate
                self.state = self.RUN
                taskMgr.remove('lerp-snow')
                self.loader.snow.lerpPos(self.runPos, time, task = 'lerp-snow')
            
        elif rotSpeed != 0.0:
            if self.state != self.ROTATE:
                if self.state == self.RUN:
                    taskMgr.remove('lerp-snow')
                
                self.state = self.ROTATE
                self.loader.snow.setPos(self.rotatePos)
            
        elif self.state != self.STILL:
            if self.state == self.RUN:
                taskMgr.remove('lerp-snow')
            
            self.state = self.STILL
            self.loader.snow.setPos(self.stillPos)
        
        return Task.cont


