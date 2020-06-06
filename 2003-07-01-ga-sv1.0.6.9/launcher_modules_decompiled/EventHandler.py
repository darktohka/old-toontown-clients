# File: E (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import TypedObject

class EventHandler(TypedObject.TypedObject, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self, queue):
        self.this = libpandaexpress._inPekxowhlR(queue.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inPekxoIKI8:
            libpandaexpress._inPekxoIKI8(self.this)
        

    
    def getClassType():
        returnValue = libpandaexpress._inPekxoQkjs()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def processEvents(self):
        returnValue = libpandaexpress._inPekxoIZkG(self.this)
        return returnValue

    
    def dispatchEvent(self, event):
        returnValue = libpandaexpress._inPekxouZmX(self.this, event.this)
        return returnValue

    
    def write(self, out):
        returnValue = libpandaexpress._inPekxo9LkH(self.this, out.this)
        return returnValue


