# File: E (Python 2.2)

import types
import libpandaegg
import libpandaeggDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import EggNamedObject

class EggVertexUV(EggNamedObject.EggNamedObject, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaeggDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _EggVertexUV__overloaded_constructor_ptrConstEggVertexUV(self, copy):
        self.this = libpandaegg._inPkAOMfgDe(copy.this)
        self.userManagesMemory = 1

    
    def _EggVertexUV__overloaded_constructor_atomicstring_ptrConstLPoint2d(self, name, uv):
        self.this = libpandaegg._inPkAOMrGLE(name, uv.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaegg and libpandaegg._inPkAOMpgi_:
            libpandaegg._inPkAOMpgi_(self.this)
        

    
    def getClassType():
        returnValue = libpandaegg._inPkAOMBqeg()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def assign(self, copy):
        returnValue = libpandaegg._inPkAOMDsRd(self.this, copy.this)
        returnObject = EggVertexUV(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getUv(self):
        returnValue = libpandaegg._inPkAOMWnKk(self.this)
        import Point2D
        returnObject = Point2D.Point2D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setUv(self, texCoord):
        returnValue = libpandaegg._inPkAOMC1GK(self.this, texCoord.this)
        return returnValue

    
    def write(self, out, indentLevel):
        returnValue = libpandaegg._inPkAOMaahg(self.this, out.this, indentLevel)
        return returnValue

    
    def compareTo(self, other):
        returnValue = libpandaegg._inPkAOMpA7a(self.this, other.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._EggVertexUV__overloaded_constructor_ptrConstEggVertexUV(*_args)
        elif numArgs == 2:
            return self._EggVertexUV__overloaded_constructor_atomicstring_ptrConstLPoint2d(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


