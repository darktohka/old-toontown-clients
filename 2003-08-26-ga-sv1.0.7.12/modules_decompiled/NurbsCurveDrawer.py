# File: N (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import ParametricCurveDrawer

class NurbsCurveDrawer(ParametricCurveDrawer.ParametricCurveDrawer, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self):
        self.this = libpanda._inPHc9W7Cap()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClassType():
        returnValue = libpanda._inPHc9W_Wm8()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setCvColor(self, r, g, b):
        returnValue = libpanda._inPHc9WFdLu(self.this, r, g, b)
        return returnValue

    
    def setHullColor(self, r, g, b):
        returnValue = libpanda._inPHc9Whht2(self.this, r, g, b)
        return returnValue

    
    def setKnotColor(self, r, g, b):
        returnValue = libpanda._inPHc9W6p8C(self.this, r, g, b)
        return returnValue

    
    def _NurbsCurveDrawer__overloaded_recompute_ptrNurbsCurveDrawer_float_float_ptrParametricCurve(self, t1, t2, curve):
        returnValue = libpanda._inPHc9WYxwY(self.this, t1, t2, curve.this)
        return returnValue

    
    def _NurbsCurveDrawer__overloaded_recompute_ptrNurbsCurveDrawer_float_float(self, t1, t2):
        returnValue = libpanda._inPHc9WzpkB(self.this, t1, t2)
        return returnValue

    
    def setShowCvs(self, flag):
        returnValue = libpanda._inPHc9Wlzti(self.this, flag)
        return returnValue

    
    def getShowCvs(self):
        returnValue = libpanda._inPHc9WB3jn(self.this)
        return returnValue

    
    def setShowHull(self, flag):
        returnValue = libpanda._inPHc9WCCJk(self.this, flag)
        return returnValue

    
    def getShowHull(self):
        returnValue = libpanda._inPHc9WwROr(self.this)
        return returnValue

    
    def setShowKnots(self, flag):
        returnValue = libpanda._inPHc9WlYX4(self.this, flag)
        return returnValue

    
    def getShowKnots(self):
        returnValue = libpanda._inPHc9WmU_G(self.this)
        return returnValue

    
    def _NurbsCurveDrawer__overloaded_hilight_ptrNurbsCurveDrawer_int(self, n):
        returnValue = libpanda._inPHc9W1FqG(self.this, n)
        return returnValue

    
    def _NurbsCurveDrawer__overloaded_hilight_ptrNurbsCurveDrawer_int_float_float_float(self, n, hr, hg, hb):
        returnValue = libpanda._inPHc9Wjevm(self.this, n, hr, hg, hb)
        return returnValue

    
    def unhilight(self, n):
        returnValue = libpanda._inPHc9WRIem(self.this, n)
        return returnValue

    
    def hilight(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._NurbsCurveDrawer__overloaded_hilight_ptrNurbsCurveDrawer_int(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        elif numArgs == 4:
            if isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                            return self._NurbsCurveDrawer__overloaded_hilight_ptrNurbsCurveDrawer_int_float_float_float(_args[0], _args[1], _args[2], _args[3])
                        else:
                            raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 4 '

    
    def recompute(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    return self._NurbsCurveDrawer__overloaded_recompute_ptrNurbsCurveDrawer_float_float(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        elif numArgs == 3:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    import ParametricCurve
                    if isinstance(_args[2], ParametricCurve.ParametricCurve):
                        return self._NurbsCurveDrawer__overloaded_recompute_ptrNurbsCurveDrawer_float_float_ptrParametricCurve(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <ParametricCurve.ParametricCurve> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '


