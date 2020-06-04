# File: C (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import CollisionHandlerPhysical

class CollisionHandlerPusher(CollisionHandlerPhysical.CollisionHandlerPhysical, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self):
        self.this = libpanda._inPHwcaOYFg()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPHwcac4lv:
            libpanda._inPHwcac4lv(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPHwcaQVou()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setHorizontal(self, flag):
        returnValue = libpanda._inPHwcaLy7k(self.this, flag)
        return returnValue

    
    def getHorizontal(self):
        returnValue = libpanda._inPHwca9VDN(self.this)
        return returnValue


