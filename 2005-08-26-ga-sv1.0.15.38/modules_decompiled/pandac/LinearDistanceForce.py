# File: L (Python 2.2)

import types
import libpandaphysics
import libpandaphysicsDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import LinearForce

class LinearDistanceForce(LinearForce.LinearForce, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaphysicsDowncasts,
        libpandaexpressDowncasts]
    FTONEOVERR = 0
    FTONEOVERRSQUARED = 1
    FTONEOVERRCUBED = 2
    
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
        returnValue = libpandaphysics._inP9fJJ4jKf()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setRadius(self, r):
        returnValue = libpandaphysics._inP9fJJnZ9d(self.this, r)
        return returnValue

    
    def setFalloffType(self, ft):
        returnValue = libpandaphysics._inP9fJJsEHZ(self.this, ft)
        return returnValue

    
    def setForceCenter(self, p):
        returnValue = libpandaphysics._inP9fJJjHEK(self.this, p.this)
        return returnValue

    
    def getRadius(self):
        returnValue = libpandaphysics._inP9fJJ6NAO(self.this)
        return returnValue

    
    def getFalloffType(self):
        returnValue = libpandaphysics._inP9fJJfx6e(self.this)
        return returnValue

    
    def getForceCenter(self):
        returnValue = libpandaphysics._inP9fJJXLIy(self.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getScalarTerm(self):
        returnValue = libpandaphysics._inP9fJJSM3k(self.this)
        return returnValue


