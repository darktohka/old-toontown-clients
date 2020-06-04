# File: B (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import FiniteBoundingVolume

class BoundingSphere(FiniteBoundingVolume.FiniteBoundingVolume, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _BoundingSphere__overloaded_constructor(self):
        self.this = libpanda._inPSkjPqeoF()
        self.userManagesMemory = 1

    
    def _BoundingSphere__overloaded_constructor_ptrConstLPoint3f_float(self, center, radius):
        self.this = libpanda._inPSkjPX3ZH(center.this, radius)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPSkjPtO8B:
            libpanda._inPSkjPtO8B(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPSkjPwySa()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def getCenter(self):
        returnValue = libpanda._inPSkjPzKph(self.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getRadius(self):
        returnValue = libpanda._inPSkjPyYsx(self.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._BoundingSphere__overloaded_constructor(*_args)
        elif numArgs == 2:
            return self._BoundingSphere__overloaded_constructor_ptrConstLPoint3f_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 2 '


