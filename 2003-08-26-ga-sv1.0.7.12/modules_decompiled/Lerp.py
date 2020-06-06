# File: L (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import TypedReferenceCount

class Lerp(TypedReferenceCount.TypedReferenceCount, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _Lerp__overloaded_constructor_ptrConstLerp(self, parameter0):
        self.this = libpanda._inPgRdzQD6d(parameter0.this)
        self.userManagesMemory = 1

    
    def _Lerp__overloaded_constructor_ptrLerpFunctor_float_ptrLerpBlendType(self, func, endt, blend):
        self.this = libpanda._inPgRdzt6jr(func.this, endt, blend.this)
        self.userManagesMemory = 1

    
    def _Lerp__overloaded_constructor_ptrLerpFunctor_float_float_ptrLerpBlendType(self, func, startt, endt, blend):
        self.this = libpanda._inPgRdzeiEF(func.this, startt, endt, blend.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClassType():
        returnValue = libpanda._inPgRdzz5da()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def assign(self, parameter1):
        returnValue = libpanda._inPgRdz6tt_(self.this, parameter1.this)
        returnObject = Lerp(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def step(self):
        returnValue = libpanda._inPgRdzhuTk(self.this)
        return returnValue

    
    def setStepSize(self, parameter1):
        returnValue = libpanda._inPgRdzHRoq(self.this, parameter1)
        return returnValue

    
    def getStepSize(self):
        returnValue = libpanda._inPgRdzMVTI(self.this)
        return returnValue

    
    def setT(self, parameter1):
        returnValue = libpanda._inPgRdzlUwT(self.this, parameter1)
        return returnValue

    
    def getT(self):
        returnValue = libpanda._inPgRdzDscX(self.this)
        return returnValue

    
    def isDone(self):
        returnValue = libpanda._inPgRdz6Ojs(self.this)
        return returnValue

    
    def getFunctor(self):
        returnValue = libpanda._inPgRdz4rPj(self.this)
        import LerpFunctor
        returnObject = LerpFunctor.LerpFunctor(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def setEndEvent(self, parameter1):
        returnValue = libpanda._inPgRdzg2aG(self.this, parameter1)
        return returnValue

    
    def getEndEvent(self):
        returnValue = libpanda._inPgRdzyUUS(self.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], Lerp):
                return self._Lerp__overloaded_constructor_ptrConstLerp(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Lerp> '
        elif numArgs == 3:
            import LerpFunctor
            if isinstance(_args[0], LerpFunctor.LerpFunctor):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    import LerpBlendType
                    if isinstance(_args[2], LerpBlendType.LerpBlendType):
                        return self._Lerp__overloaded_constructor_ptrLerpFunctor_float_ptrLerpBlendType(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <LerpBlendType.LerpBlendType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <LerpFunctor.LerpFunctor> '
        elif numArgs == 4:
            import LerpFunctor
            if isinstance(_args[0], LerpFunctor.LerpFunctor):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        import LerpBlendType
                        if isinstance(_args[3], LerpBlendType.LerpBlendType):
                            return self._Lerp__overloaded_constructor_ptrLerpFunctor_float_float_ptrLerpBlendType(_args[0], _args[1], _args[2], _args[3])
                        else:
                            raise TypeError, 'Invalid argument 3, expected one of: <LerpBlendType.LerpBlendType> '
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <LerpFunctor.LerpFunctor> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 4 '


