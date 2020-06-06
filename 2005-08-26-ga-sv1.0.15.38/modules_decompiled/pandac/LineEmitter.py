# File: L (Python 2.2)

import types
import libpandaphysics
import libpandaphysicsDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import BaseParticleEmitter

class LineEmitter(BaseParticleEmitter.BaseParticleEmitter, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaphysicsDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _LineEmitter__overloaded_constructor(self):
        self.this = libpandaphysics._inPKBUAmO71()
        self.userManagesMemory = 1

    
    def _LineEmitter__overloaded_constructor_ptrConstLineEmitter(self, copy):
        self.this = libpandaphysics._inPKBUAvJIy(copy.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandaphysics and libpandaphysics._inPKBUAg60H:
            libpandaphysics._inPKBUAg60H(self.this)
        

    
    def setEndpoint1(self, point):
        returnValue = libpandaphysics._inPKBUAkFGJ(self.this, point.this)
        return returnValue

    
    def setEndpoint2(self, point):
        returnValue = libpandaphysics._inPKBUAEBtJ(self.this, point.this)
        return returnValue

    
    def getEndpoint1(self):
        returnValue = libpandaphysics._inPKBUA6l0h(self.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getEndpoint2(self):
        returnValue = libpandaphysics._inPKBUAaobi(self.this)
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
            return self._LineEmitter__overloaded_constructor(*_args)
        elif numArgs == 1:
            return self._LineEmitter__overloaded_constructor_ptrConstLineEmitter(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


