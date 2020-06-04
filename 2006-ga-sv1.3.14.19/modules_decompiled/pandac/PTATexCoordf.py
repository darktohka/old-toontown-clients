# File: P (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject
import PointerToBaseRefCountObjvectorLPoint2f

class PTATexCoordf(PointerToBaseRefCountObjvectorLPoint2f.PointerToBaseRefCountObjvectorLPoint2f, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _PTATexCoordf__overloaded_constructor(self):
        self.this = libpanda._inPVZN3Z1EP()
        self.userManagesMemory = 1

    
    def _PTATexCoordf__overloaded_constructor_ptrConstPTATexCoordf(self, copy):
        self.this = libpanda._inPVZN3VgWz(copy.this)
        self.userManagesMemory = 1

    
    def _PTATexCoordf__overloaded_constructor_unsignedint_ptrConstLPoint2f(self, n, value):
        self.this = libpanda._inPVZN3sNOf(n, value.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPVZN34MGs:
            libpanda._inPVZN34MGs(self.this)
        

    
    def emptyArray(n):
        returnValue = libpanda._inPVZN3vJr3(n)
        returnObject = PTATexCoordf(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    emptyArray = staticmethod(emptyArray)
    
    def size(self):
        returnValue = libpanda._inPVZN3DO_L(self.this)
        return returnValue

    
    def getElement(self, n):
        returnValue = libpanda._inPVZN3OiVs(self.this, n)
        return returnValue

    
    def pushBack(self, x):
        returnValue = libpanda._inPVZN3YTFP(self.this, x.this)
        return returnValue

    
    def popBack(self):
        returnValue = libpanda._inPVZN3pi7V(self.this)
        return returnValue

    
    def makeEmpty(self):
        returnValue = libpanda._inPVZN3k0tT(self.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._PTATexCoordf__overloaded_constructor(*_args)
        elif numArgs == 1:
            return self._PTATexCoordf__overloaded_constructor_ptrConstPTATexCoordf(*_args)
        elif numArgs == 2:
            return self._PTATexCoordf__overloaded_constructor_unsignedint_ptrConstLPoint2f(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '


