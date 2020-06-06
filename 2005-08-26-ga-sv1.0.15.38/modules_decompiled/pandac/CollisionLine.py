# File: C (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import CollisionRay

class CollisionLine(CollisionRay.CollisionRay, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _CollisionLine__overloaded_constructor(self):
        self.this = libpanda._inPHwcabj0W()
        self.userManagesMemory = 1

    
    def _CollisionLine__overloaded_constructor_ptrConstLPoint3f_ptrConstLVector3f(self, origin, direction):
        self.this = libpanda._inPHwcakrPl(origin.this, direction.this)
        self.userManagesMemory = 1

    
    def _CollisionLine__overloaded_constructor_float_float_float_float_float_float(self, ox, oy, oz, dx, dy, dz):
        self.this = libpanda._inPHwcaXh24(ox, oy, oz, dx, dy, dz)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPHwcaq086:
            libpanda._inPHwcaq086(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPHwcaRXQf()
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
        if numArgs == 0:
            return self._CollisionLine__overloaded_constructor(*_args)
        elif numArgs == 2:
            return self._CollisionLine__overloaded_constructor_ptrConstLPoint3f_ptrConstLVector3f(*_args)
        elif numArgs == 6:
            return self._CollisionLine__overloaded_constructor_float_float_float_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 2 6 '


