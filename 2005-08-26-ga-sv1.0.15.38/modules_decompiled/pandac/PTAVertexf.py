# File: P (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject
import PointerToBaseRefCountObjvectorLPoint3f

class PTAVertexf(PointerToBaseRefCountObjvectorLPoint3f.PointerToBaseRefCountObjvectorLPoint3f, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _PTAVertexf__overloaded_constructor(self):
        self.this = libpanda._inPVZN3mnFP()
        self.userManagesMemory = 1

    
    def _PTAVertexf__overloaded_constructor_ptrConstPTAVertexf(self, copy):
        self.this = libpanda._inPVZN3JbXT(copy.this)
        self.userManagesMemory = 1

    
    def _PTAVertexf__overloaded_constructor_unsignedint_ptrConstLPoint3f(self, n, value):
        self.this = libpanda._inPVZN3h_e7(n, value.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPVZN3zSHs:
            libpanda._inPVZN3zSHs(self.this)
        

    
    def emptyArray(n):
        returnValue = libpanda._inPVZN3WYs3(n)
        returnObject = PTAVertexf(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    emptyArray = staticmethod(emptyArray)
    
    def size(self):
        returnValue = libpanda._inPVZN3Iw_L(self.this)
        return returnValue

    
    def getElement(self, n):
        returnValue = libpanda._inPVZN31wUs(self.this, n)
        return returnValue

    
    def pushBack(self, x):
        returnValue = libpanda._inPVZN3OhiH(self.this, x.this)
        return returnValue

    
    def popBack(self):
        returnValue = libpanda._inPVZN3mQ8V(self.this)
        return returnValue

    
    def makeEmpty(self):
        returnValue = libpanda._inPVZN37KuT(self.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._PTAVertexf__overloaded_constructor(*_args)
        elif numArgs == 1:
            return self._PTAVertexf__overloaded_constructor_ptrConstPTAVertexf(*_args)
        elif numArgs == 2:
            return self._PTAVertexf__overloaded_constructor_unsignedint_ptrConstLPoint3f(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '


