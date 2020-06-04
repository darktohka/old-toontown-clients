# File: E (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject

class EventParameter(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _EventParameter__overloaded_constructor(self):
        self.this = libpandaexpress._inPekxoDmAg()
        self.userManagesMemory = 1

    
    def _EventParameter__overloaded_constructor_ptrConstEventParameter(self, copy):
        self.this = libpandaexpress._inPekxouMqR(copy.this)
        self.userManagesMemory = 1

    
    def _EventParameter__overloaded_constructor_ptrConstTypedReferenceCount(self, ptr):
        self.this = libpandaexpress._inPekxoqTUl(ptr.this)
        self.userManagesMemory = 1

    
    def _EventParameter__overloaded_constructor_atomicstring(self, value):
        self.this = libpandaexpress._inPekxofaFB(value)
        self.userManagesMemory = 1

    
    def _EventParameter__overloaded_constructor_double(self, value):
        self.this = libpandaexpress._inPekxonJZK(value)
        self.userManagesMemory = 1

    
    def _EventParameter__overloaded_constructor_int(self, value):
        self.this = libpandaexpress._inPekxouZZH(value)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inPekxokzTN:
            libpandaexpress._inPekxokzTN(self.this)
        

    
    def assign(self, copy):
        returnValue = libpandaexpress._inPekxo5fZ1(self.this, copy.this)
        returnObject = EventParameter(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def isEmpty(self):
        returnValue = libpandaexpress._inPekxobeRx(self.this)
        return returnValue

    
    def isInt(self):
        returnValue = libpandaexpress._inPekxodncs(self.this)
        return returnValue

    
    def getIntValue(self):
        returnValue = libpandaexpress._inPekxoJOzj(self.this)
        return returnValue

    
    def isDouble(self):
        returnValue = libpandaexpress._inPekxo9jXI(self.this)
        return returnValue

    
    def getDoubleValue(self):
        returnValue = libpandaexpress._inPekxo66KS(self.this)
        return returnValue

    
    def isString(self):
        returnValue = libpandaexpress._inPekxoHB1z(self.this)
        return returnValue

    
    def getStringValue(self):
        returnValue = libpandaexpress._inPekxogAhB(self.this)
        return returnValue

    
    def getPtr(self):
        returnValue = libpandaexpress._inPekxoaU2M(self.this)
        import TypedReferenceCount
        returnObject = TypedReferenceCount.TypedReferenceCount(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def output(self, out):
        returnValue = libpandaexpress._inPekxohvV2(self.this, out.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._EventParameter__overloaded_constructor()
        elif numArgs == 1:
            import TypedReferenceCount
            if isinstance(_args[0], types.IntType):
                return self._EventParameter__overloaded_constructor_int(_args[0])
            elif isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return self._EventParameter__overloaded_constructor_double(_args[0])
            elif isinstance(_args[0], types.StringType):
                return self._EventParameter__overloaded_constructor_atomicstring(_args[0])
            elif isinstance(_args[0], TypedReferenceCount.TypedReferenceCount):
                return self._EventParameter__overloaded_constructor_ptrConstTypedReferenceCount(_args[0])
            elif isinstance(_args[0], EventParameter):
                return self._EventParameter__overloaded_constructor_ptrConstEventParameter(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <types.FloatType> <types.StringType> <TypedReferenceCount.TypedReferenceCount> <EventParameter> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


