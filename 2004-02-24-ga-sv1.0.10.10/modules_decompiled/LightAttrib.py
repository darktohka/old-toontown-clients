# File: L (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import RenderAttrib

class LightAttrib(RenderAttrib.RenderAttrib, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    OAdd = 1
    ORemove = 2
    OSet = 0
    
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
        

    
    def destructor(self):
        if libpanda and libpanda._inPkJyouz6f:
            libpanda._inPkJyouz6f(self.this)
        

    
    def makeAllOff():
        returnValue = libpanda._inPkJyo3HyF()
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    makeAllOff = staticmethod(makeAllOff)
    
    def _LightAttrib__overloaded_make___enum__Operation_ptrLight(op, light):
        returnValue = libpanda._inPkJyobsHl(op, light.this)
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _LightAttrib__overloaded_make___enum__Operation_ptrLight = staticmethod(_LightAttrib__overloaded_make___enum__Operation_ptrLight)
    
    def _LightAttrib__overloaded_make___enum__Operation_ptrLight_ptrLight(op, light1, light2):
        returnValue = libpanda._inPkJyoUa32(op, light1.this, light2.this)
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _LightAttrib__overloaded_make___enum__Operation_ptrLight_ptrLight = staticmethod(_LightAttrib__overloaded_make___enum__Operation_ptrLight_ptrLight)
    
    def _LightAttrib__overloaded_make___enum__Operation_ptrLight_ptrLight_ptrLight(op, light1, light2, light3):
        returnValue = libpanda._inPkJyoLIAJ(op, light1.this, light2.this, light3.this)
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _LightAttrib__overloaded_make___enum__Operation_ptrLight_ptrLight_ptrLight = staticmethod(_LightAttrib__overloaded_make___enum__Operation_ptrLight_ptrLight_ptrLight)
    
    def _LightAttrib__overloaded_make___enum__Operation_ptrLight_ptrLight_ptrLight_ptrLight(op, light1, light2, light3, light4):
        returnValue = libpanda._inPkJyo6FSb(op, light1.this, light2.this, light3.this, light4.this)
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _LightAttrib__overloaded_make___enum__Operation_ptrLight_ptrLight_ptrLight_ptrLight = staticmethod(_LightAttrib__overloaded_make___enum__Operation_ptrLight_ptrLight_ptrLight_ptrLight)
    
    def getClassType():
        returnValue = libpanda._inPkJyojHBU()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def getOperation(self):
        returnValue = libpanda._inPkJyoI94C(self.this)
        return returnValue

    
    def getNumLights(self):
        returnValue = libpanda._inPkJyoRNtr(self.this)
        return returnValue

    
    def getLight(self, n):
        returnValue = libpanda._inPkJyoxj1p(self.this, n)
        import Light
        returnObject = Light.Light(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def hasLight(self, light):
        returnValue = libpanda._inPkJyosmqi(self.this, light.this)
        return returnValue

    
    def addLight(self, light):
        returnValue = libpanda._inPkJyo4p4X(self.this, light.this)
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def removeLight(self, light):
        returnValue = libpanda._inPkJyo9Dht(self.this, light.this)
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def isIdentity(self):
        returnValue = libpanda._inPkJyo4lP4(self.this)
        return returnValue

    
    def isAllOff(self):
        returnValue = libpanda._inPkJyoAeP1(self.this)
        return returnValue

    
    def make(*_args):
        numArgs = len(_args)
        if numArgs == 2:
            if isinstance(_args[0], types.IntType):
                import Light
                if isinstance(_args[1], Light.Light):
                    return LightAttrib._LightAttrib__overloaded_make___enum__Operation_ptrLight(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <Light.Light> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        elif numArgs == 3:
            if isinstance(_args[0], types.IntType):
                import Light
                if isinstance(_args[1], Light.Light):
                    import Light
                    if isinstance(_args[2], Light.Light):
                        return LightAttrib._LightAttrib__overloaded_make___enum__Operation_ptrLight_ptrLight(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <Light.Light> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <Light.Light> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        elif numArgs == 4:
            if isinstance(_args[0], types.IntType):
                import Light
                if isinstance(_args[1], Light.Light):
                    import Light
                    if isinstance(_args[2], Light.Light):
                        import Light
                        if isinstance(_args[3], Light.Light):
                            return LightAttrib._LightAttrib__overloaded_make___enum__Operation_ptrLight_ptrLight_ptrLight(_args[0], _args[1], _args[2], _args[3])
                        else:
                            raise TypeError, 'Invalid argument 3, expected one of: <Light.Light> '
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <Light.Light> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <Light.Light> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        elif numArgs == 5:
            if isinstance(_args[0], types.IntType):
                import Light
                if isinstance(_args[1], Light.Light):
                    import Light
                    if isinstance(_args[2], Light.Light):
                        import Light
                        if isinstance(_args[3], Light.Light):
                            import Light
                            if isinstance(_args[4], Light.Light):
                                return LightAttrib._LightAttrib__overloaded_make___enum__Operation_ptrLight_ptrLight_ptrLight_ptrLight(_args[0], _args[1], _args[2], _args[3], _args[4])
                            else:
                                raise TypeError, 'Invalid argument 4, expected one of: <Light.Light> '
                        else:
                            raise TypeError, 'Invalid argument 3, expected one of: <Light.Light> '
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <Light.Light> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <Light.Light> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 4 5 '

    make = staticmethod(make)

