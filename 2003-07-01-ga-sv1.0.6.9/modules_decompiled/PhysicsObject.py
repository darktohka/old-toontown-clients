# File: P (Python 2.2)

import types
import libpandaphysics
import libpandaphysicsDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import TypedReferenceCount

class PhysicsObject(TypedReferenceCount.TypedReferenceCount, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaphysicsDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _PhysicsObject__overloaded_constructor(self):
        self.this = libpandaphysics._inP9fJJ09Dv()
        self.userManagesMemory = 1

    
    def _PhysicsObject__overloaded_constructor_ptrConstPhysicsObject(self, copy):
        self.this = libpandaphysics._inP9fJJniDU(copy.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClassType():
        returnValue = libpandaphysics._inP9fJJbfoM()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def assign(self, other):
        returnValue = libpandaphysics._inP9fJJK_qc(self.this, other.this)
        returnObject = PhysicsObject(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def setMass(self, parameter1):
        returnValue = libpandaphysics._inP9fJJ4Zyt(self.this, parameter1)
        return returnValue

    
    def getMass(self):
        returnValue = libpandaphysics._inP9fJJ5psm(self.this)
        return returnValue

    
    def _PhysicsObject__overloaded_setPosition_ptrPhysicsObject_ptrConstLPoint3f(self, pos):
        returnValue = libpandaphysics._inP9fJJ2gAg(self.this, pos.this)
        return returnValue

    
    def _PhysicsObject__overloaded_setPosition_ptrPhysicsObject_float_float_float(self, x, y, z):
        returnValue = libpandaphysics._inP9fJJ2VGQ(self.this, x, y, z)
        return returnValue

    
    def getPosition(self):
        returnValue = libpandaphysics._inP9fJJ3Mf1(self.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setPositionHandOfGod(self, pos):
        returnValue = libpandaphysics._inP9fJJ2n4n(self.this, pos.this)
        return returnValue

    
    def setLastPosition(self, pos):
        returnValue = libpandaphysics._inP9fJJ99P2(self.this, pos.this)
        return returnValue

    
    def getLastPosition(self):
        returnValue = libpandaphysics._inP9fJJcPBj(self.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def _PhysicsObject__overloaded_setVelocity_ptrPhysicsObject_ptrConstLVector3f(self, vel):
        returnValue = libpandaphysics._inP9fJJZTzH(self.this, vel.this)
        return returnValue

    
    def _PhysicsObject__overloaded_setVelocity_ptrPhysicsObject_float_float_float(self, x, y, z):
        returnValue = libpandaphysics._inP9fJJAJOH(self.this, x, y, z)
        return returnValue

    
    def getVelocity(self):
        returnValue = libpandaphysics._inP9fJJbDns(self.this)
        import Vec3
        returnObject = Vec3.Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setActive(self, flag):
        returnValue = libpandaphysics._inP9fJJl3K1(self.this, flag)
        return returnValue

    
    def getActive(self):
        returnValue = libpandaphysics._inP9fJJA4xf(self.this)
        return returnValue

    
    def setOriented(self, flag):
        returnValue = libpandaphysics._inP9fJJ_NXG(self.this, flag)
        return returnValue

    
    def getOriented(self):
        returnValue = libpandaphysics._inP9fJJfb01(self.this)
        return returnValue

    
    def setTerminalVelocity(self, tv):
        returnValue = libpandaphysics._inP9fJJdEdt(self.this, tv)
        return returnValue

    
    def getTerminalVelocity(self):
        returnValue = libpandaphysics._inP9fJJWEE2(self.this)
        return returnValue

    
    def setOrientation(self, orientation):
        returnValue = libpandaphysics._inP9fJJRXq_(self.this, orientation.this)
        return returnValue

    
    def getOrientation(self):
        returnValue = libpandaphysics._inP9fJJUaE6(self.this)
        import LOrientationf
        returnObject = LOrientationf.LOrientationf(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setRotation(self, rotation):
        returnValue = libpandaphysics._inP9fJJZq8W(self.this, rotation.this)
        return returnValue

    
    def getRotation(self):
        returnValue = libpandaphysics._inP9fJJXNx7(self.this)
        import Vec3
        returnObject = Vec3.Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getInertialTensor(self):
        returnValue = libpandaphysics._inP9fJJ3KW7(self.this)
        import Mat4
        returnObject = Mat4.Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getLcs(self):
        returnValue = libpandaphysics._inP9fJJg4Kt(self.this)
        import Mat4
        returnObject = Mat4.Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def makeCopy(self):
        returnValue = libpandaphysics._inP9fJJWP2J(self.this)
        returnObject = PhysicsObject(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._PhysicsObject__overloaded_constructor()
        elif numArgs == 1:
            if isinstance(_args[0], PhysicsObject):
                return self._PhysicsObject__overloaded_constructor_ptrConstPhysicsObject(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <PhysicsObject> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def setPosition(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Point3
            if isinstance(_args[0], Point3.Point3):
                return self._PhysicsObject__overloaded_setPosition_ptrPhysicsObject_ptrConstLPoint3f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Point3.Point3> '
        elif numArgs == 3:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        return self._PhysicsObject__overloaded_setPosition_ptrPhysicsObject_float_float_float(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '

    
    def setVelocity(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Vec3
            if isinstance(_args[0], Vec3.Vec3):
                return self._PhysicsObject__overloaded_setVelocity_ptrPhysicsObject_ptrConstLVector3f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Vec3.Vec3> '
        elif numArgs == 3:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        return self._PhysicsObject__overloaded_setVelocity_ptrPhysicsObject_float_float_float(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '


