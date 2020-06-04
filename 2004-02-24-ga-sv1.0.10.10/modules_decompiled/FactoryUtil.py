# File: F (Python 2.2)

from ShowBaseGlobal import *
from IntervalGlobal import *
import ToontownGlobals
import MovingPlatform
import Suit
import AvatarDNA

class Ouch(DirectObject):
    
    def __init__(self, keyEvent, callback):
        self.accept(keyEvent, callback)

    
    def destroy(self):
        self.ignoreAll()



class CyclePlacer(DirectObject):
    
    def __init__(self, locations, keyEvent, startIndex = 0):
        self.locations = locations
        self.index = startIndex
        self.accept(keyEvent, self.gotoNextLocation)

    
    def destroy(self):
        self.locations = None
        self.ignoreAll()

    
    def gotoNextLocation(self):
        self.index = (self.index + 1) % len(self.locations)
        self.gotoLocation()

    
    def gotoLocation(self, index = None):
        if index is None:
            index = self.index
        
        (pos, h) = self.locations[index]
        toonbase.localToon.reparentTo(render)
        toonbase.localToon.setPos(*pos)
        toonbase.localToon.setH(h)



class ToonLifter(DirectObject):
    SerialNum = 0
    
    def __init__(self, keyDownEvent, speed = 2):
        self.serialNum = ToonLifter.SerialNum
        ToonLifter.SerialNum += 1
        self.taskName = 'ToonLifter%s' % self.serialNum
        self.keyDownEvent = keyDownEvent
        self.keyUpEvent = self.keyDownEvent + '-up'
        self.speed = speed
        self.accept(self.keyDownEvent, self.startLifting)

    
    def destroy(self):
        self.ignoreAll()
        taskMgr.remove(self.taskName)

    
    def startLifting(self):
        
        def liftTask(task, self = self):
            toonbase.localToon.setZ(toonbase.localToon.getZ() + self.speed)
            return Task.cont

        
        def stopLifting(self = self):
            taskMgr.remove(self.taskName)
            self.ignore(self.keyUpEvent)
            self.accept(self.keyDownEvent, self.startLifting)

        self.ignore(self.keyDownEvent)
        self.accept(self.keyUpEvent, stopLifting)
        taskMgr.add(liftTask, self.taskName)


