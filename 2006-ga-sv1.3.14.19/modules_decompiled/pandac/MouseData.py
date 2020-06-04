# File: M (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject

class MouseData(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _MouseData__overloaded_constructor(self):
        self.this = libpanda._inPflbogWcW()
        self.userManagesMemory = 1

    
    def _MouseData__overloaded_constructor_ptrConstMouseData(self, copy):
        self.this = libpanda._inPflboja_u(copy.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPflboAm_W:
            libpanda._inPflboAm_W(self.this)
        

    
    def assign(self, copy):
        returnValue = libpanda._inPflboqtbu(self.this, copy.this)
        returnObject = MouseData(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getX(self):
        returnValue = libpanda._inPflboRo5w(self.this)
        return returnValue

    
    def getY(self):
        returnValue = libpanda._inPflbop4Dx(self.this)
        return returnValue

    
    def getInWindow(self):
        returnValue = libpanda._inPflbo370X(self.this)
        return returnValue

    
    def output(self, out):
        returnValue = libpanda._inPflbolQkK(self.this, out.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._MouseData__overloaded_constructor(*_args)
        elif numArgs == 1:
            return self._MouseData__overloaded_constructor_ptrConstMouseData(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


