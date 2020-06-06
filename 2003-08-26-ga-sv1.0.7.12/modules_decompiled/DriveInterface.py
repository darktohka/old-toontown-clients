# File: D (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import DataNode

class DriveInterface(DataNode.DataNode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _DriveInterface__overloaded_constructor_atomicstring(self, name):
        self.this = libpanda._inPziw5qXDJ(name)
        self.userManagesMemory = 1

    
    def _DriveInterface__overloaded_constructor(self):
        self.this = libpanda._inPziw5Jz9n()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClassType():
        returnValue = libpanda._inPziw50qRB()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setForwardSpeed(self, speed):
        returnValue = libpanda._inPziw5JTpq(self.this, speed)
        return returnValue

    
    def getForwardSpeed(self):
        returnValue = libpanda._inPziw5fKJb(self.this)
        return returnValue

    
    def setReverseSpeed(self, speed):
        returnValue = libpanda._inPziw5924G(self.this, speed)
        return returnValue

    
    def getReverseSpeed(self):
        returnValue = libpanda._inPziw5tNX3(self.this)
        return returnValue

    
    def setRotateSpeed(self, speed):
        returnValue = libpanda._inPziw5NuQt(self.this, speed)
        return returnValue

    
    def getRotateSpeed(self):
        returnValue = libpanda._inPziw582Ba(self.this)
        return returnValue

    
    def setVerticalDeadZone(self, zone):
        returnValue = libpanda._inPziw5_K6o(self.this, zone)
        return returnValue

    
    def getVerticalDeadZone(self):
        returnValue = libpanda._inPziw5WqfE(self.this)
        return returnValue

    
    def setHorizontalDeadZone(self, zone):
        returnValue = libpanda._inPziw5yXFf(self.this, zone)
        return returnValue

    
    def getHorizontalDeadZone(self):
        returnValue = libpanda._inPziw5h_JJ(self.this)
        return returnValue

    
    def setVerticalRampUpTime(self, rampUpTime):
        returnValue = libpanda._inPziw5bQ8o(self.this, rampUpTime)
        return returnValue

    
    def getVerticalRampUpTime(self):
        returnValue = libpanda._inPziw5q_RD(self.this)
        return returnValue

    
    def setVerticalRampDownTime(self, rampDownTime):
        returnValue = libpanda._inPziw5nWik(self.this, rampDownTime)
        return returnValue

    
    def getVerticalRampDownTime(self):
        returnValue = libpanda._inPziw5i7QW(self.this)
        return returnValue

    
    def setHorizontalRampUpTime(self, rampUpTime):
        returnValue = libpanda._inPziw561dH(self.this, rampUpTime)
        return returnValue

    
    def getHorizontalRampUpTime(self):
        returnValue = libpanda._inPziw5MIM5(self.this)
        return returnValue

    
    def setHorizontalRampDownTime(self, rampDownTime):
        returnValue = libpanda._inPziw53qn5(self.this, rampDownTime)
        return returnValue

    
    def getHorizontalRampDownTime(self):
        returnValue = libpanda._inPziw5ACXI(self.this)
        return returnValue

    
    def getSpeed(self):
        returnValue = libpanda._inPziw5u7hx(self.this)
        return returnValue

    
    def getRotSpeed(self):
        returnValue = libpanda._inPziw5RzD6(self.this)
        return returnValue

    
    def reset(self):
        returnValue = libpanda._inPziw5KbcV(self.this)
        return returnValue

    
    def getPos(self):
        returnValue = libpanda._inPziw5dmzH(self.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getX(self):
        returnValue = libpanda._inPziw5ARV2(self.this)
        return returnValue

    
    def getY(self):
        returnValue = libpanda._inPziw5Qvo2(self.this)
        return returnValue

    
    def getZ(self):
        returnValue = libpanda._inPziw5gN82(self.this)
        return returnValue

    
    def _DriveInterface__overloaded_setPos_ptrDriveInterface_ptrConstLVecBase3f(self, vec):
        returnValue = libpanda._inPziw5Dmwj(self.this, vec.this)
        return returnValue

    
    def _DriveInterface__overloaded_setPos_ptrDriveInterface_float_float_float(self, x, y, z):
        returnValue = libpanda._inPziw5jVcP(self.this, x, y, z)
        return returnValue

    
    def setX(self, x):
        returnValue = libpanda._inPziw5mTmn(self.this, x)
        return returnValue

    
    def setY(self, y):
        returnValue = libpanda._inPziw5Wx6n(self.this, y)
        return returnValue

    
    def setZ(self, z):
        returnValue = libpanda._inPziw5GXNo(self.this, z)
        return returnValue

    
    def getHpr(self):
        returnValue = libpanda._inPziw5Y8sW(self.this)
        import VBase3
        returnObject = VBase3.VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getH(self):
        returnValue = libpanda._inPziw5Atcx(self.this)
        return returnValue

    
    def getP(self):
        returnValue = libpanda._inPziw5Af5z(self.this)
        return returnValue

    
    def getR(self):
        returnValue = libpanda._inPziw5gbg0(self.this)
        return returnValue

    
    def _DriveInterface__overloaded_setHpr_ptrDriveInterface_ptrConstLVecBase3f(self, hpr):
        returnValue = libpanda._inPziw5Ecoy(self.this, hpr.this)
        return returnValue

    
    def _DriveInterface__overloaded_setHpr_ptrDriveInterface_float_float_float(self, h, p, r):
        returnValue = libpanda._inPziw54DVe(self.this, h, p, r)
        return returnValue

    
    def setH(self, h):
        returnValue = libpanda._inPziw5m3ui(self.this, h)
        return returnValue

    
    def setP(self, p):
        returnValue = libpanda._inPziw5mBKl(self.this, p)
        return returnValue

    
    def setR(self, r):
        returnValue = libpanda._inPziw5GFxl(self.this, r)
        return returnValue

    
    def setForceRoll(self, forceRoll):
        returnValue = libpanda._inPziw5L1Ry(self.this, forceRoll)
        return returnValue

    
    def setIgnoreMouse(self, ignoreMouse):
        returnValue = libpanda._inPziw5sn9J(self.this, ignoreMouse)
        return returnValue

    
    def getIgnoreMouse(self):
        returnValue = libpanda._inPziw5EO_x(self.this)
        return returnValue

    
    def setForceMouse(self, forceMouse):
        returnValue = libpanda._inPziw5umA_(self.this, forceMouse)
        return returnValue

    
    def getForceMouse(self):
        returnValue = libpanda._inPziw5lWhe(self.this)
        return returnValue

    
    def setStopThisFrame(self, stopThisFrame):
        returnValue = libpanda._inPziw5waMx(self.this, stopThisFrame)
        return returnValue

    
    def getStopThisFrame(self):
        returnValue = libpanda._inPziw5idTo(self.this)
        return returnValue

    
    def setMat(self, mat):
        returnValue = libpanda._inPziw5SToo(self.this, mat.this)
        return returnValue

    
    def getMat(self):
        returnValue = libpanda._inPziw5oJtK(self.this)
        import Mat4
        returnObject = Mat4.Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def forceDgraph(self):
        returnValue = libpanda._inPziw5T2Wr(self.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._DriveInterface__overloaded_constructor()
        elif numArgs == 1:
            if isinstance(_args[0], types.StringType):
                return self._DriveInterface__overloaded_constructor_atomicstring(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def setPos(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import VBase3
            if isinstance(_args[0], VBase3.VBase3):
                return self._DriveInterface__overloaded_setPos_ptrDriveInterface_ptrConstLVecBase3f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase3.VBase3> '
        elif numArgs == 3:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        return self._DriveInterface__overloaded_setPos_ptrDriveInterface_float_float_float(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '

    
    def setHpr(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import VBase3
            if isinstance(_args[0], VBase3.VBase3):
                return self._DriveInterface__overloaded_setHpr_ptrDriveInterface_ptrConstLVecBase3f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase3.VBase3> '
        elif numArgs == 3:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        return self._DriveInterface__overloaded_setHpr_ptrDriveInterface_float_float_float(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '


