# File: C (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import CollisionHandler

class CollisionHandlerQueue(CollisionHandler.CollisionHandler, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self):
        self.this = libpanda._inPHwcaQGY4()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPHwcaB4Rj:
            libpanda._inPHwcaB4Rj(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPHwcamngh()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def sortEntries(self):
        returnValue = libpanda._inPHwca4_OE(self.this)
        return returnValue

    
    def clearEntries(self):
        returnValue = libpanda._inPHwcaZKav(self.this)
        return returnValue

    
    def getNumEntries(self):
        returnValue = libpanda._inPHwca0Ndh(self.this)
        return returnValue

    
    def getEntry(self, n):
        returnValue = libpanda._inPHwcabEk_(self.this, n)
        import CollisionEntry
        returnObject = CollisionEntry.CollisionEntry(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()


