# File: E (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject

class EventQueue(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self):
        self.this = libpanda._inPfkxoJzfw()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPfkxoa_QX:
            libpanda._inPfkxoa_QX(self.this)
        

    
    def getGlobalEventQueue():
        returnValue = libpanda._inPfkxosJeO()
        returnObject = EventQueue(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    getGlobalEventQueue = staticmethod(getGlobalEventQueue)
    
    def queueEvent(self, event):
        returnValue = libpanda._inPfkxomDd1(self.this, event.this)
        return returnValue

    
    def clear(self):
        returnValue = libpanda._inPfkxoWhuh(self.this)
        return returnValue

    
    def isQueueEmpty(self):
        returnValue = libpanda._inPfkxoXt8W(self.this)
        return returnValue

    
    def isQueueFull(self):
        returnValue = libpanda._inPfkxoAyXu(self.this)
        return returnValue

    
    def dequeueEvent(self):
        returnValue = libpanda._inPfkxoCDK_(self.this)
        import Event
        returnObject = Event.Event(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()


