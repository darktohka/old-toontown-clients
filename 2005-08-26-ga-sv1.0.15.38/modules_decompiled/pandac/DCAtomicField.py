# File: D (Python 2.2)

import types
import libdirect
import libdirectDowncasts
from direct.ffi import FFIExternalObject
import DCField

class DCAtomicField(DCField.DCField, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libdirectDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self):
        raise RuntimeError, 'No C++ constructor defined for class: ' + self.__class__.__name__

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libdirect and libdirect._inP5HfQSs2p:
            libdirect._inP5HfQSs2p(self.this)
        

    
    def getNumElements(self):
        returnValue = libdirect._inP5HfQz94I(self.this)
        return returnValue

    
    def getElement(self, n):
        returnValue = libdirect._inP5HfQMXfe(self.this, n)
        import DCParameter
        returnObject = DCParameter.DCParameter(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getElementDefault(self, n):
        returnValue = libdirect._inP5HfQkDFi(self.this, n)
        return returnValue

    
    def hasElementDefault(self, n):
        returnValue = libdirect._inP5HfQjDfy(self.this, n)
        return returnValue

    
    def getElementName(self, n):
        returnValue = libdirect._inP5HfQKM_N(self.this, n)
        return returnValue

    
    def getElementType(self, n):
        returnValue = libdirect._inP5HfQwNXT(self.this, n)
        return returnValue

    
    def getElementDivisor(self, n):
        returnValue = libdirect._inP5HfQ_HmD(self.this, n)
        return returnValue


