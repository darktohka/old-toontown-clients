# File: P (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import LightNode

class PointLight(LightNode.LightNode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self, name):
        self.this = libpanda._inPkJyodSGa(name)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPkJyoD7C2:
            libpanda._inPkJyoD7C2(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPkJyocV_e()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def getSpecularColor(self):
        returnValue = libpanda._inPkJyoVj3W(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setSpecularColor(self, color):
        returnValue = libpanda._inPkJyo9PIn(self.this, color.this)
        return returnValue

    
    def getAttenuation(self):
        returnValue = libpanda._inPkJyoc4ld(self.this)
        import VBase3
        returnObject = VBase3.VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setAttenuation(self, attenuation):
        returnValue = libpanda._inPkJyoZO9o(self.this, attenuation.this)
        return returnValue

    
    def getPoint(self):
        returnValue = libpanda._inPkJyoHjL5(self.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setPoint(self, point):
        returnValue = libpanda._inPkJyoFPGB(self.this, point.this)
        return returnValue


