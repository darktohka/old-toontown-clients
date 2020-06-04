# File: P (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import PointerToBaseRefCountObjvectorLVecBase4f

class PTAColorf(PointerToBaseRefCountObjvectorLVecBase4f.PointerToBaseRefCountObjvectorLVecBase4f, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _PTAColorf__overloaded_constructor(self):
        self.this = libpanda._inPUZN3e_Zx()
        self.userManagesMemory = 1

    
    def _PTAColorf__overloaded_constructor_ptrConstPTAColorf(self, copy):
        self.this = libpanda._inPUZN3yy4B(copy.this)
        self.userManagesMemory = 1

    
    def _PTAColorf__overloaded_constructor_unsignedint_ptrConstLVecBase4f(self, n, value):
        self.this = libpanda._inPUZN3NSjW(n, value.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPUZN36SyC:
            libpanda._inPUZN36SyC(self.this)
        

    
    def emptyArray(n):
        returnValue = libpanda._inPUZN3kFH6(n)
        returnObject = PTAColorf(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    emptyArray = staticmethod(emptyArray)
    
    def size(self):
        returnValue = libpanda._inPUZN3iy67(self.this)
        return returnValue

    
    def pushBack(self, x):
        returnValue = libpanda._inPUZN3iRDO(self.this, x.this)
        return returnValue

    
    def popBack(self):
        returnValue = libpanda._inPUZN3AOTD(self.this)
        return returnValue

    
    def makeEmpty(self):
        returnValue = libpanda._inPUZN3Qcsd(self.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._PTAColorf__overloaded_constructor()
        elif numArgs == 1:
            if isinstance(_args[0], PTAColorf):
                return self._PTAColorf__overloaded_constructor_ptrConstPTAColorf(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <PTAColorf> '
        elif numArgs == 2:
            if isinstance(_args[0], types.IntType):
                import VBase4
                if isinstance(_args[1], VBase4.VBase4):
                    return self._PTAColorf__overloaded_constructor_unsignedint_ptrConstLVecBase4f(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <VBase4.VBase4> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '


