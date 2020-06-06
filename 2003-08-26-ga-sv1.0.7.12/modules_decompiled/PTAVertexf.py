# File: P (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import PointerToBaseRefCountObjvectorLPoint3f

class PTAVertexf(PointerToBaseRefCountObjvectorLPoint3f.PointerToBaseRefCountObjvectorLPoint3f, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _PTAVertexf__overloaded_constructor(self):
        self.this = libpanda._inPUZN3mnFP()
        self.userManagesMemory = 1

    
    def _PTAVertexf__overloaded_constructor_ptrConstPTAVertexf(self, copy):
        self.this = libpanda._inPUZN3JbXT(copy.this)
        self.userManagesMemory = 1

    
    def _PTAVertexf__overloaded_constructor_unsignedint_ptrConstLPoint3f(self, n, value):
        self.this = libpanda._inPUZN3g_e7(n, value.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPUZN3ySHs:
            libpanda._inPUZN3ySHs(self.this)
        

    
    def emptyArray(n):
        returnValue = libpanda._inPUZN3XYs3(n)
        returnObject = PTAVertexf(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    emptyArray = staticmethod(emptyArray)
    
    def size(self):
        returnValue = libpanda._inPUZN3Iw_L(self.this)
        return returnValue

    
    def pushBack(self, x):
        returnValue = libpanda._inPUZN3OhiH(self.this, x.this)
        return returnValue

    
    def popBack(self):
        returnValue = libpanda._inPUZN3mQ8V(self.this)
        return returnValue

    
    def makeEmpty(self):
        returnValue = libpanda._inPUZN37KuT(self.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._PTAVertexf__overloaded_constructor()
        elif numArgs == 1:
            if isinstance(_args[0], PTAVertexf):
                return self._PTAVertexf__overloaded_constructor_ptrConstPTAVertexf(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <PTAVertexf> '
        elif numArgs == 2:
            if isinstance(_args[0], types.IntType):
                import Point3
                if isinstance(_args[1], Point3.Point3):
                    return self._PTAVertexf__overloaded_constructor_unsignedint_ptrConstLPoint3f(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <Point3.Point3> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '


