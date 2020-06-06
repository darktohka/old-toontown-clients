# File: C (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import CollisionSolid

class CollisionSphere(CollisionSolid.CollisionSolid, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _CollisionSphere__overloaded_constructor_ptrConstLPoint3f_float(self, center, radius):
        self.this = libpanda._inPHwcaLNNB(center.this, radius)
        self.userManagesMemory = 1

    
    def _CollisionSphere__overloaded_constructor_float_float_float_float(self, cx, cy, cz, radius):
        self.this = libpanda._inPHwca2Rzm(cx, cy, cz, radius)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPHwcaQay2:
            libpanda._inPHwcaQay2(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPHwcaOm79()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _CollisionSphere__overloaded_setCenter_ptrCollisionSphere_ptrConstLPoint3f(self, center):
        returnValue = libpanda._inPHwca3CUl(self.this, center.this)
        return returnValue

    
    def _CollisionSphere__overloaded_setCenter_ptrCollisionSphere_float_float_float(self, x, y, z):
        returnValue = libpanda._inPHwcaodaV(self.this, x, y, z)
        return returnValue

    
    def getCenter(self):
        returnValue = libpanda._inPHwcazgAq(self.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setRadius(self, radius):
        returnValue = libpanda._inPHwcauEwq(self.this, radius)
        return returnValue

    
    def getRadius(self):
        returnValue = libpanda._inPHwcaLSzr(self.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            return self._CollisionSphere__overloaded_constructor_ptrConstLPoint3f_float(*_args)
        elif numArgs == 4:
            return self._CollisionSphere__overloaded_constructor_float_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 4 '

    
    def setCenter(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._CollisionSphere__overloaded_setCenter_ptrCollisionSphere_ptrConstLPoint3f(*_args)
        elif numArgs == 3:
            return self._CollisionSphere__overloaded_setCenter_ptrCollisionSphere_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '


