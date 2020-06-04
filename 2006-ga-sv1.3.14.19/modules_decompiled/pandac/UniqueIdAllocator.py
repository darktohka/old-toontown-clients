# File: U (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject

class UniqueIdAllocator(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _UniqueIdAllocator__overloaded_constructor_longUnsignedlongint_longUnsignedlongint(self, min, max):
        self.this = libpanda._inPflbozTyP(min, max)
        self.userManagesMemory = 1

    
    def _UniqueIdAllocator__overloaded_constructor_longUnsignedlongint(self, min):
        self.this = libpanda._inPflboiPTL(min)
        self.userManagesMemory = 1

    
    def _UniqueIdAllocator__overloaded_constructor(self):
        self.this = libpanda._inPflboK9nc()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPflbo15vN:
            libpanda._inPflbo15vN(self.this)
        

    
    def allocate(self):
        returnValue = libpanda._inPflboD7pt(self.this)
        return returnValue

    
    def free(self, index):
        returnValue = libpanda._inPflbocayj(self.this, index)
        return returnValue

    
    def fractionUsed(self):
        returnValue = libpanda._inPflboAmoe(self.this)
        return returnValue

    
    def _UniqueIdAllocator__overloaded_output_ptrConstUniqueIdAllocator_ptrOstream_bool(self, os, verbose):
        returnValue = libpanda._inPflbopDb_(self.this, os.this, verbose)
        return returnValue

    
    def _UniqueIdAllocator__overloaded_output_ptrConstUniqueIdAllocator_ptrOstream(self, os):
        returnValue = libpanda._inPflboMD2Z(self.this, os.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._UniqueIdAllocator__overloaded_constructor(*_args)
        elif numArgs == 1:
            return self._UniqueIdAllocator__overloaded_constructor_longUnsignedlongint(*_args)
        elif numArgs == 2:
            return self._UniqueIdAllocator__overloaded_constructor_longUnsignedlongint_longUnsignedlongint(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '

    
    def output(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._UniqueIdAllocator__overloaded_output_ptrConstUniqueIdAllocator_ptrOstream(*_args)
        elif numArgs == 2:
            return self._UniqueIdAllocator__overloaded_output_ptrConstUniqueIdAllocator_ptrOstream_bool(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


