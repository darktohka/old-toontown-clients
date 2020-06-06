# File: C (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import RenderAttrib

class ColorBlendAttrib(RenderAttrib.RenderAttrib, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    MMax = 5
    MAdd = 1
    MNone = 0
    MSubtract = 2
    MInvSubtract = 3
    MMin = 4
    OIncomingColor = 2
    OOneMinusConstantColor = 11
    OOneMinusFbufferAlpha = 9
    OIncomingColorSaturate = 14
    OOneMinusIncomingColor = 3
    OOneMinusConstantAlpha = 13
    OConstantColor = 10
    OConstantAlpha = 12
    OIncomingAlpha = 6
    OFbufferAlpha = 8
    OOneMinusFbufferColor = 5
    OOne = 1
    OOneMinusIncomingAlpha = 7
    OZero = 0
    OFbufferColor = 4
    
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
        if libpanda and libpanda._inPnJyot6Br:
            libpanda._inPnJyot6Br(self.this)
        

    
    def makeOff():
        returnValue = libpanda._inPnJyo5AXJ()
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    makeOff = staticmethod(makeOff)
    
    def _ColorBlendAttrib__overloaded_make___enum__Mode(mode):
        returnValue = libpanda._inPnJyo5Fac(mode)
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _ColorBlendAttrib__overloaded_make___enum__Mode = staticmethod(_ColorBlendAttrib__overloaded_make___enum__Mode)
    
    def _ColorBlendAttrib__overloaded_make___enum__Mode___enum__Operand___enum__Operand_ptrConstLVecBase4f(mode, a, b, color):
        returnValue = libpanda._inPnJyo_Hc8(mode, a, b, color.this)
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _ColorBlendAttrib__overloaded_make___enum__Mode___enum__Operand___enum__Operand_ptrConstLVecBase4f = staticmethod(_ColorBlendAttrib__overloaded_make___enum__Mode___enum__Operand___enum__Operand_ptrConstLVecBase4f)
    
    def _ColorBlendAttrib__overloaded_make___enum__Mode___enum__Operand___enum__Operand(mode, a, b):
        returnValue = libpanda._inPnJyoVZIK(mode, a, b)
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _ColorBlendAttrib__overloaded_make___enum__Mode___enum__Operand___enum__Operand = staticmethod(_ColorBlendAttrib__overloaded_make___enum__Mode___enum__Operand___enum__Operand)
    
    def involvesConstantColor(operand):
        returnValue = libpanda._inPnJyoZuVD(operand)
        return returnValue

    involvesConstantColor = staticmethod(involvesConstantColor)
    
    def getClassType():
        returnValue = libpanda._inPnJyodCAT()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def getMode(self):
        returnValue = libpanda._inPnJyoVa3Z(self.this)
        return returnValue

    
    def getOperandA(self):
        returnValue = libpanda._inPnJyo2xBv(self.this)
        return returnValue

    
    def getOperandB(self):
        returnValue = libpanda._inPnJyo2oPw(self.this)
        return returnValue

    
    def getColor(self):
        returnValue = libpanda._inPnJyolK1Z(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def make(*_args):
        numArgs = len(_args)
        if numArgs == 1:
            return ColorBlendAttrib._ColorBlendAttrib__overloaded_make___enum__Mode(*_args)
        elif numArgs == 3:
            return ColorBlendAttrib._ColorBlendAttrib__overloaded_make___enum__Mode___enum__Operand___enum__Operand(*_args)
        elif numArgs == 4:
            return ColorBlendAttrib._ColorBlendAttrib__overloaded_make___enum__Mode___enum__Operand___enum__Operand_ptrConstLVecBase4f(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 4 '

    make = staticmethod(make)

