# File: P (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject
import PointerToBaseRefCountObjvectorLVector3f

class PTANormalf(PointerToBaseRefCountObjvectorLVector3f.PointerToBaseRefCountObjvectorLVector3f, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _PTANormalf__overloaded_constructor(self):
        self.this = libpanda._inPVZN3lt7W()
        self.userManagesMemory = 1

    
    def _PTANormalf__overloaded_constructor_ptrConstPTANormalf(self, copy):
        self.this = libpanda._inPVZN3tYAY(copy.this)
        self.userManagesMemory = 1

    
    def _PTANormalf__overloaded_constructor_unsignedint_ptrConstLVector3f(self, n, value):
        self.this = libpanda._inPVZN3BSal(n, value.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPVZN38tc3:
            libpanda._inPVZN38tc3(self.this)
        

    
    def emptyArray(n):
        returnValue = libpanda._inPVZN3YxLr(n)
        returnObject = PTANormalf(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    emptyArray = staticmethod(emptyArray)
    
    def size(self):
        returnValue = libpanda._inPVZN3XQQz(self.this)
        return returnValue

    
    def getElement(self, n):
        returnValue = libpanda._inPVZN3rqbA(self.this, n)
        return returnValue

    
    def pushBack(self, x):
        returnValue = libpanda._inPVZN3cCnk(self.this, x.this)
        return returnValue

    
    def popBack(self):
        returnValue = libpanda._inPVZN3DNfx(self.this)
        return returnValue

    
    def makeEmpty(self):
        returnValue = libpanda._inPVZN3ASVq(self.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._PTANormalf__overloaded_constructor(*_args)
        elif numArgs == 1:
            return self._PTANormalf__overloaded_constructor_ptrConstPTANormalf(*_args)
        elif numArgs == 2:
            return self._PTANormalf__overloaded_constructor_unsignedint_ptrConstLVector3f(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '


