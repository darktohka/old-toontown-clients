# File: C (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import CollisionSolid

class CollisionPlane(CollisionSolid.CollisionSolid, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _CollisionPlane__overloaded_constructor_ptrConstCollisionPlane(self, copy):
        self.this = libpanda._inPHwca21w1(copy.this)
        self.userManagesMemory = 1

    
    def _CollisionPlane__overloaded_constructor_ptrConstPlanef(self, planeBase):
        self.this = libpanda._inPHwcalkhc(planeBase.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPHwcau0SK:
            libpanda._inPHwcau0SK(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPHwca8byU()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def getNormal(self):
        returnValue = libpanda._inPHwcamYK9(self.this)
        import Vec3
        returnObject = Vec3.Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def distToPlane(self, point):
        returnValue = libpanda._inPHwcaOb8M(self.this, point.this)
        return returnValue

    
    def setPlane(self, planeBase):
        returnValue = libpanda._inPHwcaAQAO(self.this, planeBase.this)
        return returnValue

    
    def getPlane(self):
        returnValue = libpanda._inPHwcar8W5(self.this)
        import Plane
        returnObject = Plane.Plane(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Plane
            if isinstance(_args[0], Plane.Plane):
                return self._CollisionPlane__overloaded_constructor_ptrConstPlanef(*_args)
            
            if isinstance(_args[0], CollisionPlane):
                return self._CollisionPlane__overloaded_constructor_ptrConstCollisionPlane(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <Plane.Plane> <CollisionPlane> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


