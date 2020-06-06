# File: R (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import TypedWritableReferenceCount

class RenderState(TypedWritableReferenceCount.TypedWritableReferenceCount, FFIExternalObject.FFIExternalObject):
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
        returnValue = libpanda._inPkJyoGuHJ()
        returnObject = RenderState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    makeEmpty = staticmethod(makeEmpty)
    
    def _RenderState__overloaded_make_ptrConstRenderAttrib_ptrConstRenderAttrib_ptrConstRenderAttrib_ptrConstRenderAttrib_int(attrib1, attrib2, attrib3, attrib4, override):
        returnValue = libpanda._inPkJyoSRYz(attrib1.this, attrib2.this, attrib3.this, attrib4.this, override)
        returnObject = RenderState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _RenderState__overloaded_make_ptrConstRenderAttrib_ptrConstRenderAttrib_ptrConstRenderAttrib_ptrConstRenderAttrib_int = staticmethod(_RenderState__overloaded_make_ptrConstRenderAttrib_ptrConstRenderAttrib_ptrConstRenderAttrib_ptrConstRenderAttrib_int)
    
    def _RenderState__overloaded_make_ptrConstRenderAttrib_ptrConstRenderAttrib_ptrConstRenderAttrib_ptrConstRenderAttrib(attrib1, attrib2, attrib3, attrib4):
        returnValue = libpanda._inPkJyojeWF(attrib1.this, attrib2.this, attrib3.this, attrib4.this)
        returnObject = RenderState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _RenderState__overloaded_make_ptrConstRenderAttrib_ptrConstRenderAttrib_ptrConstRenderAttrib_ptrConstRenderAttrib = staticmethod(_RenderState__overloaded_make_ptrConstRenderAttrib_ptrConstRenderAttrib_ptrConstRenderAttrib_ptrConstRenderAttrib)
    
    def _RenderState__overloaded_make_ptrConstRenderAttrib_ptrConstRenderAttrib_ptrConstRenderAttrib_int(attrib1, attrib2, attrib3, override):
        returnValue = libpanda._inPkJyoJ6X3(attrib1.this, attrib2.this, attrib3.this, override)
        returnObject = RenderState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _RenderState__overloaded_make_ptrConstRenderAttrib_ptrConstRenderAttrib_ptrConstRenderAttrib_int = staticmethod(_RenderState__overloaded_make_ptrConstRenderAttrib_ptrConstRenderAttrib_ptrConstRenderAttrib_int)
    
    def _RenderState__overloaded_make_ptrConstRenderAttrib_ptrConstRenderAttrib_ptrConstRenderAttrib(attrib1, attrib2, attrib3):
        returnValue = libpanda._inPkJyobtvX(attrib1.this, attrib2.this, attrib3.this)
        returnObject = RenderState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _RenderState__overloaded_make_ptrConstRenderAttrib_ptrConstRenderAttrib_ptrConstRenderAttrib = staticmethod(_RenderState__overloaded_make_ptrConstRenderAttrib_ptrConstRenderAttrib_ptrConstRenderAttrib)
    
    def _RenderState__overloaded_make_ptrConstRenderAttrib_ptrConstRenderAttrib_int(attrib1, attrib2, override):
        returnValue = libpanda._inPkJyou7vK(attrib1.this, attrib2.this, override)
        returnObject = RenderState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _RenderState__overloaded_make_ptrConstRenderAttrib_ptrConstRenderAttrib_int = staticmethod(_RenderState__overloaded_make_ptrConstRenderAttrib_ptrConstRenderAttrib_int)
    
    def _RenderState__overloaded_make_ptrConstRenderAttrib_ptrConstRenderAttrib(attrib1, attrib2):
        returnValue = libpanda._inPkJyodK5z(attrib1.this, attrib2.this)
        returnObject = RenderState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _RenderState__overloaded_make_ptrConstRenderAttrib_ptrConstRenderAttrib = staticmethod(_RenderState__overloaded_make_ptrConstRenderAttrib_ptrConstRenderAttrib)
    
    def _RenderState__overloaded_make_ptrConstRenderAttrib_int(attrib, override):
        returnValue = libpanda._inPkJyojqB_(attrib.this, override)
        returnObject = RenderState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _RenderState__overloaded_make_ptrConstRenderAttrib_int = staticmethod(_RenderState__overloaded_make_ptrConstRenderAttrib_int)
    
    def _RenderState__overloaded_make_ptrConstRenderAttrib(attrib):
        returnValue = libpanda._inPkJyoQ9E9(attrib.this)
        returnObject = RenderState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _RenderState__overloaded_make_ptrConstRenderAttrib = staticmethod(_RenderState__overloaded_make_ptrConstRenderAttrib)
    
    def getMaxPriority():
        returnValue = libpanda._inPkJyoV3mc()
        return returnValue

    getMaxPriority = staticmethod(getMaxPriority)
    
    def getNumStates():
        returnValue = libpanda._inPkJyoSXJI()
        return returnValue

    getNumStates = staticmethod(getNumStates)
    
    def getNumUnusedStates():
        returnValue = libpanda._inPkJyoA8ph()
        return returnValue

    getNumUnusedStates = staticmethod(getNumUnusedStates)
    
    def clearCache():
        returnValue = libpanda._inPkJyofP1U()
        return returnValue

    clearCache = staticmethod(clearCache)
    
    def getClassType():
        returnValue = libpanda._inPkJyo6592()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def isEmpty(self):
        returnValue = libpanda._inPkJyocG0o(self.this)
        return returnValue

    
    def getNumAttribs(self):
        returnValue = libpanda._inPkJyo4N6n(self.this)
        return returnValue

    
    def _RenderState__overloaded_getAttrib_ptrConstRenderState_ptrTypeHandle(self, type):
        returnValue = libpanda._inPkJyoRqmu(self.this, type.this)
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _RenderState__overloaded_getAttrib_ptrConstRenderState_int(self, n):
        returnValue = libpanda._inPkJyoVEFr(self.this, n)
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getOverride(self, n):
        returnValue = libpanda._inPkJyoUchm(self.this, n)
        return returnValue

    
    def findAttrib(self, type):
        returnValue = libpanda._inPkJyoH_dV(self.this, type.this)
        return returnValue

    
    def compose(self, other):
        returnValue = libpanda._inPkJyosYED(self.this, other.this)
        returnObject = RenderState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def invertCompose(self, other):
        returnValue = libpanda._inPkJyo_7EZ(self.this, other.this)
        returnObject = RenderState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _RenderState__overloaded_addAttrib_ptrConstRenderState_ptrConstRenderAttrib_int(self, attrib, override):
        returnValue = libpanda._inPkJyoNVE4(self.this, attrib.this, override)
        returnObject = RenderState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _RenderState__overloaded_addAttrib_ptrConstRenderState_ptrConstRenderAttrib(self, attrib):
        returnValue = libpanda._inPkJyozvO6(self.this, attrib.this)
        returnObject = RenderState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def removeAttrib(self, type):
        returnValue = libpanda._inPkJyoyYRK(self.this, type.this)
        returnObject = RenderState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def adjustAllPriorities(self, adjustment):
        returnValue = libpanda._inPkJyo4mZy(self.this, adjustment)
        returnObject = RenderState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def output(self, out):
        returnValue = libpanda._inPkJyo5YiO(self.this, out.this)
        return returnValue

    
    def write(self, out, indentLevel):
        returnValue = libpanda._inPkJyoBrA3(self.this, out.this, indentLevel)
        return returnValue

    
    def getDrawOrder(self):
        returnValue = libpanda._inPkJyozxn3(self.this)
        return returnValue

    
    def getFog(self):
        returnValue = libpanda._inPkJyojPK8(self.this)
        import FogAttrib
        returnObject = FogAttrib.FogAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject.setPointer()

    
    def getBin(self):
        returnValue = libpanda._inPkJyoqXWB(self.this)
        import CullBinAttrib
        returnObject = CullBinAttrib.CullBinAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject.setPointer()

    
    def getTransparency(self):
        returnValue = libpanda._inPkJyoRM0R(self.this)
        import TransparencyAttrib
        returnObject = TransparencyAttrib.TransparencyAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject.setPointer()

    
    def getBinIndex(self):
        returnValue = libpanda._inPkJyoP6sb(self.this)
        return returnValue

    
    def make(*_args):
        numArgs = len(_args)
        if numArgs == 1:
            import RenderAttrib
            if isinstance(_args[0], RenderAttrib.RenderAttrib):
                return RenderState._RenderState__overloaded_make_ptrConstRenderAttrib(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <RenderAttrib.RenderAttrib> '
        elif numArgs == 2:
            import RenderAttrib
            if isinstance(_args[0], RenderAttrib.RenderAttrib):
                import RenderAttrib
                if isinstance(_args[1], types.IntType):
                    return RenderState._RenderState__overloaded_make_ptrConstRenderAttrib_int(_args[0], _args[1])
                elif isinstance(_args[1], RenderAttrib.RenderAttrib):
                    return RenderState._RenderState__overloaded_make_ptrConstRenderAttrib_ptrConstRenderAttrib(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> <RenderAttrib.RenderAttrib> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <RenderAttrib.RenderAttrib> '
        elif numArgs == 3:
            import RenderAttrib
            if isinstance(_args[0], RenderAttrib.RenderAttrib):
                import RenderAttrib
                if isinstance(_args[1], RenderAttrib.RenderAttrib):
                    import RenderAttrib
                    if isinstance(_args[2], types.IntType):
                        return RenderState._RenderState__overloaded_make_ptrConstRenderAttrib_ptrConstRenderAttrib_int(_args[0], _args[1], _args[2])
                    elif isinstance(_args[2], RenderAttrib.RenderAttrib):
                        return RenderState._RenderState__overloaded_make_ptrConstRenderAttrib_ptrConstRenderAttrib_ptrConstRenderAttrib(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> <RenderAttrib.RenderAttrib> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <RenderAttrib.RenderAttrib> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <RenderAttrib.RenderAttrib> '
        elif numArgs == 4:
            import RenderAttrib
            if isinstance(_args[0], RenderAttrib.RenderAttrib):
                import RenderAttrib
                if isinstance(_args[1], RenderAttrib.RenderAttrib):
                    import RenderAttrib
                    if isinstance(_args[2], RenderAttrib.RenderAttrib):
                        import RenderAttrib
                        if isinstance(_args[3], types.IntType):
                            return RenderState._RenderState__overloaded_make_ptrConstRenderAttrib_ptrConstRenderAttrib_ptrConstRenderAttrib_int(_args[0], _args[1], _args[2], _args[3])
                        elif isinstance(_args[3], RenderAttrib.RenderAttrib):
                            return RenderState._RenderState__overloaded_make_ptrConstRenderAttrib_ptrConstRenderAttrib_ptrConstRenderAttrib_ptrConstRenderAttrib(_args[0], _args[1], _args[2], _args[3])
                        else:
                            raise TypeError, 'Invalid argument 3, expected one of: <types.IntType> <RenderAttrib.RenderAttrib> '
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <RenderAttrib.RenderAttrib> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <RenderAttrib.RenderAttrib> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <RenderAttrib.RenderAttrib> '
        elif numArgs == 5:
            import RenderAttrib
            if isinstance(_args[0], RenderAttrib.RenderAttrib):
                import RenderAttrib
                if isinstance(_args[1], RenderAttrib.RenderAttrib):
                    import RenderAttrib
                    if isinstance(_args[2], RenderAttrib.RenderAttrib):
                        import RenderAttrib
                        if isinstance(_args[3], RenderAttrib.RenderAttrib):
                            if isinstance(_args[4], types.IntType):
                                return RenderState._RenderState__overloaded_make_ptrConstRenderAttrib_ptrConstRenderAttrib_ptrConstRenderAttrib_ptrConstRenderAttrib_int(_args[0], _args[1], _args[2], _args[3], _args[4])
                            else:
                                raise TypeError, 'Invalid argument 4, expected one of: <types.IntType> '
                        else:
                            raise TypeError, 'Invalid argument 3, expected one of: <RenderAttrib.RenderAttrib> '
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <RenderAttrib.RenderAttrib> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <RenderAttrib.RenderAttrib> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <RenderAttrib.RenderAttrib> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 4 5 '

    make = staticmethod(make)
    
    def getAttrib(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import TypeHandle
            if isinstance(_args[0], types.IntType):
                return self._RenderState__overloaded_getAttrib_ptrConstRenderState_int(_args[0])
            elif isinstance(_args[0], TypeHandle.TypeHandle):
                return self._RenderState__overloaded_getAttrib_ptrConstRenderState_ptrTypeHandle(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <TypeHandle.TypeHandle> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    
    def addAttrib(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import RenderAttrib
            if isinstance(_args[0], RenderAttrib.RenderAttrib):
                return self._RenderState__overloaded_addAttrib_ptrConstRenderState_ptrConstRenderAttrib(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <RenderAttrib.RenderAttrib> '
        elif numArgs == 2:
            import RenderAttrib
            if isinstance(_args[0], RenderAttrib.RenderAttrib):
                if isinstance(_args[1], types.IntType):
                    return self._RenderState__overloaded_addAttrib_ptrConstRenderState_ptrConstRenderAttrib_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <RenderAttrib.RenderAttrib> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


