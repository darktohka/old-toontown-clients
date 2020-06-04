# File: P (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject

class PGFrameStyle(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    TGroove = 4
    TRidge = 5
    TFlat = 1
    TBevelOut = 2
    TBevelIn = 3
    TNone = 0
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _PGFrameStyle__overloaded_constructor(self):
        self.this = libpanda._inPVvimfplg()
        self.userManagesMemory = 1

    
    def _PGFrameStyle__overloaded_constructor_ptrConstPGFrameStyle(self, copy):
        self.this = libpanda._inPVvimnhUl(copy.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPVvimYC6A:
            libpanda._inPVvimYC6A(self.this)
        

    
    def assign(self, copy):
        returnValue = libpanda._inPVvimnTPY(self.this, copy.this)
        returnObject = PGFrameStyle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setType(self, type):
        returnValue = libpanda._inPVvimI8_1(self.this, type)
        return returnValue

    
    def getType(self):
        returnValue = libpanda._inPVvimeRTB(self.this)
        return returnValue

    
    def _PGFrameStyle__overloaded_setColor_ptrPGFrameStyle_ptrConstLVecBase4f(self, color):
        returnValue = libpanda._inPVvimrDgP(self.this, color.this)
        return returnValue

    
    def _PGFrameStyle__overloaded_setColor_ptrPGFrameStyle_float_float_float_float(self, r, g, b, a):
        returnValue = libpanda._inPVvimKqux(self.this, r, g, b, a)
        return returnValue

    
    def getColor(self):
        returnValue = libpanda._inPVvimarWM(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setTexture(self, texture):
        returnValue = libpanda._inPVvimiaIb(self.this, texture.this)
        return returnValue

    
    def hasTexture(self):
        returnValue = libpanda._inPVvimJRv2(self.this)
        return returnValue

    
    def getTexture(self):
        returnValue = libpanda._inPVvimWoMM(self.this)
        import Texture
        returnObject = Texture.Texture(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def clearTexture(self):
        returnValue = libpanda._inPVvimqcTv(self.this)
        return returnValue

    
    def _PGFrameStyle__overloaded_setWidth_ptrPGFrameStyle_ptrConstLVecBase2f(self, width):
        returnValue = libpanda._inPVvimIq9R(self.this, width.this)
        return returnValue

    
    def _PGFrameStyle__overloaded_setWidth_ptrPGFrameStyle_float_float(self, x, y):
        returnValue = libpanda._inPVvimhZn4(self.this, x, y)
        return returnValue

    
    def getWidth(self):
        returnValue = libpanda._inPVvimP9TS(self.this)
        import VBase2
        returnObject = VBase2.VBase2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def output(self, out):
        returnValue = libpanda._inPVvimp6gR(self.this, out.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._PGFrameStyle__overloaded_constructor(*_args)
        elif numArgs == 1:
            return self._PGFrameStyle__overloaded_constructor_ptrConstPGFrameStyle(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def setWidth(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._PGFrameStyle__overloaded_setWidth_ptrPGFrameStyle_ptrConstLVecBase2f(*_args)
        elif numArgs == 2:
            return self._PGFrameStyle__overloaded_setWidth_ptrPGFrameStyle_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setColor(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._PGFrameStyle__overloaded_setColor_ptrPGFrameStyle_ptrConstLVecBase4f(*_args)
        elif numArgs == 4:
            return self._PGFrameStyle__overloaded_setColor_ptrPGFrameStyle_float_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 4 '


