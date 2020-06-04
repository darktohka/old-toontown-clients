# File: E (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import TypedObject

class EventHandler(TypedObject.TypedObject, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self, queue):
        self.this = libpanda._inPekxowhlR(queue.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPekxoIKI8:
            libpanda._inPekxoIKI8(self.this)
        

    
    def getGlobalEventHandler(queue):
        returnValue = libpanda._inPekxocYKa(queue.this)
        returnObject = EventHandler(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject.setPointer()

    getGlobalEventHandler = staticmethod(getGlobalEventHandler)
    
    def getClassType():
        returnValue = libpanda._inPekxoQkjs()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def processEvents(self):
        returnValue = libpanda._inPekxoIZkG(self.this)
        return returnValue

    
    def dispatchEvent(self, event):
        returnValue = libpanda._inPekxouZmX(self.this, event.this)
        return returnValue

    
    def write(self, out):
        returnValue = libpanda._inPekxo9LkH(self.this, out.this)
        return returnValue


