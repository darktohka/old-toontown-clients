# File: P (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import RenderEffect

class PolylightEffect(RenderEffect.RenderEffect, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    CTProximal = 0
    CTAll = 1
    
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
        if libpanda and libpanda._inPnJyoGFyW:
            libpanda._inPnJyoGFyW(self.this)
        

    
    def _PolylightEffect__overloaded_make():
        returnValue = libpanda._inPnJyoX4w6()
        import RenderEffect
        returnObject = RenderEffect.RenderEffect(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _PolylightEffect__overloaded_make = staticmethod(_PolylightEffect__overloaded_make)
    
    def _PolylightEffect__overloaded_make_float___enum__ContribType_ptrLPoint3f(weight, contrib, effectCenter):
        returnValue = libpanda._inPnJyowQWw(weight, contrib, effectCenter.this)
        import RenderEffect
        returnObject = RenderEffect.RenderEffect(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _PolylightEffect__overloaded_make_float___enum__ContribType_ptrLPoint3f = staticmethod(_PolylightEffect__overloaded_make_float___enum__ContribType_ptrLPoint3f)
    
    def _PolylightEffect__overloaded_make_float___enum__ContribType_ptrLPoint3f_ptrConstVectorNodePath(weight, contrib, effectCenter, lights):
        returnValue = libpanda._inPnJyogXbG(weight, contrib, effectCenter.this, lights.this)
        import RenderEffect
        returnObject = RenderEffect.RenderEffect(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    _PolylightEffect__overloaded_make_float___enum__ContribType_ptrLPoint3f_ptrConstVectorNodePath = staticmethod(_PolylightEffect__overloaded_make_float___enum__ContribType_ptrLPoint3f_ptrConstVectorNodePath)
    
    def getClassType():
        returnValue = libpanda._inPnJyoTUuJ()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def addLight(self, newlight):
        returnValue = libpanda._inPnJyo5iCT(self.this, newlight.this)
        import RenderEffect
        returnObject = RenderEffect.RenderEffect(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def removeLight(self, newlight):
        returnValue = libpanda._inPnJyoneGr(self.this, newlight.this)
        import RenderEffect
        returnObject = RenderEffect.RenderEffect(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def setWeight(self, w):
        returnValue = libpanda._inPnJyo5_KQ(self.this, w)
        import RenderEffect
        returnObject = RenderEffect.RenderEffect(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def setContrib(self, c):
        returnValue = libpanda._inPnJyoqn_x(self.this, c)
        import RenderEffect
        returnObject = RenderEffect.RenderEffect(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def setEffectCenter(self, ec):
        returnValue = libpanda._inPnJyo2mzF(self.this, ec.this)
        import RenderEffect
        returnObject = RenderEffect.RenderEffect(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getWeight(self):
        returnValue = libpanda._inPnJyoTSvb(self.this)
        return returnValue

    
    def getContrib(self):
        returnValue = libpanda._inPnJyoQ433(self.this)
        return returnValue

    
    def getEffectCenter(self):
        returnValue = libpanda._inPnJyoGfeT(self.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def hasLight(self, light):
        returnValue = libpanda._inPnJyoedsj(self.this, light.this)
        return returnValue

    
    def make(*_args):
        numArgs = len(_args)
        if numArgs == 0:
            return PolylightEffect._PolylightEffect__overloaded_make(*_args)
        elif numArgs == 3:
            return PolylightEffect._PolylightEffect__overloaded_make_float___enum__ContribType_ptrLPoint3f(*_args)
        elif numArgs == 4:
            return PolylightEffect._PolylightEffect__overloaded_make_float___enum__ContribType_ptrLPoint3f_ptrConstVectorNodePath(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 3 4 '

    make = staticmethod(make)

