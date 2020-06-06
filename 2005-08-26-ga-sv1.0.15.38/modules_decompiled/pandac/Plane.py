# File: P (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject
import VBase4

class Plane(VBase4.VBase4, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _Plane__overloaded_constructor(self):
        self.this = libpanda._inPSkjPN3bW()
        self.userManagesMemory = 1

    
    def _Plane__overloaded_constructor_ptrConstLPoint3f_ptrConstLPoint3f_ptrConstLPoint3f(self, a, b, c):
        self.this = libpanda._inPSkjPgFjF(a.this, b.this, c.this)
        self.userManagesMemory = 1

    
    def _Plane__overloaded_constructor_ptrConstLVecBase4f(self, copy):
        self.this = libpanda._inPSkjPc48O(copy.this)
        self.userManagesMemory = 1

    
    def _Plane__overloaded_constructor_ptrConstLVector3f_ptrConstLPoint3f(self, normal, point):
        self.this = libpanda._inPSkjPEC54(normal.this, point.this)
        self.userManagesMemory = 1

    
    def _Plane__overloaded_constructor_float_float_float_float(self, a, b, c, d):
        self.this = libpanda._inPSkjPIw6g(a, b, c, d)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPSkjPk_wL:
            libpanda._inPSkjPk_wL(self.this)
        

    
    def _Plane__overloaded___mul___ptrConstPlanef_ptrConstLMatrix3f(self, mat):
        returnValue = libpanda._inPSkjPVdcZ(self.this, mat.this)
        returnObject = Plane(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _Plane__overloaded___mul___ptrConstPlanef_ptrConstLMatrix4f(self, mat):
        returnValue = libpanda._inPSkjPVN_s(self.this, mat.this)
        returnObject = Plane(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __sub__(self):
        returnValue = libpanda._inPSkjPQINL(self.this)
        returnObject = Plane(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getReflectionMat(self):
        returnValue = libpanda._inPSkjPX_l3(self.this)
        import Mat4
        returnObject = Mat4.Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getNormal(self):
        returnValue = libpanda._inPSkjPUHNM(self.this)
        import Vec3
        returnObject = Vec3.Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getPoint(self):
        returnValue = libpanda._inPSkjPpIwN(self.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def distToPlane(self, point):
        returnValue = libpanda._inPSkjPyRLi(self.this, point.this)
        return returnValue

    
    def intersectsLine(self, intersectionPoint, p1, p2):
        returnValue = libpanda._inPSkjP7eH0(self.this, intersectionPoint.this, p1.this, p2.this)
        return returnValue

    
    def intersectsPlane(self, _from, delta, other):
        returnValue = libpanda._inPSkjPP8pH(self.this, _from.this, delta.this, other.this)
        return returnValue

    
    def output(self, out):
        returnValue = libpanda._inPSkjPt6yW(self.this, out.this)
        return returnValue

    
    def _Plane__overloaded_write_ptrConstPlanef_ptrOstream_int(self, out, indentLevel):
        returnValue = libpanda._inPSkjP4DCL(self.this, out.this, indentLevel)
        return returnValue

    
    def _Plane__overloaded_write_ptrConstPlanef_ptrOstream(self, out):
        returnValue = libpanda._inPSkjPYLcN(self.this, out.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._Plane__overloaded_constructor(*_args)
        elif numArgs == 1:
            return self._Plane__overloaded_constructor_ptrConstLVecBase4f(*_args)
        elif numArgs == 2:
            return self._Plane__overloaded_constructor_ptrConstLVector3f_ptrConstLPoint3f(*_args)
        elif numArgs == 3:
            return self._Plane__overloaded_constructor_ptrConstLPoint3f_ptrConstLPoint3f_ptrConstLPoint3f(*_args)
        elif numArgs == 4:
            return self._Plane__overloaded_constructor_float_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 3 4 '

    
    def write(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._Plane__overloaded_write_ptrConstPlanef_ptrOstream(*_args)
        elif numArgs == 2:
            return self._Plane__overloaded_write_ptrConstPlanef_ptrOstream_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def __mul__(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Mat4
            if isinstance(_args[0], Mat4.Mat4):
                return self._Plane__overloaded___mul___ptrConstPlanef_ptrConstLMatrix4f(*_args)
            
            import Mat3
            if isinstance(_args[0], Mat3.Mat3):
                return self._Plane__overloaded___mul___ptrConstPlanef_ptrConstLMatrix3f(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <Mat4.Mat4> <Mat3.Mat3> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


