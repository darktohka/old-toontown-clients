# File: G (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import TypedReferenceCount
import ClearableRegion

class GraphicsWindow(TypedReferenceCount.TypedReferenceCount, ClearableRegion.ClearableRegion, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self):
        raise RuntimeError, 'No C++ constructor defined for class: ' + self.__class__.__name__

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPO9cYLgow:
            libpanda._inPO9cYLgow(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPO9cYjGVA()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def getProperties(self):
        returnValue = libpanda._inPO9cYhbmW(self.this)
        import WindowProperties
        returnObject = WindowProperties.WindowProperties(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getRequestedProperties(self):
        returnValue = libpanda._inPO9cY7Htu(self.this)
        import WindowProperties
        returnObject = WindowProperties.WindowProperties(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def clearRejectedProperties(self):
        returnValue = libpanda._inPO9cYYZ4X(self.this)
        return returnValue

    
    def getRejectedProperties(self):
        returnValue = libpanda._inPO9cYcXSI(self.this)
        import WindowProperties
        returnObject = WindowProperties.WindowProperties(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def requestProperties(self, requestedProperties):
        returnValue = libpanda._inPO9cYHdcu(self.this, requestedProperties.this)
        return returnValue

    
    def isClosed(self):
        returnValue = libpanda._inPO9cYh9q8(self.this)
        return returnValue

    
    def isActive(self):
        returnValue = libpanda._inPO9cYIlWk(self.this)
        return returnValue

    
    def isFullscreen(self):
        returnValue = libpanda._inPO9cYIaEs(self.this)
        return returnValue

    
    def setWindowEvent(self, windowEvent):
        returnValue = libpanda._inPO9cYHNv6(self.this, windowEvent)
        return returnValue

    
    def getWindowEvent(self):
        returnValue = libpanda._inPO9cY_R55(self.this)
        return returnValue

    
    def getGsg(self):
        returnValue = libpanda._inPO9cYc07F(self.this)
        import GraphicsStateGuardian
        returnObject = GraphicsStateGuardian.GraphicsStateGuardian(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getPipe(self):
        returnValue = libpanda._inPO9cY54lk(self.this)
        import GraphicsPipe
        returnObject = GraphicsPipe.GraphicsPipe(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getChannel(self, index):
        returnValue = libpanda._inPO9cY4Q0c(self.this, index)
        import GraphicsChannel
        returnObject = GraphicsChannel.GraphicsChannel(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def removeChannel(self, index):
        returnValue = libpanda._inPO9cYTTmb(self.this, index)
        return returnValue

    
    def getMaxChannelIndex(self):
        returnValue = libpanda._inPO9cY376M(self.this)
        return returnValue

    
    def isChannelDefined(self, index):
        returnValue = libpanda._inPO9cYFJ2y(self.this, index)
        return returnValue

    
    def getNumDisplayRegions(self):
        returnValue = libpanda._inPO9cYGL3s(self.this)
        return returnValue

    
    def getDisplayRegion(self, n):
        returnValue = libpanda._inPO9cYr5mc(self.this, n)
        import DisplayRegion
        returnObject = DisplayRegion.DisplayRegion(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getNumInputDevices(self):
        returnValue = libpanda._inPO9cYWc_C(self.this)
        return returnValue

    
    def getInputDeviceName(self, device):
        returnValue = libpanda._inPO9cYqhfW(self.this, device)
        return returnValue

    
    def hasPointer(self, device):
        returnValue = libpanda._inPO9cYYErM(self.this, device)
        return returnValue

    
    def hasKeyboard(self, device):
        returnValue = libpanda._inPO9cYeEpH(self.this, device)
        return returnValue

    
    def upcastToClearableRegion(self):
        returnValue = libpanda._inPO9cYoMck(self.this)
        import ClearableRegion
        returnObject = ClearableRegion.ClearableRegion(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def upcastToReferenceCount(self):
        upcastSelf = self
        returnValue = libpandaexpress._inPJoxtKE8f(upcastSelf.this)
        import ReferenceCount
        returnObject = ReferenceCount.ReferenceCount(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getType(self):
        upcastSelf = self
        returnValue = libpandaexpress._inPJoxt1uxI(upcastSelf.this)
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getTypeIndex(self):
        upcastSelf = self
        returnValue = libpandaexpress._inPJoxtm7AU(upcastSelf.this)
        return returnValue

    
    def isOfType(self, handle):
        upcastSelf = self
        returnValue = libpandaexpress._inPJoxtmFKt(upcastSelf.this, handle.this)
        return returnValue

    
    def isExactType(self, handle):
        upcastSelf = self
        returnValue = libpandaexpress._inPJoxtkXzz(upcastSelf.this, handle.this)
        return returnValue

    
    def getRefCount(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPJoxtM11_(upcastSelf.this)
        return returnValue

    
    def ref(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPJoxtVS5_(upcastSelf.this)
        return returnValue

    
    def unref(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPJoxtzyVy(upcastSelf.this)
        return returnValue

    
    def testRefCountIntegrity(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPJoxtupj2(upcastSelf.this)
        return returnValue

    
    def setClearColorActive(self, clearColorActive):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToClearableRegion()
        returnValue = libpanda._inPO9cYrI_a(upcastSelf.this, clearColorActive)
        return returnValue

    
    def getClearColorActive(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToClearableRegion()
        returnValue = libpanda._inPO9cY73cT(upcastSelf.this)
        return returnValue

    
    def setClearDepthActive(self, clearDepthActive):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToClearableRegion()
        returnValue = libpanda._inPO9cYD0jz(upcastSelf.this, clearDepthActive)
        return returnValue

    
    def getClearDepthActive(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToClearableRegion()
        returnValue = libpanda._inPO9cYIBBs(upcastSelf.this)
        return returnValue

    
    def setClearColor(self, color):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToClearableRegion()
        returnValue = libpanda._inPO9cYEJb_(upcastSelf.this, color.this)
        return returnValue

    
    def getClearColor(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToClearableRegion()
        returnValue = libpanda._inPO9cYHnZM(upcastSelf.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setClearDepth(self, depth):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToClearableRegion()
        returnValue = libpanda._inPO9cYg8RQ(upcastSelf.this, depth)
        return returnValue

    
    def getClearDepth(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToClearableRegion()
        returnValue = libpanda._inPO9cYkm_k(upcastSelf.this)
        return returnValue

    
    def isAnyClearActive(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToClearableRegion()
        returnValue = libpanda._inPO9cYNXIL(upcastSelf.this)
        return returnValue


