# File: C (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import CollisionSolid

class CollisionRay(CollisionSolid.CollisionSolid, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _CollisionRay__overloaded_constructor(self):
        self.this = libpanda._inPHwcaOnzJ()
        self.userManagesMemory = 1

    
    def _CollisionRay__overloaded_constructor_ptrConstLPoint3f_ptrConstLVector3f(self, origin, direction):
        self.this = libpanda._inPHwcauWsc(origin.this, direction.this)
        self.userManagesMemory = 1

    
    def _CollisionRay__overloaded_constructor_float_float_float_float_float_float(self, ox, oy, oz, dx, dy, dz):
        self.this = libpanda._inPHwcasJco(ox, oy, oz, dx, dy, dz)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPHwcamAyp:
            libpanda._inPHwcamAyp(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPHwcaVl1_()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _CollisionRay__overloaded_setOrigin_ptrCollisionRay_ptrConstLPoint3f(self, origin):
        returnValue = libpanda._inPHwcaWQg4(self.this, origin.this)
        return returnValue

    
    def _CollisionRay__overloaded_setOrigin_ptrCollisionRay_float_float_float(self, x, y, z):
        returnValue = libpanda._inPHwcaCEZ5(self.this, x, y, z)
        return returnValue

    
    def getOrigin(self):
        returnValue = libpanda._inPHwcao7AW(self.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _CollisionRay__overloaded_setDirection_ptrCollisionRay_ptrConstLVector3f(self, direction):
        returnValue = libpanda._inPHwcaFnJ_(self.this, direction.this)
        return returnValue

    
    def _CollisionRay__overloaded_setDirection_ptrCollisionRay_float_float_float(self, x, y, z):
        returnValue = libpanda._inPHwcau5k9(self.this, x, y, z)
        return returnValue

    
    def getDirection(self):
        returnValue = libpanda._inPHwcaxcuk(self.this)
        import Vec3
        returnObject = Vec3.Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _CollisionRay__overloaded_setFromLens_ptrCollisionRay_ptrLensNode_ptrConstLPoint2f(self, camera, point):
        returnValue = libpanda._inPHwcaDz4_(self.this, camera.this, point.this)
        return returnValue

    
    def _CollisionRay__overloaded_setFromLens_ptrCollisionRay_ptrLensNode_float_float(self, camera, px, py):
        returnValue = libpanda._inPHwcakXhs(self.this, camera.this, px, py)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._CollisionRay__overloaded_constructor(*_args)
        elif numArgs == 2:
            return self._CollisionRay__overloaded_constructor_ptrConstLPoint3f_ptrConstLVector3f(*_args)
        elif numArgs == 6:
            return self._CollisionRay__overloaded_constructor_float_float_float_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 2 6 '

    
    def setOrigin(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._CollisionRay__overloaded_setOrigin_ptrCollisionRay_ptrConstLPoint3f(*_args)
        elif numArgs == 3:
            return self._CollisionRay__overloaded_setOrigin_ptrCollisionRay_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '

    
    def setDirection(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._CollisionRay__overloaded_setDirection_ptrCollisionRay_ptrConstLVector3f(*_args)
        elif numArgs == 3:
            return self._CollisionRay__overloaded_setDirection_ptrCollisionRay_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '

    
    def setFromLens(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            return self._CollisionRay__overloaded_setFromLens_ptrCollisionRay_ptrLensNode_ptrConstLPoint2f(*_args)
        elif numArgs == 3:
            return self._CollisionRay__overloaded_setFromLens_ptrCollisionRay_ptrLensNode_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '


