# File: L (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
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
        
        self.constructor(*_args)

    
    def constructor(self):
        raise RuntimeError, 'No C++ constructor defined for class: ' + self.__class__.__name__

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPnJyouz6f:
            libpanda._inPnJyouz6f(self.this)
        

    
    def _LightAttrib__overloaded_make():
        returnValue = libpanda._inPnJyoZznk()
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _LightAttrib__overloaded_make = staticmethod(_LightAttrib__overloaded_make)
    
    def _LightAttrib__overloaded_make___enum__Operation_ptrLight(op, light):
        returnValue = libpanda._inPnJyoasHl(op, light.this)
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _LightAttrib__overloaded_make___enum__Operation_ptrLight = staticmethod(_LightAttrib__overloaded_make___enum__Operation_ptrLight)
    
    def _LightAttrib__overloaded_make___enum__Operation_ptrLight_ptrLight(op, light1, light2):
        returnValue = libpanda._inPnJyoVa32(op, light1.this, light2.this)
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _LightAttrib__overloaded_make___enum__Operation_ptrLight_ptrLight = staticmethod(_LightAttrib__overloaded_make___enum__Operation_ptrLight_ptrLight)
    
    def _LightAttrib__overloaded_make___enum__Operation_ptrLight_ptrLight_ptrLight(op, light1, light2, light3):
        returnValue = libpanda._inPnJyoLIAJ(op, light1.this, light2.this, light3.this)
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _LightAttrib__overloaded_make___enum__Operation_ptrLight_ptrLight_ptrLight = staticmethod(_LightAttrib__overloaded_make___enum__Operation_ptrLight_ptrLight_ptrLight)
    
    def _LightAttrib__overloaded_make___enum__Operation_ptrLight_ptrLight_ptrLight_ptrLight(op, light1, light2, light3, light4):
        returnValue = libpanda._inPnJyo6FSb(op, light1.this, light2.this, light3.this, light4.this)
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _LightAttrib__overloaded_make___enum__Operation_ptrLight_ptrLight_ptrLight_ptrLight = staticmethod(_LightAttrib__overloaded_make___enum__Operation_ptrLight_ptrLight_ptrLight_ptrLight)
    
    def makeAllOff():
        returnValue = libpanda._inPnJyo3HyF()
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    makeAllOff = staticmethod(makeAllOff)
    
    def getClassType():
        returnValue = libpanda._inPnJyojHBU()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def getOperation(self):
        returnValue = libpanda._inPnJyoI94C(self.this)
        return returnValue

    
    def getNumLights(self):
        returnValue = libpanda._inPnJyoSNtr(self.this)
        return returnValue

    
    def getLight(self, n):
        returnValue = libpanda._inPnJyowj1p(self.this, n)
        import Light
        returnObject = Light.Light(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def hasLight(self, light):
        returnValue = libpanda._inPnJyoTmqi(self.this, light.this)
        return returnValue

    
    def addLight(self, light):
        returnValue = libpanda._inPnJyo4p4X(self.this, light.this)
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def removeLight(self, light):
        returnValue = libpanda._inPnJyo_Dht(self.this, light.this)
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getNumOnLights(self):
        returnValue = libpanda._inPnJyo0Byr(self.this)
        return returnValue

    
    def getOnLight(self, n):
        returnValue = libpanda._inPnJyoGoP5(self.this, n)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def hasOnLight(self, light):
        returnValue = libpanda._inPnJyoCXs0(self.this, light.this)
        return returnValue

    
    def getNumOffLights(self):
        returnValue = libpanda._inPnJyomfMm(self.this)
        return returnValue

    
    def getOffLight(self, n):
        returnValue = libpanda._inPnJyo7rCU(self.this, n)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def hasOffLight(self, light):
        returnValue = libpanda._inPnJyo4Fzb(self.this, light.this)
        return returnValue

    
    def hasAllOff(self):
        returnValue = libpanda._inPnJyoqnRX(self.this)
        return returnValue

    
    def isIdentity(self):
        returnValue = libpanda._inPnJyo5lP4(self.this)
        return returnValue

    
    def addOnLight(self, light):
        returnValue = libpanda._inPnJyo3_7p(self.this, light.this)
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def removeOnLight(self, light):
        returnValue = libpanda._inPnJyoQ7jl(self.this, light.this)
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def addOffLight(self, light):
        returnValue = libpanda._inPnJyo6_CR(self.this, light.this)
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def removeOffLight(self, light):
        returnValue = libpanda._inPnJyoIQ_X(self.this, light.this)
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def make(*_args):
        numArgs = len(_args)
        if numArgs == 0:
            return LightAttrib._LightAttrib__overloaded_make(*_args)
        elif numArgs == 2:
            return LightAttrib._LightAttrib__overloaded_make___enum__Operation_ptrLight(*_args)
        elif numArgs == 3:
            return LightAttrib._LightAttrib__overloaded_make___enum__Operation_ptrLight_ptrLight(*_args)
        elif numArgs == 4:
            return LightAttrib._LightAttrib__overloaded_make___enum__Operation_ptrLight_ptrLight_ptrLight(*_args)
        elif numArgs == 5:
            return LightAttrib._LightAttrib__overloaded_make___enum__Operation_ptrLight_ptrLight_ptrLight_ptrLight(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 2 3 4 5 '

    make = staticmethod(make)

