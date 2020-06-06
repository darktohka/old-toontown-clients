# File: C (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import CollisionPlane

class CollisionPolygon(CollisionPlane.CollisionPlane, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _CollisionPolygon__overloaded_constructor_ptrConstLPoint3f_ptrConstLPoint3f(self, begin, end):
        self.this = libpanda._inPHwcaLCpw(begin.this, end.this)
        self.userManagesMemory = 1

    
    def _CollisionPolygon__overloaded_constructor_ptrConstLPoint3f_ptrConstLPoint3f_ptrConstLPoint3f(self, a, b, c):
        self.this = libpanda._inPHwcaxiiq(a.this, b.this, c.this)
        self.userManagesMemory = 1

    
    def _CollisionPolygon__overloaded_constructor_ptrConstLPoint3f_ptrConstLPoint3f_ptrConstLPoint3f_ptrConstLPoint3f(self, a, b, c, d):
        self.this = libpanda._inPHwcaF9sC(a.this, b.this, c.this, d.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPHwcaEL82:
            libpanda._inPHwcaEL82(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPHwcaI99a()
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
            return self._CollisionPolygon__overloaded_constructor_ptrConstLPoint3f_ptrConstLPoint3f(*_args)
        elif numArgs == 3:
            return self._CollisionPolygon__overloaded_constructor_ptrConstLPoint3f_ptrConstLPoint3f_ptrConstLPoint3f(*_args)
        elif numArgs == 4:
            return self._CollisionPolygon__overloaded_constructor_ptrConstLPoint3f_ptrConstLPoint3f_ptrConstLPoint3f_ptrConstLPoint3f(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 4 '


