# File: T (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import MouseInterfaceNode

class Trackball(MouseInterfaceNode.MouseInterfaceNode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self, name):
        self.this = libpanda._inPyiw5FM2w(name)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClassType():
        returnValue = libpanda._inPyiw5ATvH()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def reset(self):
        returnValue = libpanda._inPyiw5QM3x(self.this)
        return returnValue

    
    def getForwardScale(self):
        returnValue = libpanda._inPyiw5ylhr(self.this)
        return returnValue

    
    def setForwardScale(self, fwdscale):
        returnValue = libpanda._inPyiw5eGTT(self.this, fwdscale)
        return returnValue

    
    def getPos(self):
        returnValue = libpanda._inPyiw5AeAL(self.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getX(self):
        returnValue = libpanda._inPyiw52VRC(self.this)
        return returnValue

    
    def getY(self):
        returnValue = libpanda._inPyiw5_EbC(self.this)
        return returnValue

    
    def getZ(self):
        returnValue = libpanda._inPyiw5m3kC(self.this)
        return returnValue

    
    def _Trackball__overloaded_setPos_ptrTrackball_ptrConstLVecBase3f(self, vec):
        returnValue = libpanda._inPyiw52sA5(self.this, vec.this)
        return returnValue

    
    def _Trackball__overloaded_setPos_ptrTrackball_float_float_float(self, x, y, z):
        returnValue = libpanda._inPyiw5Sryu(self.this, x, y, z)
        return returnValue

    
    def setX(self, x):
        returnValue = libpanda._inPyiw5CF66(self.this, x)
        return returnValue

    
    def setY(self, y):
        returnValue = libpanda._inPyiw5a0E7(self.this, y)
        return returnValue

    
    def setZ(self, z):
        returnValue = libpanda._inPyiw5SnO7(self.this, z)
        return returnValue

    
    def getHpr(self):
        returnValue = libpanda._inPyiw59kcy(self.this)
        import VBase3
        returnObject = VBase3.VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getH(self):
        returnValue = libpanda._inPyiw51H1_(self.this)
        return returnValue

    
    def getP(self):
        returnValue = libpanda._inPyiw52MDB(self.this)
        return returnValue

    
    def getR(self):
        returnValue = libpanda._inPyiw5muWB(self.this)
        return returnValue

    
    def _Trackball__overloaded_setHpr_ptrTrackball_ptrConstLVecBase3f(self, hpr):
        returnValue = libpanda._inPyiw5w7cg(self.this, hpr.this)
        return returnValue

    
    def _Trackball__overloaded_setHpr_ptrTrackball_float_float_float(self, h, p, r):
        returnValue = libpanda._inPyiw5QARW(self.this, h, p, r)
        return returnValue

    
    def setH(self, h):
        returnValue = libpanda._inPyiw5C3e4(self.this, h)
        return returnValue

    
    def setP(self, p):
        returnValue = libpanda._inPyiw5CMs5(self.this, p)
        return returnValue

    
    def setR(self, r):
        returnValue = libpanda._inPyiw5SuA6(self.this, r)
        return returnValue

    
    def resetOriginHere(self):
        returnValue = libpanda._inPyiw5QuKj(self.this)
        return returnValue

    
    def moveOrigin(self, x, y, z):
        returnValue = libpanda._inPyiw5gy67(self.this, x, y, z)
        return returnValue

    
    def getOrigin(self):
        returnValue = libpanda._inPyiw58Sdj(self.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setOrigin(self, origin):
        returnValue = libpanda._inPyiw5szQ3(self.this, origin.this)
        return returnValue

    
    def setInvert(self, flag):
        returnValue = libpanda._inPyiw5UESo(self.this, flag)
        return returnValue

    
    def getInvert(self):
        returnValue = libpanda._inPyiw5P3xR(self.this)
        return returnValue

    
    def setRelTo(self, relTo):
        returnValue = libpanda._inPyiw5lgYv(self.this, relTo.this)
        return returnValue

    
    def getRelTo(self):
        returnValue = libpanda._inPyiw5Mggh(self.this)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setCoordinateSystem(self, cs):
        returnValue = libpanda._inPyiw52veS(self.this, cs)
        return returnValue

    
    def getCoordinateSystem(self):
        returnValue = libpanda._inPyiw55ZF5(self.this)
        return returnValue

    
    def setMat(self, mat):
        returnValue = libpanda._inPyiw5inab(self.this, mat.this)
        return returnValue

    
    def getMat(self):
        returnValue = libpanda._inPyiw5Z1ai(self.this)
        import Mat4
        returnObject = Mat4.Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getTransMat(self):
        returnValue = libpanda._inPyiw5WvGL(self.this)
        import Mat4
        returnObject = Mat4.Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setPos(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._Trackball__overloaded_setPos_ptrTrackball_ptrConstLVecBase3f(*_args)
        elif numArgs == 3:
            return self._Trackball__overloaded_setPos_ptrTrackball_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '

    
    def setHpr(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            return self._Trackball__overloaded_setHpr_ptrTrackball_ptrConstLVecBase3f(*_args)
        elif numArgs == 3:
            return self._Trackball__overloaded_setHpr_ptrTrackball_float_float_float(*_args)
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '


