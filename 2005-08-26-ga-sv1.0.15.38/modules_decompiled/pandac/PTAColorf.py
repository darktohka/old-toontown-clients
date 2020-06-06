# File: P (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject
import PointerToBaseRefCountObjvectorLVecBase4f

class PTAColorf(PointerToBaseRefCountObjvectorLVecBase4f.PointerToBaseRefCountObjvectorLVecBase4f, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _PTAColorf__overloaded_constructor(self):
        self.this = libpanda._inPVZN3R_Zx()
        self.userManagesMemory = 1

    
    def _PTAColorf__overloaded_constructor_ptrConstPTAColorf(self, copy):
        self.this = libpanda._inPVZN3yy4B(copy.this)
        self.userManagesMemory = 1

    
    def _PTAColorf__overloaded_constructor_unsignedint_ptrConstLVecBase4f(self, n, value):
        self.this = libpanda._inPVZN3NSjW(n, value.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPVZN36SyC:
            libpanda._inPVZN36SyC(self.this)
        

    
    def emptyArray(n):
        returnValue = libpanda._inPVZN3nFH6(n)
        returnObject = PTAColorf(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    emptyArray = staticmethod(emptyArray)
    
    def size(self):
        returnValue = libpanda._inPVZN3ly67(self.this)
        return returnValue

    
    def getElement(self, n):
        returnValue = libpanda._inPVZN3LXPj(self.this, n)
        return returnValue

    
    def pushBack(self, x):
        returnValue = libpanda._inPVZN3iRDO(self.this, x.this)
        return returnValue

    
    def popBack(self):
        returnValue = libpanda._inPVZN3AOTD(self.this)
        return returnValue

    
    def makeEmpty(self):
        returnValue = libpanda._inPVZN3Qcsd(self.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._PTAColorf__overloaded_constructor(*_args)
        elif numArgs == 1:
            return self._PTAColorf__overloaded_constructor_ptrConstPTAColorf(*_args)
        elif numArgs == 2:
            return self._PTAColorf__overloaded_constructor_unsignedint_ptrConstLVecBase4f(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '


