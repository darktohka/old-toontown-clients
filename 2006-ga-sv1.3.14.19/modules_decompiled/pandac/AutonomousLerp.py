# File: A (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import TypedReferenceCount

class AutonomousLerp(TypedReferenceCount.TypedReferenceCount, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _AutonomousLerp__overloaded_constructor_ptrConstAutonomousLerp(self, parameter0):
        self.this = libpanda._inPjRdzn1mi(parameter0.this)
        self.userManagesMemory = 1

    
    def _AutonomousLerp__overloaded_constructor_ptrLerpFunctor_float_ptrLerpBlendType_ptrEventHandler(self, func, endt, blend, handler):
        self.this = libpanda._inPjRdzyGSy(func.this, endt, blend.this, handler.this)
        self.userManagesMemory = 1

    
    def _AutonomousLerp__overloaded_constructor_ptrLerpFunctor_float_float_ptrLerpBlendType_ptrEventHandler(self, func, startt, endt, blend, handler):
        self.this = libpanda._inPjRdzIqNi(func.this, startt, endt, blend.this, handler.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClassType():
        returnValue = libpanda._inPjRdznSlS()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def assign(self, parameter1):
        returnValue = libpanda._inPjRdzk3L_(self.this, parameter1.this)
        returnObject = AutonomousLerp(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def start(self):
        returnValue = libpanda._inPjRdzubE1(self.this)
        return returnValue

    
    def stop(self):
        returnValue = libpanda._inPjRdz__s_(self.this)
        return returnValue

    
    def resume(self):
        returnValue = libpanda._inPjRdzf999(self.this)
        return returnValue

    
    def isDone(self):
        returnValue = libpanda._inPjRdzch0a(self.this)
        return returnValue

    
    def getFunctor(self):
        returnValue = libpanda._inPjRdzkqo1(self.this)
        import LerpFunctor
        returnObject = LerpFunctor.LerpFunctor(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def setT(self, parameter1):
        returnValue = libpanda._inPjRdzUKt3(self.this, parameter1)
        return returnValue

    
    def getT(self):
        returnValue = libpanda._inPjRdzTsbG(self.this)
        return returnValue

    
    def setEndEvent(self, parameter1):
        returnValue = libpanda._inPjRdzkmdC(self.this, parameter1)
        return returnValue

    
    def getEndEvent(self):
        returnValue = libpanda._inPjRdzIF7x(self.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._AutonomousLerp__overloaded_constructor_ptrConstAutonomousLerp(*_args)
        elif numArgs == 4:
            return self._AutonomousLerp__overloaded_constructor_ptrLerpFunctor_float_ptrLerpBlendType_ptrEventHandler(*_args)
        elif numArgs == 5:
            return self._AutonomousLerp__overloaded_constructor_ptrLerpFunctor_float_float_ptrLerpBlendType_ptrEventHandler(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 4 5 '


