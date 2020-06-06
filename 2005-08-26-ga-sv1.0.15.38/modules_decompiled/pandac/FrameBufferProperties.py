# File: F (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject

class FrameBufferProperties(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    FMDoubleBuffer = 2
    FMDepth = 32
    FMSingleBuffer = 0
    FMIndex = 1
    FMAlpha = 16
    FMBuffer = 6
    FMTripleBuffer = 4
    FMStencil = 64
    FMHardware = 1024
    FMSoftware = 512
    FMRgba = 16
    FMRgb = 0
    FMStereo = 256
    FMMultisample = 128
    FMAccum = 8
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _FrameBufferProperties__overloaded_constructor(self):
        self.this = libpanda._inPO9cY0P03()
        self.userManagesMemory = 1

    
    def _FrameBufferProperties__overloaded_constructor_ptrConstFrameBufferProperties(self, copy):
        self.this = libpanda._inPO9cYOlPt(copy.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPO9cY7WOg:
            libpanda._inPO9cY7WOg(self.this)
        

    
    def getDefault():
        returnValue = libpanda._inPO9cYFGOb()
        returnObject = FrameBufferProperties(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getDefault = staticmethod(getDefault)
    
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
        returnValue = libpanda._inPO9cYiGu_(self.this, other.this)
        return returnValue

    
    def clear(self):
        returnValue = libpanda._inPO9cYfz7q(self.this)
        return returnValue

    
    def isAnySpecified(self):
        returnValue = libpanda._inPO9cY5Lag(self.this)
        return returnValue

    
    def setFrameBufferMode(self, frameBufferMode):
        returnValue = libpanda._inPO9cYXX9l(self.this, frameBufferMode)
        return returnValue

    
    def getFrameBufferMode(self):
        returnValue = libpanda._inPO9cYOUkc(self.this)
        return returnValue

    
    def hasFrameBufferMode(self):
        returnValue = libpanda._inPO9cYue4p(self.this)
        return returnValue

    
    def clearFrameBufferMode(self):
        returnValue = libpanda._inPO9cYO0YH(self.this)
        return returnValue

    
    def isSingleBuffered(self):
        returnValue = libpanda._inPO9cYWlX5(self.this)
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
        returnValue = libpanda._inPO9cYgD26(self.this, colorBits)
        return returnValue

    
    def getColorBits(self):
        returnValue = libpanda._inPO9cYp9ex(self.this)
        return returnValue

    
    def hasColorBits(self):
        returnValue = libpanda._inPO9cYB7y_(self.this)
        return returnValue

    
    def clearColorBits(self):
        returnValue = libpanda._inPO9cYCy05(self.this)
        return returnValue

    
    def setAlphaBits(self, alphaBits):
        returnValue = libpanda._inPO9cYjyyk(self.this, alphaBits)
        return returnValue

    
    def getAlphaBits(self):
        returnValue = libpanda._inPO9cYYuZb(self.this)
        return returnValue

    
    def hasAlphaBits(self):
        returnValue = libpanda._inPO9cYAUto(self.this)
        return returnValue

    
    def clearAlphaBits(self):
        returnValue = libpanda._inPO9cY7UBu(self.this)
        return returnValue

    
    def setStencilBits(self, stencilBits):
        returnValue = libpanda._inPO9cYwbci(self.this, stencilBits)
        return returnValue

    
    def getStencilBits(self):
        returnValue = libpanda._inPO9cYCuvJ(self.this)
        return returnValue

    
    def hasStencilBits(self):
        returnValue = libpanda._inPO9cYqQEX(self.this)
        return returnValue

    
    def clearStencilBits(self):
        returnValue = libpanda._inPO9cYNwAv(self.this)
        return returnValue

    
    def setMultisamples(self, multisamples):
        returnValue = libpanda._inPO9cY6_qN(self.this, multisamples)
        return returnValue

    
    def getMultisamples(self):
        returnValue = libpanda._inPO9cYSH90(self.this)
        return returnValue

    
    def hasMultisamples(self):
        returnValue = libpanda._inPO9cY78QC(self.this)
        return returnValue

    
    def clearMultisamples(self):
        returnValue = libpanda._inPO9cY9kEG(self.this)
        return returnValue

    
    def addProperties(self, other):
        returnValue = libpanda._inPO9cYHaxr(self.this, other.this)
        return returnValue

    
    def output(self, out):
        returnValue = libpanda._inPO9cYCzSe(self.this, out.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._FrameBufferProperties__overloaded_constructor(*_args)
        elif numArgs == 1:
            return self._FrameBufferProperties__overloaded_constructor_ptrConstFrameBufferProperties(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


