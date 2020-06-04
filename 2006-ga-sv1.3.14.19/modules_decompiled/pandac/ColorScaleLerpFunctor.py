# File: C (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import SimpleLerpFunctorLVecBase4f

class ColorScaleLerpFunctor(SimpleLerpFunctorLVecBase4f.SimpleLerpFunctorLVecBase4f, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _ColorScaleLerpFunctor__overloaded_constructor_ptrNodePath_ptrLVecBase4f_ptrLVecBase4f(self, np, start, end):
        self.this = libpanda._inPnJyoLC1H(np.this, start.this, end.this)
        self.userManagesMemory = 1

    
    def _ColorScaleLerpFunctor__overloaded_constructor_ptrNodePath_ptrLVecBase4f_ptrLVecBase4f_ptrNodePath(self, np, start, end, wrt):
        self.this = libpanda._inPnJyoqMFY(np.this, start.this, end.this, wrt.this)
        self.userManagesMemory = 1

    
    def _ColorScaleLerpFunctor__overloaded_constructor_ptrNodePath_float_float_float_float_float_float_float_float(self, np, sr, sg, sb, sa, er, eg, eb, ea):
        self.this = libpanda._inPnJyojybb(np.this, sr, sg, sb, sa, er, eg, eb, ea)
        self.userManagesMemory = 1

    
    def _ColorScaleLerpFunctor__overloaded_constructor_ptrNodePath_float_float_float_float_float_float_float_float_ptrNodePath(self, np, sr, sg, sb, sa, er, eg, eb, ea, wrt):
        self.this = libpanda._inPnJyoCjMP(np.this, sr, sg, sb, sa, er, eg, eb, ea, wrt.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClassType():
        returnValue = libpanda._inPnJyotvME()
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
            return self._ColorScaleLerpFunctor__overloaded_constructor_ptrNodePath_ptrLVecBase4f_ptrLVecBase4f(*_args)
        elif numArgs == 4:
            return self._ColorScaleLerpFunctor__overloaded_constructor_ptrNodePath_ptrLVecBase4f_ptrLVecBase4f_ptrNodePath(*_args)
        elif numArgs == 9:
            return self._ColorScaleLerpFunctor__overloaded_constructor_ptrNodePath_float_float_float_float_float_float_float_float(*_args)
        elif numArgs == 10:
            return self._ColorScaleLerpFunctor__overloaded_constructor_ptrNodePath_float_float_float_float_float_float_float_float_ptrNodePath(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 3 4 9 10 '


