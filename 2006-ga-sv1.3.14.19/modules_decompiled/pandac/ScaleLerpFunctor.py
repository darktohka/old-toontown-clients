# File: S (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import SimpleLerpFunctorLVecBase3f

class ScaleLerpFunctor(SimpleLerpFunctorLVecBase3f.SimpleLerpFunctorLVecBase3f, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _ScaleLerpFunctor__overloaded_constructor_ptrNodePath_ptrLVecBase3f_ptrLVecBase3f(self, np, start, end):
        self.this = libpanda._inPnJyoP7Ek(np.this, start.this, end.this)
        self.userManagesMemory = 1

    
    def _ScaleLerpFunctor__overloaded_constructor_ptrNodePath_ptrLVecBase3f_ptrLVecBase3f_ptrNodePath(self, np, start, end, wrt):
        self.this = libpanda._inPnJyocsJY(np.this, start.this, end.this, wrt.this)
        self.userManagesMemory = 1

    
    def _ScaleLerpFunctor__overloaded_constructor_ptrNodePath_float_float_float_float_float_float(self, np, sx, sy, sz, ex, ey, ez):
        self.this = libpanda._inPnJyooNcS(np.this, sx, sy, sz, ex, ey, ez)
        self.userManagesMemory = 1

    
    def _ScaleLerpFunctor__overloaded_constructor_ptrNodePath_float_float_float_float_float_float_ptrNodePath(self, np, sx, sy, sz, ex, ey, ez, wrt):
        self.this = libpanda._inPnJyo3jPG(np.this, sx, sy, sz, ex, ey, ez, wrt.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClassType():
        returnValue = libpanda._inPnJyo_dcM()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 3:
            return self._ScaleLerpFunctor__overloaded_constructor_ptrNodePath_ptrLVecBase3f_ptrLVecBase3f(*_args)
        elif numArgs == 4:
            return self._ScaleLerpFunctor__overloaded_constructor_ptrNodePath_ptrLVecBase3f_ptrLVecBase3f_ptrNodePath(*_args)
        elif numArgs == 7:
            return self._ScaleLerpFunctor__overloaded_constructor_ptrNodePath_float_float_float_float_float_float(*_args)
        elif numArgs == 8:
            return self._ScaleLerpFunctor__overloaded_constructor_ptrNodePath_float_float_float_float_float_float_ptrNodePath(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 3 4 7 8 '


