# File: P (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import LerpFunctor

class PosHprScaleLerpFunctor(LerpFunctor.LerpFunctor, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _PosHprScaleLerpFunctor__overloaded_constructor_ptrNodePath_ptrLPoint3f_ptrLPoint3f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f(self, np, pstart, pend, hstart, hend, sstart, send):
        self.this = libpanda._inPnJyoP4RJ(np.this, pstart.this, pend.this, hstart.this, hend.this, sstart.this, send.this)
        self.userManagesMemory = 1

    
    def _PosHprScaleLerpFunctor__overloaded_constructor_ptrNodePath_ptrLPoint3f_ptrLPoint3f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f_ptrNodePath(self, np, pstart, pend, hstart, hend, sstart, send, wrt):
        self.this = libpanda._inPnJyotRMm(np.this, pstart.this, pend.this, hstart.this, hend.this, sstart.this, send.this, wrt.this)
        self.userManagesMemory = 1

    
    def _PosHprScaleLerpFunctor__overloaded_constructor_ptrNodePath_float_float_float_float_float_float_float_float_float_float_float_float_float_float_float_float_float_float(self, np, psx, psy, psz, pex, pey, pez, hsx, hsy, hsz, hex, hey, hez, ssx, ssy, ssz, sex, sey, sez):
        self.this = libpanda._inPnJyouyws(np.this, psx, psy, psz, pex, pey, pez, hsx, hsy, hsz, hex, hey, hez, ssx, ssy, ssz, sex, sey, sez)
        self.userManagesMemory = 1

    
    def _PosHprScaleLerpFunctor__overloaded_constructor_ptrNodePath_float_float_float_float_float_float_float_float_float_float_float_float_float_float_float_float_float_float_ptrNodePath(self, np, psx, psy, psz, pex, pey, pez, hsx, hsy, hsz, hex, hey, hez, ssx, ssy, ssz, sex, sey, sez, wrt):
        self.this = libpanda._inPnJyoPFig(np.this, psx, psy, psz, pex, pey, pez, hsx, hsy, hsz, hex, hey, hez, ssx, ssy, ssz, sex, sey, sez, wrt.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClassType():
        returnValue = libpanda._inPnJyo1G7x()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def takeShortest(self):
        returnValue = libpanda._inPnJyo8q_U(self.this)
        return returnValue

    
    def takeLongest(self):
        returnValue = libpanda._inPnJyoFgah(self.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 7:
            return self._PosHprScaleLerpFunctor__overloaded_constructor_ptrNodePath_ptrLPoint3f_ptrLPoint3f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f(*_args)
        elif numArgs == 8:
            return self._PosHprScaleLerpFunctor__overloaded_constructor_ptrNodePath_ptrLPoint3f_ptrLPoint3f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f_ptrNodePath(*_args)
        elif numArgs == 19:
            return self._PosHprScaleLerpFunctor__overloaded_constructor_ptrNodePath_float_float_float_float_float_float_float_float_float_float_float_float_float_float_float_float_float_float(*_args)
        elif numArgs == 20:
            return self._PosHprScaleLerpFunctor__overloaded_constructor_ptrNodePath_float_float_float_float_float_float_float_float_float_float_float_float_float_float_float_float_float_float_ptrNodePath(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 7 8 19 20 '


