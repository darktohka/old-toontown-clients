# File: C (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import CollisionSphere

class CollisionInvSphere(CollisionSphere.CollisionSphere, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _CollisionInvSphere__overloaded_constructor_ptrConstLPoint3f_float(self, center, radius):
        self.this = libpanda._inPHwca_yWY(center.this, radius)
        self.userManagesMemory = 1

    
    def _CollisionInvSphere__overloaded_constructor_float_float_float_float(self, cx, cy, cz, radius):
        self.this = libpanda._inPHwcaUKHB(cx, cy, cz, radius)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPHwcab3nP:
            libpanda._inPHwcab3nP(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPHwca9Ep8()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            return self._CollisionInvSphere__overloaded_constructor_ptrConstLPoint3f_float(*_args)
        elif numArgs == 4:
            return self._CollisionInvSphere__overloaded_constructor_float_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 4 '


