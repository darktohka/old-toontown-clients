# File: P (Python 2.2)

import types
import libpandaphysics
import libpandaphysicsDowncasts
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import CollisionHandlerPusher

class PhysicsCollisionHandler(CollisionHandlerPusher.CollisionHandlerPusher, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaphysicsDowncasts,
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self):
        self.this = libpandaphysics._inP9fJJ4b5t()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClassType():
        returnValue = libpandaphysics._inP9fJJm1_7()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setAlmostStationarySpeed(self, speed):
        returnValue = libpandaphysics._inP9fJJbPFH(self.this, speed)
        return returnValue

    
    def getAlmostStationarySpeed(self):
        returnValue = libpandaphysics._inP9fJJkpbd(self.this)
        return returnValue

    
    def setStaticFrictionCoef(self, coef):
        returnValue = libpandaphysics._inP9fJJnSD1(self.this, coef)
        return returnValue

    
    def getStaticFrictionCoef(self):
        returnValue = libpandaphysics._inP9fJJDybx(self.this)
        return returnValue

    
    def setDynamicFrictionCoef(self, coef):
        returnValue = libpandaphysics._inP9fJJ_3NV(self.this, coef)
        return returnValue

    
    def getDynamicFrictionCoef(self):
        returnValue = libpandaphysics._inP9fJJXqrD(self.this)
        return returnValue


