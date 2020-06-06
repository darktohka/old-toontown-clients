# File: B (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject

class BitMask32(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _BitMask32__overloaded_constructor(self):
        self.this = libpanda._inPflboTPkW()
        self.userManagesMemory = 1

    
    def _BitMask32__overloaded_constructor_ptrConstBitMask32(self, copy):
        self.this = libpanda._inPflboWYCg(copy.this)
        self.userManagesMemory = 1

    
    def _BitMask32__overloaded_constructor_longUnsignedlongint(self, initValue):
        self.this = libpanda._inPflboVEq5(initValue)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPflbo7umd:
            libpanda._inPflbo7umd(self.this)
        

    
    def allOn():
        returnValue = libpanda._inPflbooN5O()
        returnObject = BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    allOn = staticmethod(allOn)
    
    def allOff():
        returnValue = libpanda._inPflboLnqL()
        returnObject = BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    allOff = staticmethod(allOff)
    
    def lowerOn(onBits):
        returnValue = libpanda._inPflbovC9k(onBits)
        returnObject = BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    lowerOn = staticmethod(lowerOn)
    
    def bit(index):
        returnValue = libpanda._inPflboQD4A(index)
        returnObject = BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    bit = staticmethod(bit)
    
    def range(lowBit, size):
        returnValue = libpanda._inPflbozwm_(lowBit, size)
        returnObject = BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    range = staticmethod(range)
    
    def getClassType():
        returnValue = libpanda._inPflbo_o_7()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def assign(self, copy):
        returnValue = libpanda._inPflboGa6b(self.this, copy.this)
        returnObject = BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getNumBits(self):
        returnValue = libpanda._inPflboC7dD(self.this)
        return returnValue

    
    def getBit(self, index):
        returnValue = libpanda._inPflbov5vi(self.this, index)
        return returnValue

    
    def setBit(self, index):
        returnValue = libpanda._inPflboGDr_(self.this, index)
        return returnValue

    
    def clearBit(self, index):
        returnValue = libpanda._inPflbo1JjI(self.this, index)
        return returnValue

    
    def setBitTo(self, index, value):
        returnValue = libpanda._inPflboU2qQ(self.this, index, value)
        return returnValue

    
    def isZero(self):
        returnValue = libpanda._inPflboEmKJ(self.this)
        return returnValue

    
    def extract(self, lowBit, size):
        returnValue = libpanda._inPflboLfUb(self.this, lowBit, size)
        return returnValue

    
    def store(self, value, lowBit, size):
        returnValue = libpanda._inPflbo_V11(self.this, value, lowBit, size)
        return returnValue

    
    def getWord(self):
        returnValue = libpanda._inPflbo3r65(self.this)
        return returnValue

    
    def setWord(self, value):
        returnValue = libpanda._inPflbobcJe(self.this, value)
        return returnValue

    
    def invertInPlace(self):
        returnValue = libpanda._inPflbo8MCN(self.this)
        return returnValue

    
    def clear(self):
        returnValue = libpanda._inPflbo6nVZ(self.this)
        return returnValue

    
    def output(self, out):
        returnValue = libpanda._inPflbobmsC(self.this, out.this)
        return returnValue

    
    def _BitMask32__overloaded_outputBinary_ptrConstBitMask32_ptrOstream_int(self, out, spacesEvery):
        returnValue = libpanda._inPflboKv4A(self.this, out.this, spacesEvery)
        return returnValue

    
    def _BitMask32__overloaded_outputBinary_ptrConstBitMask32_ptrOstream(self, out):
        returnValue = libpanda._inPflboStFS(self.this, out.this)
        return returnValue

    
    def _BitMask32__overloaded_outputHex_ptrConstBitMask32_ptrOstream_int(self, out, spacesEvery):
        returnValue = libpanda._inPflbo6eyU(self.this, out.this, spacesEvery)
        return returnValue

    
    def _BitMask32__overloaded_outputHex_ptrConstBitMask32_ptrOstream(self, out):
        returnValue = libpanda._inPflboSBFt(self.this, out.this)
        return returnValue

    
    def _BitMask32__overloaded_write_ptrConstBitMask32_ptrOstream_int(self, out, indentLevel):
        returnValue = libpanda._inPflbo_J_l(self.this, out.this, indentLevel)
        return returnValue

    
    def _BitMask32__overloaded_write_ptrConstBitMask32_ptrOstream(self, out):
        returnValue = libpanda._inPflboAgGS(self.this, out.this)
        return returnValue

    
    def eq(self, other):
        returnValue = libpanda._inPflbo8n_q(self.this, other.this)
        return returnValue

    
    def ne(self, other):
        returnValue = libpanda._inPflbowHmZ(self.this, other.this)
        return returnValue

    
    def lessThan(self, other):
        returnValue = libpanda._inPflboGQ7z(self.this, other.this)
        return returnValue

    
    def compareTo(self, other):
        returnValue = libpanda._inPflboSmzz(self.this, other.this)
        return returnValue

    
    def __and__(self, other):
        returnValue = libpanda._inPflboDAId(self.this, other.this)
        returnObject = BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __or__(self, other):
        returnValue = libpanda._inPflboQQzk(self.this, other.this)
        returnObject = BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __xor__(self, other):
        returnValue = libpanda._inPflboLA5_(self.this, other.this)
        returnObject = BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def bitwiseNot(self):
        returnValue = libpanda._inPflboE12A(self.this)
        returnObject = BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __lshift__(self, shift):
        returnValue = libpanda._inPflboUz1Y(self.this, shift)
        returnObject = BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __rshift__(self, shift):
        returnValue = libpanda._inPflboeDOd(self.this, shift)
        returnObject = BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __iand__(self, other):
        returnValue = libpanda._inPflboFdwQ(self.this, other.this)
        return self

    
    def __ior__(self, other):
        returnValue = libpanda._inPflbo6sdY(self.this, other.this)
        return self

    
    def __ixor__(self, other):
        returnValue = libpanda._inPflbo9cjz(self.this, other.this)
        return self

    
    def __ilshift__(self, shift):
        returnValue = libpanda._inPflbowBO2(self.this, shift)
        return self

    
    def __irshift__(self, shift):
        returnValue = libpanda._inPflbo6xn6(self.this, shift)
        return self

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._BitMask32__overloaded_constructor(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._BitMask32__overloaded_constructor_longUnsignedlongint(*_args)
            
            if isinstance(_args[0], BitMask32):
                return self._BitMask32__overloaded_constructor_ptrConstBitMask32(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <BitMask32> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def outputBinary(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._BitMask32__overloaded_outputBinary_ptrConstBitMask32_ptrOstream(*_args)
        elif numArgs == 2:
            return self._BitMask32__overloaded_outputBinary_ptrConstBitMask32_ptrOstream_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def write(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._BitMask32__overloaded_write_ptrConstBitMask32_ptrOstream(*_args)
        elif numArgs == 2:
            return self._BitMask32__overloaded_write_ptrConstBitMask32_ptrOstream_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def outputHex(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._BitMask32__overloaded_outputHex_ptrConstBitMask32_ptrOstream(*_args)
        elif numArgs == 2:
            return self._BitMask32__overloaded_outputHex_ptrConstBitMask32_ptrOstream_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


