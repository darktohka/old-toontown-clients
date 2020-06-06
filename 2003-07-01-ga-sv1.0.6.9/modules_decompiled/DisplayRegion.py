# File: D (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import ReferenceCount
import ClearableRegion

class DisplayRegion(ReferenceCount.ReferenceCount, ClearableRegion.ClearableRegion, FFIExternalObject.FFIExternalObject):
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
        if libpanda and libpanda._inPO9cYl3bD:
            libpanda._inPO9cYl3bD(self.this)
        

    
    def getLeft(self):
        returnValue = libpanda._inPO9cY8EnQ(self.this)
        return returnValue

    
    def getRight(self):
        returnValue = libpanda._inPO9cY85BK(self.this)
        return returnValue

    
    def getBottom(self):
        returnValue = libpanda._inPO9cYCJld(self.this)
        return returnValue

    
    def getTop(self):
        returnValue = libpanda._inPO9cYoTxi(self.this)
        return returnValue

    
    def setDimensions(self, l, r, b, t):
        returnValue = libpanda._inPO9cYta7G(self.this, l, r, b, t)
        return returnValue

    
    def getLayer(self):
        returnValue = libpanda._inPO9cYVs9x(self.this)
        import GraphicsLayer
        returnObject = GraphicsLayer.GraphicsLayer(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject.setPointer()

    
    def getChannel(self):
        returnValue = libpanda._inPO9cYzt6W(self.this)
        import GraphicsChannel
        returnObject = GraphicsChannel.GraphicsChannel(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject.setPointer()

    
    def getWindow(self):
        returnValue = libpanda._inPO9cYLjj6(self.this)
        import GraphicsWindow
        returnObject = GraphicsWindow.GraphicsWindow(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject.setPointer()

    
    def getPipe(self):
        returnValue = libpanda._inPO9cY568k(self.this)
        import GraphicsPipe
        returnObject = GraphicsPipe.GraphicsPipe(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject.setPointer()

    
    def setCamera(self, camera):
        returnValue = libpanda._inPO9cYrRD1(self.this, camera.this)
        return returnValue

    
    def getCamera(self):
        returnValue = libpanda._inPO9cYM2LQ(self.this)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setActive(self, active):
        returnValue = libpanda._inPO9cYPMVE(self.this, active)
        return returnValue

    
    def isActive(self):
        returnValue = libpanda._inPO9cYpe7G(self.this)
        return returnValue

    
    def _DisplayRegion__overloaded_computePixels_ptrDisplayRegion(self):
        returnValue = libpanda._inPO9cYZxAV(self.this)
        return returnValue

    
    def _DisplayRegion__overloaded_computePixels_ptrDisplayRegion_int_int(self, xSize, ySize):
        returnValue = libpanda._inPO9cYiMLv(self.this, xSize, ySize)
        return returnValue

    
    def getPixelWidth(self):
        returnValue = libpanda._inPO9cY_Qnq(self.this)
        return returnValue

    
    def getPixelHeight(self):
        returnValue = libpanda._inPO9cYKQDR(self.this)
        return returnValue

    
    def output(self, out):
        returnValue = libpanda._inPO9cYxKBx(self.this, out.this)
        return returnValue

    
    def upcastToClearableRegion(self):
        returnValue = libpanda._inPO9cYXU4e(self.this)
        import ClearableRegion
        returnObject = ClearableRegion.ClearableRegion(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getRefCount(self):
        upcastSelf = self
        returnValue = libpandaexpress._inPJoxtM11_(upcastSelf.this)
        return returnValue

    
    def ref(self):
        upcastSelf = self
        returnValue = libpandaexpress._inPJoxtVS5_(upcastSelf.this)
        return returnValue

    
    def unref(self):
        upcastSelf = self
        returnValue = libpandaexpress._inPJoxtzyVy(upcastSelf.this)
        return returnValue

    
    def testRefCountIntegrity(self):
        upcastSelf = self
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

    
    def computePixels(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._DisplayRegion__overloaded_computePixels_ptrDisplayRegion()
        elif numArgs == 2:
            if isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.IntType):
                    return self._DisplayRegion__overloaded_computePixels_ptrDisplayRegion_int_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 2 '


