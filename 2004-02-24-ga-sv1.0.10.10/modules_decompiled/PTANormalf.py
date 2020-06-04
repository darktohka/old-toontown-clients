# File: P (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import PointerToBaseRefCountObjvectorLVector3f

class PTANormalf(PointerToBaseRefCountObjvectorLVector3f.PointerToBaseRefCountObjvectorLVector3f, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _PTANormalf__overloaded_constructor(self):
        self.this = libpanda._inPUZN3lt7W()
        self.userManagesMemory = 1

    
    def _PTANormalf__overloaded_constructor_ptrConstPTANormalf(self, copy):
        self.this = libpanda._inPUZN3tYAY(copy.this)
        self.userManagesMemory = 1

    
    def _PTANormalf__overloaded_constructor_unsignedint_ptrConstLVector3f(self, n, value):
        self.this = libpanda._inPUZN3OSal(n, value.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPUZN39tc3:
            libpanda._inPUZN39tc3(self.this)
        

    
    def emptyArray(n):
        returnValue = libpanda._inPUZN3n_Lr(n)
        returnObject = PTANormalf(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    emptyArray = staticmethod(emptyArray)
    
    def size(self):
        returnValue = libpanda._inPUZN3UQQz(self.this)
        return returnValue

    
    def pushBack(self, x):
        returnValue = libpanda._inPUZN3bCnk(self.this, x.this)
        return returnValue

    
    def popBack(self):
        returnValue = libpanda._inPUZN3ANfx(self.this)
        return returnValue

    
    def makeEmpty(self):
        returnValue = libpanda._inPUZN3DSVq(self.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._PTANormalf__overloaded_constructor()
        elif numArgs == 1:
            if isinstance(_args[0], PTANormalf):
                return self._PTANormalf__overloaded_constructor_ptrConstPTANormalf(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <PTANormalf> '
        elif numArgs == 2:
            if isinstance(_args[0], types.IntType):
                import Vec3
                if isinstance(_args[1], Vec3.Vec3):
                    return self._PTANormalf__overloaded_constructor_unsignedint_ptrConstLVector3f(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <Vec3.Vec3> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '


