# File: D (Python 2.2)

from MessengerGlobal import *
from direct.directnotify.DirectNotifyGlobal import *
from PythonUtil import *

class DirectObject:
    
    def __init__(self):
        pass

    
    def _DirectObject__initEvents(self):
        if not hasattr(self, 'events'):
            self.events = { }
        

    
    def accept(self, event, method, extraArgs = []):
        self._DirectObject__initEvents()
        self.events.setdefault(event, None)
        messenger.accept(event, self, method, extraArgs, 1)

    
    def acceptOnce(self, event, method, extraArgs = []):
        self._DirectObject__initEvents()
        self.events.setdefault(event, None)
        messenger.accept(event, self, method, extraArgs, 0)

    
    def _INTERNAL_acceptOnceExpired(self, event):
        if self.events.has_key(event):
            del self.events[event]
        

    
    def ignore(self, event):
        self._DirectObject__initEvents()
        if self.events.has_key(event):
            del self.events[event]
        
        messenger.ignore(event, self)

    
    def ignoreAll(self):
        self._DirectObject__initEvents()
        for event in self.events.keys():
            messenger.ignore(event, self)
        
        self.events.clear()

    
    def isAccepting(self, event):
        self._DirectObject__initEvents()
        return self.events.has_key(event)

    
    def isIgnoring(self, event):
        return not self.isAccepting(event)


