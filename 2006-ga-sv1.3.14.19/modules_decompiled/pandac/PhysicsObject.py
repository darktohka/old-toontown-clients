# File: P (Python 2.2)

import types
import libpandaphysics
import libpandaphysicsDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import TypedReferenceCount

class PhysicsObject(TypedReferenceCount.TypedReferenceCount, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaphysicsDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _PhysicsObject__overloaded_constructor(self):
        self.this = libpandaphysics._inP9fJJ19Dv()
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

    
    def setActive(self, flag):
        returnValue = libpandaphysics._inP9fJJk3K1(self.this, flag)
        return returnValue

    
    def getActive(self):
        returnValue = libpandaphysics._inP9fJJA4xf(self.this)
        return returnValue

    
    def setMass(self, parameter1):
        returnValue = libpandaphysics._inP9fJJ7Zyt(self.this, parameter1)
        return returnValue

    
    def getMass(self):
        returnValue = libpandaphysics._inP9fJJ4psm(self.this)
        return returnValue

    
    def _PhysicsObject__overloaded_setPosition_ptrPhysicsObject_ptrConstLPoint3f(self, pos):
        returnValue = libpandaphysics._inP9fJJxgAg(self.this, pos.this)
        return returnValue

    
    def _PhysicsObject__overloaded_setPosition_ptrPhysicsObject_float_float_float(self, x, y, z):
        returnValue = libpandaphysics._inP9fJJ2VGQ(self.this, x, y, z)
        return returnValue

    
    def getPosition(self):
        returnValue = libpandaphysics._inP9fJJ2Mf1(self.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def resetPosition(self, pos):
        returnValue = libpandaphysics._inP9fJJrXx9(self.this, pos.this)
        return returnValue

    
    def setLastPosition(self, pos):
        returnValue = libpandaphysics._inP9fJJy9P2(self.this, pos.this)
        return returnValue

    
    def getLastPosition(self):
        returnValue = libpandaphysics._inP9fJJfPBj(self.this)
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
        returnValue = libpandaphysics._inP9fJJYDns(self.this)
        import Vec3
        returnObject = Vec3.Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getImplicitVelocity(self):
        returnValue = libpandaphysics._inP9fJJm1Ut(self.this)
        import Vec3
        returnObject = Vec3.Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def addImpulse(self, impulse):
        returnValue = libpandaphysics._inP9fJJuEW4(self.this, impulse.this)
        return returnValue

    
    def setTerminalVelocity(self, tv):
        returnValue = libpandaphysics._inP9fJJcEdt(self.this, tv)
        return returnValue

    
    def getTerminalVelocity(self):
        returnValue = libpandaphysics._inP9fJJVEE2(self.this)
        return returnValue

    
    def setOriented(self, flag):
        returnValue = libpandaphysics._inP9fJJ_NXG(self.this, flag)
        return returnValue

    
    def getOriented(self):
        returnValue = libpandaphysics._inP9fJJeb01(self.this)
        return returnValue

    
    def setOrientation(self, orientation):
        returnValue = libpandaphysics._inP9fJJQXq_(self.this, orientation.this)
        return returnValue

    
    def getOrientation(self):
        returnValue = libpandaphysics._inP9fJJLaE6(self.this)
        import LOrientationf
        returnObject = LOrientationf.LOrientationf(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def resetOrientation(self, orientation):
        returnValue = libpandaphysics._inP9fJJueOQ(self.this, orientation.this)
        return returnValue

    
    def setRotation(self, rotation):
        returnValue = libpandaphysics._inP9fJJZq8W(self.this, rotation.this)
        return returnValue

    
    def getRotation(self):
        returnValue = libpandaphysics._inP9fJJYNx7(self.this)
        import Vec3
        returnObject = Vec3.Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getInertialTensor(self):
        returnValue = libpandaphysics._inP9fJJ2KW7(self.this)
        import Mat4
        returnObject = Mat4.Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getLcs(self):
        returnValue = libpandaphysics._inP9fJJj4Kt(self.this)
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

    
    def output(self, out):
        returnValue = libpandaphysics._inP9fJJkx3h(self.this, out.this)
        return returnValue

    
    def _PhysicsObject__overloaded_write_ptrConstPhysicsObject_ptrOstream_unsignedint(self, out, indent):
        returnValue = libpandaphysics._inP9fJJygbI(self.this, out.this, indent)
        return returnValue

    
    def _PhysicsObject__overloaded_write_ptrConstPhysicsObject_ptrOstream(self, out):
        returnValue = libpandaphysics._inP9fJJax5t(self.this, out.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._PhysicsObject__overloaded_constructor(*_args)
        elif numArgs == 1:
            return self._PhysicsObject__overloaded_constructor_ptrConstPhysicsObject(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def write(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._PhysicsObject__overloaded_write_ptrConstPhysicsObject_ptrOstream(*_args)
        elif numArgs == 2:
            return self._PhysicsObject__overloaded_write_ptrConstPhysicsObject_ptrOstream_unsignedint(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setPosition(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._PhysicsObject__overloaded_setPosition_ptrPhysicsObject_ptrConstLPoint3f(*_args)
        elif numArgs == 3:
            return self._PhysicsObject__overloaded_setPosition_ptrPhysicsObject_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '

    
    def setVelocity(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._PhysicsObject__overloaded_setVelocity_ptrPhysicsObject_ptrConstLVector3f(*_args)
        elif numArgs == 3:
            return self._PhysicsObject__overloaded_setVelocity_ptrPhysicsObject_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '


