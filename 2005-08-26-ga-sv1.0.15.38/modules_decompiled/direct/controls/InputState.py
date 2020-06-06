# File: I (Python 2.2)

from direct.directnotify import DirectNotifyGlobal
from direct.showbase import DirectObject

class InputState(DirectObject.DirectObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('InputState')
    
    def __init__(self):
        self.state = { }
        self.watching = { }
        self.forcing = { }

    
    def delete(self):
        self.ignoreAll()

    
    def watch(self, name, eventOn, eventOff, default = 0):
        self.accept(eventOn, self.set, [
            name,
            1])
        self.accept(eventOff, self.set, [
            name,
            0])
        self.state[name] = default
        self.watching[name] = (eventOn, eventOff)

    
    def force(self, name, value):
        self.forcing[name] = value

    
    def unforce(self, name):
        del self.forcing[name]

    
    def ignore(self, name):
        (eventOn, eventOff) = self.watching[name]
        DirectObject.DirectObject.ignore(self, eventOn)
        DirectObject.DirectObject.ignore(self, eventOff)
        del self.watching[name]
        del self.state[name]

    
    def set(self, name, isSet):
        self.state[name] = isSet
        messenger.send('InputState-%s' % (name,), [
            isSet])

    
    def isSet(self, name):
        r = self.forcing.get(name)
        if r is not None:
            return r
        
        return self.state.get(name)

    
    def debugPrint(self, message):
        return self.notify.debug('%s (%s) %s' % (id(self), len(self.state), message))


