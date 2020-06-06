# File: L (Python 2.2)

import types
import libpandaphysics
import libpandaphysicsDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import BaseForce

class LinearForce(BaseForce.BaseForce, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaphysicsDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self):
        raise RuntimeError, 'No C++ constructor defined for class: ' + self.__class__.__name__

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClassType():
        returnValue = libpandaphysics._inP9fJJEdvs()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setAmplitude(self, a):
        returnValue = libpandaphysics._inP9fJJak2L(self.this, a)
        return returnValue

    
    def setMassDependent(self, m):
        returnValue = libpandaphysics._inP9fJJK6uI(self.this, m)
        return returnValue

    
    def getAmplitude(self):
        returnValue = libpandaphysics._inP9fJJUWPK(self.this)
        return returnValue

    
    def getMassDependent(self):
        returnValue = libpandaphysics._inP9fJJbO05(self.this)
        return returnValue

    
    def setVectorMasks(self, x, y, z):
        returnValue = libpandaphysics._inP9fJJI9tL(self.this, x, y, z)
        return returnValue

    
    def makeCopy(self):
        returnValue = libpandaphysics._inP9fJJyEgT(self.this)
        returnObject = LinearForce(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()


