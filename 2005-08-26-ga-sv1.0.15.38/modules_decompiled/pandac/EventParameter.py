# File: E (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject

class EventParameter(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _EventParameter__overloaded_constructor(self):
        self.this = libpanda._inPfkxoEmAg()
        self.userManagesMemory = 1

    
    def _EventParameter__overloaded_constructor_ptrConstEventParameter(self, copy):
        self.this = libpanda._inPfkxouMqR(copy.this)
        self.userManagesMemory = 1

    
    def _EventParameter__overloaded_constructor_ptrConstTypedWritableReferenceCount(self, ptr):
        self.this = libpanda._inPfkxo3aRa(ptr.this)
        self.userManagesMemory = 1

    
    def _EventParameter__overloaded_constructor_atomicstring(self, value):
        self.this = libpanda._inPfkxofaFB(value)
        self.userManagesMemory = 1

    
    def _EventParameter__overloaded_constructor_double(self, value):
        self.this = libpanda._inPfkxonJZK(value)
        self.userManagesMemory = 1

    
    def _EventParameter__overloaded_constructor_int(self, value):
        self.this = libpanda._inPfkxouZZH(value)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPfkxokzTN:
            libpanda._inPfkxokzTN(self.this)
        

    
    def assign(self, copy):
        returnValue = libpanda._inPfkxo4fZ1(self.this, copy.this)
        returnObject = EventParameter(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def isEmpty(self):
        returnValue = libpanda._inPfkxoYeRx(self.this)
        return returnValue

    
    def isInt(self):
        returnValue = libpanda._inPfkxocncs(self.this)
        return returnValue

    
    def getIntValue(self):
        returnValue = libpanda._inPfkxoIOzj(self.this)
        return returnValue

    
    def isDouble(self):
        returnValue = libpanda._inPfkxo9jXI(self.this)
        return returnValue

    
    def getDoubleValue(self):
        returnValue = libpanda._inPfkxo66KS(self.this)
        return returnValue

    
    def isString(self):
        returnValue = libpanda._inPfkxoEB1z(self.this)
        return returnValue

    
    def getStringValue(self):
        returnValue = libpanda._inPfkxogAhB(self.this)
        return returnValue

    
    def getPtr(self):
        returnValue = libpanda._inPfkxoaU2M(self.this)
        import TypedWritableReferenceCount
        returnObject = TypedWritableReferenceCount.TypedWritableReferenceCount(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def output(self, out):
        returnValue = libpanda._inPfkxoevV2(self.this, out.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._EventParameter__overloaded_constructor(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._EventParameter__overloaded_constructor_int(*_args)
            
            if isinstance(_args[0], types.FloatType) and isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._EventParameter__overloaded_constructor_double(*_args)
            
            if isinstance(_args[0], types.StringType):
                return self._EventParameter__overloaded_constructor_atomicstring(*_args)
            
            import TypedWritableReferenceCount
            if isinstance(_args[0], TypedWritableReferenceCount.TypedWritableReferenceCount):
                return self._EventParameter__overloaded_constructor_ptrConstTypedWritableReferenceCount(*_args)
            
            if isinstance(_args[0], EventParameter):
                return self._EventParameter__overloaded_constructor_ptrConstEventParameter(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <types.FloatType> <types.StringType> <TypedWritableReferenceCount.TypedWritableReferenceCount> <EventParameter> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


