# File: C (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import CollisionSolid

class CollisionTube(CollisionSolid.CollisionSolid, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _CollisionTube__overloaded_constructor_ptrConstLPoint3f_ptrConstLPoint3f_float(self, a, db, radius):
        self.this = libpanda._inPHwcayNS4(a.this, db.this, radius)
        self.userManagesMemory = 1

    
    def _CollisionTube__overloaded_constructor_float_float_float_float_float_float_float(self, ax, ay, az, bx, by, bz, radius):
        self.this = libpanda._inPHwcae_eG(ax, ay, az, bx, by, bz, radius)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPHwcauuTD:
            libpanda._inPHwcauuTD(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPHwcaur7C()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _CollisionTube__overloaded_setPointA_ptrCollisionTube_ptrConstLPoint3f(self, a):
        returnValue = libpanda._inPHwca8Wt6(self.this, a.this)
        return returnValue

    
    def _CollisionTube__overloaded_setPointA_ptrCollisionTube_float_float_float(self, x, y, z):
        returnValue = libpanda._inPHwca2wJc(self.this, x, y, z)
        return returnValue

    
    def getPointA(self):
        returnValue = libpanda._inPHwcaoxl7(self.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _CollisionTube__overloaded_setPointB_ptrCollisionTube_ptrConstLPoint3f(self, b):
        returnValue = libpanda._inPHwcacSS7(self.this, b.this)
        return returnValue

    
    def _CollisionTube__overloaded_setPointB_ptrCollisionTube_float_float_float(self, x, y, z):
        returnValue = libpanda._inPHwcaWPxc(self.this, x, y, z)
        return returnValue

    
    def getPointB(self):
        returnValue = libpanda._inPHwcaI1M8(self.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setRadius(self, radius):
        returnValue = libpanda._inPHwca_G54(self.this, radius)
        return returnValue

    
    def getRadius(self):
        returnValue = libpanda._inPHwcaSKpL(self.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 3:
            return self._CollisionTube__overloaded_constructor_ptrConstLPoint3f_ptrConstLPoint3f_float(*_args)
        elif numArgs == 7:
            return self._CollisionTube__overloaded_constructor_float_float_float_float_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 3 7 '

    
    def setPointB(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._CollisionTube__overloaded_setPointB_ptrCollisionTube_ptrConstLPoint3f(*_args)
        elif numArgs == 3:
            return self._CollisionTube__overloaded_setPointB_ptrCollisionTube_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '

    
    def setPointA(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._CollisionTube__overloaded_setPointA_ptrCollisionTube_ptrConstLPoint3f(*_args)
        elif numArgs == 3:
            return self._CollisionTube__overloaded_setPointA_ptrCollisionTube_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '


