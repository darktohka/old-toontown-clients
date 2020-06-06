# File: S (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import LerpFunctor

class SimpleLerpFunctorLPoint2f(LerpFunctor.LerpFunctor, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
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
        returnValue = libpanda._inPjRdzL5G7()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def interpolate(self, parameter1):
        returnValue = libpanda._inPjRdziDFn(self.this, parameter1)
        import Point2
        returnObject = Point2.Point2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getStart(self):
        returnValue = libpanda._inPjRdzSIRf(self.this)
        import Point2
        returnObject = Point2.Point2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getEnd(self):
        returnValue = libpanda._inPjRdzVF2Z(self.this)
        import Point2
        returnObject = Point2.Point2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject


