# File: B (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import GeometricBoundingVolume

class BoundingLine(GeometricBoundingVolume.GeometricBoundingVolume, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _BoundingLine__overloaded_constructor(self):
        self.this = libpanda._inPSkjPHsL1()
        self.userManagesMemory = 1

    
    def _BoundingLine__overloaded_constructor_ptrConstLPoint3f_ptrConstLPoint3f(self, a, b):
        self.this = libpanda._inPSkjPAR_R(a.this, b.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPSkjPnAIV:
            libpanda._inPSkjPnAIV(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPSkjPmcUv()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def getPointA(self):
        returnValue = libpanda._inPSkjPRIF_(self.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getPointB(self):
        returnValue = libpanda._inPSkjPI2G_(self.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._BoundingLine__overloaded_constructor(*_args)
        elif numArgs == 2:
            return self._BoundingLine__overloaded_constructor_ptrConstLPoint3f_ptrConstLPoint3f(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 2 '


