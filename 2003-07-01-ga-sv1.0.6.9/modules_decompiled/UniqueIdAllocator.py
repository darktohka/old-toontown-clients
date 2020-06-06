# File: U (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import FFIExternalObject

class UniqueIdAllocator(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _UniqueIdAllocator__overloaded_constructor_longUnsignedlongint_longUnsignedlongint(self, min, max):
        self.this = libpanda._inPelbozTyP(min, max)
        self.userManagesMemory = 1

    
    def _UniqueIdAllocator__overloaded_constructor_longUnsignedlongint(self, min):
        self.this = libpanda._inPelboiPTL(min)
        self.userManagesMemory = 1

    
    def _UniqueIdAllocator__overloaded_constructor(self):
        self.this = libpanda._inPelboK9nc()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPelbo15vN:
            libpanda._inPelbo15vN(self.this)
        

    
    def allocate(self):
        returnValue = libpanda._inPelboA7pt(self.this)
        return returnValue

    
    def free(self, index):
        returnValue = libpanda._inPelbodayj(self.this, index)
        return returnValue

    
    def percentUsed(self):
        returnValue = libpanda._inPelboAQCN(self.this)
        return returnValue

    
    def _UniqueIdAllocator__overloaded_output_ptrConstUniqueIdAllocator_ptrOstream_bool(self, os, verbose):
        returnValue = libpanda._inPelboqDb_(self.this, os.this, verbose)
        return returnValue

    
    def _UniqueIdAllocator__overloaded_output_ptrConstUniqueIdAllocator_ptrOstream(self, os):
        returnValue = libpanda._inPelboMD2Z(self.this, os.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._UniqueIdAllocator__overloaded_constructor()
        elif numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._UniqueIdAllocator__overloaded_constructor_longUnsignedlongint(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        elif numArgs == 2:
            if isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.IntType):
                    return self._UniqueIdAllocator__overloaded_constructor_longUnsignedlongint_longUnsignedlongint(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '

    
    def output(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                return self._UniqueIdAllocator__overloaded_output_ptrConstUniqueIdAllocator_ptrOstream(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        elif numArgs == 2:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                if isinstance(_args[1], types.IntType):
                    return self._UniqueIdAllocator__overloaded_output_ptrConstUniqueIdAllocator_ptrOstream_bool(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


