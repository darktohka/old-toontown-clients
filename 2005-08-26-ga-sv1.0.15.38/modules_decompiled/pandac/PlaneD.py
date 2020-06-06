# File: P (Python 2.2)

import types
import libpanda
import libpandaDowncasts
from direct.ffi import FFIExternalObject
import VBase4D

class PlaneD(VBase4D.VBase4D, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _PlaneD__overloaded_constructor(self):
        self.this = libpanda._inPSkjPnOXP()
        self.userManagesMemory = 1

    
    def _PlaneD__overloaded_constructor_ptrConstLPoint3d_ptrConstLPoint3d_ptrConstLPoint3d(self, a, b, c):
        self.this = libpanda._inPSkjPgIG8(a.this, b.this, c.this)
        self.userManagesMemory = 1

    
    def _PlaneD__overloaded_constructor_ptrConstLVecBase4d(self, copy):
        self.this = libpanda._inPSkjPIv1H(copy.this)
        self.userManagesMemory = 1

    
    def _PlaneD__overloaded_constructor_ptrConstLVector3d_ptrConstLPoint3d(self, normal, point):
        self.this = libpanda._inPSkjPB10l(normal.this, point.this)
        self.userManagesMemory = 1

    
    def _PlaneD__overloaded_constructor_double_double_double_double(self, a, b, c, d):
        self.this = libpanda._inPSkjP6cFb(a, b, c, d)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPSkjPNvqr:
            libpanda._inPSkjPNvqr(self.this)
        

    
    def _PlaneD__overloaded___mul___ptrConstPlaned_ptrConstLMatrix3d(self, mat):
        returnValue = libpanda._inPSkjPVTn3(self.this, mat.this)
        returnObject = PlaneD(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _PlaneD__overloaded___mul___ptrConstPlaned_ptrConstLMatrix4d(self, mat):
        returnValue = libpanda._inPSkjPUDJL(self.this, mat.this)
        returnObject = PlaneD(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def __sub__(self):
        returnValue = libpanda._inPSkjPsBIL(self.this)
        returnObject = PlaneD(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getReflectionMat(self):
        returnValue = libpanda._inPSkjPz5g3(self.this)
        import Mat4D
        returnObject = Mat4D.Mat4D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getNormal(self):
        returnValue = libpanda._inPSkjP4OIM(self.this)
        import Vec3D
        returnObject = Vec3D.Vec3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getPoint(self):
        returnValue = libpanda._inPSkjPNQrN(self.this)
        import Point3D
        returnObject = Point3D.Point3D(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def distToPlane(self, point):
        returnValue = libpanda._inPSkjPKgCi(self.this, point.this)
        return returnValue

    
    def intersectsLine(self, intersectionPoint, p1, p2):
        returnValue = libpanda._inPSkjPzf1l(self.this, intersectionPoint.this, p1.this, p2.this)
        return returnValue

    
    def intersectsPlane(self, _from, delta, other):
        returnValue = libpanda._inPSkjPEkbi(self.this, _from.this, delta.this, other.this)
        return returnValue

    
    def output(self, out):
        returnValue = libpanda._inPSkjPxytW(self.this, out.this)
        return returnValue

    
    def _PlaneD__overloaded_write_ptrConstPlaned_ptrOstream_int(self, out, indentLevel):
        returnValue = libpanda._inPSkjPkL9K(self.this, out.this, indentLevel)
        return returnValue

    
    def _PlaneD__overloaded_write_ptrConstPlaned_ptrOstream(self, out):
        returnValue = libpanda._inPSkjP8yXN(self.this, out.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._PlaneD__overloaded_constructor(*_args)
        elif numArgs == 1:
            return self._PlaneD__overloaded_constructor_ptrConstLVecBase4d(*_args)
        elif numArgs == 2:
            return self._PlaneD__overloaded_constructor_ptrConstLVector3d_ptrConstLPoint3d(*_args)
        elif numArgs == 3:
            return self._PlaneD__overloaded_constructor_ptrConstLPoint3d_ptrConstLPoint3d_ptrConstLPoint3d(*_args)
        elif numArgs == 4:
            return self._PlaneD__overloaded_constructor_double_double_double_double(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 3 4 '

    
    def write(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._PlaneD__overloaded_write_ptrConstPlaned_ptrOstream(*_args)
        elif numArgs == 2:
            return self._PlaneD__overloaded_write_ptrConstPlaned_ptrOstream_int(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def __mul__(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Mat4D
            if isinstance(_args[0], Mat4D.Mat4D):
                return self._PlaneD__overloaded___mul___ptrConstPlaned_ptrConstLMatrix4d(*_args)
            
            import Mat3D
            if isinstance(_args[0], Mat3D.Mat3D):
                return self._PlaneD__overloaded___mul___ptrConstPlaned_ptrConstLMatrix3d(*_args)
            
            raise TypeError, 'Invalid argument 0, expected one of: <Mat4D.Mat4D> <Mat3D.Mat3D> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


