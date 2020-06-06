# File: C (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import CollisionSolid

class CollisionSegment(CollisionSolid.CollisionSolid, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _CollisionSegment__overloaded_constructor(self):
        self.this = libpanda._inPHwcaG_0_()
        self.userManagesMemory = 1

    
    def _CollisionSegment__overloaded_constructor_ptrConstLPoint3f_ptrConstLPoint3f(self, a, db):
        self.this = libpanda._inPHwcahcIM(a.this, db.this)
        self.userManagesMemory = 1

    
    def _CollisionSegment__overloaded_constructor_float_float_float_float_float_float(self, ax, ay, az, bx, by, bz):
        self.this = libpanda._inPHwcaGSlK(ax, ay, az, bx, by, bz)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPHwcaWHZw:
            libpanda._inPHwcaWHZw(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPHwcakImW()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _CollisionSegment__overloaded_setPointA_ptrCollisionSegment_ptrConstLPoint3f(self, a):
        returnValue = libpanda._inPHwca5ebw(self.this, a.this)
        return returnValue

    
    def _CollisionSegment__overloaded_setPointA_ptrCollisionSegment_float_float_float(self, x, y, z):
        returnValue = libpanda._inPHwcayePy(self.this, x, y, z)
        return returnValue

    
    def getPointA(self):
        returnValue = libpanda._inPHwcaxXkX(self.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _CollisionSegment__overloaded_setPointB_ptrCollisionSegment_ptrConstLPoint3f(self, b):
        returnValue = libpanda._inPHwcayVbM(self.this, b.this)
        return returnValue

    
    def _CollisionSegment__overloaded_setPointB_ptrCollisionSegment_float_float_float(self, x, y, z):
        returnValue = libpanda._inPHwca1bPO(self.this, x, y, z)
        return returnValue

    
    def getPointB(self):
        returnValue = libpanda._inPHwca5Kkz(self.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _CollisionSegment__overloaded_setFromLens_ptrCollisionSegment_ptrLensNode_ptrConstLPoint2f(self, camera, point):
        returnValue = libpanda._inPHwcalPim(self.this, camera.this, point.this)
        return returnValue

    
    def _CollisionSegment__overloaded_setFromLens_ptrCollisionSegment_ptrLensNode_float_float(self, camera, px, py):
        returnValue = libpanda._inPHwcaq5Ut(self.this, camera.this, px, py)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._CollisionSegment__overloaded_constructor(*_args)
        elif numArgs == 2:
            return self._CollisionSegment__overloaded_constructor_ptrConstLPoint3f_ptrConstLPoint3f(*_args)
        elif numArgs == 6:
            return self._CollisionSegment__overloaded_constructor_float_float_float_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 2 6 '

    
    def setPointB(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._CollisionSegment__overloaded_setPointB_ptrCollisionSegment_ptrConstLPoint3f(*_args)
        elif numArgs == 3:
            return self._CollisionSegment__overloaded_setPointB_ptrCollisionSegment_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '

    
    def setPointA(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._CollisionSegment__overloaded_setPointA_ptrCollisionSegment_ptrConstLPoint3f(*_args)
        elif numArgs == 3:
            return self._CollisionSegment__overloaded_setPointA_ptrCollisionSegment_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '

    
    def setFromLens(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            return self._CollisionSegment__overloaded_setFromLens_ptrCollisionSegment_ptrLensNode_ptrConstLPoint2f(*_args)
        elif numArgs == 3:
            return self._CollisionSegment__overloaded_setFromLens_ptrCollisionSegment_ptrLensNode_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '


