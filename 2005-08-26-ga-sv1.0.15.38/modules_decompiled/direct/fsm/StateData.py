# File: S (Python 2.2)

from direct.showbase.DirectObject import *
from direct.directnotify import DirectNotifyGlobal

class StateData(DirectObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('StateData')
    
    def __init__(self, doneEvent):
        self.doneEvent = doneEvent
        self.doneStatus = None
        self.isLoaded = 0
        self.isEntered = 0

    
    def enter(self):
        if self.isEntered:
            return 0
        
        if not (self.isLoaded):
            self.notify.warning('entered StateData before it was loaded')
            self.load()
        
        self.isEntered = 1
        StateData.notify.debug('enter()')
        return 1

    
    def exit(self):
        if not (self.isEntered):
            return 0
        
        self.isEntered = 0
        StateData.notify.debug('exit()')
        return 1

    
    def load(self):
        if self.isLoaded:
            return 0
        
        self.isLoaded = 1
        StateData.notify.debug('load()')
        return 1

    
    def unload(self):
        if not (self.isLoaded):
            return 0
        
        if self.isEntered:
            self.notify.warning('unloaded StateData before it was exited')
            self.exit()
        
        self.isLoaded = 0
        StateData.notify.debug('unload()')
        return 1

    
    def getDoneStatus(self):
        return self.doneStatus


