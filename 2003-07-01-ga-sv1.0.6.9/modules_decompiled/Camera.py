# File: C (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import LensNode

class Camera(LensNode.LensNode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self, name):
        self.this = libpanda._inPkJyoDDNS(name)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPkJyo10eB:
            libpanda._inPkJyo10eB(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPkJyo7jVC()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setActive(self, active):
        returnValue = libpanda._inPkJyo3QAN(self.this, active)
        return returnValue

    
    def isActive(self):
        returnValue = libpanda._inPkJyoQY9N(self.this)
        return returnValue

    
    def setScene(self, scene):
        returnValue = libpanda._inPkJyo2aj6(self.this, scene.this)
        return returnValue

    
    def getScene(self):
        returnValue = libpanda._inPkJyo_CJc(self.this)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getNumDisplayRegions(self):
        returnValue = libpanda._inPkJyoekXi(self.this)
        return returnValue

    
    def getDisplayRegion(self, n):
        returnValue = libpanda._inPkJyoHanc(self.this, n)
        import DisplayRegion
        returnObject = DisplayRegion.DisplayRegion(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setCameraMask(self, mask):
        returnValue = libpanda._inPkJyoSRdR(self.this, mask.this)
        return returnValue

    
    def getCameraMask(self):
        returnValue = libpanda._inPkJyoIHXi(self.this)
        import BitMask32
        returnObject = BitMask32.BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject


