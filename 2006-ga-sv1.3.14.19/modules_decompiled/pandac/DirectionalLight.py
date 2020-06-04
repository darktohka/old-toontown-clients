# File: D (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import LightNode

class DirectionalLight(LightNode.LightNode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self, name):
        self.this = libpanda._inPnJyoFmND(name)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPnJyoORYZ:
            libpanda._inPnJyoORYZ(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPnJyov7PH()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def getSpecularColor(self):
        returnValue = libpanda._inPnJyoetKC(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setSpecularColor(self, color):
        returnValue = libpanda._inPnJyoCHLU(self.this, color.this)
        return returnValue

    
    def getPoint(self):
        returnValue = libpanda._inPnJyopsIS(self.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setPoint(self, point):
        returnValue = libpanda._inPnJyoE91O(self.this, point.this)
        return returnValue

    
    def getDirection(self):
        returnValue = libpanda._inPnJyoFGi1(self.this)
        import Vec3
        returnObject = Vec3.Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setDirection(self, direction):
        returnValue = libpanda._inPnJyoFGF_(self.this, direction.this)
        return returnValue


