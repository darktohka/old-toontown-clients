# File: D (Python 2.2)

import types
import libdirect
import libdirectDowncasts
from direct.ffi import FFIExternalObject

class DCDeclaration(FFIExternalObject.FFIExternalObject):
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
        if libdirect and libdirect._inP5HfQ9AVj:
            libdirect._inP5HfQ9AVj(self.this)
        

    
    def _DCDeclaration__overloaded_asClass_ptrDCDeclaration(self):
        returnValue = libdirect._inP5HfQ9iGM(self.this)
        import DCClass
        returnObject = DCClass.DCClass(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _DCDeclaration__overloaded_asClass_ptrConstDCDeclaration(self):
        returnValue = libdirect._inP5HfQa4C4(self.this)
        import DCClass
        returnObject = DCClass.DCClass(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _DCDeclaration__overloaded_asSwitch_ptrDCDeclaration(self):
        returnValue = libdirect._inP5HfQQXd6(self.this)
        import DCSwitch
        returnObject = DCSwitch.DCSwitch(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _DCDeclaration__overloaded_asSwitch_ptrConstDCDeclaration(self):
        returnValue = libdirect._inP5HfQE_84(self.this)
        import DCSwitch
        returnObject = DCSwitch.DCSwitch(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def output(self, out):
        returnValue = libdirect._inP5HfQ0qWE(self.this, out.this)
        return returnValue

    
    def write(self, out, indentLevel):
        returnValue = libdirect._inP5HfQ5mxH(self.this, out.this, indentLevel)
        return returnValue

    
    def asSwitch(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._DCDeclaration__overloaded_asSwitch_ptrConstDCDeclaration(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 '

    
    def asClass(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._DCDeclaration__overloaded_asClass_ptrConstDCDeclaration(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 '


