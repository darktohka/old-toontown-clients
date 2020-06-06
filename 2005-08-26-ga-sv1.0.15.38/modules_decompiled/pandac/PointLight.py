# File: P (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import LightNode

class PointLight(LightNode.LightNode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self, name):
        self.this = libpanda._inPnJyodSGa(name)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPnJyoA7C2:
            libpanda._inPnJyoA7C2(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPnJyocV_e()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def getSpecularColor(self):
        returnValue = libpanda._inPnJyoVj3W(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setSpecularColor(self, color):
        returnValue = libpanda._inPnJyo_PIn(self.this, color.this)
        return returnValue

    
    def getAttenuation(self):
        returnValue = libpanda._inPnJyoc4ld(self.this)
        import VBase3
        returnObject = VBase3.VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setAttenuation(self, attenuation):
        returnValue = libpanda._inPnJyoeO9o(self.this, attenuation.this)
        return returnValue

    
    def getPoint(self):
        returnValue = libpanda._inPnJyoAjL5(self.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setPoint(self, point):
        returnValue = libpanda._inPnJyoFPGB(self.this, point.this)
        return returnValue


