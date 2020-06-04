# File: H (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject

class HTTPEntityTag(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _HTTPEntityTag__overloaded_constructor(self):
        self.this = libpandaexpress._inP2KOd4tMA()
        self.userManagesMemory = 1

    
    def _HTTPEntityTag__overloaded_constructor_ptrConstHTTPEntityTag(self, copy):
        self.this = libpandaexpress._inP2KOdRDIw(copy.this)
        self.userManagesMemory = 1

    
    def _HTTPEntityTag__overloaded_constructor_atomicstring(self, text):
        self.this = libpandaexpress._inP2KOd6Xv8(text)
        self.userManagesMemory = 1

    
    def _HTTPEntityTag__overloaded_constructor_bool_atomicstring(self, weak, tag):
        self.this = libpandaexpress._inP2KOdY_ii(weak, tag)
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
        returnValue = libpandaexpress._inP2KOdt54_(self.this)
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
        returnValue = libpandaexpress._inP2KOdQ6L5(self.this, other.this)
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
            return self._HTTPEntityTag__overloaded_constructor()
        elif numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._HTTPEntityTag__overloaded_constructor_atomicstring(_args[0])
            elif isinstance(_args[0], HTTPEntityTag):
                return self._HTTPEntityTag__overloaded_constructor_ptrConstHTTPEntityTag(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <HTTPEntityTag> '
        elif numArgs == 2:
            if isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.StringType):
                    return self._HTTPEntityTag__overloaded_constructor_bool_atomicstring(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.StringType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '


