# File: B (Python 2.2)

import types
import libpandaphysics
import libpandaphysicsDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import BaseParticleEmitter

class BoxEmitter(BaseParticleEmitter.BaseParticleEmitter, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaphysicsDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _BoxEmitter__overloaded_constructor(self):
        self.this = libpandaphysics._inPKBUAkwIq()
        self.userManagesMemory = 1

    
    def _BoxEmitter__overloaded_constructor_ptrConstBoxEmitter(self, copy):
        self.this = libpandaphysics._inPKBUA42fc(copy.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaphysics and libpandaphysics._inPKBUAg60H:
            libpandaphysics._inPKBUAg60H(self.this)
        

    
    def setMinBound(self, vmin):
        returnValue = libpandaphysics._inPKBUAfUdv(self.this, vmin.this)
        return returnValue

    
    def setMaxBound(self, vmax):
        returnValue = libpandaphysics._inPKBUAhptT(self.this, vmax.this)
        return returnValue

    
    def getMinBound(self):
        returnValue = libpandaphysics._inPKBUAtfR4(self.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getMaxBound(self):
        returnValue = libpandaphysics._inPKBUAgZgc(self.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._BoxEmitter__overloaded_constructor(*_args)
        elif numArgs == 1:
            return self._BoxEmitter__overloaded_constructor_ptrConstBoxEmitter(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


