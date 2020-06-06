# File: D (Python 2.2)

import types
import libdirect
import libdirectDowncasts
from direct.ffi import FFIExternalObject
import DCField

class DCParameter(DCField.DCField, FFIExternalObject.FFIExternalObject):
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
        

    
    def _DCParameter__overloaded_asSimpleParameter_ptrDCParameter(self):
        returnValue = libdirect._inP5HfQz9PJ(self.this)
        import DCSimpleParameter
        returnObject = DCSimpleParameter.DCSimpleParameter(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _DCParameter__overloaded_asSimpleParameter_ptrConstDCParameter(self):
        returnValue = libdirect._inP5HfQGnt_(self.this)
        import DCSimpleParameter
        returnObject = DCSimpleParameter.DCSimpleParameter(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _DCParameter__overloaded_asArrayParameter_ptrDCParameter(self):
        returnValue = libdirect._inP5HfQIgNV(self.this)
        import DCArrayParameter
        returnObject = DCArrayParameter.DCArrayParameter(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _DCParameter__overloaded_asArrayParameter_ptrConstDCParameter(self):
        returnValue = libdirect._inP5HfQdS2O(self.this)
        import DCArrayParameter
        returnObject = DCArrayParameter.DCArrayParameter(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def makeCopy(self):
        returnValue = libdirect._inP5HfQCNI1(self.this)
        returnObject = DCParameter(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def isValid(self):
        returnValue = libdirect._inP5HfQuxsw(self.this)
        return returnValue

    
    def getTypedef(self):
        returnValue = libdirect._inP5HfQ1UHS(self.this)
        import DCTypedef
        returnObject = DCTypedef.DCTypedef(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def asArrayParameter(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._DCParameter__overloaded_asArrayParameter_ptrConstDCParameter(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 '

    
    def asSimpleParameter(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._DCParameter__overloaded_asSimpleParameter_ptrConstDCParameter(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 '


