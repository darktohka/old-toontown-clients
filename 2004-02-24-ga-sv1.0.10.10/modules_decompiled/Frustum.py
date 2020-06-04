# File: F (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import FFIExternalObject

class Frustum(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self):
        self.this = libpanda._inPSkjPykLF()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPSkjP6wqV:
            libpanda._inPSkjP6wqV(self.this)
        

    
    def _Frustum__overloaded_makeOrtho2D_ptrFrustumf(self):
        returnValue = libpanda._inPSkjPHiaH(self.this)
        return returnValue

    
    def _Frustum__overloaded_makeOrtho2D_ptrFrustumf_float_float_float_float(self, l, r, t, b):
        returnValue = libpanda._inPSkjPRDrY(self.this, l, r, t, b)
        return returnValue

    
    def _Frustum__overloaded_makeOrtho_ptrFrustumf_float_float(self, fnear, ffar):
        returnValue = libpanda._inPSkjPtsCo(self.this, fnear, ffar)
        return returnValue

    
    def _Frustum__overloaded_makeOrtho_ptrFrustumf_float_float_float_float_float_float(self, fnear, ffar, l, r, t, b):
        returnValue = libpanda._inPSkjPHulf(self.this, fnear, ffar, l, r, t, b)
        return returnValue

    
    def makePerspectiveHfov(self, xfov, aspect, fnear, ffar):
        returnValue = libpanda._inPSkjPcYOF(self.this, xfov, aspect, fnear, ffar)
        return returnValue

    
    def makePerspectiveVfov(self, yfov, aspect, fnear, ffar):
        returnValue = libpanda._inPSkjPraex(self.this, yfov, aspect, fnear, ffar)
        return returnValue

    
    def makePerspective(self, xfov, yfov, fnear, ffar):
        returnValue = libpanda._inPSkjP8E42(self.this, xfov, yfov, fnear, ffar)
        return returnValue

    
    def makeOrtho2D(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Frustum__overloaded_makeOrtho2D_ptrFrustumf()
        elif numArgs == 4:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                            return self._Frustum__overloaded_makeOrtho2D_ptrFrustumf_float_float_float_float(_args[0], _args[1], _args[2], _args[3])
                        else:
                            raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 4 '

    
    def makeOrtho(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    return self._Frustum__overloaded_makeOrtho_ptrFrustumf_float_float(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        elif numArgs == 6:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                            if isinstance(_args[4], types.FloatType) or isinstance(_args[4], types.IntType):
                                if isinstance(_args[5], types.FloatType) or isinstance(_args[5], types.IntType):
                                    return self._Frustum__overloaded_makeOrtho_ptrFrustumf_float_float_float_float_float_float(_args[0], _args[1], _args[2], _args[3], _args[4], _args[5])
                                else:
                                    raise TypeError, 'Invalid argument 5, expected one of: <types.FloatType> '
                            else:
                                raise TypeError, 'Invalid argument 4, expected one of: <types.FloatType> '
                        else:
                            raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 6 '


