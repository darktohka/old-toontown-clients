# File: R (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import TypedWritableReferenceCount

class RenderEffects(TypedWritableReferenceCount.TypedWritableReferenceCount, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self):
        raise RuntimeError, 'No C++ constructor defined for class: ' + self.__class__.__name__

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def makeEmpty():
        returnValue = libpanda._inPkJyogrKD()
        returnObject = RenderEffects(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    makeEmpty = staticmethod(makeEmpty)
    
    def _RenderEffects__overloaded_make_ptrConstRenderEffect(effect):
        returnValue = libpanda._inPkJyoiDSO(effect.this)
        returnObject = RenderEffects(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _RenderEffects__overloaded_make_ptrConstRenderEffect = staticmethod(_RenderEffects__overloaded_make_ptrConstRenderEffect)
    
    def _RenderEffects__overloaded_make_ptrConstRenderEffect_ptrConstRenderEffect(effect1, effect2):
        returnValue = libpanda._inPkJyo2y67(effect1.this, effect2.this)
        returnObject = RenderEffects(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _RenderEffects__overloaded_make_ptrConstRenderEffect_ptrConstRenderEffect = staticmethod(_RenderEffects__overloaded_make_ptrConstRenderEffect_ptrConstRenderEffect)
    
    def _RenderEffects__overloaded_make_ptrConstRenderEffect_ptrConstRenderEffect_ptrConstRenderEffect(effect1, effect2, effect3):
        returnValue = libpanda._inPkJyoZQ3C(effect1.this, effect2.this, effect3.this)
        returnObject = RenderEffects(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _RenderEffects__overloaded_make_ptrConstRenderEffect_ptrConstRenderEffect_ptrConstRenderEffect = staticmethod(_RenderEffects__overloaded_make_ptrConstRenderEffect_ptrConstRenderEffect_ptrConstRenderEffect)
    
    def _RenderEffects__overloaded_make_ptrConstRenderEffect_ptrConstRenderEffect_ptrConstRenderEffect_ptrConstRenderEffect(effect1, effect2, effect3, effect4):
        returnValue = libpanda._inPkJyozo_d(effect1.this, effect2.this, effect3.this, effect4.this)
        returnObject = RenderEffects(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _RenderEffects__overloaded_make_ptrConstRenderEffect_ptrConstRenderEffect_ptrConstRenderEffect_ptrConstRenderEffect = staticmethod(_RenderEffects__overloaded_make_ptrConstRenderEffect_ptrConstRenderEffect_ptrConstRenderEffect_ptrConstRenderEffect)
    
    def getClassType():
        returnValue = libpanda._inPkJyoqe17()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def isEmpty(self):
        returnValue = libpanda._inPkJyom56U(self.this)
        return returnValue

    
    def getNumEffects(self):
        returnValue = libpanda._inPkJyojXcl(self.this)
        return returnValue

    
    def _RenderEffects__overloaded_getEffect_ptrConstRenderEffects_ptrTypeHandle(self, type):
        returnValue = libpanda._inPkJyo8AJ6(self.this, type.this)
        import RenderEffect
        returnObject = RenderEffect.RenderEffect(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _RenderEffects__overloaded_getEffect_ptrConstRenderEffects_int(self, n):
        returnValue = libpanda._inPkJyouvc2(self.this, n)
        import RenderEffect
        returnObject = RenderEffect.RenderEffect(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def findEffect(self, type):
        returnValue = libpanda._inPkJyoNzuE(self.this, type.this)
        return returnValue

    
    def addEffect(self, effect):
        returnValue = libpanda._inPkJyo9sn3(self.this, effect.this)
        returnObject = RenderEffects(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def removeEffect(self, type):
        returnValue = libpanda._inPkJyoMxu4(self.this, type.this)
        returnObject = RenderEffects(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def output(self, out):
        returnValue = libpanda._inPkJyoxmDR(self.this, out.this)
        return returnValue

    
    def write(self, out, indentLevel):
        returnValue = libpanda._inPkJyo_6eU(self.this, out.this, indentLevel)
        return returnValue

    
    def make(*_args):
        numArgs = len(_args)
        if numArgs == 1:
            import RenderEffect
            if isinstance(_args[0], RenderEffect.RenderEffect):
                return RenderEffects._RenderEffects__overloaded_make_ptrConstRenderEffect(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <RenderEffect.RenderEffect> '
        elif numArgs == 2:
            import RenderEffect
            if isinstance(_args[0], RenderEffect.RenderEffect):
                import RenderEffect
                if isinstance(_args[1], RenderEffect.RenderEffect):
                    return RenderEffects._RenderEffects__overloaded_make_ptrConstRenderEffect_ptrConstRenderEffect(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <RenderEffect.RenderEffect> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <RenderEffect.RenderEffect> '
        elif numArgs == 3:
            import RenderEffect
            if isinstance(_args[0], RenderEffect.RenderEffect):
                import RenderEffect
                if isinstance(_args[1], RenderEffect.RenderEffect):
                    import RenderEffect
                    if isinstance(_args[2], RenderEffect.RenderEffect):
                        return RenderEffects._RenderEffects__overloaded_make_ptrConstRenderEffect_ptrConstRenderEffect_ptrConstRenderEffect(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <RenderEffect.RenderEffect> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <RenderEffect.RenderEffect> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <RenderEffect.RenderEffect> '
        elif numArgs == 4:
            import RenderEffect
            if isinstance(_args[0], RenderEffect.RenderEffect):
                import RenderEffect
                if isinstance(_args[1], RenderEffect.RenderEffect):
                    import RenderEffect
                    if isinstance(_args[2], RenderEffect.RenderEffect):
                        import RenderEffect
                        if isinstance(_args[3], RenderEffect.RenderEffect):
                            return RenderEffects._RenderEffects__overloaded_make_ptrConstRenderEffect_ptrConstRenderEffect_ptrConstRenderEffect_ptrConstRenderEffect(_args[0], _args[1], _args[2], _args[3])
                        else:
                            raise TypeError, 'Invalid argument 3, expected one of: <RenderEffect.RenderEffect> '
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <RenderEffect.RenderEffect> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <RenderEffect.RenderEffect> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <RenderEffect.RenderEffect> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 4 '

    make = staticmethod(make)
    
    def getEffect(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import TypeHandle
            if isinstance(_args[0], types.IntType):
                return self._RenderEffects__overloaded_getEffect_ptrConstRenderEffects_int(_args[0])
            elif isinstance(_args[0], TypeHandle.TypeHandle):
                return self._RenderEffects__overloaded_getEffect_ptrConstRenderEffects_ptrTypeHandle(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <TypeHandle.TypeHandle> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


