# File: H (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject

class HTTPEntityTag(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _HTTPEntityTag__overloaded_constructor(self):
        self.this = libpandaexpress._inP2KOd4tMA()
        self.userManagesMemory = 1

    
    def _HTTPEntityTag__overloaded_constructor_ptrConstHTTPEntityTag(self, copy):
        self.this = libpandaexpress._inP2KOdQDIw(copy.this)
        self.userManagesMemory = 1

    
    def _HTTPEntityTag__overloaded_constructor_atomicstring(self, text):
        self.this = libpandaexpress._inP2KOd5Xv8(text)
        self.userManagesMemory = 1

    
    def _HTTPEntityTag__overloaded_constructor_bool_atomicstring(self, weak, tag):
        self.this = libpandaexpress._inP2KOdZ_ii(weak, tag)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inP2KOdO7Jf:
            libpandaexpress._inP2KOdO7Jf(self.this)
        

    
    def assign(self, copy):
        returnValue = libpandaexpress._inP2KOdF2kZ(self.this, copy.this)
        returnObject = HTTPEntityTag(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def isWeak(self):
        returnValue = libpandaexpress._inP2KOds54_(self.this)
        return returnValue

    
    def getTag(self):
        returnValue = libpandaexpress._inP2KOdHG7c(self.this)
        return returnValue

    
    def getString(self):
        returnValue = libpandaexpress._inP2KOdJDGH(self.this)
        return returnValue

    
    def strongEquiv(self, other):
        returnValue = libpandaexpress._inP2KOdICzc(self.this, other.this)
        return returnValue

    
    def weakEquiv(self, other):
        returnValue = libpandaexpress._inP2KOduDMa(self.this, other.this)
        return returnValue

    
    def eq(self, other):
        returnValue = libpandaexpress._inP2KOduwLK(self.this, other.this)
        return returnValue

    
    def ne(self, other):
        returnValue = libpandaexpress._inP2KOdqnpJ(self.this, other.this)
        return returnValue

    
    def lessThan(self, other):
        returnValue = libpandaexpress._inP2KOdT6L5(self.this, other.this)
        return returnValue

    
    def compareTo(self, other):
        returnValue = libpandaexpress._inP2KOddIqM(self.this, other.this)
        return returnValue

    
    def output(self, out):
        returnValue = libpandaexpress._inP2KOdGXUH(self.this, out.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._HTTPEntityTag__overloaded_constructor(*_args)
        elif numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._HTTPEntityTag__overloaded_constructor_atomicstring(*_args)
            
            if isinstance(_args[0], HTTPEntityTag):
                return self._HTTPEntityTag__overloaded_constructor_ptrConstHTTPEntityTag(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <HTTPEntityTag> '
        elif numArgs == 2:
            return self._HTTPEntityTag__overloaded_constructor_bool_atomicstring(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '


