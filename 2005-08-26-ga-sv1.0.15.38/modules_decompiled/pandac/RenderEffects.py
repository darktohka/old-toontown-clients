# File: R (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import TypedWritableReferenceCount

class RenderEffects(TypedWritableReferenceCount.TypedWritableReferenceCount, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self):
        raise RuntimeError, 'No C++ constructor defined for class: ' + self.__class__.__name__

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def makeEmpty():
        returnValue = libpanda._inPnJyogrKD()
        returnObject = RenderEffects(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    makeEmpty = staticmethod(makeEmpty)
    
    def _RenderEffects__overloaded_make_ptrConstRenderEffect(effect):
        returnValue = libpanda._inPnJyoiDSO(effect.this)
        returnObject = RenderEffects(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _RenderEffects__overloaded_make_ptrConstRenderEffect = staticmethod(_RenderEffects__overloaded_make_ptrConstRenderEffect)
    
    def _RenderEffects__overloaded_make_ptrConstRenderEffect_ptrConstRenderEffect(effect1, effect2):
        returnValue = libpanda._inPnJyo3y67(effect1.this, effect2.this)
        returnObject = RenderEffects(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _RenderEffects__overloaded_make_ptrConstRenderEffect_ptrConstRenderEffect = staticmethod(_RenderEffects__overloaded_make_ptrConstRenderEffect_ptrConstRenderEffect)
    
    def _RenderEffects__overloaded_make_ptrConstRenderEffect_ptrConstRenderEffect_ptrConstRenderEffect(effect1, effect2, effect3):
        returnValue = libpanda._inPnJyoZQ3C(effect1.this, effect2.this, effect3.this)
        returnObject = RenderEffects(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _RenderEffects__overloaded_make_ptrConstRenderEffect_ptrConstRenderEffect_ptrConstRenderEffect = staticmethod(_RenderEffects__overloaded_make_ptrConstRenderEffect_ptrConstRenderEffect_ptrConstRenderEffect)
    
    def _RenderEffects__overloaded_make_ptrConstRenderEffect_ptrConstRenderEffect_ptrConstRenderEffect_ptrConstRenderEffect(effect1, effect2, effect3, effect4):
        returnValue = libpanda._inPnJyozo_d(effect1.this, effect2.this, effect3.this, effect4.this)
        returnObject = RenderEffects(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _RenderEffects__overloaded_make_ptrConstRenderEffect_ptrConstRenderEffect_ptrConstRenderEffect_ptrConstRenderEffect = staticmethod(_RenderEffects__overloaded_make_ptrConstRenderEffect_ptrConstRenderEffect_ptrConstRenderEffect_ptrConstRenderEffect)
    
    def getNumStates():
        returnValue = libpanda._inPnJyoELqs()
        return returnValue

    getNumStates = staticmethod(getNumStates)
    
    def listStates(out):
        returnValue = libpanda._inPnJyoFHwJ(out.this)
        return returnValue

    listStates = staticmethod(listStates)
    
    def validateStates():
        returnValue = libpanda._inPnJyoP68o()
        return returnValue

    validateStates = staticmethod(validateStates)
    
    def getClassType():
        returnValue = libpanda._inPnJyope17()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def lessThan(self, other):
        returnValue = libpanda._inPnJyomaIr(self.this, other.this)
        return returnValue

    
    def isEmpty(self):
        returnValue = libpanda._inPnJyom56U(self.this)
        return returnValue

    
    def getNumEffects(self):
        returnValue = libpanda._inPnJyoiXcl(self.this)
        return returnValue

    
    def _RenderEffects__overloaded_getEffect_ptrConstRenderEffects_ptrTypeHandle(self, type):
        returnValue = libpanda._inPnJyo_AJ6(self.this, type.this)
        import RenderEffect
        returnObject = RenderEffect.RenderEffect(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _RenderEffects__overloaded_getEffect_ptrConstRenderEffects_int(self, n):
        returnValue = libpanda._inPnJyopvc2(self.this, n)
        import RenderEffect
        returnObject = RenderEffect.RenderEffect(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def findEffect(self, type):
        returnValue = libpanda._inPnJyoNzuE(self.this, type.this)
        return returnValue

    
    def addEffect(self, effect):
        returnValue = libpanda._inPnJyo8sn3(self.this, effect.this)
        returnObject = RenderEffects(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def removeEffect(self, type):
        returnValue = libpanda._inPnJyoNxu4(self.this, type.this)
        returnObject = RenderEffects(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def output(self, out):
        returnValue = libpanda._inPnJyoxmDR(self.this, out.this)
        return returnValue

    
    def write(self, out, indentLevel):
        returnValue = libpanda._inPnJyo_6eU(self.this, out.this, indentLevel)
        return returnValue

    
    def make(*_args):
        numArgs = len(_args)
        if numArgs == 1:
            return RenderEffects._RenderEffects__overloaded_make_ptrConstRenderEffect(*_args)
        elif numArgs == 2:
            return RenderEffects._RenderEffects__overloaded_make_ptrConstRenderEffect_ptrConstRenderEffect(*_args)
        elif numArgs == 3:
            return RenderEffects._RenderEffects__overloaded_make_ptrConstRenderEffect_ptrConstRenderEffect_ptrConstRenderEffect(*_args)
        elif numArgs == 4:
            return RenderEffects._RenderEffects__overloaded_make_ptrConstRenderEffect_ptrConstRenderEffect_ptrConstRenderEffect_ptrConstRenderEffect(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 4 '

    make = staticmethod(make)
    
    def getEffect(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._RenderEffects__overloaded_getEffect_ptrConstRenderEffects_int(*_args)
            
            import TypeHandle
            if isinstance(_args[0], TypeHandle.TypeHandle):
                return self._RenderEffects__overloaded_getEffect_ptrConstRenderEffects_ptrTypeHandle(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <TypeHandle.TypeHandle> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


