# File: L (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import TypedWritableReferenceCount

class Lens(TypedWritableReferenceCount.TypedWritableReferenceCount, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    FCShear = 16
    FCRoll = 1
    FCAspectRatio = 8
    FCOffAxis = 4
    FCCameraPlane = 2
    
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
        if libpanda and libpanda._inPMAKPO1zx:
            libpanda._inPMAKPO1zx(self.this)
        

    
    def getDefaultNear():
        returnValue = libpanda._inPMAKP1de1()
        return returnValue

    getDefaultNear = staticmethod(getDefaultNear)
    
    def getDefaultFar():
        returnValue = libpanda._inPMAKPDhjq()
        return returnValue

    getDefaultFar = staticmethod(getDefaultFar)
    
    def getClassType():
        returnValue = libpanda._inPMAKPX6_e()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def makeCopy(self):
        returnValue = libpanda._inPMAKPg23I(self.this)
        returnObject = Lens(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def _Lens__overloaded_extrude_ptrConstLens_ptrConstLPoint2f_ptrLPoint3f_ptrLPoint3f(self, point2d, nearPoint, farPoint):
        returnValue = libpanda._inPMAKPEXAo(self.this, point2d.this, nearPoint.this, farPoint.this)
        return returnValue

    
    def _Lens__overloaded_extrude_ptrConstLens_ptrConstLPoint3f_ptrLPoint3f_ptrLPoint3f(self, point2d, nearPoint, farPoint):
        returnValue = libpanda._inPMAKPUxUo(self.this, point2d.this, nearPoint.this, farPoint.this)
        return returnValue

    
    def _Lens__overloaded_project_ptrConstLens_ptrConstLPoint3f_ptrLPoint2f(self, point3d, point2d):
        returnValue = libpanda._inPMAKPy6hM(self.this, point3d.this, point2d.this)
        return returnValue

    
    def _Lens__overloaded_project_ptrConstLens_ptrConstLPoint3f_ptrLPoint3f(self, point3d, point2d):
        returnValue = libpanda._inPMAKPyFwN(self.this, point3d.this, point2d.this)
        return returnValue

    
    def setChangeEvent(self, event):
        returnValue = libpanda._inPMAKPOGXC(self.this, event)
        return returnValue

    
    def getChangeEvent(self):
        returnValue = libpanda._inPMAKPJ_Ni(self.this)
        return returnValue

    
    def setCoordinateSystem(self, cs):
        returnValue = libpanda._inPMAKP0iUE(self.this, cs)
        return returnValue

    
    def getCoordinateSystem(self):
        returnValue = libpanda._inPMAKPsmpX(self.this)
        return returnValue

    
    def clear(self):
        returnValue = libpanda._inPMAKPOuga(self.this)
        return returnValue

    
    def _Lens__overloaded_setFilmSize_ptrLens_ptrConstLVecBase2f(self, filmSize):
        returnValue = libpanda._inPMAKPkLtR(self.this, filmSize.this)
        return returnValue

    
    def _Lens__overloaded_setFilmSize_ptrLens_float(self, width):
        returnValue = libpanda._inPMAKPkFkr(self.this, width)
        return returnValue

    
    def _Lens__overloaded_setFilmSize_ptrLens_float_float(self, width, height):
        returnValue = libpanda._inPMAKP7VW8(self.this, width, height)
        return returnValue

    
    def getFilmSize(self):
        returnValue = libpanda._inPMAKPpaPJ(self.this)
        import VBase2
        returnObject = VBase2.VBase2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _Lens__overloaded_setFilmOffset_ptrLens_ptrConstLVecBase2f(self, filmOffset):
        returnValue = libpanda._inPMAKP54pC(self.this, filmOffset.this)
        return returnValue

    
    def _Lens__overloaded_setFilmOffset_ptrLens_float_float(self, x, y):
        returnValue = libpanda._inPMAKPYcn6(self.this, x, y)
        return returnValue

    
    def getFilmOffset(self):
        returnValue = libpanda._inPMAKPb8t_(self.this)
        import Vec2
        returnObject = Vec2.Vec2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setFocalLength(self, focalLength):
        returnValue = libpanda._inPMAKPNiTK(self.this, focalLength)
        return returnValue

    
    def getFocalLength(self):
        returnValue = libpanda._inPMAKPZQhl(self.this)
        return returnValue

    
    def _Lens__overloaded_setFov_ptrLens_ptrConstLVecBase2f(self, fov):
        returnValue = libpanda._inPMAKPTIxI(self.this, fov.this)
        return returnValue

    
    def _Lens__overloaded_setFov_ptrLens_float(self, fov):
        returnValue = libpanda._inPMAKPakJq(self.this, fov)
        return returnValue

    
    def _Lens__overloaded_setFov_ptrLens_float_float(self, hfov, vfov):
        returnValue = libpanda._inPMAKPwNaC(self.this, hfov, vfov)
        return returnValue

    
    def getFov(self):
        returnValue = libpanda._inPMAKPHTNq(self.this)
        import VBase2
        returnObject = VBase2.VBase2(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getHfov(self):
        returnValue = libpanda._inPMAKPFGjN(self.this)
        return returnValue

    
    def getVfov(self):
        returnValue = libpanda._inPMAKP9tnO(self.this)
        return returnValue

    
    def setAspectRatio(self, aspectRatio):
        returnValue = libpanda._inPMAKP8kwh(self.this, aspectRatio)
        return returnValue

    
    def getAspectRatio(self):
        returnValue = libpanda._inPMAKPib98(self.this)
        return returnValue

    
    def setNear(self, nearDistance):
        returnValue = libpanda._inPMAKPxQgw(self.this, nearDistance)
        return returnValue

    
    def getNear(self):
        returnValue = libpanda._inPMAKPwVA4(self.this)
        return returnValue

    
    def setFar(self, farDistance):
        returnValue = libpanda._inPMAKPcoiP(self.this, farDistance)
        return returnValue

    
    def getFar(self):
        returnValue = libpanda._inPMAKP9WmP(self.this)
        return returnValue

    
    def setNearFar(self, nearDistance, farDistance):
        returnValue = libpanda._inPMAKP9vjM(self.this, nearDistance, farDistance)
        return returnValue

    
    def _Lens__overloaded_setViewHpr_ptrLens_ptrConstLVecBase3f(self, viewHpr):
        returnValue = libpanda._inPMAKPEI9n(self.this, viewHpr.this)
        return returnValue

    
    def _Lens__overloaded_setViewHpr_ptrLens_float_float_float(self, h, p, r):
        returnValue = libpanda._inPMAKPlvxd(self.this, h, p, r)
        return returnValue

    
    def getViewHpr(self):
        returnValue = libpanda._inPMAKPzOnI(self.this)
        import VBase3
        returnObject = VBase3.VBase3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def _Lens__overloaded_setViewVector_ptrLens_ptrConstLVector3f_ptrConstLVector3f(self, viewVector, upVector):
        returnValue = libpanda._inPMAKPtmpn(self.this, viewVector.this, upVector.this)
        return returnValue

    
    def _Lens__overloaded_setViewVector_ptrLens_float_float_float_float_float_float(self, x, y, z, i, j, k):
        returnValue = libpanda._inPMAKPRtqd(self.this, x, y, z, i, j, k)
        return returnValue

    
    def getViewVector(self):
        returnValue = libpanda._inPMAKPzzLu(self.this)
        import Vec3
        returnObject = Vec3.Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getUpVector(self):
        returnValue = libpanda._inPMAKPqyc7(self.this)
        import Vec3
        returnObject = Vec3.Vec3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getNodalPoint(self):
        returnValue = libpanda._inPMAKPMlmp(self.this)
        import Point3
        returnObject = Point3.Point3(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setIodOffset(self, offset):
        returnValue = libpanda._inPMAKPJeae(self.this, offset)
        return returnValue

    
    def getIodOffset(self):
        returnValue = libpanda._inPMAKPnMEa(self.this)
        return returnValue

    
    def setViewMat(self, viewMat):
        returnValue = libpanda._inPMAKPK_7i(self.this, viewMat.this)
        return returnValue

    
    def getViewMat(self):
        returnValue = libpanda._inPMAKPP_m4(self.this)
        import Mat4
        returnObject = Mat4.Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def setFrustumFromCorners(self, ul, ur, ll, lr, flags):
        returnValue = libpanda._inPMAKPEH8Q(self.this, ul.this, ur.this, ll.this, lr.this, flags)
        return returnValue

    
    def recomputeAll(self):
        returnValue = libpanda._inPMAKPSJre(self.this)
        return returnValue

    
    def isLinear(self):
        returnValue = libpanda._inPMAKP7Z__(self.this)
        return returnValue

    
    def makeGeometry(self):
        returnValue = libpanda._inPMAKPIeEy(self.this)
        import Geom
        returnObject = Geom.Geom(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def makeBounds(self):
        returnValue = libpanda._inPMAKPa5g0(self.this)
        import BoundingVolume
        returnObject = BoundingVolume.BoundingVolume(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def getProjectionMat(self):
        returnValue = libpanda._inPMAKPrmTG(self.this)
        import Mat4
        returnObject = Mat4.Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def getProjectionMatInv(self):
        returnValue = libpanda._inPMAKPmcoU(self.this)
        import Mat4
        returnObject = Mat4.Mat4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        return returnObject

    
    def output(self, out):
        returnValue = libpanda._inPMAKPB_GJ(self.this, out.this)
        return returnValue

    
    def _Lens__overloaded_write_ptrConstLens_ptrOstream_int(self, out, indentLevel):
        returnValue = libpanda._inPMAKPqMpk(self.this, out.this, indentLevel)
        return returnValue

    
    def _Lens__overloaded_write_ptrConstLens_ptrOstream(self, out):
        returnValue = libpanda._inPMAKPsXWp(self.this, out.this)
        return returnValue

    
    def extrude(self, *_args):
        numArgs = len(_args)
        if numArgs == 3:
            import Point3
            import Point2
            if isinstance(_args[0], Point3.Point3):
                import Point3
                if isinstance(_args[1], Point3.Point3):
                    import Point3
                    if isinstance(_args[2], Point3.Point3):
                        return self._Lens__overloaded_extrude_ptrConstLens_ptrConstLPoint3f_ptrLPoint3f_ptrLPoint3f(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <Point3.Point3> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <Point3.Point3> '
            elif isinstance(_args[0], Point2.Point2):
                import Point3
                if isinstance(_args[1], Point3.Point3):
                    import Point3
                    if isinstance(_args[2], Point3.Point3):
                        return self._Lens__overloaded_extrude_ptrConstLens_ptrConstLPoint2f_ptrLPoint3f_ptrLPoint3f(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <Point3.Point3> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <Point3.Point3> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Point3.Point3> <Point2.Point2> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 3 '

    
    def write(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                return self._Lens__overloaded_write_ptrConstLens_ptrOstream(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        elif numArgs == 2:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                if isinstance(_args[1], types.IntType):
                    return self._Lens__overloaded_write_ptrConstLens_ptrOstream_int(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setFilmOffset(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import VBase2
            if isinstance(_args[0], VBase2.VBase2):
                return self._Lens__overloaded_setFilmOffset_ptrLens_ptrConstLVecBase2f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase2.VBase2> '
        elif numArgs == 2:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    return self._Lens__overloaded_setFilmOffset_ptrLens_float_float(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def project(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            import Point3
            if isinstance(_args[0], Point3.Point3):
                import Point3
                import Point2
                if isinstance(_args[1], Point3.Point3):
                    return self._Lens__overloaded_project_ptrConstLens_ptrConstLPoint3f_ptrLPoint3f(_args[0], _args[1])
                elif isinstance(_args[1], Point2.Point2):
                    return self._Lens__overloaded_project_ptrConstLens_ptrConstLPoint3f_ptrLPoint2f(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <Point3.Point3> <Point2.Point2> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Point3.Point3> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 '

    
    def setViewVector(self, *_args):
        numArgs = len(_args)
        if numArgs == 2:
            import Vec3
            if isinstance(_args[0], Vec3.Vec3):
                import Vec3
                if isinstance(_args[1], Vec3.Vec3):
                    return self._Lens__overloaded_setViewVector_ptrLens_ptrConstLVector3f_ptrConstLVector3f(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <Vec3.Vec3> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Vec3.Vec3> '
        elif numArgs == 6:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                            if isinstance(_args[4], types.FloatType) or isinstance(_args[4], types.IntType):
                                if isinstance(_args[5], types.FloatType) or isinstance(_args[5], types.IntType):
                                    return self._Lens__overloaded_setViewVector_ptrLens_float_float_float_float_float_float(_args[0], _args[1], _args[2], _args[3], _args[4], _args[5])
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
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 6 '

    
    def setViewHpr(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import VBase3
            if isinstance(_args[0], VBase3.VBase3):
                return self._Lens__overloaded_setViewHpr_ptrLens_ptrConstLVecBase3f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <VBase3.VBase3> '
        elif numArgs == 3:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        return self._Lens__overloaded_setViewHpr_ptrLens_float_float_float(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '

    
    def setFov(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import VBase2
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return self._Lens__overloaded_setFov_ptrLens_float(_args[0])
            elif isinstance(_args[0], VBase2.VBase2):
                return self._Lens__overloaded_setFov_ptrLens_ptrConstLVecBase2f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase2.VBase2> '
        elif numArgs == 2:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    return self._Lens__overloaded_setFov_ptrLens_float_float(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    
    def setFilmSize(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import VBase2
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                return self._Lens__overloaded_setFilmSize_ptrLens_float(_args[0])
            elif isinstance(_args[0], VBase2.VBase2):
                return self._Lens__overloaded_setFilmSize_ptrLens_ptrConstLVecBase2f(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase2.VBase2> '
        elif numArgs == 2:
            if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    return self._Lens__overloaded_setFilmSize_ptrLens_float_float(_args[0], _args[1])
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


