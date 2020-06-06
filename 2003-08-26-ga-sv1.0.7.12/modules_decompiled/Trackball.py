# File: T (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import DataNode

class Trackball(DataNode.DataNode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self, name):
        self.this = libpanda._inPziw5KM2w(name)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClassType():
        returnValue = libpanda._inPziw5ATvH()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def reset(self):
        returnValue = libpanda._inPziw5RM3x(self.this)
        return returnValue

    
    def getForwardScale(self):
        returnValue = libpanda._inPziw5zlhr(self.this)
        return returnValue

    
    def setForwardScale(self, fwdscale):
        returnValue = libpanda._inPziw5eGTT(self.this, fwdscale)
        return returnValue

    
    def getPos(self):
        returnValue = libpanda._inPziw5AeAL(self.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getX(self):
        returnValue = libpanda._inPziw52VRC(self.this)
        return returnValue

    
    def getY(self):
        returnValue = libpanda._inPziw5_EbC(self.this)
        return returnValue

    
    def getZ(self):
        returnValue = libpanda._inPziw5m3kC(self.this)
        return returnValue

    
    def _Trackball__overloaded_setPos_ptrTrackball_ptrConstLVecBase3f(self, vec):
        returnValue = libpanda._inPziw51sA5(self.this, vec.this)
        return returnValue

    
    def _Trackball__overloaded_setPos_ptrTrackball_float_float_float(self, x, y, z):
        returnValue = libpanda._inPziw5Tryu(self.this, x, y, z)
        return returnValue

    
    def setX(self, x):
        returnValue = libpanda._inPziw5DF66(self.this, x)
        return returnValue

    
    def setY(self, y):
        returnValue = libpanda._inPziw5b0E7(self.this, y)
        return returnValue

    
    def setZ(self, z):
        returnValue = libpanda._inPziw5TnO7(self.this, z)
        return returnValue

    
    def getHpr(self):
        returnValue = libpanda._inPziw5Clcy(self.this)
        import VBase3
        returnObject = VBase3.VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getH(self):
        returnValue = libpanda._inPziw52H1_(self.this)
        return returnValue

    
    def getP(self):
        returnValue = libpanda._inPziw52MDB(self.this)
        return returnValue

    
    def getR(self):
        returnValue = libpanda._inPziw5muWB(self.this)
        return returnValue

    
    def _Trackball__overloaded_setHpr_ptrTrackball_ptrConstLVecBase3f(self, hpr):
        returnValue = libpanda._inPziw537cg(self.this, hpr.this)
        return returnValue

    
    def _Trackball__overloaded_setHpr_ptrTrackball_float_float_float(self, h, p, r):
        returnValue = libpanda._inPziw5QARW(self.this, h, p, r)
        return returnValue

    
    def setH(self, h):
        returnValue = libpanda._inPziw5D3e4(self.this, h)
        return returnValue

    
    def setP(self, p):
        returnValue = libpanda._inPziw5DMs5(self.this, p)
        return returnValue

    
    def setR(self, r):
        returnValue = libpanda._inPziw5TuA6(self.this, r)
        return returnValue

    
    def resetOriginHere(self):
        returnValue = libpanda._inPziw5PuKj(self.this)
        return returnValue

    
    def moveOrigin(self, x, y, z):
        returnValue = libpanda._inPziw5hy67(self.this, x, y, z)
        return returnValue

    
    def getOrigin(self):
        returnValue = libpanda._inPziw59Sdj(self.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setOrigin(self, origin):
        returnValue = libpanda._inPziw5rzQ3(self.this, origin.this)
        return returnValue

    
    def setInvert(self, flag):
        returnValue = libpanda._inPziw5VESo(self.this, flag)
        return returnValue

    
    def getInvert(self):
        returnValue = libpanda._inPziw5P3xR(self.this)
        return returnValue

    
    def setRelTo(self, relTo):
        returnValue = libpanda._inPziw5kgYv(self.this, relTo.this)
        return returnValue

    
    def getRelTo(self):
        returnValue = libpanda._inPziw5Nggh(self.this)
        import NodePath
        returnObject = NodePath.NodePath(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setCoordinateSystem(self, cs):
        returnValue = libpanda._inPziw52veS(self.this, cs)
        return returnValue

    
    def getCoordinateSystem(self):
        returnValue = libpanda._inPziw54ZF5(self.this)
        return returnValue

    
    def setMat(self, mat):
        returnValue = libpanda._inPziw5inab(self.this, mat.this)
        return returnValue

    
    def getMat(self):
        returnValue = libpanda._inPziw5e1ai(self.this)
        import Mat4
        returnObject = Mat4.Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getTransMat(self):
        returnValue = libpanda._inPziw5WvGL(self.this)
        import Mat4
        returnObject = Mat4.Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setPos(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import VBase3
            if isinstance(_args[0], VBase3.VBase3):
                return self._Trackball__overloaded_setPos_ptrTrackball_ptrConstLVecBase3f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase3.VBase3> '
        elif numArgs == 3:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        return self._Trackball__overloaded_setPos_ptrTrackball_float_float_float(_args[0], _args[1], _args[2])
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
                return self._Trackball__overloaded_setHpr_ptrTrackball_ptrConstLVecBase3f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase3.VBase3> '
        elif numArgs == 3:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        return self._Trackball__overloaded_setHpr_ptrTrackball_float_float_float(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '


