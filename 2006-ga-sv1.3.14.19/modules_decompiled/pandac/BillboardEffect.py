# File: B (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import RenderEffect

class BillboardEffect(RenderEffect.RenderEffect, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self):
        raise RuntimeError, 'No C++ constructor defined for class: ' + self.__class__.__name__

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPnJyo0pHv:
            libpanda._inPnJyo0pHv(self.this)
        

    
    def make(upVector, eyeRelative, axialRotate, offset, lookAt, lookAtPoint):
        returnValue = libpanda._inPnJyoMLb2(upVector.this, eyeRelative, axialRotate, offset, lookAt.this, lookAtPoint.this)
        import RenderEffect
        returnObject = RenderEffect.RenderEffect(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    make = staticmethod(make)
    
    def makeAxis():
        returnValue = libpanda._inPnJyoZkox()
        import RenderEffect
        returnObject = RenderEffect.RenderEffect(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    makeAxis = staticmethod(makeAxis)
    
    def makePointEye():
        returnValue = libpanda._inPnJyoKjao()
        import RenderEffect
        returnObject = RenderEffect.RenderEffect(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    makePointEye = staticmethod(makePointEye)
    
    def makePointWorld():
        returnValue = libpanda._inPnJyo5nHa()
        import RenderEffect
        returnObject = RenderEffect.RenderEffect(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    makePointWorld = staticmethod(makePointWorld)
    
    def getClassType():
        returnValue = libpanda._inPnJyoEm5V()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def isOff(self):
        returnValue = libpanda._inPnJyoFuxD(self.this)
        return returnValue

    
    def getUpVector(self):
        returnValue = libpanda._inPnJyoamrP(self.this)
        import Vec3
        returnObject = Vec3.Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getEyeRelative(self):
        returnValue = libpanda._inPnJyoDPkT(self.this)
        return returnValue

    
    def getAxialRotate(self):
        returnValue = libpanda._inPnJyojfqI(self.this)
        return returnValue

    
    def getOffset(self):
        returnValue = libpanda._inPnJyoJ6nm(self.this)
        return returnValue

    
    def getLookAt(self):
        returnValue = libpanda._inPnJyoeWpx(self.this)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getLookAtPoint(self):
        returnValue = libpanda._inPnJyoA3tu(self.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject


