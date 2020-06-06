# File: D (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import ReferenceCount
import DrawableRegion

class DisplayRegion(ReferenceCount.ReferenceCount, DrawableRegion.DrawableRegion, FFIExternalObject.FFIExternalObject):
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
        returnValue = libpanda._inPO9cYpTxi(self.this)
        return returnValue

    
    def setDimensions(self, l, r, b, t):
        returnValue = libpanda._inPO9cYta7G(self.this, l, r, b, t)
        return returnValue

    
    def getWindow(self):
        returnValue = libpanda._inPO9cYKjj6(self.this)
        import GraphicsOutput
        returnObject = GraphicsOutput.GraphicsOutput(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject.setPointer()

    
    def getPipe(self):
        returnValue = libpanda._inPO9cY668k(self.this)
        import GraphicsPipe
        returnObject = GraphicsPipe.GraphicsPipe(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject.setPointer()

    
    def setCamera(self, camera):
        returnValue = libpanda._inPO9cYsRD1(self.this, camera.this)
        return returnValue

    
    def getCamera(self):
        returnValue = libpanda._inPO9cYM2LQ(self.this)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setActive(self, active):
        returnValue = libpanda._inPO9cYPMVE(self.this, active)
        return returnValue

    
    def isActive(self):
        returnValue = libpanda._inPO9cYpe7G(self.this)
        return returnValue

    
    def setSort(self, sort):
        returnValue = libpanda._inPO9cYJhLw(self.this, sort)
        return returnValue

    
    def getSort(self):
        returnValue = libpanda._inPO9cYkJ4o(self.this)
        return returnValue

    
    def _DisplayRegion__overloaded_computePixels_ptrDisplayRegion(self):
        returnValue = libpanda._inPO9cYZxAV(self.this)
        return returnValue

    
    def _DisplayRegion__overloaded_computePixels_ptrDisplayRegion_int_int(self, xSize, ySize):
        returnValue = libpanda._inPO9cYjMLv(self.this, xSize, ySize)
        return returnValue

    
    def getPixelWidth(self):
        returnValue = libpanda._inPO9cY9Qnq(self.this)
        return returnValue

    
    def getPixelHeight(self):
        returnValue = libpanda._inPO9cYKQDR(self.this)
        return returnValue

    
    def output(self, out):
        returnValue = libpanda._inPO9cYwKBx(self.this, out.this)
        return returnValue

    
    def _DisplayRegion__overloaded_saveScreenshotDefault_ptrDisplayRegion_atomicstring(self, prefix):
        returnValue = libpanda._inPO9cYcz2s(self.this, prefix)
        import Filename
        returnObject = Filename.Filename(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _DisplayRegion__overloaded_saveScreenshotDefault_ptrDisplayRegion(self):
        returnValue = libpanda._inPO9cYJTg6(self.this)
        import Filename
        returnObject = Filename.Filename(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def saveScreenshot(self, filename):
        returnValue = libpanda._inPO9cYN5lm(self.this, filename.this)
        return returnValue

    
    def getScreenshot(self, image):
        returnValue = libpanda._inPO9cY__qS(self.this, image.this)
        return returnValue

    
    def upcastToDrawableRegion(self):
        returnValue = libpanda._inPO9cYlwzo(self.this)
        import DrawableRegion
        returnObject = DrawableRegion.DrawableRegion(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getRefCount(self):
        upcastSelf = self
        returnValue = libpandaexpress._inPKoxtP11_(upcastSelf.this)
        return returnValue

    
    def ref(self):
        upcastSelf = self
        returnValue = libpandaexpress._inPKoxtaS5_(upcastSelf.this)
        return returnValue

    
    def unref(self):
        upcastSelf = self
        returnValue = libpandaexpress._inPKoxtwyVy(upcastSelf.this)
        return returnValue

    
    def testRefCountIntegrity(self):
        upcastSelf = self
        returnValue = libpandaexpress._inPKoxtvpj2(upcastSelf.this)
        return returnValue

    
    def setClearColorActive(self, clearColorActive):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToDrawableRegion()
        returnValue = libpanda._inPO9cY5_NM(upcastSelf.this, clearColorActive)
        return returnValue

    
    def getClearColorActive(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToDrawableRegion()
        returnValue = libpanda._inPO9cYQ__5(upcastSelf.this)
        return returnValue

    
    def setClearDepthActive(self, clearDepthActive):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToDrawableRegion()
        returnValue = libpanda._inPO9cY_x_a(upcastSelf.this, clearDepthActive)
        return returnValue

    
    def getClearDepthActive(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToDrawableRegion()
        returnValue = libpanda._inPO9cYklwI(upcastSelf.this)
        return returnValue

    
    def setClearColor(self, color):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToDrawableRegion()
        returnValue = libpanda._inPO9cYrSVN(upcastSelf.this, color.this)
        return returnValue

    
    def getClearColor(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToDrawableRegion()
        returnValue = libpanda._inPO9cY4kxz(upcastSelf.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setClearDepth(self, depth):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToDrawableRegion()
        returnValue = libpanda._inPO9cYw_6X(upcastSelf.this, depth)
        return returnValue

    
    def getClearDepth(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToDrawableRegion()
        returnValue = libpanda._inPO9cYMYjC(upcastSelf.this)
        return returnValue

    
    def isAnyClearActive(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToDrawableRegion()
        returnValue = libpanda._inPO9cY0Gt_(upcastSelf.this)
        return returnValue

    
    def saveScreenshotDefault(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._DisplayRegion__overloaded_saveScreenshotDefault_ptrDisplayRegion(*_args)
        elif numArgs == 1:
            return self._DisplayRegion__overloaded_saveScreenshotDefault_ptrDisplayRegion_atomicstring(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def computePixels(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._DisplayRegion__overloaded_computePixels_ptrDisplayRegion(*_args)
        elif numArgs == 2:
            return self._DisplayRegion__overloaded_computePixels_ptrDisplayRegion_int_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 2 '


