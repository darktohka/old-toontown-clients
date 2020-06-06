# File: F (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import PandaNode

class Fog(PandaNode.PandaNode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    MLinear = 0
    MExponential = 1
    MExponentialSquared = 2
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self, name):
        self.this = libpanda._inPnJyoWpyF(name)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPnJyo0yAx:
            libpanda._inPnJyo0yAx(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPnJyofLii()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def getMode(self):
        returnValue = libpanda._inPnJyoNq_P(self.this)
        return returnValue

    
    def setMode(self, mode):
        returnValue = libpanda._inPnJyoGgPt(self.this, mode)
        return returnValue

    
    def getColor(self):
        returnValue = libpanda._inPnJyoRSgO(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _Fog__overloaded_setColor_ptrFog_ptrConstLVecBase4f(self, color):
        returnValue = libpanda._inPnJyoJg2n(self.this, color.this)
        return returnValue

    
    def _Fog__overloaded_setColor_ptrFog_float_float_float(self, r, g, b):
        returnValue = libpanda._inPnJyo_xx3(self.this, r, g, b)
        return returnValue

    
    def setLinearRange(self, onset, opaque):
        returnValue = libpanda._inPnJyo3of3(self.this, onset, opaque)
        return returnValue

    
    def getLinearOnsetPoint(self):
        returnValue = libpanda._inPnJyo9LTt(self.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _Fog__overloaded_setLinearOnsetPoint_ptrFog_ptrConstLPoint3f(self, linearOnsetPoint):
        returnValue = libpanda._inPnJyo6RcW(self.this, linearOnsetPoint.this)
        return returnValue

    
    def _Fog__overloaded_setLinearOnsetPoint_ptrFog_float_float_float(self, x, y, z):
        returnValue = libpanda._inPnJyo36iG(self.this, x, y, z)
        return returnValue

    
    def getLinearOpaquePoint(self):
        returnValue = libpanda._inPnJyojQae(self.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _Fog__overloaded_setLinearOpaquePoint_ptrFog_ptrConstLPoint3f(self, linearOpaquePoint):
        returnValue = libpanda._inPnJyoHhA1(self.this, linearOpaquePoint.this)
        return returnValue

    
    def _Fog__overloaded_setLinearOpaquePoint_ptrFog_float_float_float(self, x, y, z):
        returnValue = libpanda._inPnJyoEcC5(self.this, x, y, z)
        return returnValue

    
    def setLinearFallback(self, angle, onset, opaque):
        returnValue = libpanda._inPnJyody8d(self.this, angle, onset, opaque)
        return returnValue

    
    def getExpDensity(self):
        returnValue = libpanda._inPnJyoE35n(self.this)
        return returnValue

    
    def setExpDensity(self, expDensity):
        returnValue = libpanda._inPnJyoGCDe(self.this, expDensity)
        return returnValue

    
    def setLinearOpaquePoint(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._Fog__overloaded_setLinearOpaquePoint_ptrFog_ptrConstLPoint3f(*_args)
        elif numArgs == 3:
            return self._Fog__overloaded_setLinearOpaquePoint_ptrFog_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '

    
    def setColor(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._Fog__overloaded_setColor_ptrFog_ptrConstLVecBase4f(*_args)
        elif numArgs == 3:
            return self._Fog__overloaded_setColor_ptrFog_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '

    
    def setLinearOnsetPoint(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._Fog__overloaded_setLinearOnsetPoint_ptrFog_ptrConstLPoint3f(*_args)
        elif numArgs == 3:
            return self._Fog__overloaded_setLinearOnsetPoint_ptrFog_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '


