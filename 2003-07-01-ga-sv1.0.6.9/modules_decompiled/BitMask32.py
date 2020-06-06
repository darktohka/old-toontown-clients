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
        self.this = libpanda._inPelbonVQd()
        self.userManagesMemory = 1

    
    def _BitMask32__overloaded_constructor_ptrConstBitMask32(self, copy):
        self.this = libpanda._inPelbo7gMO(copy.this)
        self.userManagesMemory = 1

    
    def _BitMask32__overloaded_constructor_unsignedint(self, initValue):
        self.this = libpanda._inPelbo3eoo(initValue)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPelbo_fwA:
            libpanda._inPelbo_fwA(self.this)
        

    
    def allOn():
        returnValue = libpanda._inPelboRObZ()
        returnObject = BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    allOn = staticmethod(allOn)
    
    def allOff():
        returnValue = libpanda._inPelbojEzX()
        returnObject = BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    allOff = staticmethod(allOff)
    
    def lowerOn(onBits):
        returnValue = libpanda._inPelboLQak(onBits)
        returnObject = BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    lowerOn = staticmethod(lowerOn)
    
    def bit(index):
        returnValue = libpanda._inPelbosGZS(index)
        returnObject = BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    bit = staticmethod(bit)
    
    def getClassType():
        returnValue = libpanda._inPelbor17v()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def assign(self, copy):
        returnValue = libpanda._inPelboCaYM(self.this, copy.this)
        returnObject = BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getNumBits(self):
        returnValue = libpanda._inPelbo0nrT(self.this)
        return returnValue

    
    def getBit(self, index):
        returnValue = libpanda._inPelboe0SD(self.this, index)
        return returnValue

    
    def setBit(self, index):
        returnValue = libpanda._inPelboc8Sx(self.this, index)
        return returnValue

    
    def clearBit(self, index):
        returnValue = libpanda._inPelboeFOW(self.this, index)
        return returnValue

    
    def setBitTo(self, index, value):
        returnValue = libpanda._inPelboeoR6(self.this, index, value)
        return returnValue

    
    def isZero(self):
        returnValue = libpanda._inPelbo2yi2(self.this)
        return returnValue

    
    def extract(self, lowBit, size):
        returnValue = libpanda._inPelbouCn_(self.this, lowBit, size)
        return returnValue

    
    def store(self, value, lowBit, size):
        returnValue = libpanda._inPelboSp78(self.this, value, lowBit, size)
        return returnValue

    
    def getWord(self):
        returnValue = libpanda._inPelboiD5O(self.this)
        return returnValue

    
    def setWord(self, value):
        returnValue = libpanda._inPelboERWc(self.this, value)
        return returnValue

    
    def invertInPlace(self):
        returnValue = libpanda._inPelboKld4(self.this)
        return returnValue

    
    def clear(self):
        returnValue = libpanda._inPelboYEpe(self.this)
        return returnValue

    
    def output(self, out):
        returnValue = libpanda._inPelbo2eSz(self.this, out.this)
        return returnValue

    
    def _BitMask32__overloaded_outputBinary_ptrConstBitMask32_ptrOstream_int(self, out, spacesEvery):
        returnValue = libpanda._inPelboAOXy(self.this, out.this, spacesEvery)
        return returnValue

    
    def _BitMask32__overloaded_outputBinary_ptrConstBitMask32_ptrOstream(self, out):
        returnValue = libpanda._inPelbo9596(self.this, out.this)
        return returnValue

    
    def _BitMask32__overloaded_outputHex_ptrConstBitMask32_ptrOstream_int(self, out, spacesEvery):
        returnValue = libpanda._inPelboHJUc(self.this, out.this, spacesEvery)
        return returnValue

    
    def _BitMask32__overloaded_outputHex_ptrConstBitMask32_ptrOstream(self, out):
        returnValue = libpanda._inPelbo6TeI(self.this, out.this)
        return returnValue

    
    def _BitMask32__overloaded_write_ptrConstBitMask32_ptrOstream_int(self, out, indentLevel):
        returnValue = libpanda._inPelboA_7k(self.this, out.this, indentLevel)
        return returnValue

    
    def _BitMask32__overloaded_write_ptrConstBitMask32_ptrOstream(self, out):
        returnValue = libpanda._inPelbo4vA7(self.this, out.this)
        return returnValue

    
    def eq(self, other):
        returnValue = libpanda._inPelbomOwJ(self.this, other.this)
        return returnValue

    
    def ne(self, other):
        returnValue = libpanda._inPelbok_DB(self.this, other.this)
        return returnValue

    
    def lessThan(self, other):
        returnValue = libpanda._inPelboi58v(self.this, other.this)
        return returnValue

    
    def compareTo(self, other):
        returnValue = libpanda._inPelboo_4v(self.this, other.this)
        return returnValue

    
    def __and__(self, other):
        returnValue = libpanda._inPelbogBiE(self.this, other.this)
        returnObject = BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __or__(self, other):
        returnValue = libpanda._inPelbop5Yo(self.this, other.this)
        returnObject = BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __xor__(self, other):
        returnValue = libpanda._inPelbokh7V(self.this, other.this)
        returnObject = BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def bitwiseNot(self):
        returnValue = libpanda._inPelbo1pXy(self.this)
        returnObject = BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __lshift__(self, shift):
        returnValue = libpanda._inPelbo9uW_(self.this, shift)
        returnObject = BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __rshift__(self, shift):
        returnValue = libpanda._inPelbo62jA(self.this, shift)
        returnObject = BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __iand__(self, other):
        returnValue = libpanda._inPelboRRDL(self.this, other.this)
        return self

    
    def __ior__(self, other):
        returnValue = libpanda._inPelboYJ5u(self.this, other.this)
        return self

    
    def __ixor__(self, other):
        returnValue = libpanda._inPelbodxcc(self.this, other.this)
        return self

    
    def __ilshift__(self, shift):
        returnValue = libpanda._inPelboM4Dt(self.this, shift)
        return self

    
    def __irshift__(self, shift):
        returnValue = libpanda._inPelboJwQv(self.this, shift)
        return self

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._BitMask32__overloaded_constructor()
        elif numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._BitMask32__overloaded_constructor_unsignedint(_args[0])
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


