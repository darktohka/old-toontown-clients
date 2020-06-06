# File: G (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import BoundingVolume

class GeometricBoundingVolume(BoundingVolume.BoundingVolume, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self):
        raise RuntimeError, 'No C++ constructor defined for class: ' + self.__class__.__name__

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPSkjPkfdG:
            libpanda._inPSkjPkfdG(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPSkjPA1fo()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _GeometricBoundingVolume__overloaded_extendBy_ptrGeometricBoundingVolume_ptrConstGeometricBoundingVolume(self, vol):
        returnValue = libpanda._inPSkjPyZa3(self.this, vol.this)
        return returnValue

    
    def _GeometricBoundingVolume__overloaded_extendBy_ptrGeometricBoundingVolume_ptrConstLPoint3f(self, point):
        returnValue = libpanda._inPSkjP5ZtT(self.this, point.this)
        return returnValue

    
    def around(self, first, last):
        returnValue = libpanda._inPSkjPcv6k(self.this, first.this, last.this)
        return returnValue

    
    def _GeometricBoundingVolume__overloaded_contains_ptrConstGeometricBoundingVolume_ptrConstGeometricBoundingVolume(self, vol):
        returnValue = libpanda._inPSkjPA8A3(self.this, vol.this)
        return returnValue

    
    def _GeometricBoundingVolume__overloaded_contains_ptrConstGeometricBoundingVolume_ptrConstLPoint3f(self, point):
        returnValue = libpanda._inPSkjPEncR(self.this, point.this)
        return returnValue

    
    def _GeometricBoundingVolume__overloaded_contains_ptrConstGeometricBoundingVolume_ptrConstLPoint3f_ptrConstLPoint3f(self, a, b):
        returnValue = libpanda._inPSkjP0SwX(self.this, a.this, b.this)
        return returnValue

    
    def getApproxCenter(self):
        returnValue = libpanda._inPSkjPHh7m(self.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def xform(self, mat):
        returnValue = libpanda._inPSkjPLb98(self.this, mat.this)
        return returnValue

    
    def contains(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Point3
            if isinstance(_args[0], Point3.Point3):
                return self._GeometricBoundingVolume__overloaded_contains_ptrConstGeometricBoundingVolume_ptrConstLPoint3f(_args[0])
            elif isinstance(_args[0], GeometricBoundingVolume):
                return self._GeometricBoundingVolume__overloaded_contains_ptrConstGeometricBoundingVolume_ptrConstGeometricBoundingVolume(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Point3.Point3> <GeometricBoundingVolume> '
        elif numArgs == 2:
            import Point3
            if isinstance(_args[0], Point3.Point3):
                import Point3
                if isinstance(_args[1], Point3.Point3):
                    return self._GeometricBoundingVolume__overloaded_contains_ptrConstGeometricBoundingVolume_ptrConstLPoint3f_ptrConstLPoint3f(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <Point3.Point3> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Point3.Point3> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def extendBy(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Point3
            if isinstance(_args[0], Point3.Point3):
                return self._GeometricBoundingVolume__overloaded_extendBy_ptrGeometricBoundingVolume_ptrConstLPoint3f(_args[0])
            elif isinstance(_args[0], GeometricBoundingVolume):
                return self._GeometricBoundingVolume__overloaded_extendBy_ptrGeometricBoundingVolume_ptrConstGeometricBoundingVolume(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Point3.Point3> <GeometricBoundingVolume> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


