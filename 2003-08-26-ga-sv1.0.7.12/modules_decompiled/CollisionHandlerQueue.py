# File: C (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import CollisionHandler

class CollisionHandlerQueue(CollisionHandler.CollisionHandler, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self):
        self.this = libpanda._inPHwcaXGY4()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPHwcaA4Rj:
            libpanda._inPHwcaA4Rj(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPHwcanngh()
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
        returnValue = libpanda._inPHwcaYKav(self.this)
        return returnValue

    
    def getNumEntries(self):
        returnValue = libpanda._inPHwcazNdh(self.this)
        return returnValue

    
    def getEntry(self, n):
        returnValue = libpanda._inPHwcakFk_(self.this, n)
        import CollisionEntry
        returnObject = CollisionEntry.CollisionEntry(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()


