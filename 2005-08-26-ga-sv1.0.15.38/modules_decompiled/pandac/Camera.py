# File: C (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import LensNode

class Camera(LensNode.LensNode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self, name):
        self.this = libpanda._inPnJyoDDNS(name)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPnJyo10eB:
            libpanda._inPnJyo10eB(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPnJyo7jVC()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setActive(self, active):
        returnValue = libpanda._inPnJyo3QAN(self.this, active)
        return returnValue

    
    def isActive(self):
        returnValue = libpanda._inPnJyoQY9N(self.this)
        return returnValue

    
    def setScene(self, scene):
        returnValue = libpanda._inPnJyo1aj6(self.this, scene.this)
        return returnValue

    
    def getScene(self):
        returnValue = libpanda._inPnJyo_CJc(self.this)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getNumDisplayRegions(self):
        returnValue = libpanda._inPnJyofkXi(self.this)
        return returnValue

    
    def getDisplayRegion(self, n):
        returnValue = libpanda._inPnJyoHanc(self.this, n)
        import DisplayRegion
        returnObject = DisplayRegion.DisplayRegion(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setCameraMask(self, mask):
        returnValue = libpanda._inPnJyocS7v(self.this, mask.this)
        return returnValue

    
    def getCameraMask(self):
        returnValue = libpanda._inPnJyoXHXi(self.this)
        import BitMask32
        returnObject = BitMask32.BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setCullCenter(self, cullCenter):
        returnValue = libpanda._inPnJyodwtU(self.this, cullCenter.this)
        return returnValue

    
    def getCullCenter(self):
        returnValue = libpanda._inPnJyoYdSn(self.this)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setInitialState(self, state):
        returnValue = libpanda._inPnJyoRVZ2(self.this, state.this)
        return returnValue

    
    def getInitialState(self):
        returnValue = libpanda._inPnJyoD4v3(self.this)
        import RenderState
        returnObject = RenderState.RenderState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def setTagStateKey(self, tagStateKey):
        returnValue = libpanda._inPnJyoCBek(self.this, tagStateKey)
        return returnValue

    
    def getTagStateKey(self):
        returnValue = libpanda._inPnJyooh3v(self.this)
        return returnValue

    
    def setTagState(self, tagState, state):
        returnValue = libpanda._inPnJyoT5SH(self.this, tagState, state.this)
        return returnValue

    
    def clearTagState(self, tagState):
        returnValue = libpanda._inPnJyotFjq(self.this, tagState)
        return returnValue

    
    def hasTagState(self, tagState):
        returnValue = libpanda._inPnJyo388o(self.this, tagState)
        return returnValue

    
    def getTagState(self, tagState):
        returnValue = libpanda._inPnJyo7bRn(self.this, tagState)
        import RenderState
        returnObject = RenderState.RenderState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def setAuxSceneData(self, nodePath, data):
        returnValue = libpanda._inPnJyorz56(self.this, nodePath.this, data.this)
        return returnValue

    
    def clearAuxSceneData(self, nodePath):
        returnValue = libpanda._inPnJyogEb_(self.this, nodePath.this)
        return returnValue

    
    def getAuxSceneData(self, nodePath):
        returnValue = libpanda._inPnJyo9tPd(self.this, nodePath.this)
        import AuxSceneData
        returnObject = AuxSceneData.AuxSceneData(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def listAuxSceneData(self, out):
        returnValue = libpanda._inPnJyo72v7(self.this, out.this)
        return returnValue

    
    def cleanupAuxSceneData(self):
        returnValue = libpanda._inPnJyoARBt(self.this)
        return returnValue


