# File: D (Python 2.2)

import types
import libdirect
import libdirectDowncasts
import FFIExternalObject
import DCField

class DCAtomicField(DCField.DCField, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libdirectDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self):
        raise RuntimeError, 'No C++ constructor defined for class: ' + self.__class__.__name__

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libdirect and libdirect._inP5HfQBA_T:
            libdirect._inP5HfQBA_T(self.this)
        

    
    def getNumElements(self):
        returnValue = libdirect._inP5HfQz94I(self.this)
        return returnValue

    
    def getElementType(self, n):
        returnValue = libdirect._inP5HfQwNXT(self.this, n)
        return returnValue

    
    def getElementName(self, n):
        returnValue = libdirect._inP5HfQKM_N(self.this, n)
        return returnValue

    
    def getElementDivisor(self, n):
        returnValue = libdirect._inP5HfQ_HmD(self.this, n)
        return returnValue

    
    def getElementDefault(self, n):
        returnValue = libdirect._inP5HfQnDFi(self.this, n)
        return returnValue

    
    def hasElementDefault(self, n):
        returnValue = libdirect._inP5HfQiDfy(self.this, n)
        return returnValue

    
    def isRequired(self):
        returnValue = libdirect._inP5HfQbbzo(self.this)
        return returnValue

    
    def isBroadcast(self):
        returnValue = libdirect._inP5HfQqSGH(self.this)
        return returnValue

    
    def isP2p(self):
        returnValue = libdirect._inP5HfQIz0D(self.this)
        return returnValue

    
    def isRam(self):
        returnValue = libdirect._inP5HfQw2Xx(self.this)
        return returnValue

    
    def isDb(self):
        returnValue = libdirect._inP5HfQI6M0(self.this)
        return returnValue

    
    def isClsend(self):
        returnValue = libdirect._inP5HfQfiB2(self.this)
        return returnValue

    
    def isClrecv(self):
        returnValue = libdirect._inP5HfQMv5E(self.this)
        return returnValue

    
    def isOwnsend(self):
        returnValue = libdirect._inP5HfQaK40(self.this)
        return returnValue


