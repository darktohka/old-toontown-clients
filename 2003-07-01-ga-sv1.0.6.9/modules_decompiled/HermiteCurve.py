# File: H (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import PiecewiseCurve

class HermiteCurve(PiecewiseCurve.PiecewiseCurve, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _HermiteCurve__overloaded_constructor(self):
        self.this = libpanda._inPHc9WzsME()
        self.userManagesMemory = 1

    
    def _HermiteCurve__overloaded_constructor_ptrConstParametricCurve(self, pc):
        self.this = libpanda._inPHc9WzviK(pc.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClassType():
        returnValue = libpanda._inPHc9W0huh()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def getNumCvs(self):
        returnValue = libpanda._inPHc9W6fOV(self.this)
        return returnValue

    
    def insertCv(self, t):
        returnValue = libpanda._inPHc9WLZ8L(self.this, t)
        return returnValue

    
    def _HermiteCurve__overloaded_appendCv_ptrHermiteCurve_int_ptrConstLVecBase3f(self, type, v):
        returnValue = libpanda._inPHc9WxceQ(self.this, type, v.this)
        return returnValue

    
    def _HermiteCurve__overloaded_appendCv_ptrHermiteCurve_int_float_float_float(self, type, x, y, z):
        returnValue = libpanda._inPHc9WP_6n(self.this, type, x, y, z)
        return returnValue

    
    def removeCv(self, n):
        returnValue = libpanda._inPHc9WTGlz(self.this, n)
        return returnValue

    
    def removeAllCvs(self):
        returnValue = libpanda._inPHc9WYfOG(self.this)
        return returnValue

    
    def setCvType(self, n, type):
        returnValue = libpanda._inPHc9WEeDJ(self.this, n, type)
        return returnValue

    
    def _HermiteCurve__overloaded_setCvPoint_ptrHermiteCurve_int_ptrConstLVecBase3f(self, n, v):
        returnValue = libpanda._inPHc9W0ifu(self.this, n, v.this)
        return returnValue

    
    def _HermiteCurve__overloaded_setCvPoint_ptrHermiteCurve_int_float_float_float(self, n, x, y, z):
        returnValue = libpanda._inPHc9W2q7R(self.this, n, x, y, z)
        return returnValue

    
    def _HermiteCurve__overloaded_setCvIn_ptrHermiteCurve_int_ptrConstLVecBase3f(self, n, v):
        returnValue = libpanda._inPHc9WWhVD(self.this, n, v.this)
        return returnValue

    
    def _HermiteCurve__overloaded_setCvIn_ptrHermiteCurve_int_float_float_float(self, n, x, y, z):
        returnValue = libpanda._inPHc9WFkya(self.this, n, x, y, z)
        return returnValue

    
    def _HermiteCurve__overloaded_setCvOut_ptrHermiteCurve_int_ptrConstLVecBase3f(self, n, v):
        returnValue = libpanda._inPHc9Wzv4x(self.this, n, v.this)
        return returnValue

    
    def _HermiteCurve__overloaded_setCvOut_ptrHermiteCurve_int_float_float_float(self, n, x, y, z):
        returnValue = libpanda._inPHc9WnRXh(self.this, n, x, y, z)
        return returnValue

    
    def setCvTstart(self, n, tstart):
        returnValue = libpanda._inPHc9Wo3DW(self.this, n, tstart)
        return returnValue

    
    def setCvName(self, n, name):
        returnValue = libpanda._inPHc9WZy1_(self.this, n, name)
        return returnValue

    
    def getCvType(self, n):
        returnValue = libpanda._inPHc9WoOER(self.this, n)
        return returnValue

    
    def _HermiteCurve__overloaded_getCvPoint_ptrConstHermiteCurve_int(self, n):
        returnValue = libpanda._inPHc9WAAkK(self.this, n)
        import VBase3
        returnObject = VBase3.VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _HermiteCurve__overloaded_getCvPoint_ptrConstHermiteCurve_int_ptrLVecBase3f(self, n, v):
        returnValue = libpanda._inPHc9WWbj7(self.this, n, v.this)
        return returnValue

    
    def _HermiteCurve__overloaded_getCvIn_ptrConstHermiteCurve_int(self, n):
        returnValue = libpanda._inPHc9WDkRx(self.this, n)
        import VBase3
        returnObject = VBase3.VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _HermiteCurve__overloaded_getCvIn_ptrConstHermiteCurve_int_ptrLVecBase3f(self, n, v):
        returnValue = libpanda._inPHc9WOXkH(self.this, n, v.this)
        return returnValue

    
    def _HermiteCurve__overloaded_getCvOut_ptrConstHermiteCurve_int(self, n):
        returnValue = libpanda._inPHc9WDKEx(self.this, n)
        import VBase3
        returnObject = VBase3.VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _HermiteCurve__overloaded_getCvOut_ptrConstHermiteCurve_int_ptrLVecBase3f(self, n, v):
        returnValue = libpanda._inPHc9WNr47(self.this, n, v.this)
        return returnValue

    
    def getCvTstart(self, n):
        returnValue = libpanda._inPHc9WBbZE(self.this, n)
        return returnValue

    
    def getCvName(self, n):
        returnValue = libpanda._inPHc9Wm1_h(self.this, n)
        return returnValue

    
    def writeCv(self, out, n):
        returnValue = libpanda._inPHc9WeyiA(self.this, out.this, n)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._HermiteCurve__overloaded_constructor()
        elif numArgs == 1:
            import ParametricCurve
            if isinstance(_args[0], ParametricCurve.ParametricCurve):
                return self._HermiteCurve__overloaded_constructor_ptrConstParametricCurve(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <ParametricCurve.ParametricCurve> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def getCvIn(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._HermiteCurve__overloaded_getCvIn_ptrConstHermiteCurve_int(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        elif numArgs == 2:
            if isinstance(_args[0], types.IntType):
                import VBase3
                if isinstance(_args[1], VBase3.VBase3):
                    return self._HermiteCurve__overloaded_getCvIn_ptrConstHermiteCurve_int_ptrLVecBase3f(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setCvOut(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            if isinstance(_args[0], types.IntType):
                import VBase3
                if isinstance(_args[1], VBase3.VBase3):
                    return self._HermiteCurve__overloaded_setCvOut_ptrHermiteCurve_int_ptrConstLVecBase3f(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        elif numArgs == 4:
            if isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                            return self._HermiteCurve__overloaded_setCvOut_ptrHermiteCurve_int_float_float_float(_args[0], _args[1], _args[2], _args[3])
                        else:
                            raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 4 '

    
    def getCvPoint(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._HermiteCurve__overloaded_getCvPoint_ptrConstHermiteCurve_int(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        elif numArgs == 2:
            if isinstance(_args[0], types.IntType):
                import VBase3
                if isinstance(_args[1], VBase3.VBase3):
                    return self._HermiteCurve__overloaded_getCvPoint_ptrConstHermiteCurve_int_ptrLVecBase3f(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def getCvOut(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            if isinstance(_args[0], types.IntType):
                return self._HermiteCurve__overloaded_getCvOut_ptrConstHermiteCurve_int(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        elif numArgs == 2:
            if isinstance(_args[0], types.IntType):
                import VBase3
                if isinstance(_args[1], VBase3.VBase3):
                    return self._HermiteCurve__overloaded_getCvOut_ptrConstHermiteCurve_int_ptrLVecBase3f(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setCvPoint(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            if isinstance(_args[0], types.IntType):
                import VBase3
                if isinstance(_args[1], VBase3.VBase3):
                    return self._HermiteCurve__overloaded_setCvPoint_ptrHermiteCurve_int_ptrConstLVecBase3f(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        elif numArgs == 4:
            if isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                            return self._HermiteCurve__overloaded_setCvPoint_ptrHermiteCurve_int_float_float_float(_args[0], _args[1], _args[2], _args[3])
                        else:
                            raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 4 '

    
    def appendCv(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            if isinstance(_args[0], types.IntType):
                import VBase3
                if isinstance(_args[1], VBase3.VBase3):
                    return self._HermiteCurve__overloaded_appendCv_ptrHermiteCurve_int_ptrConstLVecBase3f(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        elif numArgs == 4:
            if isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                            return self._HermiteCurve__overloaded_appendCv_ptrHermiteCurve_int_float_float_float(_args[0], _args[1], _args[2], _args[3])
                        else:
                            raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 4 '

    
    def setCvIn(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            if isinstance(_args[0], types.IntType):
                import VBase3
                if isinstance(_args[1], VBase3.VBase3):
                    return self._HermiteCurve__overloaded_setCvIn_ptrHermiteCurve_int_ptrConstLVecBase3f(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        elif numArgs == 4:
            if isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                            return self._HermiteCurve__overloaded_setCvIn_ptrHermiteCurve_int_float_float_float(_args[0], _args[1], _args[2], _args[3])
                        else:
                            raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 4 '


