# File: L (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import TypedReferenceCount

class Lerp(TypedReferenceCount.TypedReferenceCount, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _Lerp__overloaded_constructor_ptrConstLerp(self, parameter0):
        self.this = libpanda._inPjRdzQD6d(parameter0.this)
        self.userManagesMemory = 1

    
    def _Lerp__overloaded_constructor_ptrLerpFunctor_float_ptrLerpBlendType(self, func, endt, blend):
        self.this = libpanda._inPjRdzs6jr(func.this, endt, blend.this)
        self.userManagesMemory = 1

    
    def _Lerp__overloaded_constructor_ptrLerpFunctor_float_float_ptrLerpBlendType(self, func, startt, endt, blend):
        self.this = libpanda._inPjRdzeiEF(func.this, startt, endt, blend.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClassType():
        returnValue = libpanda._inPjRdzz5da()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def assign(self, parameter1):
        returnValue = libpanda._inPjRdz7tt_(self.this, parameter1.this)
        returnObject = Lerp(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def step(self):
        returnValue = libpanda._inPjRdziuTk(self.this)
        return returnValue

    
    def setStepSize(self, parameter1):
        returnValue = libpanda._inPjRdzARoq(self.this, parameter1)
        return returnValue

    
    def getStepSize(self):
        returnValue = libpanda._inPjRdzMVTI(self.this)
        return returnValue

    
    def setT(self, parameter1):
        returnValue = libpanda._inPjRdzlUwT(self.this, parameter1)
        return returnValue

    
    def getT(self):
        returnValue = libpanda._inPjRdzDscX(self.this)
        return returnValue

    
    def isDone(self):
        returnValue = libpanda._inPjRdz7Ojs(self.this)
        return returnValue

    
    def getFunctor(self):
        returnValue = libpanda._inPjRdz7rPj(self.this)
        import LerpFunctor
        returnObject = LerpFunctor.LerpFunctor(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def setEndEvent(self, parameter1):
        returnValue = libpanda._inPjRdzg2aG(self.this, parameter1)
        return returnValue

    
    def getEndEvent(self):
        returnValue = libpanda._inPjRdzyUUS(self.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._Lerp__overloaded_constructor_ptrConstLerp(*_args)
        elif numArgs == 3:
            return self._Lerp__overloaded_constructor_ptrLerpFunctor_float_ptrLerpBlendType(*_args)
        elif numArgs == 4:
            return self._Lerp__overloaded_constructor_ptrLerpFunctor_float_float_ptrLerpBlendType(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 4 '


