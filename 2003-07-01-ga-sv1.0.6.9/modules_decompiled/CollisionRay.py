# File: C (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import CollisionSolid

class CollisionRay(CollisionSolid.CollisionSolid, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _CollisionRay__overloaded_constructor(self):
        self.this = libpanda._inPHwcaOnzJ()
        self.userManagesMemory = 1

    
    def _CollisionRay__overloaded_constructor_ptrConstLPoint3f_ptrConstLVector3f(self, origin, direction):
        self.this = libpanda._inPHwcauWsc(origin.this, direction.this)
        self.userManagesMemory = 1

    
    def _CollisionRay__overloaded_constructor_float_float_float_float_float_float(self, ox, oy, oz, dx, dy, dz):
        self.this = libpanda._inPHwcatJco(ox, oy, oz, dx, dy, dz)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpanda and libpanda._inPHwcanAyp:
            libpanda._inPHwcanAyp(self.this)
        

    
    def getClassType():
        returnValue = libpanda._inPHwcaUl1_()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def _CollisionRay__overloaded_setOrigin_ptrCollisionRay_ptrConstLPoint3f(self, origin):
        returnValue = libpanda._inPHwcaVQg4(self.this, origin.this)
        return returnValue

    
    def _CollisionRay__overloaded_setOrigin_ptrCollisionRay_float_float_float(self, x, y, z):
        returnValue = libpanda._inPHwcaDEZ5(self.this, x, y, z)
        return returnValue

    
    def getOrigin(self):
        returnValue = libpanda._inPHwcao7AW(self.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _CollisionRay__overloaded_setDirection_ptrCollisionRay_ptrConstLVector3f(self, direction):
        returnValue = libpanda._inPHwcaEnJ_(self.this, direction.this)
        return returnValue

    
    def _CollisionRay__overloaded_setDirection_ptrCollisionRay_float_float_float(self, x, y, z):
        returnValue = libpanda._inPHwcat5k9(self.this, x, y, z)
        return returnValue

    
    def getDirection(self):
        returnValue = libpanda._inPHwcawcuk(self.this)
        import Vec3
        returnObject = Vec3.Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _CollisionRay__overloaded_setFromLens_ptrCollisionRay_ptrLensNode_ptrConstLPoint2f(self, camera, point):
        returnValue = libpanda._inPHwcaAz4_(self.this, camera.this, point.this)
        return returnValue

    
    def _CollisionRay__overloaded_setFromLens_ptrCollisionRay_ptrLensNode_float_float(self, camera, px, py):
        returnValue = libpanda._inPHwcanXhs(self.this, camera.this, px, py)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._CollisionRay__overloaded_constructor()
        elif numArgs == 2:
            import Point3
            if isinstance(_args[0], Point3.Point3):
                import Vec3
                if isinstance(_args[1], Vec3.Vec3):
                    return self._CollisionRay__overloaded_constructor_ptrConstLPoint3f_ptrConstLVector3f(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <Vec3.Vec3> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Point3.Point3> '
        elif numArgs == 6:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                            if isinstance(_args[4], types.FloatType) or isinstance(_args[4], types.IntType):
                                if isinstance(_args[5], types.FloatType) or isinstance(_args[5], types.IntType):
                                    return self._CollisionRay__overloaded_constructor_float_float_float_float_float_float(_args[0], _args[1], _args[2], _args[3], _args[4], _args[5])
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
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 2 6 '

    
    def setFromLens(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            import LensNode
            if isinstance(_args[0], LensNode.LensNode):
                import Point2
                if isinstance(_args[1], Point2.Point2):
                    return self._CollisionRay__overloaded_setFromLens_ptrCollisionRay_ptrLensNode_ptrConstLPoint2f(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <Point2.Point2> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <LensNode.LensNode> '
        elif numArgs == 3:
            import LensNode
            if isinstance(_args[0], LensNode.LensNode):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        return self._CollisionRay__overloaded_setFromLens_ptrCollisionRay_ptrLensNode_float_float(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <LensNode.LensNode> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '

    
    def setDirection(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Vec3
            if isinstance(_args[0], Vec3.Vec3):
                return self._CollisionRay__overloaded_setDirection_ptrCollisionRay_ptrConstLVector3f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Vec3.Vec3> '
        elif numArgs == 3:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        return self._CollisionRay__overloaded_setDirection_ptrCollisionRay_float_float_float(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '

    
    def setOrigin(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Point3
            if isinstance(_args[0], Point3.Point3):
                return self._CollisionRay__overloaded_setOrigin_ptrCollisionRay_ptrConstLPoint3f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Point3.Point3> '
        elif numArgs == 3:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        return self._CollisionRay__overloaded_setOrigin_ptrCollisionRay_float_float_float(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '


