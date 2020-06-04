# File: E (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import FFIExternalObject

class EventQueue(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self):
        self.this = libpanda._inPekxoIzfw()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPekxoa_QX:
            libpanda._inPekxoa_QX(self.this)
        

    
    def getGlobalEventQueue():
        returnValue = libpanda._inPekxosJeO()
        returnObject = EventQueue(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    getGlobalEventQueue = staticmethod(getGlobalEventQueue)
    
    def queueEvent(self, event):
        returnValue = libpanda._inPekxonDd1(self.this, event.this)
        return returnValue

    
    def clear(self):
        returnValue = libpanda._inPekxoRhuh(self.this)
        return returnValue

    
    def isQueueEmpty(self):
        returnValue = libpanda._inPekxoXt8W(self.this)
        return returnValue

    
    def isQueueFull(self):
        returnValue = libpanda._inPekxoDyXu(self.this)
        return returnValue

    
    def dequeueEvent(self):
        returnValue = libpanda._inPekxoBDK_(self.this)
        import Event
        returnObject = Event.Event(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()


