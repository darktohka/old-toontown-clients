# File: P (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import LerpFunctor

class PosHprLerpFunctor(LerpFunctor.LerpFunctor, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _PosHprLerpFunctor__overloaded_constructor_ptrNodePath_ptrLPoint3f_ptrLPoint3f_ptrLVecBase3f_ptrLVecBase3f(self, np, pstart, pend, hstart, hend):
        self.this = libpanda._inPnJyo_6uU(np.this, pstart.this, pend.this, hstart.this, hend.this)
        self.userManagesMemory = 1

    
    def _PosHprLerpFunctor__overloaded_constructor_ptrNodePath_ptrLPoint3f_ptrLPoint3f_ptrLVecBase3f_ptrLVecBase3f_ptrNodePath(self, np, pstart, pend, hstart, hend, wrt):
        self.this = libpanda._inPnJyoL66r(np.this, pstart.this, pend.this, hstart.this, hend.this, wrt.this)
        self.userManagesMemory = 1

    
    def _PosHprLerpFunctor__overloaded_constructor_ptrNodePath_float_float_float_float_float_float_float_float_float_float_float_float(self, np, psx, psy, psz, pex, pey, pez, hsx, hsy, hsz, hex, hey, hez):
        self.this = libpanda._inPnJyoB14f(np.this, psx, psy, psz, pex, pey, pez, hsx, hsy, hsz, hex, hey, hez)
        self.userManagesMemory = 1

    
    def _PosHprLerpFunctor__overloaded_constructor_ptrNodePath_float_float_float_float_float_float_float_float_float_float_float_float_ptrNodePath(self, np, psx, psy, psz, pex, pey, pez, hsx, hsy, hsz, hex, hey, hez, wrt):
        self.this = libpanda._inPnJyoFS2c(np.this, psx, psy, psz, pex, pey, pez, hsx, hsy, hsz, hex, hey, hez, wrt.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClassType():
        returnValue = libpanda._inPnJyoDdZH()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def takeShortest(self):
        returnValue = libpanda._inPnJyoeK94(self.this)
        return returnValue

    
    def takeLongest(self):
        returnValue = libpanda._inPnJyoCAL_(self.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 5:
            return self._PosHprLerpFunctor__overloaded_constructor_ptrNodePath_ptrLPoint3f_ptrLPoint3f_ptrLVecBase3f_ptrLVecBase3f(*_args)
        elif numArgs == 6:
            return self._PosHprLerpFunctor__overloaded_constructor_ptrNodePath_ptrLPoint3f_ptrLPoint3f_ptrLVecBase3f_ptrLVecBase3f_ptrNodePath(*_args)
        elif numArgs == 13:
            return self._PosHprLerpFunctor__overloaded_constructor_ptrNodePath_float_float_float_float_float_float_float_float_float_float_float_float(*_args)
        elif numArgs == 14:
            return self._PosHprLerpFunctor__overloaded_constructor_ptrNodePath_float_float_float_float_float_float_float_float_float_float_float_float_ptrNodePath(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 5 6 13 14 '


