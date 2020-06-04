# File: D (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import MouseInterfaceNode

class DriveInterface(MouseInterfaceNode.MouseInterfaceNode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def _DriveInterface__overloaded_constructor_atomicstring(self, name):
        self.this = libpanda._inPyiw5qXDJ(name)
        self.userManagesMemory = 1

    
    def _DriveInterface__overloaded_constructor(self):
        self.this = libpanda._inPyiw5Iz9n()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClassType():
        returnValue = libpanda._inPyiw50qRB()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setForwardSpeed(self, speed):
        returnValue = libpanda._inPyiw5KTpq(self.this, speed)
        return returnValue

    
    def getForwardSpeed(self):
        returnValue = libpanda._inPyiw5fKJb(self.this)
        return returnValue

    
    def setReverseSpeed(self, speed):
        returnValue = libpanda._inPyiw5924G(self.this, speed)
        return returnValue

    
    def getReverseSpeed(self):
        returnValue = libpanda._inPyiw5sNX3(self.this)
        return returnValue

    
    def setRotateSpeed(self, speed):
        returnValue = libpanda._inPyiw5MuQt(self.this, speed)
        return returnValue

    
    def getRotateSpeed(self):
        returnValue = libpanda._inPyiw582Ba(self.this)
        return returnValue

    
    def setVerticalDeadZone(self, zone):
        returnValue = libpanda._inPyiw5_K6o(self.this, zone)
        return returnValue

    
    def getVerticalDeadZone(self):
        returnValue = libpanda._inPyiw5WqfE(self.this)
        return returnValue

    
    def setHorizontalDeadZone(self, zone):
        returnValue = libpanda._inPyiw5yXFf(self.this, zone)
        return returnValue

    
    def getHorizontalDeadZone(self):
        returnValue = libpanda._inPyiw5h_JJ(self.this)
        return returnValue

    
    def setVerticalRampUpTime(self, rampUpTime):
        returnValue = libpanda._inPyiw5aQ8o(self.this, rampUpTime)
        return returnValue

    
    def getVerticalRampUpTime(self):
        returnValue = libpanda._inPyiw5q_RD(self.this)
        return returnValue

    
    def setVerticalRampDownTime(self, rampDownTime):
        returnValue = libpanda._inPyiw5kWik(self.this, rampDownTime)
        return returnValue

    
    def getVerticalRampDownTime(self):
        returnValue = libpanda._inPyiw5i7QW(self.this)
        return returnValue

    
    def setHorizontalRampUpTime(self, rampUpTime):
        returnValue = libpanda._inPyiw561dH(self.this, rampUpTime)
        return returnValue

    
    def getHorizontalRampUpTime(self):
        returnValue = libpanda._inPyiw5NIM5(self.this)
        return returnValue

    
    def setHorizontalRampDownTime(self, rampDownTime):
        returnValue = libpanda._inPyiw52qn5(self.this, rampDownTime)
        return returnValue

    
    def getHorizontalRampDownTime(self):
        returnValue = libpanda._inPyiw5ACXI(self.this)
        return returnValue

    
    def getSpeed(self):
        returnValue = libpanda._inPyiw5v7hx(self.this)
        return returnValue

    
    def getRotSpeed(self):
        returnValue = libpanda._inPyiw5QzD6(self.this)
        return returnValue

    
    def reset(self):
        returnValue = libpanda._inPyiw5KbcV(self.this)
        return returnValue

    
    def getPos(self):
        returnValue = libpanda._inPyiw5dmzH(self.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getX(self):
        returnValue = libpanda._inPyiw5BRV2(self.this)
        return returnValue

    
    def getY(self):
        returnValue = libpanda._inPyiw5Rvo2(self.this)
        return returnValue

    
    def getZ(self):
        returnValue = libpanda._inPyiw5hN82(self.this)
        return returnValue

    
    def _DriveInterface__overloaded_setPos_ptrDriveInterface_ptrConstLVecBase3f(self, vec):
        returnValue = libpanda._inPyiw5Amwj(self.this, vec.this)
        return returnValue

    
    def _DriveInterface__overloaded_setPos_ptrDriveInterface_float_float_float(self, x, y, z):
        returnValue = libpanda._inPyiw5jVcP(self.this, x, y, z)
        return returnValue

    
    def setX(self, x):
        returnValue = libpanda._inPyiw5pTmn(self.this, x)
        return returnValue

    
    def setY(self, y):
        returnValue = libpanda._inPyiw5Zx6n(self.this, y)
        return returnValue

    
    def setZ(self, z):
        returnValue = libpanda._inPyiw5JXNo(self.this, z)
        return returnValue

    
    def getHpr(self):
        returnValue = libpanda._inPyiw5Y8sW(self.this)
        import VBase3
        returnObject = VBase3.VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getH(self):
        returnValue = libpanda._inPyiw5Btcx(self.this)
        return returnValue

    
    def getP(self):
        returnValue = libpanda._inPyiw5Bf5z(self.this)
        return returnValue

    
    def getR(self):
        returnValue = libpanda._inPyiw5hbg0(self.this)
        return returnValue

    
    def _DriveInterface__overloaded_setHpr_ptrDriveInterface_ptrConstLVecBase3f(self, hpr):
        returnValue = libpanda._inPyiw5Fcoy(self.this, hpr.this)
        return returnValue

    
    def _DriveInterface__overloaded_setHpr_ptrDriveInterface_float_float_float(self, h, p, r):
        returnValue = libpanda._inPyiw54DVe(self.this, h, p, r)
        return returnValue

    
    def setH(self, h):
        returnValue = libpanda._inPyiw5p3ui(self.this, h)
        return returnValue

    
    def setP(self, p):
        returnValue = libpanda._inPyiw5pBKl(self.this, p)
        return returnValue

    
    def setR(self, r):
        returnValue = libpanda._inPyiw5JFxl(self.this, r)
        return returnValue

    
    def setForceRoll(self, forceRoll):
        returnValue = libpanda._inPyiw5I1Ry(self.this, forceRoll)
        return returnValue

    
    def setIgnoreMouse(self, ignoreMouse):
        returnValue = libpanda._inPyiw5sn9J(self.this, ignoreMouse)
        return returnValue

    
    def getIgnoreMouse(self):
        returnValue = libpanda._inPyiw5HO_x(self.this)
        return returnValue

    
    def setForceMouse(self, forceMouse):
        returnValue = libpanda._inPyiw5pmA_(self.this, forceMouse)
        return returnValue

    
    def getForceMouse(self):
        returnValue = libpanda._inPyiw5lWhe(self.this)
        return returnValue

    
    def setStopThisFrame(self, stopThisFrame):
        returnValue = libpanda._inPyiw5xaMx(self.this, stopThisFrame)
        return returnValue

    
    def getStopThisFrame(self):
        returnValue = libpanda._inPyiw5jdTo(self.this)
        return returnValue

    
    def setMat(self, mat):
        returnValue = libpanda._inPyiw5TToo(self.this, mat.this)
        return returnValue

    
    def getMat(self):
        returnValue = libpanda._inPyiw5oJtK(self.this)
        import Mat4
        returnObject = Mat4.Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def forceDgraph(self):
        returnValue = libpanda._inPyiw5Q2Wr(self.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 0:
            return self._DriveInterface__overloaded_constructor(*_args)
        elif numArgs == 1:
            return self._DriveInterface__overloaded_constructor_atomicstring(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    
    def setPos(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._DriveInterface__overloaded_setPos_ptrDriveInterface_ptrConstLVecBase3f(*_args)
        elif numArgs == 3:
            return self._DriveInterface__overloaded_setPos_ptrDriveInterface_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '

    
    def setHpr(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._DriveInterface__overloaded_setHpr_ptrDriveInterface_ptrConstLVecBase3f(*_args)
        elif numArgs == 3:
            return self._DriveInterface__overloaded_setHpr_ptrDriveInterface_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '


