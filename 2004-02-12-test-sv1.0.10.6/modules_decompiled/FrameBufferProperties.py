# File: F (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import FFIExternalObject

class FrameBufferProperties(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    FMDoubleBuffer = 2
    FMDepth = 32
    FMSingleBuffer = 0
    FMIndex = 1
    FMAlpha = 16
    FMLuminance = 512
    FMTripleBuffer = 4
    FMStencil = 64
    FMRgba = 0
    FMRgb = 0
    FMStereo = 256
    FMMultisample = 128
    FMAccum = 8
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _FrameBufferProperties__overloaded_constructor(self):
        self.this = libpanda._inPO9cY1P03()
        self.userManagesMemory = 1

    
    def _FrameBufferProperties__overloaded_constructor_ptrConstFrameBufferProperties(self, copy):
        self.this = libpanda._inPO9cYBlPt(copy.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPO9cY6WOg:
            libpanda._inPO9cY6WOg(self.this)
        

    
    def assign(self, copy):
        returnValue = libpanda._inPO9cYLWDE(self.this, copy.this)
        returnObject = FrameBufferProperties(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def eq(self, other):
        returnValue = libpanda._inPO9cY_xuw(self.this, other.this)
        return returnValue

    
    def ne(self, other):
        returnValue = libpanda._inPO9cYhGu_(self.this, other.this)
        return returnValue

    
    def clear(self):
        returnValue = libpanda._inPO9cYcz7q(self.this)
        return returnValue

    
    def isAnySpecified(self):
        returnValue = libpanda._inPO9cY4Lag(self.this)
        return returnValue

    
    def setFrameBufferMode(self, frameBufferMode):
        returnValue = libpanda._inPO9cYWX9l(self.this, frameBufferMode)
        return returnValue

    
    def getFrameBufferMode(self):
        returnValue = libpanda._inPO9cYOUkc(self.this)
        return returnValue

    
    def hasFrameBufferMode(self):
        returnValue = libpanda._inPO9cYte4p(self.this)
        return returnValue

    
    def clearFrameBufferMode(self):
        returnValue = libpanda._inPO9cYO0YH(self.this)
        return returnValue

    
    def setDepthBits(self, depthBits):
        returnValue = libpanda._inPO9cY4McT(self.this, depthBits)
        return returnValue

    
    def getDepthBits(self):
        returnValue = libpanda._inPO9cY6uCK(self.this)
        return returnValue

    
    def hasDepthBits(self):
        returnValue = libpanda._inPO9cYikWX(self.this)
        return returnValue

    
    def clearDepthBits(self):
        returnValue = libpanda._inPO9cYG8mC(self.this)
        return returnValue

    
    def setColorBits(self, colorBits):
        returnValue = libpanda._inPO9cYjD26(self.this, colorBits)
        return returnValue

    
    def getColorBits(self):
        returnValue = libpanda._inPO9cYo9ex(self.this)
        return returnValue

    
    def hasColorBits(self):
        returnValue = libpanda._inPO9cYA7y_(self.this)
        return returnValue

    
    def clearColorBits(self):
        returnValue = libpanda._inPO9cYdy05(self.this)
        return returnValue

    
    def addProperties(self, other):
        returnValue = libpanda._inPO9cYEaxr(self.this, other.this)
        return returnValue

    
    def output(self, out):
        returnValue = libpanda._inPO9cYCzSe(self.this, out.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._FrameBufferProperties__overloaded_constructor()
        elif numArgs == 1:
            if isinstance(_args[0], FrameBufferProperties):
                return self._FrameBufferProperties__overloaded_constructor_ptrConstFrameBufferProperties(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <FrameBufferProperties> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


