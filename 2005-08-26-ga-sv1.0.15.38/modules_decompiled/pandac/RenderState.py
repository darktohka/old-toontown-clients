# File: R (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import CachedTypedWritableReferenceCount

class RenderState(CachedTypedWritableReferenceCount.CachedTypedWritableReferenceCount, FFIExternalObject.FFIExternalObject):
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
        returnValue = libpanda._inPnJyoGuHJ()
        returnObject = RenderState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    makeEmpty = staticmethod(makeEmpty)
    
    def _RenderState__overloaded_make_ptrConstRenderAttrib_ptrConstRenderAttrib_ptrConstRenderAttrib_ptrConstRenderAttrib_int(attrib1, attrib2, attrib3, attrib4, override):
        returnValue = libpanda._inPnJyoRRYz(attrib1.this, attrib2.this, attrib3.this, attrib4.this, override)
        returnObject = RenderState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _RenderState__overloaded_make_ptrConstRenderAttrib_ptrConstRenderAttrib_ptrConstRenderAttrib_ptrConstRenderAttrib_int = staticmethod(_RenderState__overloaded_make_ptrConstRenderAttrib_ptrConstRenderAttrib_ptrConstRenderAttrib_ptrConstRenderAttrib_int)
    
    def _RenderState__overloaded_make_ptrConstRenderAttrib_ptrConstRenderAttrib_ptrConstRenderAttrib_ptrConstRenderAttrib(attrib1, attrib2, attrib3, attrib4):
        returnValue = libpanda._inPnJyojeWF(attrib1.this, attrib2.this, attrib3.this, attrib4.this)
        returnObject = RenderState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _RenderState__overloaded_make_ptrConstRenderAttrib_ptrConstRenderAttrib_ptrConstRenderAttrib_ptrConstRenderAttrib = staticmethod(_RenderState__overloaded_make_ptrConstRenderAttrib_ptrConstRenderAttrib_ptrConstRenderAttrib_ptrConstRenderAttrib)
    
    def _RenderState__overloaded_make_ptrConstRenderAttrib_ptrConstRenderAttrib_ptrConstRenderAttrib_int(attrib1, attrib2, attrib3, override):
        returnValue = libpanda._inPnJyoK6X3(attrib1.this, attrib2.this, attrib3.this, override)
        returnObject = RenderState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _RenderState__overloaded_make_ptrConstRenderAttrib_ptrConstRenderAttrib_ptrConstRenderAttrib_int = staticmethod(_RenderState__overloaded_make_ptrConstRenderAttrib_ptrConstRenderAttrib_ptrConstRenderAttrib_int)
    
    def _RenderState__overloaded_make_ptrConstRenderAttrib_ptrConstRenderAttrib_ptrConstRenderAttrib(attrib1, attrib2, attrib3):
        returnValue = libpanda._inPnJyobtvX(attrib1.this, attrib2.this, attrib3.this)
        returnObject = RenderState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _RenderState__overloaded_make_ptrConstRenderAttrib_ptrConstRenderAttrib_ptrConstRenderAttrib = staticmethod(_RenderState__overloaded_make_ptrConstRenderAttrib_ptrConstRenderAttrib_ptrConstRenderAttrib)
    
    def _RenderState__overloaded_make_ptrConstRenderAttrib_ptrConstRenderAttrib_int(attrib1, attrib2, override):
        returnValue = libpanda._inPnJyou7vK(attrib1.this, attrib2.this, override)
        returnObject = RenderState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _RenderState__overloaded_make_ptrConstRenderAttrib_ptrConstRenderAttrib_int = staticmethod(_RenderState__overloaded_make_ptrConstRenderAttrib_ptrConstRenderAttrib_int)
    
    def _RenderState__overloaded_make_ptrConstRenderAttrib_ptrConstRenderAttrib(attrib1, attrib2):
        returnValue = libpanda._inPnJyoSK5z(attrib1.this, attrib2.this)
        returnObject = RenderState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _RenderState__overloaded_make_ptrConstRenderAttrib_ptrConstRenderAttrib = staticmethod(_RenderState__overloaded_make_ptrConstRenderAttrib_ptrConstRenderAttrib)
    
    def _RenderState__overloaded_make_ptrConstRenderAttrib_int(attrib, override):
        returnValue = libpanda._inPnJyoiqB_(attrib.this, override)
        returnObject = RenderState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _RenderState__overloaded_make_ptrConstRenderAttrib_int = staticmethod(_RenderState__overloaded_make_ptrConstRenderAttrib_int)
    
    def _RenderState__overloaded_make_ptrConstRenderAttrib(attrib):
        returnValue = libpanda._inPnJyoT9E9(attrib.this)
        returnObject = RenderState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _RenderState__overloaded_make_ptrConstRenderAttrib = staticmethod(_RenderState__overloaded_make_ptrConstRenderAttrib)
    
    def getMaxPriority():
        returnValue = libpanda._inPnJyoV3mc()
        return returnValue

    getMaxPriority = staticmethod(getMaxPriority)
    
    def getNumStates():
        returnValue = libpanda._inPnJyoSXJI()
        return returnValue

    getNumStates = staticmethod(getNumStates)
    
    def getNumUnusedStates():
        returnValue = libpanda._inPnJyoB8ph()
        return returnValue

    getNumUnusedStates = staticmethod(getNumUnusedStates)
    
    def clearCache():
        returnValue = libpanda._inPnJyofP1U()
        return returnValue

    clearCache = staticmethod(clearCache)
    
    def listCycles(out):
        returnValue = libpanda._inPnJyoyu1u(out.this)
        return returnValue

    listCycles = staticmethod(listCycles)
    
    def listStates(out):
        returnValue = libpanda._inPnJyoMySM(out.this)
        return returnValue

    listStates = staticmethod(listStates)
    
    def validateStates():
        returnValue = libpanda._inPnJyoYm1k()
        return returnValue

    validateStates = staticmethod(validateStates)
    
    def getClassType():
        returnValue = libpanda._inPnJyoF592()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def lessThan(self, other):
        returnValue = libpanda._inPnJyoAt5L(self.this, other.this)
        return returnValue

    
    def isEmpty(self):
        returnValue = libpanda._inPnJyobG0o(self.this)
        return returnValue

    
    def getNumAttribs(self):
        returnValue = libpanda._inPnJyo3N6n(self.this)
        return returnValue

    
    def _RenderState__overloaded_getAttrib_ptrConstRenderState_ptrTypeHandle(self, type):
        returnValue = libpanda._inPnJyoQqmu(self.this, type.this)
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _RenderState__overloaded_getAttrib_ptrConstRenderState_int(self, n):
        returnValue = libpanda._inPnJyoUEFr(self.this, n)
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _RenderState__overloaded_getOverride_ptrConstRenderState_ptrTypeHandle(self, type):
        returnValue = libpanda._inPnJyouZNq(self.this, type.this)
        return returnValue

    
    def _RenderState__overloaded_getOverride_ptrConstRenderState_int(self, n):
        returnValue = libpanda._inPnJyobchm(self.this, n)
        return returnValue

    
    def findAttrib(self, type):
        returnValue = libpanda._inPnJyoH_dV(self.this, type.this)
        return returnValue

    
    def compose(self, other):
        returnValue = libpanda._inPnJyosYED(self.this, other.this)
        returnObject = RenderState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def invertCompose(self, other):
        returnValue = libpanda._inPnJyo_7EZ(self.this, other.this)
        returnObject = RenderState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _RenderState__overloaded_addAttrib_ptrConstRenderState_ptrConstRenderAttrib_int(self, attrib, override):
        returnValue = libpanda._inPnJyoMVE4(self.this, attrib.this, override)
        returnObject = RenderState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _RenderState__overloaded_addAttrib_ptrConstRenderState_ptrConstRenderAttrib(self, attrib):
        returnValue = libpanda._inPnJyoyvO6(self.this, attrib.this)
        returnObject = RenderState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def removeAttrib(self, type):
        returnValue = libpanda._inPnJyoyYRK(self.this, type.this)
        returnObject = RenderState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def adjustAllPriorities(self, adjustment):
        returnValue = libpanda._inPnJyo_mZy(self.this, adjustment)
        returnObject = RenderState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def unref(self):
        returnValue = libpanda._inPnJyoevlZ(self.this)
        return returnValue

    
    def output(self, out):
        returnValue = libpanda._inPnJyo5YiO(self.this, out.this)
        return returnValue

    
    def write(self, out, indentLevel):
        returnValue = libpanda._inPnJyoArA3(self.this, out.this, indentLevel)
        return returnValue

    
    def getDrawOrder(self):
        returnValue = libpanda._inPnJyowxn3(self.this)
        return returnValue

    
    def getFog(self):
        returnValue = libpanda._inPnJyosPK8(self.this)
        import FogAttrib
        returnObject = FogAttrib.FogAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject.setPointer()

    
    def getBin(self):
        returnValue = libpanda._inPnJyoqXWB(self.this)
        import CullBinAttrib
        returnObject = CullBinAttrib.CullBinAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject.setPointer()

    
    def getTransparency(self):
        returnValue = libpanda._inPnJyoRM0R(self.this)
        import TransparencyAttrib
        returnObject = TransparencyAttrib.TransparencyAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject.setPointer()

    
    def getBinIndex(self):
        returnValue = libpanda._inPnJyoP6sb(self.this)
        return returnValue

    
    def make(*_args):
        numArgs = len(_args)
        if numArgs == 1:
            return RenderState._RenderState__overloaded_make_ptrConstRenderAttrib(*_args)
        elif numArgs == 2:
            import RenderAttrib
            if isinstance(_args[0], RenderAttrib.RenderAttrib):
                if isinstance(_args[1], types.IntType) or isinstance(_args[1], types.LongType):
                    return RenderState._RenderState__overloaded_make_ptrConstRenderAttrib_int(*_args)
                
                import RenderAttrib
                if isinstance(_args[1], RenderAttrib.RenderAttrib):
                    return RenderState._RenderState__overloaded_make_ptrConstRenderAttrib_ptrConstRenderAttrib(*_args)
                
                raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> <RenderAttrib.RenderAttrib> '
            
            raise TypeError, 'Invalid argument 0, expected one of: <RenderAttrib.RenderAttrib> '
        elif numArgs == 3:
            import RenderAttrib
            if isinstance(_args[0], RenderAttrib.RenderAttrib):
                import RenderAttrib
                if isinstance(_args[1], RenderAttrib.RenderAttrib):
                    if isinstance(_args[2], types.IntType) or isinstance(_args[2], types.LongType):
                        return RenderState._RenderState__overloaded_make_ptrConstRenderAttrib_ptrConstRenderAttrib_int(*_args)
                    
                    import RenderAttrib
                    if isinstance(_args[2], RenderAttrib.RenderAttrib):
                        return RenderState._RenderState__overloaded_make_ptrConstRenderAttrib_ptrConstRenderAttrib_ptrConstRenderAttrib(*_args)
                    
                    raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> <RenderAttrib.RenderAttrib> '
                
                raise TypeError, 'Invalid argument 1, expected one of: <RenderAttrib.RenderAttrib> '
            
            raise TypeError, 'Invalid argument 0, expected one of: <RenderAttrib.RenderAttrib> '
        elif numArgs == 4:
            import RenderAttrib
            if isinstance(_args[0], RenderAttrib.RenderAttrib):
                import RenderAttrib
                if isinstance(_args[1], RenderAttrib.RenderAttrib):
                    import RenderAttrib
                    if isinstance(_args[2], RenderAttrib.RenderAttrib):
                        if isinstance(_args[3], types.IntType) or isinstance(_args[3], types.LongType):
                            return RenderState._RenderState__overloaded_make_ptrConstRenderAttrib_ptrConstRenderAttrib_ptrConstRenderAttrib_int(*_args)
                        
                        import RenderAttrib
                        if isinstance(_args[3], RenderAttrib.RenderAttrib):
                            return RenderState._RenderState__overloaded_make_ptrConstRenderAttrib_ptrConstRenderAttrib_ptrConstRenderAttrib_ptrConstRenderAttrib(*_args)
                        
                        raise TypeError, 'Invalid argument 3, expected one of: <types.IntType> <RenderAttrib.RenderAttrib> '
                    
                    raise TypeError, 'Invalid argument 2, expected one of: <RenderAttrib.RenderAttrib> '
                
                raise TypeError, 'Invalid argument 1, expected one of: <RenderAttrib.RenderAttrib> '
            
            raise TypeError, 'Invalid argument 0, expected one of: <RenderAttrib.RenderAttrib> '
        elif numArgs == 5:
            return RenderState._RenderState__overloaded_make_ptrConstRenderAttrib_ptrConstRenderAttrib_ptrConstRenderAttrib_ptrConstRenderAttrib_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 4 5 '

    make = staticmethod(make)
    
    def getAttrib(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._RenderState__overloaded_getAttrib_ptrConstRenderState_int(*_args)
            
            import TypeHandle
            if isinstance(_args[0], TypeHandle.TypeHandle):
                return self._RenderState__overloaded_getAttrib_ptrConstRenderState_ptrTypeHandle(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <TypeHandle.TypeHandle> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def addAttrib(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._RenderState__overloaded_addAttrib_ptrConstRenderState_ptrConstRenderAttrib(*_args)
        elif numArgs == 2:
            return self._RenderState__overloaded_addAttrib_ptrConstRenderState_ptrConstRenderAttrib_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def getOverride(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
                return self._RenderState__overloaded_getOverride_ptrConstRenderState_int(*_args)
            
            import TypeHandle
            if isinstance(_args[0], TypeHandle.TypeHandle):
                return self._RenderState__overloaded_getOverride_ptrConstRenderState_ptrTypeHandle(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <TypeHandle.TypeHandle> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


