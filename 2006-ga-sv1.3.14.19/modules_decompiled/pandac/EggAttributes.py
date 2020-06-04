# File: E (Python 2.2)

import types
import libpandaegg
import libpandaeggDowncasts
from direct.ffi import FFIExternalObject

class EggAttributes(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaeggDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _EggAttributes__overloaded_constructor(self):
        self.this = libpandaegg._inPkAOMhfwD()
        self.userManagesMemory = 1

    
    def _EggAttributes__overloaded_constructor_ptrConstEggAttributes(self, copy):
        self.this = libpandaegg._inPkAOMepOm(copy.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaegg and libpandaegg._inPkAOM1lbg:
            libpandaegg._inPkAOM1lbg(self.this)
        

    
    def getClassType():
        returnValue = libpandaegg._inPkAOMX9Yr()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def assign(self, copy):
        returnValue = libpandaegg._inPkAOMUF8y(self.this, copy.this)
        returnObject = EggAttributes(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def hasNormal(self):
        returnValue = libpandaegg._inPkAOMw9Eb(self.this)
        return returnValue

    
    def getNormal(self):
        returnValue = libpandaegg._inPkAOMVCpK(self.this)
        import Vec3D
        returnObject = Vec3D.Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setNormal(self, normal):
        returnValue = libpandaegg._inPkAOMpRK6(self.this, normal.this)
        return returnValue

    
    def clearNormal(self):
        returnValue = libpandaegg._inPkAOMS6MT(self.this)
        return returnValue

    
    def hasColor(self):
        returnValue = libpandaegg._inPkAOMKFjr(self.this)
        return returnValue

    
    def getColor(self):
        returnValue = libpandaegg._inPkAOMXGJb(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setColor(self, color):
        returnValue = libpandaegg._inPkAOMFNlA(self.this, color.this)
        return returnValue

    
    def clearColor(self):
        returnValue = libpandaegg._inPkAOMfqMj(self.this)
        return returnValue

    
    def write(self, out, indentLevel):
        returnValue = libpandaegg._inPkAOMgbBE(self.this, out.this, indentLevel)
        return returnValue

    
    def sortsLessThan(self, other):
        returnValue = libpandaegg._inPkAOMOpUR(self.this, other.this)
        return returnValue

    
    def transform(self, mat):
        returnValue = libpandaegg._inPkAOMZnUo(self.this, mat.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._EggAttributes__overloaded_constructor(*_args)
        elif numArgs == 1:
            return self._EggAttributes__overloaded_constructor_ptrConstEggAttributes(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


