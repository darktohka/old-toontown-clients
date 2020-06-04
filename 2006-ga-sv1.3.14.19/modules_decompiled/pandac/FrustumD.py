# File: F (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject

class FrustumD(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self):
        self.this = libpanda._inPSkjP9ko_()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPSkjPc9j5:
            libpanda._inPSkjPc9j5(self.this)
        

    
    def _FrustumD__overloaded_makeOrtho2D_ptrFrustumd(self):
        returnValue = libpanda._inPSkjPFiT5(self.this)
        return returnValue

    
    def _FrustumD__overloaded_makeOrtho2D_ptrFrustumd_double_double_double_double(self, l, r, t, b):
        returnValue = libpanda._inPSkjPPyqK(self.this, l, r, t, b)
        return returnValue

    
    def _FrustumD__overloaded_makeOrtho_ptrFrustumd_double_double(self, fnear, ffar):
        returnValue = libpanda._inPSkjPoaj7(self.this, fnear, ffar)
        return returnValue

    
    def _FrustumD__overloaded_makeOrtho_ptrFrustumd_double_double_double_double_double_double(self, fnear, ffar, l, r, t, b):
        returnValue = libpanda._inPSkjPBpZ4(self.this, fnear, ffar, l, r, t, b)
        return returnValue

    
    def makePerspectiveHfov(self, xfov, aspect, fnear, ffar):
        returnValue = libpanda._inPSkjPWxk6(self.this, xfov, aspect, fnear, ffar)
        return returnValue

    
    def makePerspectiveVfov(self, yfov, aspect, fnear, ffar):
        returnValue = libpanda._inPSkjPNz0m(self.this, yfov, aspect, fnear, ffar)
        return returnValue

    
    def makePerspective(self, xfov, yfov, fnear, ffar):
        returnValue = libpanda._inPSkjP7tfK(self.this, xfov, yfov, fnear, ffar)
        return returnValue

    
    def makeOrtho2D(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._FrustumD__overloaded_makeOrtho2D_ptrFrustumd(*_args)
        elif numArgs == 4:
            return self._FrustumD__overloaded_makeOrtho2D_ptrFrustumd_double_double_double_double(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 4 '

    
    def makeOrtho(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            return self._FrustumD__overloaded_makeOrtho_ptrFrustumd_double_double(*_args)
        elif numArgs == 6:
            return self._FrustumD__overloaded_makeOrtho_ptrFrustumd_double_double_double_double_double_double(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 6 '


