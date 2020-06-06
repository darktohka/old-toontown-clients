# File: B (Python 2.2)

from direct.directnotify import DirectNotifyGlobal
from direct.showbase.PythonUtil import Functor
from direct.showbase import DirectObject

class BulletinBoardWatcher(DirectObject.DirectObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('BulletinBoardWatcher')
    
    def __init__(self, name, postNames, callback):
        self.notify.debug('__init__: %s, %s, %s' % (name, postNames, callback))
        self.name = name
        if type(postNames) == type(''):
            postNames = [
                postNames]
        
        self.postNames = postNames
        self.callback = callback
        self.waitingOn = { }
        for name in postNames:
            if not bboard.has(name):
                eventName = bboard.getEventName(name)
                self.acceptOnce(eventName, Functor(self.handlePost, eventName))
                self.waitingOn[eventName] = None
            
        
        self.checkDone()

    
    def destroy(self):
        self.ignoreAll()
        del self.callback
        del self.waitingOn

    
    def isDone(self):
        return len(self.waitingOn) == 0

    
    def checkDone(self):
        if self.isDone():
            self.notify.debug('%s: done' % self.name)
            self.callback()
        

    
    def handlePost(self, eventName):
        self.notify.debug('%s: handlePost(%s)' % (self.name, eventName))
        del self.waitingOn[eventName]
        self.checkDone()


