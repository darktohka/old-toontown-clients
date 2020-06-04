# File: P (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import PandaNode

class PolylightNode(PandaNode.PandaNode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    FRANDOM = 0
    FCUSTOM = 2
    FSIN = 1
    AQUADRATIC = 1
    ALINEAR = 0
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self, name):
        self.this = libpanda._inPnJyoQvIh(name)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPnJyoJQpS:
            libpanda._inPnJyoJQpS(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPnJyoz1P9()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def enable(self):
        returnValue = libpanda._inPnJyoJ7oX(self.this)
        return returnValue

    
    def disable(self):
        returnValue = libpanda._inPnJyoqVNP(self.this)
        return returnValue

    
    def _PolylightNode__overloaded_setPos_ptrPolylightNode_ptrLVecBase3f(self, position):
        returnValue = libpanda._inPnJyo5EU0(self.this, position.this)
        return returnValue

    
    def _PolylightNode__overloaded_setPos_ptrPolylightNode_float_float_float(self, x, y, z):
        returnValue = libpanda._inPnJyol5pP(self.this, x, y, z)
        return returnValue

    
    def getPos(self):
        returnValue = libpanda._inPnJyo6Ddh(self.this)
        import VBase3
        returnObject = VBase3.VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _PolylightNode__overloaded_setColor_ptrPolylightNode_ptrLVecBase4f(self, color):
        returnValue = libpanda._inPnJyolWcS(self.this, color.this)
        return returnValue

    
    def _PolylightNode__overloaded_setColor_ptrPolylightNode_float_float_float(self, r, g, b):
        returnValue = libpanda._inPnJyorXKS(self.this, r, g, b)
        return returnValue

    
    def getColor(self):
        returnValue = libpanda._inPnJyorYAt(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getColorScenegraph(self):
        returnValue = libpanda._inPnJyos21Z(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setRadius(self, r):
        returnValue = libpanda._inPnJyojENz(self.this, r)
        return returnValue

    
    def getRadius(self):
        returnValue = libpanda._inPnJyomN_F(self.this)
        return returnValue

    
    def setAttenuation(self, type):
        returnValue = libpanda._inPnJyoNzMK(self.this, type)
        return returnValue

    
    def getAttenuation(self):
        returnValue = libpanda._inPnJyogukW(self.this)
        return returnValue

    
    def setA0(self, a0):
        returnValue = libpanda._inPnJyo6AyF(self.this, a0)
        return returnValue

    
    def setA1(self, a1):
        returnValue = libpanda._inPnJyoqeGG(self.this, a1)
        return returnValue

    
    def setA2(self, a2):
        returnValue = libpanda._inPnJyoa8aG(self.this, a2)
        return returnValue

    
    def getA0(self):
        returnValue = libpanda._inPnJyofYRN(self.this)
        return returnValue

    
    def getA1(self):
        returnValue = libpanda._inPnJyov_lN(self.this)
        return returnValue

    
    def getA2(self):
        returnValue = libpanda._inPnJyo_c4N(self.this)
        return returnValue

    
    def flickerOn(self):
        returnValue = libpanda._inPnJyo6XFe(self.this)
        return returnValue

    
    def flickerOff(self):
        returnValue = libpanda._inPnJyoTEHE(self.this)
        return returnValue

    
    def isFlickering(self):
        returnValue = libpanda._inPnJyoLCTy(self.this)
        return returnValue

    
    def setFlickerType(self, type):
        returnValue = libpanda._inPnJyorALY(self.this, type)
        return returnValue

    
    def getFlickerType(self):
        returnValue = libpanda._inPnJyol3py(self.this)
        return returnValue

    
    def setOffset(self, offset):
        returnValue = libpanda._inPnJyopyo8(self.this, offset)
        return returnValue

    
    def getOffset(self):
        returnValue = libpanda._inPnJyoy2YP(self.this)
        return returnValue

    
    def setScale(self, scale):
        returnValue = libpanda._inPnJyo5u_H(self.this, scale)
        return returnValue

    
    def getScale(self):
        returnValue = libpanda._inPnJyoriye(self.this)
        return returnValue

    
    def setStepSize(self, step):
        returnValue = libpanda._inPnJyoN2Pf(self.this, step)
        return returnValue

    
    def getStepSize(self):
        returnValue = libpanda._inPnJyoCj7S(self.this)
        return returnValue

    
    def setFreq(self, f):
        returnValue = libpanda._inPnJyo_d8J(self.this, f)
        return returnValue

    
    def getFreq(self):
        returnValue = libpanda._inPnJyopD4C(self.this)
        return returnValue

    
    def eq(self, other):
        returnValue = libpanda._inPnJyoE3DF(self.this, other.this)
        return returnValue

    
    def ne(self, other):
        returnValue = libpanda._inPnJyo4ihE(self.this, other.this)
        return returnValue

    
    def lessThan(self, other):
        returnValue = libpanda._inPnJyotfyl(self.this, other.this)
        return returnValue

    
    def compareTo(self, other):
        returnValue = libpanda._inPnJyo2MS5(self.this, other.this)
        return returnValue

    
    def isEnabled(self):
        returnValue = libpanda._inPnJyohYfZ(self.this)
        return returnValue

    
    def setPos(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._PolylightNode__overloaded_setPos_ptrPolylightNode_ptrLVecBase3f(*_args)
        elif numArgs == 3:
            return self._PolylightNode__overloaded_setPos_ptrPolylightNode_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '

    
    def setColor(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._PolylightNode__overloaded_setColor_ptrPolylightNode_ptrLVecBase4f(*_args)
        elif numArgs == 3:
            return self._PolylightNode__overloaded_setColor_ptrPolylightNode_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '


