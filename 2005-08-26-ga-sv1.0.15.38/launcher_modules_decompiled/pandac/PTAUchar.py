# File: P (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import PointerToBaseRefCountObjvectorunsignedchar

class PTAUchar(PointerToBaseRefCountObjvectorunsignedchar.PointerToBaseRefCountObjvectorunsignedchar, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _PTAUchar__overloaded_constructor(self):
        self.this = libpandaexpress._inPKoxtPkXb()
        self.userManagesMemory = 1

    
    def _PTAUchar__overloaded_constructor_ptrConstPTAUchar(self, copy):
        self.this = libpandaexpress._inPKoxt6Txu(copy.this)
        self.userManagesMemory = 1

    
    def _PTAUchar__overloaded_constructor_unsignedint_unsignedchar(self, n, value):
        self.this = libpandaexpress._inPKoxtTmv9(n, value)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inPKoxtdEYV:
            libpandaexpress._inPKoxtdEYV(self.this)
        

    
    def emptyArray(n):
        returnValue = libpandaexpress._inPKoxtx6ks(n)
        returnObject = PTAUchar(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    emptyArray = staticmethod(emptyArray)
    
    def size(self):
        returnValue = libpandaexpress._inPKoxtZxGV(self.this)
        return returnValue

    
    def getElement(self, n):
        returnValue = libpandaexpress._inPKoxt7t3V(self.this, n)
        return returnValue

    
    def pushBack(self, x):
        returnValue = libpandaexpress._inPKoxtxVTf(self.this, x)
        return returnValue

    
    def popBack(self):
        returnValue = libpandaexpress._inPKoxtz2Bp(self.this)
        return returnValue

    
    def makeEmpty(self):
        returnValue = libpandaexpress._inPKoxt1Lkk(self.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._PTAUchar__overloaded_constructor(*_args)
        elif numArgs == 1:
            return self._PTAUchar__overloaded_constructor_ptrConstPTAUchar(*_args)
        elif numArgs == 2:
            return self._PTAUchar__overloaded_constructor_unsignedint_unsignedchar(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '


