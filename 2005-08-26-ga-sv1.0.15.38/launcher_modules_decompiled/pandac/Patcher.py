# File: P (Python 2.2)

import types
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject

class Patcher(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _Patcher__overloaded_constructor(self):
        self.this = libpandaexpress._inP2KOdXe93()
        self.userManagesMemory = 1

    
    def _Patcher__overloaded_constructor_ptrBuffer(self, buffer):
        self.this = libpandaexpress._inP2KOd8YxX(buffer.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaexpress and libpandaexpress._inP2KOdeP0w:
            libpandaexpress._inP2KOdeP0w(self.this)
        

    
    def initiate(self, patch, infile):
        returnValue = libpandaexpress._inP2KOdYc1E(self.this, patch.this, infile.this)
        return returnValue

    
    def run(self):
        returnValue = libpandaexpress._inP2KOd_N2z(self.this)
        return returnValue

    
    def getProgress(self):
        returnValue = libpandaexpress._inP2KOdx_F5(self.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Patcher__overloaded_constructor(*_args)
        elif numArgs == 1:
            return self._Patcher__overloaded_constructor_ptrBuffer(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


