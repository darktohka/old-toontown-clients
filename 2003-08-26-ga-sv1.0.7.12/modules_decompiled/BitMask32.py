# File: B (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import FFIExternalObject

class BitMask32(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _BitMask32__overloaded_constructor(self):
        self.this = libpanda._inPelboTPkW()
        self.userManagesMemory = 1

    
    def _BitMask32__overloaded_constructor_ptrConstBitMask32(self, copy):
        self.this = libpanda._inPelboRYCg(copy.this)
        self.userManagesMemory = 1

    
    def _BitMask32__overloaded_constructor_longUnsignedlongint(self, initValue):
        self.this = libpanda._inPelboUEq5(initValue)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPelbo7umd:
            libpanda._inPelbo7umd(self.this)
        

    
    def allOn():
        returnValue = libpanda._inPelbooN5O()
        returnObject = BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    allOn = staticmethod(allOn)
    
    def allOff():
        returnValue = libpanda._inPelboLnqL()
        returnObject = BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    allOff = staticmethod(allOff)
    
    def lowerOn(onBits):
        returnValue = libpanda._inPelbosC9k(onBits)
        returnObject = BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    lowerOn = staticmethod(lowerOn)
    
    def bit(index):
        returnValue = libpanda._inPelboQD4A(index)
        returnObject = BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    bit = staticmethod(bit)
    
    def getClassType():
        returnValue = libpanda._inPelbo_o_7()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def assign(self, copy):
        returnValue = libpanda._inPelboGa6b(self.this, copy.this)
        returnObject = BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getNumBits(self):
        returnValue = libpanda._inPelboC7dD(self.this)
        return returnValue

    
    def getBit(self, index):
        returnValue = libpanda._inPelbou5vi(self.this, index)
        return returnValue

    
    def setBit(self, index):
        returnValue = libpanda._inPelboHDr_(self.this, index)
        return returnValue

    
    def clearBit(self, index):
        returnValue = libpanda._inPelbo1JjI(self.this, index)
        return returnValue

    
    def setBitTo(self, index, value):
        returnValue = libpanda._inPelboU2qQ(self.this, index, value)
        return returnValue

    
    def isZero(self):
        returnValue = libpanda._inPelboEmKJ(self.this)
        return returnValue

    
    def extract(self, lowBit, size):
        returnValue = libpanda._inPelboLfUb(self.this, lowBit, size)
        return returnValue

    
    def store(self, value, lowBit, size):
        returnValue = libpanda._inPelbo_V11(self.this, value, lowBit, size)
        return returnValue

    
    def getWord(self):
        returnValue = libpanda._inPelbo2r65(self.this)
        return returnValue

    
    def setWord(self, value):
        returnValue = libpanda._inPelbobcJe(self.this, value)
        return returnValue

    
    def invertInPlace(self):
        returnValue = libpanda._inPelbo8MCN(self.this)
        return returnValue

    
    def clear(self):
        returnValue = libpanda._inPelbo6nVZ(self.this)
        return returnValue

    
    def output(self, out):
        returnValue = libpanda._inPelbobmsC(self.this, out.this)
        return returnValue

    
    def _BitMask32__overloaded_outputBinary_ptrConstBitMask32_ptrOstream_int(self, out, spacesEvery):
        returnValue = libpanda._inPelboKv4A(self.this, out.this, spacesEvery)
        return returnValue

    
    def _BitMask32__overloaded_outputBinary_ptrConstBitMask32_ptrOstream(self, out):
        returnValue = libpanda._inPelboStFS(self.this, out.this)
        return returnValue

    
    def _BitMask32__overloaded_outputHex_ptrConstBitMask32_ptrOstream_int(self, out, spacesEvery):
        returnValue = libpanda._inPelbo6eyU(self.this, out.this, spacesEvery)
        return returnValue

    
    def _BitMask32__overloaded_outputHex_ptrConstBitMask32_ptrOstream(self, out):
        returnValue = libpanda._inPelboTBFt(self.this, out.this)
        return returnValue

    
    def _BitMask32__overloaded_write_ptrConstBitMask32_ptrOstream_int(self, out, indentLevel):
        returnValue = libpanda._inPelbo_J_l(self.this, out.this, indentLevel)
        return returnValue

    
    def _BitMask32__overloaded_write_ptrConstBitMask32_ptrOstream(self, out):
        returnValue = libpanda._inPelboAgGS(self.this, out.this)
        return returnValue

    
    def eq(self, other):
        returnValue = libpanda._inPelbo7n_q(self.this, other.this)
        return returnValue

    
    def ne(self, other):
        returnValue = libpanda._inPelbowHmZ(self.this, other.this)
        return returnValue

    
    def lessThan(self, other):
        returnValue = libpanda._inPelboHQ7z(self.this, other.this)
        return returnValue

    
    def compareTo(self, other):
        returnValue = libpanda._inPelboTmzz(self.this, other.this)
        return returnValue

    
    def __and__(self, other):
        returnValue = libpanda._inPelboDAId(self.this, other.this)
        returnObject = BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __or__(self, other):
        returnValue = libpanda._inPelboRQzk(self.this, other.this)
        returnObject = BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __xor__(self, other):
        returnValue = libpanda._inPelboMA5_(self.this, other.this)
        returnObject = BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def bitwiseNot(self):
        returnValue = libpanda._inPelboE12A(self.this)
        returnObject = BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __lshift__(self, shift):
        returnValue = libpanda._inPelboUz1Y(self.this, shift)
        returnObject = BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __rshift__(self, shift):
        returnValue = libpanda._inPelboeDOd(self.this, shift)
        returnObject = BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __iand__(self, other):
        returnValue = libpanda._inPelboFdwQ(self.this, other.this)
        return self

    
    def __ior__(self, other):
        returnValue = libpanda._inPelbo6sdY(self.this, other.this)
        return self

    
    def __ixor__(self, other):
        returnValue = libpanda._inPelbo_cjz(self.this, other.this)
        return self

    
    def __ilshift__(self, shift):
        returnValue = libpanda._inPelbozBO2(self.this, shift)
        return self

    
    def __irshift__(self, shift):
        returnValue = libpanda._inPelbo9xn6(self.this, shift)
        return self

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._BitMask32__overloaded_constructor()
        elif numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._BitMask32__overloaded_constructor_longUnsignedlongint(_args[0])
            elif isinstance(_args[0], BitMask32):
                return self._BitMask32__overloaded_constructor_ptrConstBitMask32(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <BitMask32> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def outputBinary(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                return self._BitMask32__overloaded_outputBinary_ptrConstBitMask32_ptrOstream(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        elif numArgs == 2:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                if isinstance(_args[1], types.IntType):
                    return self._BitMask32__overloaded_outputBinary_ptrConstBitMask32_ptrOstream_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def write(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                return self._BitMask32__overloaded_write_ptrConstBitMask32_ptrOstream(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        elif numArgs == 2:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                if isinstance(_args[1], types.IntType):
                    return self._BitMask32__overloaded_write_ptrConstBitMask32_ptrOstream_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def outputHex(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                return self._BitMask32__overloaded_outputHex_ptrConstBitMask32_ptrOstream(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        elif numArgs == 2:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                if isinstance(_args[1], types.IntType):
                    return self._BitMask32__overloaded_outputHex_ptrConstBitMask32_ptrOstream_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


