# File: L (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject
import QuatD

class LOrientationd(QuatD.QuatD, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _LOrientationd__overloaded_constructor(self):
        self.this = libpanda._inPVZN32Y6p()
        self.userManagesMemory = 1

    
    def _LOrientationd__overloaded_constructor_ptrConstLMatrix3d(self, parameter0):
        self.this = libpanda._inPVZN3Yrfb(parameter0.this)
        self.userManagesMemory = 1

    
    def _LOrientationd__overloaded_constructor_ptrConstLMatrix4d(self, parameter0):
        self.this = libpanda._inPVZN3Zrmp(parameter0.this)
        self.userManagesMemory = 1

    
    def _LOrientationd__overloaded_constructor_ptrConstLQuaterniond(self, parameter0):
        self.this = libpanda._inPVZN3RFe9(parameter0.this)
        self.userManagesMemory = 1

    
    def _LOrientationd__overloaded_constructor_ptrConstLVector3d_float(self, parameter0, parameter1):
        self.this = libpanda._inPVZN3yi3y(parameter0.this, parameter1)
        self.userManagesMemory = 1

    
    def _LOrientationd__overloaded_constructor_double_double_double_double(self, parameter0, parameter1, parameter2, parameter3):
        self.this = libpanda._inPVZN3QOxM(parameter0, parameter1, parameter2, parameter3)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPVZN3d2Kq:
            libpanda._inPVZN3d2Kq(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPVZN3xK29()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _LOrientationd__overloaded___mul___ptrConstLOrientationd_ptrConstLQuaterniond(self, other):
        returnValue = libpanda._inPVZN3lgBQ(self.this, other.this)
        returnObject = LOrientationd(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _LOrientationd__overloaded___mul___ptrConstLOrientationd_ptrConstLRotationd(self, other):
        returnValue = libpanda._inPVZN39P52(self.this, other.this)
        returnObject = LOrientationd(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._LOrientationd__overloaded_constructor(*_args)
        elif numArgs == 1:
            import QuatD
            if isinstance(_args[0], QuatD.QuatD):
                return self._LOrientationd__overloaded_constructor_ptrConstLQuaterniond(*_args)
            
            import Mat4D
            if isinstance(_args[0], Mat4D.Mat4D):
                return self._LOrientationd__overloaded_constructor_ptrConstLMatrix4d(*_args)
            
            import Mat3D
            if isinstance(_args[0], Mat3D.Mat3D):
                return self._LOrientationd__overloaded_constructor_ptrConstLMatrix3d(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <QuatD.QuatD> <Mat4D.Mat4D> <Mat3D.Mat3D> '
        elif numArgs == 2:
            return self._LOrientationd__overloaded_constructor_ptrConstLVector3d_float(*_args)
        elif numArgs == 4:
            return self._LOrientationd__overloaded_constructor_double_double_double_double(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 4 '

    
    def __mul__(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import LRotationd
            if isinstance(_args[0], LRotationd.LRotationd):
                return self._LOrientationd__overloaded___mul___ptrConstLOrientationd_ptrConstLRotationd(*_args)
            
            import QuatD
            if isinstance(_args[0], QuatD.QuatD):
                return self._LOrientationd__overloaded___mul___ptrConstLOrientationd_ptrConstLQuaterniond(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <LRotationd.LRotationd> <QuatD.QuatD> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


