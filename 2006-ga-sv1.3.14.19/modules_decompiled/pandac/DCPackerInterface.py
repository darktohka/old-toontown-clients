# File: D (Python 2.2)

import types
import libdirect
import libdirectDowncasts
from direct.ffi import FFIExternalObject

class DCPackerInterface(FFIExternalObject.FFIExternalObject):
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
        

    
    def getName(self):
        returnValue = libdirect._inP5HfQEqeZ(self.this)
        return returnValue

    
    def findSeekIndex(self, name):
        returnValue = libdirect._inP5HfQ4eZn(self.this, name)
        return returnValue

    
    def _DCPackerInterface__overloaded_asField_ptrDCPackerInterface(self):
        returnValue = libdirect._inP5HfQlG9m(self.this)
        import DCField
        returnObject = DCField.DCField(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _DCPackerInterface__overloaded_asField_ptrConstDCPackerInterface(self):
        returnValue = libdirect._inP5HfQJDqB(self.this)
        import DCField
        returnObject = DCField.DCField(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _DCPackerInterface__overloaded_asSwitchParameter_ptrDCPackerInterface(self):
        returnValue = libdirect._inP5HfQUOXk(self.this)
        import DCSwitchParameter
        returnObject = DCSwitchParameter.DCSwitchParameter(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _DCPackerInterface__overloaded_asSwitchParameter_ptrConstDCPackerInterface(self):
        returnValue = libdirect._inP5HfQ1e9D(self.this)
        import DCSwitchParameter
        returnObject = DCSwitchParameter.DCSwitchParameter(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _DCPackerInterface__overloaded_asClassParameter_ptrDCPackerInterface(self):
        returnValue = libdirect._inP5HfQLrGr(self.this)
        import DCClassParameter
        returnObject = DCClassParameter.DCClassParameter(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _DCPackerInterface__overloaded_asClassParameter_ptrConstDCPackerInterface(self):
        returnValue = libdirect._inP5HfQ_GEW(self.this)
        import DCClassParameter
        returnObject = DCClassParameter.DCClassParameter(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _DCPackerInterface__overloaded_checkMatch_ptrConstDCPackerInterface_ptrConstDCPackerInterface(self, other):
        returnValue = libdirect._inP5HfQcNZX(self.this, other.this)
        return returnValue

    
    def _DCPackerInterface__overloaded_checkMatch_ptrConstDCPackerInterface_atomicstring_ptrDCFile(self, description, dcfile):
        returnValue = libdirect._inP5HfQvvj_(self.this, description, dcfile.this)
        return returnValue

    
    def _DCPackerInterface__overloaded_checkMatch_ptrConstDCPackerInterface_atomicstring(self, description):
        returnValue = libdirect._inP5HfQrsRl(self.this, description)
        return returnValue

    
    def asSwitchParameter(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._DCPackerInterface__overloaded_asSwitchParameter_ptrConstDCPackerInterface(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 '

    
    def checkMatch(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._DCPackerInterface__overloaded_checkMatch_ptrConstDCPackerInterface_atomicstring(*_args)
            
            if isinstance(_args[0], DCPackerInterface):
                return self._DCPackerInterface__overloaded_checkMatch_ptrConstDCPackerInterface_ptrConstDCPackerInterface(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <DCPackerInterface> '
        elif numArgs == 2:
            return self._DCPackerInterface__overloaded_checkMatch_ptrConstDCPackerInterface_atomicstring_ptrDCFile(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def asField(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._DCPackerInterface__overloaded_asField_ptrConstDCPackerInterface(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 '

    
    def asClassParameter(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._DCPackerInterface__overloaded_asClassParameter_ptrConstDCPackerInterface(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 '


