# File: H (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import LerpFunctor

class HprScaleLerpFunctor(LerpFunctor.LerpFunctor, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _HprScaleLerpFunctor__overloaded_constructor_ptrNodePath_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f(self, np, hstart, hend, sstart, send):
        self.this = libpanda._inPnJyo1FgG(np.this, hstart.this, hend.this, sstart.this, send.this)
        self.userManagesMemory = 1

    
    def _HprScaleLerpFunctor__overloaded_constructor_ptrNodePath_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f_ptrNodePath(self, np, hstart, hend, sstart, send, wrt):
        self.this = libpanda._inPnJyoPeDL(np.this, hstart.this, hend.this, sstart.this, send.this, wrt.this)
        self.userManagesMemory = 1

    
    def _HprScaleLerpFunctor__overloaded_constructor_ptrNodePath_float_float_float_float_float_float_float_float_float_float_float_float(self, np, hsx, hsy, hsz, hex, hey, hez, ssx, ssy, ssz, sex, sey, sez):
        self.this = libpanda._inPnJyoLBe9(np.this, hsx, hsy, hsz, hex, hey, hez, ssx, ssy, ssz, sex, sey, sez)
        self.userManagesMemory = 1

    
    def _HprScaleLerpFunctor__overloaded_constructor_ptrNodePath_float_float_float_float_float_float_float_float_float_float_float_float_ptrNodePath(self, np, hsx, hsy, hsz, hex, hey, hez, ssx, ssy, ssz, sex, sey, sez, wrt):
        self.this = libpanda._inPnJyoiyRx(np.this, hsx, hsy, hsz, hex, hey, hez, ssx, ssy, ssz, sex, sey, sez, wrt.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClassType():
        returnValue = libpanda._inPnJyoB8I8()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def takeShortest(self):
        returnValue = libpanda._inPnJyoHLXo(self.this)
        return returnValue

    
    def takeLongest(self):
        returnValue = libpanda._inPnJyoqjaH(self.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 5:
            return self._HprScaleLerpFunctor__overloaded_constructor_ptrNodePath_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f(*_args)
        elif numArgs == 6:
            return self._HprScaleLerpFunctor__overloaded_constructor_ptrNodePath_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f_ptrNodePath(*_args)
        elif numArgs == 13:
            return self._HprScaleLerpFunctor__overloaded_constructor_ptrNodePath_float_float_float_float_float_float_float_float_float_float_float_float(*_args)
        elif numArgs == 14:
            return self._HprScaleLerpFunctor__overloaded_constructor_ptrNodePath_float_float_float_float_float_float_float_float_float_float_float_float_ptrNodePath(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 5 6 13 14 '


