# File: G (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import TypedWritableReferenceCount
import DrawableRegion

class GraphicsOutput(TypedWritableReferenceCount.TypedWritableReferenceCount, DrawableRegion.DrawableRegion, FFIExternalObject.FFIExternalObject):
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
        if libpanda and libpanda._inPO9cY6u1B:
            libpanda._inPO9cY6u1B(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPO9cYg2P6()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def getGsg(self):
        returnValue = libpanda._inPO9cY6R3_(self.this)
        import GraphicsStateGuardian
        returnObject = GraphicsStateGuardian.GraphicsStateGuardian(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getPipe(self):
        returnValue = libpanda._inPO9cYRmhe(self.this)
        import GraphicsPipe
        returnObject = GraphicsPipe.GraphicsPipe(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getName(self):
        returnValue = libpanda._inPO9cYhafm(self.this)
        return returnValue

    
    def hasTexture(self):
        returnValue = libpanda._inPO9cYL5u4(self.this)
        return returnValue

    
    def getTexture(self):
        returnValue = libpanda._inPO9cYjbtr(self.this)
        import Texture
        returnObject = Texture.Texture(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def detachTexture(self):
        returnValue = libpanda._inPO9cYZpLl(self.this)
        return returnValue

    
    def setupCopyTexture(self, name):
        returnValue = libpanda._inPO9cY2Qyi(self.this, name)
        return returnValue

    
    def getXSize(self):
        returnValue = libpanda._inPO9cYpVEG(self.this)
        return returnValue

    
    def getYSize(self):
        returnValue = libpanda._inPO9cY5zZG(self.this)
        return returnValue

    
    def hasSize(self):
        returnValue = libpanda._inPO9cYqgyg(self.this)
        return returnValue

    
    def isValid(self):
        returnValue = libpanda._inPO9cYewNA(self.this)
        return returnValue

    
    def setActive(self, active):
        returnValue = libpanda._inPO9cYKShL(self.this, active)
        return returnValue

    
    def isActive(self):
        returnValue = libpanda._inPO9cYCPRe(self.this)
        return returnValue

    
    def setOneShot(self, oneShot):
        returnValue = libpanda._inPO9cYHoke(self.this, oneShot)
        return returnValue

    
    def getOneShot(self):
        returnValue = libpanda._inPO9cY2vFO(self.this)
        return returnValue

    
    def setInverted(self, inverted):
        returnValue = libpanda._inPO9cYNoPm(self.this, inverted)
        return returnValue

    
    def getInverted(self):
        returnValue = libpanda._inPO9cYx4vV(self.this)
        return returnValue

    
    def clearDeleteFlag(self):
        returnValue = libpanda._inPO9cYjxx5(self.this)
        return returnValue

    
    def getDeleteFlag(self):
        returnValue = libpanda._inPO9cYsJD_(self.this)
        return returnValue

    
    def setSort(self, sort):
        returnValue = libpanda._inPO9cYQqjF(self.this, sort)
        return returnValue

    
    def getSort(self):
        returnValue = libpanda._inPO9cYcE4c(self.this)
        return returnValue

    
    def _GraphicsOutput__overloaded_makeDisplayRegion_ptrGraphicsOutput(self):
        returnValue = libpanda._inPO9cYDSih(self.this)
        import DisplayRegion
        returnObject = DisplayRegion.DisplayRegion(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _GraphicsOutput__overloaded_makeDisplayRegion_ptrGraphicsOutput_float_float_float_float(self, l, r, b, t):
        returnValue = libpanda._inPO9cYefSE(self.this, l, r, b, t)
        import DisplayRegion
        returnObject = DisplayRegion.DisplayRegion(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def removeDisplayRegion(self, displayRegion):
        returnValue = libpanda._inPO9cYyMVJ(self.this, displayRegion.this)
        return returnValue

    
    def getNumDisplayRegions(self):
        returnValue = libpanda._inPO9cYHxxm(self.this)
        return returnValue

    
    def getDisplayRegion(self, n):
        returnValue = libpanda._inPO9cY1bhW(self.this, n)
        import DisplayRegion
        returnObject = DisplayRegion.DisplayRegion(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getNumActiveDisplayRegions(self):
        returnValue = libpanda._inPO9cY_TMd(self.this)
        return returnValue

    
    def getActiveDisplayRegion(self, n):
        returnValue = libpanda._inPO9cYjI4S(self.this, n)
        import DisplayRegion
        returnObject = DisplayRegion.DisplayRegion(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def makeTextureBuffer(self, name, xSize, ySize):
        returnValue = libpanda._inPO9cY6cMF(self.this, name, xSize, ySize)
        returnObject = GraphicsOutput(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _GraphicsOutput__overloaded_saveScreenshotDefault_ptrGraphicsOutput_atomicstring(self, prefix):
        returnValue = libpanda._inPO9cYbMge(self.this, prefix)
        import Filename
        returnObject = Filename.Filename(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _GraphicsOutput__overloaded_saveScreenshotDefault_ptrGraphicsOutput(self):
        returnValue = libpanda._inPO9cY8zcS(self.this)
        import Filename
        returnObject = Filename.Filename(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def saveScreenshot(self, filename):
        returnValue = libpanda._inPO9cYoVLU(self.this, filename.this)
        return returnValue

    
    def getScreenshot(self, image):
        returnValue = libpanda._inPO9cYIsHW(self.this, image.this)
        return returnValue

    
    def upcastToDrawableRegion(self):
        returnValue = libpanda._inPO9cYpLTb(self.this)
        import DrawableRegion
        returnObject = DrawableRegion.DrawableRegion(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def upcastToReferenceCount(self):
        upcastSelf = self
        returnValue = libpanda._inPflbokcf_(upcastSelf.this)
        import ReferenceCount
        returnObject = ReferenceCount.ReferenceCount(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getType(self):
        upcastSelf = self
        returnValue = libpandaexpress._inPKoxt1uxI(upcastSelf.this)
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getTypeIndex(self):
        upcastSelf = self
        returnValue = libpandaexpress._inPKoxtm7AU(upcastSelf.this)
        return returnValue

    
    def isOfType(self, handle):
        upcastSelf = self
        returnValue = libpandaexpress._inPKoxtnFKt(upcastSelf.this, handle.this)
        return returnValue

    
    def isExactType(self, handle):
        upcastSelf = self
        returnValue = libpandaexpress._inPKoxt7Xzz(upcastSelf.this, handle.this)
        return returnValue

    
    def getRefCount(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPKoxtP11_(upcastSelf.this)
        return returnValue

    
    def ref(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPKoxtaS5_(upcastSelf.this)
        return returnValue

    
    def unref(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPKoxtwyVy(upcastSelf.this)
        return returnValue

    
    def testRefCountIntegrity(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToReferenceCount()
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
            return self._GraphicsOutput__overloaded_saveScreenshotDefault_ptrGraphicsOutput(*_args)
        elif numArgs == 1:
            return self._GraphicsOutput__overloaded_saveScreenshotDefault_ptrGraphicsOutput_atomicstring(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def makeDisplayRegion(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._GraphicsOutput__overloaded_makeDisplayRegion_ptrGraphicsOutput(*_args)
        elif numArgs == 4:
            return self._GraphicsOutput__overloaded_makeDisplayRegion_ptrGraphicsOutput_float_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 4 '


