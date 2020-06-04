# File: E (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject

class EventQueue(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self):
        raise RuntimeError, 'No C++ constructor defined for class: ' + self.__class__.__name__

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inPekxoa_QX:
            libpandaexpress._inPekxoa_QX(self.this)
        

    
    def getGlobalEventQueue():
        returnValue = libpandaexpress._inPekxosJeO()
        returnObject = EventQueue(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    getGlobalEventQueue = staticmethod(getGlobalEventQueue)
    
    def queueEvent(self, event):
        returnValue = libpandaexpress._inPekxonDd1(self.this, event.this)
        return returnValue

    
    def isQueueEmpty(self):
        returnValue = libpandaexpress._inPekxoXt8W(self.this)
        return returnValue

    
    def isQueueFull(self):
        returnValue = libpandaexpress._inPekxoDyXu(self.this)
        return returnValue

    
    def dequeueEvent(self):
        returnValue = libpandaexpress._inPekxoBDK_(self.this)
        import Event
        returnObject = Event.Event(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()


