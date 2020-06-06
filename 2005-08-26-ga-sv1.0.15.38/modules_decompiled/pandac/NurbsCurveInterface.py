# File: N (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject

class NurbsCurveInterface(FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self):
        raise RuntimeError, 'No C++ constructor defined for class: ' + self.__class__.__name__

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPHc9WJi5Q:
            libpanda._inPHc9WJi5Q(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPHc9Whfnq()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setOrder(self, order):
        returnValue = libpanda._inPHc9WLhK6(self.this, order)
        return returnValue

    
    def getOrder(self):
        returnValue = libpanda._inPHc9WiPY_(self.this)
        return returnValue

    
    def getNumCvs(self):
        returnValue = libpanda._inPHc9WWaqD(self.this)
        return returnValue

    
    def getNumKnots(self):
        returnValue = libpanda._inPHc9WMQ5_(self.this)
        return returnValue

    
    def insertCv(self, t):
        returnValue = libpanda._inPHc9W8ScU(self.this, t)
        return returnValue

    
    def _NurbsCurveInterface__overloaded_appendCv_ptrNurbsCurveInterface_ptrConstLVecBase3f(self, v):
        returnValue = libpanda._inPHc9WofTi(self.this, v.this)
        return returnValue

    
    def _NurbsCurveInterface__overloaded_appendCv_ptrNurbsCurveInterface_ptrConstLVecBase4f(self, v):
        returnValue = libpanda._inPHc9WgMdi(self.this, v.this)
        return returnValue

    
    def _NurbsCurveInterface__overloaded_appendCv_ptrNurbsCurveInterface_float_float_float(self, x, y, z):
        returnValue = libpanda._inPHc9WB3ZR(self.this, x, y, z)
        return returnValue

    
    def removeCv(self, n):
        returnValue = libpanda._inPHc9WuA5o(self.this, n)
        return returnValue

    
    def removeAllCvs(self):
        returnValue = libpanda._inPHc9W1Nej(self.this)
        return returnValue

    
    def _NurbsCurveInterface__overloaded_setCvPoint_ptrNurbsCurveInterface_int_ptrConstLVecBase3f(self, n, v):
        returnValue = libpanda._inPHc9W03Z_(self.this, n, v.this)
        return returnValue

    
    def _NurbsCurveInterface__overloaded_setCvPoint_ptrNurbsCurveInterface_int_float_float_float(self, n, x, y, z):
        returnValue = libpanda._inPHc9WvbUc(self.this, n, x, y, z)
        return returnValue

    
    def getCvPoint(self, n):
        returnValue = libpanda._inPHc9WKFJB(self.this, n)
        import VBase3
        returnObject = VBase3.VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setCvWeight(self, n, w):
        returnValue = libpanda._inPHc9WkgWd(self.this, n, w)
        return returnValue

    
    def getCvWeight(self, n):
        returnValue = libpanda._inPHc9WQgDH(self.this, n)
        return returnValue

    
    def setCv(self, n, v):
        returnValue = libpanda._inPHc9WsLws(self.this, n, v.this)
        return returnValue

    
    def getCv(self, n):
        returnValue = libpanda._inPHc9W_TRe(self.this, n)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setKnot(self, n, t):
        returnValue = libpanda._inPHc9WDnR8(self.this, n, t)
        return returnValue

    
    def getKnot(self, n):
        returnValue = libpanda._inPHc9W_MjW(self.this, n)
        return returnValue

    
    def writeCv(self, out, n):
        returnValue = libpanda._inPHc9W6ybU(self.this, out.this, n)
        return returnValue

    
    def setCvPoint(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            return self._NurbsCurveInterface__overloaded_setCvPoint_ptrNurbsCurveInterface_int_ptrConstLVecBase3f(*_args)
        elif numArgs == 4:
            return self._NurbsCurveInterface__overloaded_setCvPoint_ptrNurbsCurveInterface_int_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 4 '

    
    def appendCv(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import VBase4
            if isinstance(_args[0], VBase4.VBase4):
                return self._NurbsCurveInterface__overloaded_appendCv_ptrNurbsCurveInterface_ptrConstLVecBase4f(*_args)
            
            import VBase3
            if isinstance(_args[0], VBase3.VBase3):
                return self._NurbsCurveInterface__overloaded_appendCv_ptrNurbsCurveInterface_ptrConstLVecBase3f(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <VBase4.VBase4> <VBase3.VBase3> '
        elif numArgs == 3:
            return self._NurbsCurveInterface__overloaded_appendCv_ptrNurbsCurveInterface_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '


