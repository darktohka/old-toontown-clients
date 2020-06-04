# File: C (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import CollisionSolid

class CollisionTube(CollisionSolid.CollisionSolid, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _CollisionTube__overloaded_constructor_ptrConstLPoint3f_ptrConstLPoint3f_float(self, a, db, radius):
        self.this = libpanda._inPHwcaxNS4(a.this, db.this, radius)
        self.userManagesMemory = 1

    
    def _CollisionTube__overloaded_constructor_float_float_float_float_float_float_float(self, ax, ay, az, bx, by, bz, radius):
        self.this = libpanda._inPHwcae_eG(ax, ay, az, bx, by, bz, radius)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPHwcauuTD:
            libpanda._inPHwcauuTD(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPHwcaur7C()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _CollisionTube__overloaded_setPointA_ptrCollisionTube_ptrConstLPoint3f(self, a):
        returnValue = libpanda._inPHwca_Wt6(self.this, a.this)
        return returnValue

    
    def _CollisionTube__overloaded_setPointA_ptrCollisionTube_float_float_float(self, x, y, z):
        returnValue = libpanda._inPHwca2wJc(self.this, x, y, z)
        return returnValue

    
    def getPointA(self):
        returnValue = libpanda._inPHwcapxl7(self.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _CollisionTube__overloaded_setPointB_ptrCollisionTube_ptrConstLPoint3f(self, b):
        returnValue = libpanda._inPHwcafSS7(self.this, b.this)
        return returnValue

    
    def _CollisionTube__overloaded_setPointB_ptrCollisionTube_float_float_float(self, x, y, z):
        returnValue = libpanda._inPHwcaWPxc(self.this, x, y, z)
        return returnValue

    
    def getPointB(self):
        returnValue = libpanda._inPHwcaJ1M8(self.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setRadius(self, radius):
        returnValue = libpanda._inPHwca5G54(self.this, radius)
        return returnValue

    
    def getRadius(self):
        returnValue = libpanda._inPHwcaSKpL(self.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 3:
            import Point3
            if isinstance(_args[0], Point3.Point3):
                import Point3
                if isinstance(_args[1], Point3.Point3):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        return self._CollisionTube__overloaded_constructor_ptrConstLPoint3f_ptrConstLPoint3f_float(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <Point3.Point3> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Point3.Point3> '
        elif numArgs == 7:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                            if isinstance(_args[4], types.FloatType) or isinstance(_args[4], types.IntType):
                                if isinstance(_args[5], types.FloatType) or isinstance(_args[5], types.IntType):
                                    if isinstance(_args[6], types.FloatType) or isinstance(_args[6], types.IntType):
                                        return self._CollisionTube__overloaded_constructor_float_float_float_float_float_float_float(_args[0], _args[1], _args[2], _args[3], _args[4], _args[5], _args[6])
                                    else:
                                        raise TypeError, 'Invalid argument 6, expected one of: <types.FloatType> '
                                else:
                                    raise TypeError, 'Invalid argument 5, expected one of: <types.FloatType> '
                            else:
                                raise TypeError, 'Invalid argument 4, expected one of: <types.FloatType> '
                        else:
                            raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 3 7 '

    
    def setPointB(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Point3
            if isinstance(_args[0], Point3.Point3):
                return self._CollisionTube__overloaded_setPointB_ptrCollisionTube_ptrConstLPoint3f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Point3.Point3> '
        elif numArgs == 3:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        return self._CollisionTube__overloaded_setPointB_ptrCollisionTube_float_float_float(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '

    
    def setPointA(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Point3
            if isinstance(_args[0], Point3.Point3):
                return self._CollisionTube__overloaded_setPointA_ptrCollisionTube_ptrConstLPoint3f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Point3.Point3> '
        elif numArgs == 3:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        return self._CollisionTube__overloaded_setPointA_ptrCollisionTube_float_float_float(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '


