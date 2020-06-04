# File: F (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
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
        
        apply(self.constructor, _args)

    
    def constructor(self, name):
        self.this = libpanda._inPkJyoWpyF(name)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPkJyo3yAx:
            libpanda._inPkJyo3yAx(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPkJyoeLii()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def getMode(self):
        returnValue = libpanda._inPkJyoNq_P(self.this)
        return returnValue

    
    def setMode(self, mode):
        returnValue = libpanda._inPkJyoHgPt(self.this, mode)
        return returnValue

    
    def getColor(self):
        returnValue = libpanda._inPkJyoRSgO(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _Fog__overloaded_setColor_ptrFog_ptrConstLVecBase4f(self, color):
        returnValue = libpanda._inPkJyo2g2n(self.this, color.this)
        return returnValue

    
    def _Fog__overloaded_setColor_ptrFog_float_float_float(self, r, g, b):
        returnValue = libpanda._inPkJyo8xx3(self.this, r, g, b)
        return returnValue

    
    def setLinearRange(self, onset, opaque):
        returnValue = libpanda._inPkJyo0of3(self.this, onset, opaque)
        return returnValue

    
    def getLinearOnsetPoint(self):
        returnValue = libpanda._inPkJyo8LTt(self.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _Fog__overloaded_setLinearOnsetPoint_ptrFog_ptrConstLPoint3f(self, linearOnsetPoint):
        returnValue = libpanda._inPkJyo6RcW(self.this, linearOnsetPoint.this)
        return returnValue

    
    def _Fog__overloaded_setLinearOnsetPoint_ptrFog_float_float_float(self, x, y, z):
        returnValue = libpanda._inPkJyo36iG(self.this, x, y, z)
        return returnValue

    
    def getLinearOpaquePoint(self):
        returnValue = libpanda._inPkJyojQae(self.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _Fog__overloaded_setLinearOpaquePoint_ptrFog_ptrConstLPoint3f(self, linearOpaquePoint):
        returnValue = libpanda._inPkJyoEhA1(self.this, linearOpaquePoint.this)
        return returnValue

    
    def _Fog__overloaded_setLinearOpaquePoint_ptrFog_float_float_float(self, x, y, z):
        returnValue = libpanda._inPkJyobcC5(self.this, x, y, z)
        return returnValue

    
    def setLinearFallback(self, angle, onset, opaque):
        returnValue = libpanda._inPkJyody8d(self.this, angle, onset, opaque)
        return returnValue

    
    def getExpDensity(self):
        returnValue = libpanda._inPkJyoH35n(self.this)
        return returnValue

    
    def setExpDensity(self, expDensity):
        returnValue = libpanda._inPkJyoGCDe(self.this, expDensity)
        return returnValue

    
    def setLinearOpaquePoint(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Point3
            if isinstance(_args[0], Point3.Point3):
                return self._Fog__overloaded_setLinearOpaquePoint_ptrFog_ptrConstLPoint3f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Point3.Point3> '
        elif numArgs == 3:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        return self._Fog__overloaded_setLinearOpaquePoint_ptrFog_float_float_float(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '

    
    def setColor(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import VBase4
            if isinstance(_args[0], VBase4.VBase4):
                return self._Fog__overloaded_setColor_ptrFog_ptrConstLVecBase4f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase4.VBase4> '
        elif numArgs == 3:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        return self._Fog__overloaded_setColor_ptrFog_float_float_float(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '

    
    def setLinearOnsetPoint(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Point3
            if isinstance(_args[0], Point3.Point3):
                return self._Fog__overloaded_setLinearOnsetPoint_ptrFog_ptrConstLPoint3f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Point3.Point3> '
        elif numArgs == 3:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        return self._Fog__overloaded_setLinearOnsetPoint_ptrFog_float_float_float(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '


