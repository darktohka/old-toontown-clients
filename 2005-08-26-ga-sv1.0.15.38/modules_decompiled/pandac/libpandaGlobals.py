# File: l (Python 2.2)

import types
import libpanda
import ConfigVariableSearchPath
import ConfigPage
import Mat3D
import Vec3D
import Mat3
import Vec3
import Mat4D
import Mat4
import QuatD
import Quat
import Point2D
import Point2
import Point3D
import Point3
import VBase3D
import VBase3
import VBase4D
import VBase4
import Vec2D
import Vec2
import Datagram
import DatagramIterator
import PandaNode
import AnimControlCollection

def rad2Deg(*_args):
    numArgs = len(_args)
    if numArgs == 1:
        if isinstance(_args[0], types.FloatType) and isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
            return __overloaded_rad2Deg_float(*_args)
        
        if isinstance(_args[0], types.FloatType) and isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
            return __overloaded_rad2Deg_double(*_args)
        
        raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <types.FloatType> '
    else:
        raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


def genericReadDatagram(*_args):
    numArgs = len(_args)
    if numArgs == 2:
        import Mat4D
        if isinstance(_args[0], Mat4D.Mat4D):
            return __overloaded_genericReadDatagram_ptrLMatrix4d_ptrDatagramIterator(*_args)
        
        import Mat4
        if isinstance(_args[0], Mat4.Mat4):
            return __overloaded_genericReadDatagram_ptrLMatrix4f_ptrDatagramIterator(*_args)
        
        import Mat3D
        if isinstance(_args[0], Mat3D.Mat3D):
            return __overloaded_genericReadDatagram_ptrLMatrix3d_ptrDatagramIterator(*_args)
        
        import Mat3
        if isinstance(_args[0], Mat3.Mat3):
            return __overloaded_genericReadDatagram_ptrLMatrix3f_ptrDatagramIterator(*_args)
        
        raise TypeError, 'Invalid argument 0, expected one of: <Mat4D.Mat4D> <Mat4.Mat4> <Mat3D.Mat3D> <Mat3.Mat3> '
    else:
        raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 '


def oldToNewHpr(*_args):
    numArgs = len(_args)
    if numArgs == 1:
        import VBase3D
        if isinstance(_args[0], VBase3D.VBase3D):
            return __overloaded_oldToNewHpr_ptrConstLVecBase3d(*_args)
        
        import VBase3
        if isinstance(_args[0], VBase3.VBase3):
            return __overloaded_oldToNewHpr_ptrConstLVecBase3f(*_args)
        
        raise TypeError, 'Invalid argument 0, expected one of: <VBase3D.VBase3D> <VBase3.VBase3> '
    else:
        raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


def decomposeMatrixOldHpr(*_args):
    numArgs = len(_args)
    if numArgs == 4:
        import Mat3D
        if isinstance(_args[0], Mat3D.Mat3D):
            return __overloaded_decomposeMatrixOldHpr_ptrConstLMatrix3d_ptrLVecBase3d_ptrLVecBase3d_ptrLVecBase3d(*_args)
        
        import Mat3
        if isinstance(_args[0], Mat3.Mat3):
            return __overloaded_decomposeMatrixOldHpr_ptrConstLMatrix3f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f(*_args)
        
        raise TypeError, 'Invalid argument 0, expected one of: <Mat3D.Mat3D> <Mat3.Mat3> '
    elif numArgs == 5:
        import Mat4D
        if isinstance(_args[0], Mat4D.Mat4D):
            return __overloaded_decomposeMatrixOldHpr_ptrConstLMatrix4d_ptrLVecBase3d_ptrLVecBase3d_ptrLVecBase3d_ptrLVecBase3d(*_args)
        
        import Mat4
        if isinstance(_args[0], Mat4.Mat4):
            return __overloaded_decomposeMatrixOldHpr_ptrConstLMatrix4f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f(*_args)
        
        import Mat3D
        if isinstance(_args[0], Mat3D.Mat3D):
            return __overloaded_decomposeMatrixOldHpr_ptrConstLMatrix3d_ptrLVecBase3d_ptrLVecBase3d_ptrLVecBase3d___enum__CoordinateSystem(*_args)
        
        import Mat3
        if isinstance(_args[0], Mat3.Mat3):
            return __overloaded_decomposeMatrixOldHpr_ptrConstLMatrix3f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f___enum__CoordinateSystem(*_args)
        
        raise TypeError, 'Invalid argument 0, expected one of: <Mat4D.Mat4D> <Mat4.Mat4> <Mat3D.Mat3D> <Mat3.Mat3> '
    elif numArgs == 6:
        import Mat4D
        if isinstance(_args[0], Mat4D.Mat4D):
            return __overloaded_decomposeMatrixOldHpr_ptrConstLMatrix4d_ptrLVecBase3d_ptrLVecBase3d_ptrLVecBase3d_ptrLVecBase3d___enum__CoordinateSystem(*_args)
        
        import Mat4
        if isinstance(_args[0], Mat4.Mat4):
            return __overloaded_decomposeMatrixOldHpr_ptrConstLMatrix4f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f___enum__CoordinateSystem(*_args)
        
        raise TypeError, 'Invalid argument 0, expected one of: <Mat4D.Mat4D> <Mat4.Mat4> '
    else:
        raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 4 5 6 '


def invert(*_args):
    numArgs = len(_args)
    if numArgs == 1:
        import QuatD
        if isinstance(_args[0], QuatD.QuatD):
            return __overloaded_invert_ptrConstLQuaterniond(*_args)
        
        import Quat
        if isinstance(_args[0], Quat.Quat):
            return __overloaded_invert_ptrConstLQuaternionf(*_args)
        
        import Mat4D
        if isinstance(_args[0], Mat4D.Mat4D):
            return __overloaded_invert_ptrConstLMatrix4d(*_args)
        
        import Mat4
        if isinstance(_args[0], Mat4.Mat4):
            return __overloaded_invert_ptrConstLMatrix4f(*_args)
        
        import Mat3D
        if isinstance(_args[0], Mat3D.Mat3D):
            return __overloaded_invert_ptrConstLMatrix3d(*_args)
        
        import Mat3
        if isinstance(_args[0], Mat3.Mat3):
            return __overloaded_invert_ptrConstLMatrix3f(*_args)
        
        raise TypeError, 'Invalid argument 0, expected one of: <QuatD.QuatD> <Quat.Quat> <Mat4D.Mat4D> <Mat4.Mat4> <Mat3D.Mat3D> <Mat3.Mat3> '
    else:
        raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


def transpose(*_args):
    numArgs = len(_args)
    if numArgs == 1:
        import Mat4D
        if isinstance(_args[0], Mat4D.Mat4D):
            return __overloaded_transpose_ptrConstLMatrix4d(*_args)
        
        import Mat4
        if isinstance(_args[0], Mat4.Mat4):
            return __overloaded_transpose_ptrConstLMatrix4f(*_args)
        
        import Mat3D
        if isinstance(_args[0], Mat3D.Mat3D):
            return __overloaded_transpose_ptrConstLMatrix3d(*_args)
        
        import Mat3
        if isinstance(_args[0], Mat3.Mat3):
            return __overloaded_transpose_ptrConstLMatrix3f(*_args)
        
        raise TypeError, 'Invalid argument 0, expected one of: <Mat4D.Mat4D> <Mat4.Mat4> <Mat3D.Mat3D> <Mat3.Mat3> '
    else:
        raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


def composeMatrixNewHpr(*_args):
    numArgs = len(_args)
    if numArgs == 4:
        import Mat3D
        if isinstance(_args[0], Mat3D.Mat3D):
            return __overloaded_composeMatrixNewHpr_ptrLMatrix3d_ptrConstLVecBase3d_ptrConstLVecBase3d_ptrConstLVecBase3d(*_args)
        
        import Mat3
        if isinstance(_args[0], Mat3.Mat3):
            return __overloaded_composeMatrixNewHpr_ptrLMatrix3f_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f(*_args)
        
        raise TypeError, 'Invalid argument 0, expected one of: <Mat3D.Mat3D> <Mat3.Mat3> '
    elif numArgs == 5:
        import Mat4D
        if isinstance(_args[0], Mat4D.Mat4D):
            return __overloaded_composeMatrixNewHpr_ptrLMatrix4d_ptrConstLVecBase3d_ptrConstLVecBase3d_ptrConstLVecBase3d_ptrConstLVecBase3d(*_args)
        
        import Mat4
        if isinstance(_args[0], Mat4.Mat4):
            return __overloaded_composeMatrixNewHpr_ptrLMatrix4f_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f(*_args)
        
        import Mat3D
        if isinstance(_args[0], Mat3D.Mat3D):
            return __overloaded_composeMatrixNewHpr_ptrLMatrix3d_ptrConstLVecBase3d_ptrConstLVecBase3d_ptrConstLVecBase3d___enum__CoordinateSystem(*_args)
        
        import Mat3
        if isinstance(_args[0], Mat3.Mat3):
            return __overloaded_composeMatrixNewHpr_ptrLMatrix3f_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f___enum__CoordinateSystem(*_args)
        
        raise TypeError, 'Invalid argument 0, expected one of: <Mat4D.Mat4D> <Mat4.Mat4> <Mat3D.Mat3D> <Mat3.Mat3> '
    elif numArgs == 6:
        import Mat4D
        if isinstance(_args[0], Mat4D.Mat4D):
            return __overloaded_composeMatrixNewHpr_ptrLMatrix4d_ptrConstLVecBase3d_ptrConstLVecBase3d_ptrConstLVecBase3d_ptrConstLVecBase3d___enum__CoordinateSystem(*_args)
        
        import Mat4
        if isinstance(_args[0], Mat4.Mat4):
            return __overloaded_composeMatrixNewHpr_ptrLMatrix4f_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f___enum__CoordinateSystem(*_args)
        
        raise TypeError, 'Invalid argument 0, expected one of: <Mat4D.Mat4D> <Mat4.Mat4> '
    else:
        raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 4 5 6 '


def genericWriteDatagram(*_args):
    numArgs = len(_args)
    if numArgs == 2:
        import Datagram
        if isinstance(_args[0], Datagram.Datagram):
            import Mat4D
            if isinstance(_args[1], Mat4D.Mat4D):
                return __overloaded_genericWriteDatagram_ptrDatagram_ptrConstLMatrix4d(*_args)
            
            import Mat4
            if isinstance(_args[1], Mat4.Mat4):
                return __overloaded_genericWriteDatagram_ptrDatagram_ptrConstLMatrix4f(*_args)
            
            import Mat3D
            if isinstance(_args[1], Mat3D.Mat3D):
                return __overloaded_genericWriteDatagram_ptrDatagram_ptrConstLMatrix3d(*_args)
            
            import Mat3
            if isinstance(_args[1], Mat3.Mat3):
                return __overloaded_genericWriteDatagram_ptrDatagram_ptrConstLMatrix3f(*_args)
            
            raise TypeError, 'Invalid argument 1, expected one of: <Mat4D.Mat4D> <Mat4.Mat4> <Mat3D.Mat3D> <Mat3.Mat3> '
        
        raise TypeError, 'Invalid argument 0, expected one of: <Datagram.Datagram> '
    else:
        raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 '


def deg2Rad(*_args):
    numArgs = len(_args)
    if numArgs == 1:
        if isinstance(_args[0], types.FloatType) and isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
            return __overloaded_deg2Rad_float(*_args)
        
        if isinstance(_args[0], types.FloatType) and isinstance(_args[0], types.IntType) or isinstance(_args[0], types.LongType):
            return __overloaded_deg2Rad_double(*_args)
        
        raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <types.FloatType> '
    else:
        raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


def __mul__(*_args):
    numArgs = len(_args)
    if numArgs == 2:
        import Vec3D
        if isinstance(_args[0], Vec3D.Vec3D):
            return __overloaded___mul___ptrConstLVector3d_ptrConstLMatrix4d(*_args)
        
        import Vec3
        if isinstance(_args[0], Vec3.Vec3):
            return __overloaded___mul___ptrConstLVector3f_ptrConstLMatrix4f(*_args)
        
        import Vec2D
        if isinstance(_args[0], Vec2D.Vec2D):
            return __overloaded___mul___ptrConstLVector2d_ptrConstLMatrix3d(*_args)
        
        import Vec2
        if isinstance(_args[0], Vec2.Vec2):
            return __overloaded___mul___ptrConstLVector2f_ptrConstLMatrix3f(*_args)
        
        import VBase4D
        if isinstance(_args[0], VBase4D.VBase4D):
            return __overloaded___mul___ptrConstLVecBase4d_ptrConstLMatrix4d(*_args)
        
        import VBase4
        if isinstance(_args[0], VBase4.VBase4):
            return __overloaded___mul___ptrConstLVecBase4f_ptrConstLMatrix4f(*_args)
        
        import VBase3D
        if isinstance(_args[0], VBase3D.VBase3D):
            return __overloaded___mul___ptrConstLVecBase3d_ptrConstLMatrix3d(*_args)
        
        import Point3
        if isinstance(_args[0], Point3.Point3):
            return __overloaded___mul___ptrConstLPoint3f_ptrConstLMatrix4f(*_args)
        
        import VBase3
        if isinstance(_args[0], VBase3.VBase3):
            return __overloaded___mul___ptrConstLVecBase3f_ptrConstLMatrix3f(*_args)
        
        import Point3D
        if isinstance(_args[0], Point3D.Point3D):
            return __overloaded___mul___ptrConstLPoint3d_ptrConstLMatrix4d(*_args)
        
        import Point2D
        if isinstance(_args[0], Point2D.Point2D):
            return __overloaded___mul___ptrConstLPoint2d_ptrConstLMatrix3d(*_args)
        
        import Point2
        if isinstance(_args[0], Point2.Point2):
            return __overloaded___mul___ptrConstLPoint2f_ptrConstLMatrix3f(*_args)
        
        import Mat4D
        if isinstance(_args[0], Mat4D.Mat4D):
            return __overloaded___mul___ptrConstLMatrix4d_ptrConstLQuaterniond(*_args)
        
        import Mat4
        if isinstance(_args[0], Mat4.Mat4):
            return __overloaded___mul___ptrConstLMatrix4f_ptrConstLQuaternionf(*_args)
        
        import Mat3D
        if isinstance(_args[0], Mat3D.Mat3D):
            return __overloaded___mul___ptrConstLMatrix3d_ptrConstLQuaterniond(*_args)
        
        import Mat3
        if isinstance(_args[0], Mat3.Mat3):
            return __overloaded___mul___ptrConstLMatrix3f_ptrConstLQuaternionf(*_args)
        
        raise TypeError, 'Invalid argument 0, expected one of: <Vec3D.Vec3D> <Vec3.Vec3> <Vec2D.Vec2D> <Vec2.Vec2> <VBase4D.VBase4D> <VBase4.VBase4> <VBase3D.VBase3D> <Point3.Point3> <VBase3.VBase3> <Point3D.Point3D> <Point2D.Point2D> <Point2.Point2> <Mat4D.Mat4D> <Mat4.Mat4> <Mat3D.Mat3D> <Mat3.Mat3> '
    else:
        raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 '


def lookAt(*_args):
    numArgs = len(_args)
    if numArgs == 2:
        import QuatD
        if isinstance(_args[0], QuatD.QuatD):
            return __overloaded_lookAt_ptrLQuaterniond_ptrConstLVector3d(*_args)
        
        import Quat
        if isinstance(_args[0], Quat.Quat):
            return __overloaded_lookAt_ptrLQuaternionf_ptrConstLVector3f(*_args)
        
        import Mat4D
        if isinstance(_args[0], Mat4D.Mat4D):
            return __overloaded_lookAt_ptrLMatrix4d_ptrConstLVector3d(*_args)
        
        import Mat4
        if isinstance(_args[0], Mat4.Mat4):
            return __overloaded_lookAt_ptrLMatrix4f_ptrConstLVector3f(*_args)
        
        import Mat3D
        if isinstance(_args[0], Mat3D.Mat3D):
            return __overloaded_lookAt_ptrLMatrix3d_ptrConstLVector3d(*_args)
        
        import Mat3
        if isinstance(_args[0], Mat3.Mat3):
            return __overloaded_lookAt_ptrLMatrix3f_ptrConstLVector3f(*_args)
        
        raise TypeError, 'Invalid argument 0, expected one of: <QuatD.QuatD> <Quat.Quat> <Mat4D.Mat4D> <Mat4.Mat4> <Mat3D.Mat3D> <Mat3.Mat3> '
    elif numArgs == 3:
        import QuatD
        if isinstance(_args[0], QuatD.QuatD):
            import Vec3D
            if isinstance(_args[1], Vec3D.Vec3D):
                if isinstance(_args[2], types.IntType) or isinstance(_args[2], types.LongType):
                    return __overloaded_lookAt_ptrLQuaterniond_ptrConstLVector3d___enum__CoordinateSystem(*_args)
                
                import Vec3D
                if isinstance(_args[2], Vec3D.Vec3D):
                    return __overloaded_lookAt_ptrLQuaterniond_ptrConstLVector3d_ptrConstLVector3d(*_args)
                
                raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> <Vec3D.Vec3D> '
            
            raise TypeError, 'Invalid argument 1, expected one of: <Vec3D.Vec3D> '
        
        import Quat
        if isinstance(_args[0], Quat.Quat):
            import Vec3
            if isinstance(_args[1], Vec3.Vec3):
                if isinstance(_args[2], types.IntType) or isinstance(_args[2], types.LongType):
                    return __overloaded_lookAt_ptrLQuaternionf_ptrConstLVector3f___enum__CoordinateSystem(*_args)
                
                import Vec3
                if isinstance(_args[2], Vec3.Vec3):
                    return __overloaded_lookAt_ptrLQuaternionf_ptrConstLVector3f_ptrConstLVector3f(*_args)
                
                raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> <Vec3.Vec3> '
            
            raise TypeError, 'Invalid argument 1, expected one of: <Vec3.Vec3> '
        
        import Mat4D
        if isinstance(_args[0], Mat4D.Mat4D):
            import Vec3D
            if isinstance(_args[1], Vec3D.Vec3D):
                if isinstance(_args[2], types.IntType) or isinstance(_args[2], types.LongType):
                    return __overloaded_lookAt_ptrLMatrix4d_ptrConstLVector3d___enum__CoordinateSystem(*_args)
                
                import Vec3D
                if isinstance(_args[2], Vec3D.Vec3D):
                    return __overloaded_lookAt_ptrLMatrix4d_ptrConstLVector3d_ptrConstLVector3d(*_args)
                
                raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> <Vec3D.Vec3D> '
            
            raise TypeError, 'Invalid argument 1, expected one of: <Vec3D.Vec3D> '
        
        import Mat4
        if isinstance(_args[0], Mat4.Mat4):
            import Vec3
            if isinstance(_args[1], Vec3.Vec3):
                if isinstance(_args[2], types.IntType) or isinstance(_args[2], types.LongType):
                    return __overloaded_lookAt_ptrLMatrix4f_ptrConstLVector3f___enum__CoordinateSystem(*_args)
                
                import Vec3
                if isinstance(_args[2], Vec3.Vec3):
                    return __overloaded_lookAt_ptrLMatrix4f_ptrConstLVector3f_ptrConstLVector3f(*_args)
                
                raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> <Vec3.Vec3> '
            
            raise TypeError, 'Invalid argument 1, expected one of: <Vec3.Vec3> '
        
        import Mat3D
        if isinstance(_args[0], Mat3D.Mat3D):
            import Vec3D
            if isinstance(_args[1], Vec3D.Vec3D):
                if isinstance(_args[2], types.IntType) or isinstance(_args[2], types.LongType):
                    return __overloaded_lookAt_ptrLMatrix3d_ptrConstLVector3d___enum__CoordinateSystem(*_args)
                
                import Vec3D
                if isinstance(_args[2], Vec3D.Vec3D):
                    return __overloaded_lookAt_ptrLMatrix3d_ptrConstLVector3d_ptrConstLVector3d(*_args)
                
                raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> <Vec3D.Vec3D> '
            
            raise TypeError, 'Invalid argument 1, expected one of: <Vec3D.Vec3D> '
        
        import Mat3
        if isinstance(_args[0], Mat3.Mat3):
            import Vec3
            if isinstance(_args[1], Vec3.Vec3):
                if isinstance(_args[2], types.IntType) or isinstance(_args[2], types.LongType):
                    return __overloaded_lookAt_ptrLMatrix3f_ptrConstLVector3f___enum__CoordinateSystem(*_args)
                
                import Vec3
                if isinstance(_args[2], Vec3.Vec3):
                    return __overloaded_lookAt_ptrLMatrix3f_ptrConstLVector3f_ptrConstLVector3f(*_args)
                
                raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> <Vec3.Vec3> '
            
            raise TypeError, 'Invalid argument 1, expected one of: <Vec3.Vec3> '
        
        raise TypeError, 'Invalid argument 0, expected one of: <QuatD.QuatD> <Quat.Quat> <Mat4D.Mat4D> <Mat4.Mat4> <Mat3D.Mat3D> <Mat3.Mat3> '
    elif numArgs == 4:
        import QuatD
        if isinstance(_args[0], QuatD.QuatD):
            return __overloaded_lookAt_ptrLQuaterniond_ptrConstLVector3d_ptrConstLVector3d___enum__CoordinateSystem(*_args)
        
        import Quat
        if isinstance(_args[0], Quat.Quat):
            return __overloaded_lookAt_ptrLQuaternionf_ptrConstLVector3f_ptrConstLVector3f___enum__CoordinateSystem(*_args)
        
        import Mat4D
        if isinstance(_args[0], Mat4D.Mat4D):
            return __overloaded_lookAt_ptrLMatrix4d_ptrConstLVector3d_ptrConstLVector3d___enum__CoordinateSystem(*_args)
        
        import Mat4
        if isinstance(_args[0], Mat4.Mat4):
            return __overloaded_lookAt_ptrLMatrix4f_ptrConstLVector3f_ptrConstLVector3f___enum__CoordinateSystem(*_args)
        
        import Mat3D
        if isinstance(_args[0], Mat3D.Mat3D):
            return __overloaded_lookAt_ptrLMatrix3d_ptrConstLVector3d_ptrConstLVector3d___enum__CoordinateSystem(*_args)
        
        import Mat3
        if isinstance(_args[0], Mat3.Mat3):
            return __overloaded_lookAt_ptrLMatrix3f_ptrConstLVector3f_ptrConstLVector3f___enum__CoordinateSystem(*_args)
        
        raise TypeError, 'Invalid argument 0, expected one of: <QuatD.QuatD> <Quat.Quat> <Mat4D.Mat4D> <Mat4.Mat4> <Mat3D.Mat3D> <Mat3.Mat3> '
    else:
        raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 4 '


def newToOldHpr(*_args):
    numArgs = len(_args)
    if numArgs == 1:
        import VBase3D
        if isinstance(_args[0], VBase3D.VBase3D):
            return __overloaded_newToOldHpr_ptrConstLVecBase3d(*_args)
        
        import VBase3
        if isinstance(_args[0], VBase3.VBase3):
            return __overloaded_newToOldHpr_ptrConstLVecBase3f(*_args)
        
        raise TypeError, 'Invalid argument 0, expected one of: <VBase3D.VBase3D> <VBase3.VBase3> '
    else:
        raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


def rotateTo(*_args):
    numArgs = len(_args)
    if numArgs == 3:
        import Mat4D
        if isinstance(_args[0], Mat4D.Mat4D):
            return __overloaded_rotateTo_ptrLMatrix4d_ptrConstLVector3d_ptrConstLVector3d(*_args)
        
        import Mat4
        if isinstance(_args[0], Mat4.Mat4):
            return __overloaded_rotateTo_ptrLMatrix4f_ptrConstLVector3f_ptrConstLVector3f(*_args)
        
        import Mat3D
        if isinstance(_args[0], Mat3D.Mat3D):
            return __overloaded_rotateTo_ptrLMatrix3d_ptrConstLVector3d_ptrConstLVector3d(*_args)
        
        import Mat3
        if isinstance(_args[0], Mat3.Mat3):
            return __overloaded_rotateTo_ptrLMatrix3f_ptrConstLVector3f_ptrConstLVector3f(*_args)
        
        raise TypeError, 'Invalid argument 0, expected one of: <Mat4D.Mat4D> <Mat4.Mat4> <Mat3D.Mat3D> <Mat3.Mat3> '
    else:
        raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 3 '


def composeMatrixOldHpr(*_args):
    numArgs = len(_args)
    if numArgs == 4:
        import Mat3D
        if isinstance(_args[0], Mat3D.Mat3D):
            return __overloaded_composeMatrixOldHpr_ptrLMatrix3d_ptrConstLVecBase3d_ptrConstLVecBase3d_ptrConstLVecBase3d(*_args)
        
        import Mat3
        if isinstance(_args[0], Mat3.Mat3):
            return __overloaded_composeMatrixOldHpr_ptrLMatrix3f_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f(*_args)
        
        raise TypeError, 'Invalid argument 0, expected one of: <Mat3D.Mat3D> <Mat3.Mat3> '
    elif numArgs == 5:
        import Mat4D
        if isinstance(_args[0], Mat4D.Mat4D):
            return __overloaded_composeMatrixOldHpr_ptrLMatrix4d_ptrConstLVecBase3d_ptrConstLVecBase3d_ptrConstLVecBase3d_ptrConstLVecBase3d(*_args)
        
        import Mat4
        if isinstance(_args[0], Mat4.Mat4):
            return __overloaded_composeMatrixOldHpr_ptrLMatrix4f_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f(*_args)
        
        import Mat3D
        if isinstance(_args[0], Mat3D.Mat3D):
            return __overloaded_composeMatrixOldHpr_ptrLMatrix3d_ptrConstLVecBase3d_ptrConstLVecBase3d_ptrConstLVecBase3d___enum__CoordinateSystem(*_args)
        
        import Mat3
        if isinstance(_args[0], Mat3.Mat3):
            return __overloaded_composeMatrixOldHpr_ptrLMatrix3f_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f___enum__CoordinateSystem(*_args)
        
        raise TypeError, 'Invalid argument 0, expected one of: <Mat4D.Mat4D> <Mat4.Mat4> <Mat3D.Mat3D> <Mat3.Mat3> '
    elif numArgs == 6:
        import Mat4D
        if isinstance(_args[0], Mat4D.Mat4D):
            return __overloaded_composeMatrixOldHpr_ptrLMatrix4d_ptrConstLVecBase3d_ptrConstLVecBase3d_ptrConstLVecBase3d_ptrConstLVecBase3d___enum__CoordinateSystem(*_args)
        
        import Mat4
        if isinstance(_args[0], Mat4.Mat4):
            return __overloaded_composeMatrixOldHpr_ptrLMatrix4f_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f___enum__CoordinateSystem(*_args)
        
        raise TypeError, 'Invalid argument 0, expected one of: <Mat4D.Mat4D> <Mat4.Mat4> '
    else:
        raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 4 5 6 '


def autoBind(*_args):
    numArgs = len(_args)
    if numArgs == 2:
        return __overloaded_autoBind_ptrPandaNode_ptrAnimControlCollection(*_args)
    elif numArgs == 3:
        return __overloaded_autoBind_ptrPandaNode_ptrAnimControlCollection_int(*_args)
    else:
        raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '


def decomposeMatrixNewHpr(*_args):
    numArgs = len(_args)
    if numArgs == 4:
        import Mat3D
        if isinstance(_args[0], Mat3D.Mat3D):
            return __overloaded_decomposeMatrixNewHpr_ptrConstLMatrix3d_ptrLVecBase3d_ptrLVecBase3d_ptrLVecBase3d(*_args)
        
        import Mat3
        if isinstance(_args[0], Mat3.Mat3):
            return __overloaded_decomposeMatrixNewHpr_ptrConstLMatrix3f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f(*_args)
        
        raise TypeError, 'Invalid argument 0, expected one of: <Mat3D.Mat3D> <Mat3.Mat3> '
    elif numArgs == 5:
        import Mat4D
        if isinstance(_args[0], Mat4D.Mat4D):
            return __overloaded_decomposeMatrixNewHpr_ptrConstLMatrix4d_ptrLVecBase3d_ptrLVecBase3d_ptrLVecBase3d_ptrLVecBase3d(*_args)
        
        import Mat4
        if isinstance(_args[0], Mat4.Mat4):
            return __overloaded_decomposeMatrixNewHpr_ptrConstLMatrix4f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f(*_args)
        
        import Mat3D
        if isinstance(_args[0], Mat3D.Mat3D):
            return __overloaded_decomposeMatrixNewHpr_ptrConstLMatrix3d_ptrLVecBase3d_ptrLVecBase3d_ptrLVecBase3d___enum__CoordinateSystem(*_args)
        
        import Mat3
        if isinstance(_args[0], Mat3.Mat3):
            return __overloaded_decomposeMatrixNewHpr_ptrConstLMatrix3f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f___enum__CoordinateSystem(*_args)
        
        raise TypeError, 'Invalid argument 0, expected one of: <Mat4D.Mat4D> <Mat4.Mat4> <Mat3D.Mat3D> <Mat3.Mat3> '
    elif numArgs == 6:
        import Mat4D
        if isinstance(_args[0], Mat4D.Mat4D):
            return __overloaded_decomposeMatrixNewHpr_ptrConstLMatrix4d_ptrLVecBase3d_ptrLVecBase3d_ptrLVecBase3d_ptrLVecBase3d___enum__CoordinateSystem(*_args)
        
        import Mat4
        if isinstance(_args[0], Mat4.Mat4):
            return __overloaded_decomposeMatrixNewHpr_ptrConstLMatrix4f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f___enum__CoordinateSystem(*_args)
        
        raise TypeError, 'Invalid argument 0, expected one of: <Mat4D.Mat4D> <Mat4.Mat4> '
    else:
        raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 4 5 6 '


def composeMatrix(*_args):
    numArgs = len(_args)
    if numArgs == 3:
        import Mat3D
        if isinstance(_args[0], Mat3D.Mat3D):
            return __overloaded_composeMatrix_ptrLMatrix3d_ptrConstLVecBase3d_ptrConstLVecBase3d(*_args)
        
        import Mat3
        if isinstance(_args[0], Mat3.Mat3):
            return __overloaded_composeMatrix_ptrLMatrix3f_ptrConstLVecBase3f_ptrConstLVecBase3f(*_args)
        
        raise TypeError, 'Invalid argument 0, expected one of: <Mat3D.Mat3D> <Mat3.Mat3> '
    elif numArgs == 4:
        import Mat4D
        if isinstance(_args[0], Mat4D.Mat4D):
            return __overloaded_composeMatrix_ptrLMatrix4d_ptrConstLVecBase3d_ptrConstLVecBase3d_ptrConstLVecBase3d(*_args)
        
        import Mat4
        if isinstance(_args[0], Mat4.Mat4):
            return __overloaded_composeMatrix_ptrLMatrix4f_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f(*_args)
        
        import Mat3D
        if isinstance(_args[0], Mat3D.Mat3D):
            import VBase3D
            if isinstance(_args[1], VBase3D.VBase3D):
                import VBase3D
                if isinstance(_args[2], VBase3D.VBase3D):
                    if isinstance(_args[3], types.IntType) or isinstance(_args[3], types.LongType):
                        return __overloaded_composeMatrix_ptrLMatrix3d_ptrConstLVecBase3d_ptrConstLVecBase3d___enum__CoordinateSystem(*_args)
                    
                    import VBase3D
                    if isinstance(_args[3], VBase3D.VBase3D):
                        return __overloaded_composeMatrix_ptrLMatrix3d_ptrConstLVecBase3d_ptrConstLVecBase3d_ptrConstLVecBase3d(*_args)
                    
                    raise TypeError, 'Invalid argument 3, expected one of: <types.IntType> <VBase3D.VBase3D> '
                
                raise TypeError, 'Invalid argument 2, expected one of: <VBase3D.VBase3D> '
            
            raise TypeError, 'Invalid argument 1, expected one of: <VBase3D.VBase3D> '
        
        import Mat3
        if isinstance(_args[0], Mat3.Mat3):
            import VBase3
            if isinstance(_args[1], VBase3.VBase3):
                import VBase3
                if isinstance(_args[2], VBase3.VBase3):
                    if isinstance(_args[3], types.IntType) or isinstance(_args[3], types.LongType):
                        return __overloaded_composeMatrix_ptrLMatrix3f_ptrConstLVecBase3f_ptrConstLVecBase3f___enum__CoordinateSystem(*_args)
                    
                    import VBase3
                    if isinstance(_args[3], VBase3.VBase3):
                        return __overloaded_composeMatrix_ptrLMatrix3f_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f(*_args)
                    
                    raise TypeError, 'Invalid argument 3, expected one of: <types.IntType> <VBase3.VBase3> '
                
                raise TypeError, 'Invalid argument 2, expected one of: <VBase3.VBase3> '
            
            raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
        
        raise TypeError, 'Invalid argument 0, expected one of: <Mat4D.Mat4D> <Mat4.Mat4> <Mat3D.Mat3D> <Mat3.Mat3> '
    elif numArgs == 5:
        import Mat4D
        if isinstance(_args[0], Mat4D.Mat4D):
            import VBase3D
            if isinstance(_args[1], VBase3D.VBase3D):
                import VBase3D
                if isinstance(_args[2], VBase3D.VBase3D):
                    import VBase3D
                    if isinstance(_args[3], VBase3D.VBase3D):
                        if isinstance(_args[4], types.IntType) or isinstance(_args[4], types.LongType):
                            return __overloaded_composeMatrix_ptrLMatrix4d_ptrConstLVecBase3d_ptrConstLVecBase3d_ptrConstLVecBase3d___enum__CoordinateSystem(*_args)
                        
                        import VBase3D
                        if isinstance(_args[4], VBase3D.VBase3D):
                            return __overloaded_composeMatrix_ptrLMatrix4d_ptrConstLVecBase3d_ptrConstLVecBase3d_ptrConstLVecBase3d_ptrConstLVecBase3d(*_args)
                        
                        raise TypeError, 'Invalid argument 4, expected one of: <types.IntType> <VBase3D.VBase3D> '
                    
                    raise TypeError, 'Invalid argument 3, expected one of: <VBase3D.VBase3D> '
                
                raise TypeError, 'Invalid argument 2, expected one of: <VBase3D.VBase3D> '
            
            raise TypeError, 'Invalid argument 1, expected one of: <VBase3D.VBase3D> '
        
        import Mat4
        if isinstance(_args[0], Mat4.Mat4):
            import VBase3
            if isinstance(_args[1], VBase3.VBase3):
                import VBase3
                if isinstance(_args[2], VBase3.VBase3):
                    import VBase3
                    if isinstance(_args[3], VBase3.VBase3):
                        if isinstance(_args[4], types.IntType) or isinstance(_args[4], types.LongType):
                            return __overloaded_composeMatrix_ptrLMatrix4f_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f___enum__CoordinateSystem(*_args)
                        
                        import VBase3
                        if isinstance(_args[4], VBase3.VBase3):
                            return __overloaded_composeMatrix_ptrLMatrix4f_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f(*_args)
                        
                        raise TypeError, 'Invalid argument 4, expected one of: <types.IntType> <VBase3.VBase3> '
                    
                    raise TypeError, 'Invalid argument 3, expected one of: <VBase3.VBase3> '
                
                raise TypeError, 'Invalid argument 2, expected one of: <VBase3.VBase3> '
            
            raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
        
        import Mat3D
        if isinstance(_args[0], Mat3D.Mat3D):
            return __overloaded_composeMatrix_ptrLMatrix3d_ptrConstLVecBase3d_ptrConstLVecBase3d_ptrConstLVecBase3d___enum__CoordinateSystem(*_args)
        
        import Mat3
        if isinstance(_args[0], Mat3.Mat3):
            return __overloaded_composeMatrix_ptrLMatrix3f_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f___enum__CoordinateSystem(*_args)
        
        raise TypeError, 'Invalid argument 0, expected one of: <Mat4D.Mat4D> <Mat4.Mat4> <Mat3D.Mat3D> <Mat3.Mat3> '
    elif numArgs == 6:
        import Mat4D
        if isinstance(_args[0], Mat4D.Mat4D):
            return __overloaded_composeMatrix_ptrLMatrix4d_ptrConstLVecBase3d_ptrConstLVecBase3d_ptrConstLVecBase3d_ptrConstLVecBase3d___enum__CoordinateSystem(*_args)
        
        import Mat4
        if isinstance(_args[0], Mat4.Mat4):
            return __overloaded_composeMatrix_ptrLMatrix4f_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f___enum__CoordinateSystem(*_args)
        
        raise TypeError, 'Invalid argument 0, expected one of: <Mat4D.Mat4D> <Mat4.Mat4> '
    else:
        raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 3 4 5 6 '


def decomposeMatrix(*_args):
    numArgs = len(_args)
    if numArgs == 3:
        import Mat3D
        if isinstance(_args[0], Mat3D.Mat3D):
            return __overloaded_decomposeMatrix_ptrConstLMatrix3d_ptrLVecBase3d_ptrLVecBase3d(*_args)
        
        import Mat3
        if isinstance(_args[0], Mat3.Mat3):
            return __overloaded_decomposeMatrix_ptrConstLMatrix3f_ptrLVecBase3f_ptrLVecBase3f(*_args)
        
        raise TypeError, 'Invalid argument 0, expected one of: <Mat3D.Mat3D> <Mat3.Mat3> '
    elif numArgs == 4:
        import Mat4D
        if isinstance(_args[0], Mat4D.Mat4D):
            return __overloaded_decomposeMatrix_ptrConstLMatrix4d_ptrLVecBase3d_ptrLVecBase3d_ptrLVecBase3d(*_args)
        
        import Mat4
        if isinstance(_args[0], Mat4.Mat4):
            return __overloaded_decomposeMatrix_ptrConstLMatrix4f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f(*_args)
        
        import Mat3D
        if isinstance(_args[0], Mat3D.Mat3D):
            import VBase3D
            if isinstance(_args[1], VBase3D.VBase3D):
                import VBase3D
                if isinstance(_args[2], VBase3D.VBase3D):
                    if isinstance(_args[3], types.IntType) or isinstance(_args[3], types.LongType):
                        return __overloaded_decomposeMatrix_ptrConstLMatrix3d_ptrLVecBase3d_ptrLVecBase3d___enum__CoordinateSystem(*_args)
                    
                    import VBase3D
                    if isinstance(_args[3], VBase3D.VBase3D):
                        return __overloaded_decomposeMatrix_ptrConstLMatrix3d_ptrLVecBase3d_ptrLVecBase3d_ptrLVecBase3d(*_args)
                    
                    raise TypeError, 'Invalid argument 3, expected one of: <types.IntType> <VBase3D.VBase3D> '
                
                raise TypeError, 'Invalid argument 2, expected one of: <VBase3D.VBase3D> '
            
            raise TypeError, 'Invalid argument 1, expected one of: <VBase3D.VBase3D> '
        
        import Mat3
        if isinstance(_args[0], Mat3.Mat3):
            import VBase3
            if isinstance(_args[1], VBase3.VBase3):
                import VBase3
                if isinstance(_args[2], VBase3.VBase3):
                    if isinstance(_args[3], types.IntType) or isinstance(_args[3], types.LongType):
                        return __overloaded_decomposeMatrix_ptrConstLMatrix3f_ptrLVecBase3f_ptrLVecBase3f___enum__CoordinateSystem(*_args)
                    
                    import VBase3
                    if isinstance(_args[3], VBase3.VBase3):
                        return __overloaded_decomposeMatrix_ptrConstLMatrix3f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f(*_args)
                    
                    raise TypeError, 'Invalid argument 3, expected one of: <types.IntType> <VBase3.VBase3> '
                
                raise TypeError, 'Invalid argument 2, expected one of: <VBase3.VBase3> '
            
            raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
        
        raise TypeError, 'Invalid argument 0, expected one of: <Mat4D.Mat4D> <Mat4.Mat4> <Mat3D.Mat3D> <Mat3.Mat3> '
    elif numArgs == 5:
        import Mat4D
        if isinstance(_args[0], Mat4D.Mat4D):
            import VBase3D
            if isinstance(_args[1], VBase3D.VBase3D):
                import VBase3D
                if isinstance(_args[2], VBase3D.VBase3D):
                    import VBase3D
                    if isinstance(_args[3], VBase3D.VBase3D):
                        if isinstance(_args[4], types.IntType) or isinstance(_args[4], types.LongType):
                            return __overloaded_decomposeMatrix_ptrConstLMatrix4d_ptrLVecBase3d_ptrLVecBase3d_ptrLVecBase3d___enum__CoordinateSystem(*_args)
                        
                        import VBase3D
                        if isinstance(_args[4], VBase3D.VBase3D):
                            return __overloaded_decomposeMatrix_ptrConstLMatrix4d_ptrLVecBase3d_ptrLVecBase3d_ptrLVecBase3d_ptrLVecBase3d(*_args)
                        
                        raise TypeError, 'Invalid argument 4, expected one of: <types.IntType> <VBase3D.VBase3D> '
                    
                    raise TypeError, 'Invalid argument 3, expected one of: <VBase3D.VBase3D> '
                
                raise TypeError, 'Invalid argument 2, expected one of: <VBase3D.VBase3D> '
            
            raise TypeError, 'Invalid argument 1, expected one of: <VBase3D.VBase3D> '
        
        import Mat4
        if isinstance(_args[0], Mat4.Mat4):
            import VBase3
            if isinstance(_args[1], VBase3.VBase3):
                import VBase3
                if isinstance(_args[2], VBase3.VBase3):
                    import VBase3
                    if isinstance(_args[3], VBase3.VBase3):
                        if isinstance(_args[4], types.IntType) or isinstance(_args[4], types.LongType):
                            return __overloaded_decomposeMatrix_ptrConstLMatrix4f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f___enum__CoordinateSystem(*_args)
                        
                        import VBase3
                        if isinstance(_args[4], VBase3.VBase3):
                            return __overloaded_decomposeMatrix_ptrConstLMatrix4f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f(*_args)
                        
                        raise TypeError, 'Invalid argument 4, expected one of: <types.IntType> <VBase3.VBase3> '
                    
                    raise TypeError, 'Invalid argument 3, expected one of: <VBase3.VBase3> '
                
                raise TypeError, 'Invalid argument 2, expected one of: <VBase3.VBase3> '
            
            raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
        
        import Mat3D
        if isinstance(_args[0], Mat3D.Mat3D):
            return __overloaded_decomposeMatrix_ptrConstLMatrix3d_ptrLVecBase3d_ptrLVecBase3d_ptrLVecBase3d___enum__CoordinateSystem(*_args)
        
        import Mat3
        if isinstance(_args[0], Mat3.Mat3):
            return __overloaded_decomposeMatrix_ptrConstLMatrix3f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f___enum__CoordinateSystem(*_args)
        
        raise TypeError, 'Invalid argument 0, expected one of: <Mat4D.Mat4D> <Mat4.Mat4> <Mat3D.Mat3D> <Mat3.Mat3> '
    elif numArgs == 6:
        import Mat4D
        if isinstance(_args[0], Mat4D.Mat4D):
            return __overloaded_decomposeMatrix_ptrConstLMatrix4d_ptrLVecBase3d_ptrLVecBase3d_ptrLVecBase3d_ptrLVecBase3d___enum__CoordinateSystem(*_args)
        
        import Mat4
        if isinstance(_args[0], Mat4.Mat4):
            return __overloaded_decomposeMatrix_ptrConstLMatrix4f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f___enum__CoordinateSystem(*_args)
        
        raise TypeError, 'Invalid argument 0, expected one of: <Mat4D.Mat4D> <Mat4.Mat4> '
    else:
        raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 3 4 5 6 '


def headsUp(*_args):
    numArgs = len(_args)
    if numArgs == 2:
        import QuatD
        if isinstance(_args[0], QuatD.QuatD):
            return __overloaded_headsUp_ptrLQuaterniond_ptrConstLVector3d(*_args)
        
        import Quat
        if isinstance(_args[0], Quat.Quat):
            return __overloaded_headsUp_ptrLQuaternionf_ptrConstLVector3f(*_args)
        
        import Mat4D
        if isinstance(_args[0], Mat4D.Mat4D):
            return __overloaded_headsUp_ptrLMatrix4d_ptrConstLVector3d(*_args)
        
        import Mat4
        if isinstance(_args[0], Mat4.Mat4):
            return __overloaded_headsUp_ptrLMatrix4f_ptrConstLVector3f(*_args)
        
        import Mat3D
        if isinstance(_args[0], Mat3D.Mat3D):
            return __overloaded_headsUp_ptrLMatrix3d_ptrConstLVector3d(*_args)
        
        import Mat3
        if isinstance(_args[0], Mat3.Mat3):
            return __overloaded_headsUp_ptrLMatrix3f_ptrConstLVector3f(*_args)
        
        raise TypeError, 'Invalid argument 0, expected one of: <QuatD.QuatD> <Quat.Quat> <Mat4D.Mat4D> <Mat4.Mat4> <Mat3D.Mat3D> <Mat3.Mat3> '
    elif numArgs == 3:
        import QuatD
        if isinstance(_args[0], QuatD.QuatD):
            import Vec3D
            if isinstance(_args[1], Vec3D.Vec3D):
                if isinstance(_args[2], types.IntType) or isinstance(_args[2], types.LongType):
                    return __overloaded_headsUp_ptrLQuaterniond_ptrConstLVector3d___enum__CoordinateSystem(*_args)
                
                import Vec3D
                if isinstance(_args[2], Vec3D.Vec3D):
                    return __overloaded_headsUp_ptrLQuaterniond_ptrConstLVector3d_ptrConstLVector3d(*_args)
                
                raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> <Vec3D.Vec3D> '
            
            raise TypeError, 'Invalid argument 1, expected one of: <Vec3D.Vec3D> '
        
        import Quat
        if isinstance(_args[0], Quat.Quat):
            import Vec3
            if isinstance(_args[1], Vec3.Vec3):
                if isinstance(_args[2], types.IntType) or isinstance(_args[2], types.LongType):
                    return __overloaded_headsUp_ptrLQuaternionf_ptrConstLVector3f___enum__CoordinateSystem(*_args)
                
                import Vec3
                if isinstance(_args[2], Vec3.Vec3):
                    return __overloaded_headsUp_ptrLQuaternionf_ptrConstLVector3f_ptrConstLVector3f(*_args)
                
                raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> <Vec3.Vec3> '
            
            raise TypeError, 'Invalid argument 1, expected one of: <Vec3.Vec3> '
        
        import Mat4D
        if isinstance(_args[0], Mat4D.Mat4D):
            import Vec3D
            if isinstance(_args[1], Vec3D.Vec3D):
                if isinstance(_args[2], types.IntType) or isinstance(_args[2], types.LongType):
                    return __overloaded_headsUp_ptrLMatrix4d_ptrConstLVector3d___enum__CoordinateSystem(*_args)
                
                import Vec3D
                if isinstance(_args[2], Vec3D.Vec3D):
                    return __overloaded_headsUp_ptrLMatrix4d_ptrConstLVector3d_ptrConstLVector3d(*_args)
                
                raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> <Vec3D.Vec3D> '
            
            raise TypeError, 'Invalid argument 1, expected one of: <Vec3D.Vec3D> '
        
        import Mat4
        if isinstance(_args[0], Mat4.Mat4):
            import Vec3
            if isinstance(_args[1], Vec3.Vec3):
                if isinstance(_args[2], types.IntType) or isinstance(_args[2], types.LongType):
                    return __overloaded_headsUp_ptrLMatrix4f_ptrConstLVector3f___enum__CoordinateSystem(*_args)
                
                import Vec3
                if isinstance(_args[2], Vec3.Vec3):
                    return __overloaded_headsUp_ptrLMatrix4f_ptrConstLVector3f_ptrConstLVector3f(*_args)
                
                raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> <Vec3.Vec3> '
            
            raise TypeError, 'Invalid argument 1, expected one of: <Vec3.Vec3> '
        
        import Mat3D
        if isinstance(_args[0], Mat3D.Mat3D):
            import Vec3D
            if isinstance(_args[1], Vec3D.Vec3D):
                if isinstance(_args[2], types.IntType) or isinstance(_args[2], types.LongType):
                    return __overloaded_headsUp_ptrLMatrix3d_ptrConstLVector3d___enum__CoordinateSystem(*_args)
                
                import Vec3D
                if isinstance(_args[2], Vec3D.Vec3D):
                    return __overloaded_headsUp_ptrLMatrix3d_ptrConstLVector3d_ptrConstLVector3d(*_args)
                
                raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> <Vec3D.Vec3D> '
            
            raise TypeError, 'Invalid argument 1, expected one of: <Vec3D.Vec3D> '
        
        import Mat3
        if isinstance(_args[0], Mat3.Mat3):
            import Vec3
            if isinstance(_args[1], Vec3.Vec3):
                if isinstance(_args[2], types.IntType) or isinstance(_args[2], types.LongType):
                    return __overloaded_headsUp_ptrLMatrix3f_ptrConstLVector3f___enum__CoordinateSystem(*_args)
                
                import Vec3
                if isinstance(_args[2], Vec3.Vec3):
                    return __overloaded_headsUp_ptrLMatrix3f_ptrConstLVector3f_ptrConstLVector3f(*_args)
                
                raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> <Vec3.Vec3> '
            
            raise TypeError, 'Invalid argument 1, expected one of: <Vec3.Vec3> '
        
        raise TypeError, 'Invalid argument 0, expected one of: <QuatD.QuatD> <Quat.Quat> <Mat4D.Mat4D> <Mat4.Mat4> <Mat3D.Mat3D> <Mat3.Mat3> '
    elif numArgs == 4:
        import QuatD
        if isinstance(_args[0], QuatD.QuatD):
            return __overloaded_headsUp_ptrLQuaterniond_ptrConstLVector3d_ptrConstLVector3d___enum__CoordinateSystem(*_args)
        
        import Quat
        if isinstance(_args[0], Quat.Quat):
            return __overloaded_headsUp_ptrLQuaternionf_ptrConstLVector3f_ptrConstLVector3f___enum__CoordinateSystem(*_args)
        
        import Mat4D
        if isinstance(_args[0], Mat4D.Mat4D):
            return __overloaded_headsUp_ptrLMatrix4d_ptrConstLVector3d_ptrConstLVector3d___enum__CoordinateSystem(*_args)
        
        import Mat4
        if isinstance(_args[0], Mat4.Mat4):
            return __overloaded_headsUp_ptrLMatrix4f_ptrConstLVector3f_ptrConstLVector3f___enum__CoordinateSystem(*_args)
        
        import Mat3D
        if isinstance(_args[0], Mat3D.Mat3D):
            return __overloaded_headsUp_ptrLMatrix3d_ptrConstLVector3d_ptrConstLVector3d___enum__CoordinateSystem(*_args)
        
        import Mat3
        if isinstance(_args[0], Mat3.Mat3):
            return __overloaded_headsUp_ptrLMatrix3f_ptrConstLVector3f_ptrConstLVector3f___enum__CoordinateSystem(*_args)
        
        raise TypeError, 'Invalid argument 0, expected one of: <QuatD.QuatD> <Quat.Quat> <Mat4D.Mat4D> <Mat4.Mat4> <Mat3D.Mat3D> <Mat3.Mat3> '
    else:
        raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 4 '


def getModelPath():
    returnValue = libpanda._inPflbo26dg()
    import ConfigVariableSearchPath
    returnObject = ConfigVariableSearchPath.ConfigVariableSearchPath(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    return returnObject


def getTexturePath():
    returnValue = libpanda._inPflboXgtZ()
    import ConfigVariableSearchPath
    returnObject = ConfigVariableSearchPath.ConfigVariableSearchPath(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    return returnObject


def getSoundPath():
    returnValue = libpanda._inPflbo18uu()
    import ConfigVariableSearchPath
    returnObject = ConfigVariableSearchPath.ConfigVariableSearchPath(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    return returnObject


def loadPrcFile(filename):
    returnValue = libpanda._inPflboBiO8(filename)
    import ConfigPage
    returnObject = ConfigPage.ConfigPage(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    return returnObject


def loadPrcFileData(name, data):
    returnValue = libpanda._inPflboDEXZ(name, data)
    import ConfigPage
    returnObject = ConfigPage.ConfigPage(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    return returnObject


def unloadPrcFile(page):
    returnValue = libpanda._inPflbow809(page.this)
    return returnValue


def __overloaded_headsUp_ptrLMatrix3d_ptrConstLVector3d___enum__CoordinateSystem(mat, fwd, cs):
    returnValue = libpanda._inPSkjPyYd4(mat.this, fwd.this, cs)
    return returnValue


def __overloaded_headsUp_ptrLMatrix3d_ptrConstLVector3d_ptrConstLVector3d___enum__CoordinateSystem(mat, fwd, up, cs):
    returnValue = libpanda._inPSkjPmjSo(mat.this, fwd.this, up.this, cs)
    return returnValue


def __overloaded_headsUp_ptrLMatrix3d_ptrConstLVector3d_ptrConstLVector3d(mat, fwd, up):
    returnValue = libpanda._inPSkjPv5m2(mat.this, fwd.this, up.this)
    return returnValue


def __overloaded_headsUp_ptrLMatrix3d_ptrConstLVector3d(mat, fwd):
    returnValue = libpanda._inPSkjPTJmh(mat.this, fwd.this)
    return returnValue


def __overloaded_headsUp_ptrLMatrix3f_ptrConstLVector3f___enum__CoordinateSystem(mat, fwd, cs):
    returnValue = libpanda._inPSkjP5qVz(mat.this, fwd.this, cs)
    return returnValue


def __overloaded_headsUp_ptrLMatrix3f_ptrConstLVector3f_ptrConstLVector3f___enum__CoordinateSystem(mat, fwd, up, cs):
    returnValue = libpanda._inPSkjPstmb(mat.this, fwd.this, up.this, cs)
    return returnValue


def __overloaded_headsUp_ptrLMatrix3f_ptrConstLVector3f_ptrConstLVector3f(mat, fwd, up):
    returnValue = libpanda._inPSkjP5P9p(mat.this, fwd.this, up.this)
    return returnValue


def __overloaded_headsUp_ptrLMatrix3f_ptrConstLVector3f(mat, fwd):
    returnValue = libpanda._inPSkjPucec(mat.this, fwd.this)
    return returnValue


def __overloaded_headsUp_ptrLMatrix4d_ptrConstLVector3d___enum__CoordinateSystem(mat, fwd, cs):
    returnValue = libpanda._inPSkjPy0V9(mat.this, fwd.this, cs)
    return returnValue


def __overloaded_headsUp_ptrLMatrix4d_ptrConstLVector3d_ptrConstLVector3d___enum__CoordinateSystem(mat, fwd, up, cs):
    returnValue = libpanda._inPSkjPm_Kt(mat.this, fwd.this, up.this, cs)
    return returnValue


def __overloaded_headsUp_ptrLMatrix4d_ptrConstLVector3d_ptrConstLVector3d(mat, fwd, up):
    returnValue = libpanda._inPSkjPvdh7(mat.this, fwd.this, up.this)
    return returnValue


def __overloaded_headsUp_ptrLMatrix4d_ptrConstLVector3d(mat, fwd):
    returnValue = libpanda._inPSkjPTtem(mat.this, fwd.this)
    return returnValue


def __overloaded_headsUp_ptrLMatrix4f_ptrConstLVector3f___enum__CoordinateSystem(mat, fwd, cs):
    returnValue = libpanda._inPSkjP5GM4(mat.this, fwd.this, cs)
    return returnValue


def __overloaded_headsUp_ptrLMatrix4f_ptrConstLVector3f_ptrConstLVector3f___enum__CoordinateSystem(mat, fwd, up, cs):
    returnValue = libpanda._inPSkjPsJfg(mat.this, fwd.this, up.this, cs)
    return returnValue


def __overloaded_headsUp_ptrLMatrix4f_ptrConstLVector3f_ptrConstLVector3f(mat, fwd, up):
    returnValue = libpanda._inPSkjP5j1u(mat.this, fwd.this, up.this)
    return returnValue


def __overloaded_headsUp_ptrLMatrix4f_ptrConstLVector3f(mat, fwd):
    returnValue = libpanda._inPSkjPuwWh(mat.this, fwd.this)
    return returnValue


def __overloaded_headsUp_ptrLQuaterniond_ptrConstLVector3d___enum__CoordinateSystem(quat, fwd, cs):
    returnValue = libpanda._inPSkjPTxQm(quat.this, fwd.this, cs)
    return returnValue


def __overloaded_headsUp_ptrLQuaterniond_ptrConstLVector3d_ptrConstLVector3d___enum__CoordinateSystem(quat, fwd, up, cs):
    returnValue = libpanda._inPSkjPd9Wi(quat.this, fwd.this, up.this, cs)
    return returnValue


def __overloaded_headsUp_ptrLQuaterniond_ptrConstLVector3d_ptrConstLVector3d(quat, fwd, up):
    returnValue = libpanda._inPSkjPiZq8(quat.this, fwd.this, up.this)
    return returnValue


def __overloaded_headsUp_ptrLQuaterniond_ptrConstLVector3d(quat, fwd):
    returnValue = libpanda._inPSkjP3Jjx(quat.this, fwd.this)
    return returnValue


def __overloaded_headsUp_ptrLQuaternionf_ptrConstLVector3f___enum__CoordinateSystem(quat, fwd, cs):
    returnValue = libpanda._inPSkjPRh3W(quat.this, fwd.this, cs)
    return returnValue


def __overloaded_headsUp_ptrLQuaternionf_ptrConstLVector3f_ptrConstLVector3f___enum__CoordinateSystem(quat, fwd, up, cs):
    returnValue = libpanda._inPSkjPjnkT(quat.this, fwd.this, up.this, cs)
    return returnValue


def __overloaded_headsUp_ptrLQuaternionf_ptrConstLVector3f_ptrConstLVector3f(quat, fwd, up):
    returnValue = libpanda._inPSkjPHl5t(quat.this, fwd.this, up.this)
    return returnValue


def __overloaded_headsUp_ptrLQuaternionf_ptrConstLVector3f(quat, fwd):
    returnValue = libpanda._inPSkjP1YKi(quat.this, fwd.this)
    return returnValue


def __overloaded_lookAt_ptrLMatrix3d_ptrConstLVector3d___enum__CoordinateSystem(mat, fwd, cs):
    returnValue = libpanda._inPSkjP2iJ6(mat.this, fwd.this, cs)
    return returnValue


def __overloaded_lookAt_ptrLMatrix3d_ptrConstLVector3d_ptrConstLVector3d___enum__CoordinateSystem(mat, fwd, up, cs):
    returnValue = libpanda._inPSkjPe3n7(mat.this, fwd.this, up.this, cs)
    return returnValue


def __overloaded_lookAt_ptrLMatrix3d_ptrConstLVector3d_ptrConstLVector3d(mat, fwd, up):
    returnValue = libpanda._inPSkjPYQHg(mat.this, fwd.this, up.this)
    return returnValue


def __overloaded_lookAt_ptrLMatrix3d_ptrConstLVector3d(mat, fwd):
    returnValue = libpanda._inPSkjPhTgt(mat.this, fwd.this)
    return returnValue


def __overloaded_lookAt_ptrLMatrix3f_ptrConstLVector3f___enum__CoordinateSystem(mat, fwd, cs):
    returnValue = libpanda._inPSkjPTR_D(mat.this, fwd.this, cs)
    return returnValue


def __overloaded_lookAt_ptrLMatrix3f_ptrConstLVector3f_ptrConstLVector3f___enum__CoordinateSystem(mat, fwd, up, cs):
    returnValue = libpanda._inPSkjPzsOP(mat.this, fwd.this, up.this, cs)
    return returnValue


def __overloaded_lookAt_ptrLMatrix3f_ptrConstLVector3f_ptrConstLVector3f(mat, fwd, up):
    returnValue = libpanda._inPSkjP04uz(mat.this, fwd.this, up.this)
    return returnValue


def __overloaded_lookAt_ptrLMatrix3f_ptrConstLVector3f(mat, fwd):
    returnValue = libpanda._inPSkjPNDW3(mat.this, fwd.this)
    return returnValue


def __overloaded_lookAt_ptrLMatrix4d_ptrConstLVector3d___enum__CoordinateSystem(mat, fwd, cs):
    returnValue = libpanda._inPSkjP_RT6(mat.this, fwd.this, cs)
    return returnValue


def __overloaded_lookAt_ptrLMatrix4d_ptrConstLVector3d_ptrConstLVector3d___enum__CoordinateSystem(mat, fwd, up, cs):
    returnValue = libpanda._inPSkjPWkx7(mat.this, fwd.this, up.this, cs)
    return returnValue


def __overloaded_lookAt_ptrLMatrix4d_ptrConstLVector3d_ptrConstLVector3d(mat, fwd, up):
    returnValue = libpanda._inPSkjPQhRg(mat.this, fwd.this, up.this)
    return returnValue


def __overloaded_lookAt_ptrLMatrix4d_ptrConstLVector3d(mat, fwd):
    returnValue = libpanda._inPSkjPpCqt(mat.this, fwd.this)
    return returnValue


def __overloaded_lookAt_ptrLMatrix4f_ptrConstLVector3f___enum__CoordinateSystem(mat, fwd, cs):
    returnValue = libpanda._inPSkjPbAJE(mat.this, fwd.this, cs)
    return returnValue


def __overloaded_lookAt_ptrLMatrix4f_ptrConstLVector3f_ptrConstLVector3f___enum__CoordinateSystem(mat, fwd, up, cs):
    returnValue = libpanda._inPSkjPLcXP(mat.this, fwd.this, up.this, cs)
    return returnValue


def __overloaded_lookAt_ptrLMatrix4f_ptrConstLVector3f_ptrConstLVector3f(mat, fwd, up):
    returnValue = libpanda._inPSkjPMJ3z(mat.this, fwd.this, up.this)
    return returnValue


def __overloaded_lookAt_ptrLMatrix4f_ptrConstLVector3f(mat, fwd):
    returnValue = libpanda._inPSkjP1yf3(mat.this, fwd.this)
    return returnValue


def __overloaded_lookAt_ptrLQuaterniond_ptrConstLVector3d___enum__CoordinateSystem(quat, fwd, cs):
    returnValue = libpanda._inPSkjPdgkh(quat.this, fwd.this, cs)
    return returnValue


def __overloaded_lookAt_ptrLQuaterniond_ptrConstLVector3d_ptrConstLVector3d___enum__CoordinateSystem(quat, fwd, up, cs):
    returnValue = libpanda._inPSkjPq4at(quat.this, fwd.this, up.this, cs)
    return returnValue


def __overloaded_lookAt_ptrLQuaterniond_ptrConstLVector3d_ptrConstLVector3d(quat, fwd, up):
    returnValue = libpanda._inPSkjP6OSa(quat.this, fwd.this, up.this)
    return returnValue


def __overloaded_lookAt_ptrLQuaterniond_ptrConstLVector3d(quat, fwd):
    returnValue = libpanda._inPSkjPmF_T(quat.this, fwd.this)
    return returnValue


def __overloaded_lookAt_ptrLQuaternionf_ptrConstLVector3f___enum__CoordinateSystem(quat, fwd, cs):
    returnValue = libpanda._inPSkjPPvHl(quat.this, fwd.this, cs)
    return returnValue


def __overloaded_lookAt_ptrLQuaternionf_ptrConstLVector3f_ptrConstLVector3f___enum__CoordinateSystem(quat, fwd, up, cs):
    returnValue = libpanda._inPSkjP_f8w(quat.this, fwd.this, up.this, cs)
    return returnValue


def __overloaded_lookAt_ptrLQuaternionf_ptrConstLVector3f_ptrConstLVector3f(quat, fwd, up):
    returnValue = libpanda._inPSkjPxh1d(quat.this, fwd.this, up.this)
    return returnValue


def __overloaded_lookAt_ptrLQuaternionf_ptrConstLVector3f(quat, fwd):
    returnValue = libpanda._inPSkjPGIgX(quat.this, fwd.this)
    return returnValue


def __overloaded_rotateTo_ptrLMatrix3d_ptrConstLVector3d_ptrConstLVector3d(mat, a, b):
    returnValue = libpanda._inPSkjP8zF6(mat.this, a.this, b.this)
    return returnValue


def __overloaded_rotateTo_ptrLMatrix3f_ptrConstLVector3f_ptrConstLVector3f(mat, a, b):
    returnValue = libpanda._inPSkjP6uMk(mat.this, a.this, b.this)
    return returnValue


def __overloaded_rotateTo_ptrLMatrix4d_ptrConstLVector3d_ptrConstLVector3d(mat, a, b):
    returnValue = libpanda._inPSkjPxzTW(mat.this, a.this, b.this)
    return returnValue


def __overloaded_rotateTo_ptrLMatrix4f_ptrConstLVector3f_ptrConstLVector3f(mat, a, b):
    returnValue = libpanda._inPSkjP_uaA(mat.this, a.this, b.this)
    return returnValue


def __overloaded_deg2Rad_double(f):
    returnValue = libpanda._inPVZN3aTo4(f)
    return returnValue


def __overloaded_deg2Rad_float(f):
    returnValue = libpanda._inPVZN3RKCI(f)
    return returnValue


def __overloaded_rad2Deg_double(f):
    returnValue = libpanda._inPVZN3gpRs(f)
    return returnValue


def __overloaded_rad2Deg_float(f):
    returnValue = libpanda._inPVZN3Ibq7(f)
    return returnValue


def getDefaultCoordinateSystem():
    returnValue = libpanda._inPVZN3t1jy()
    return returnValue


def __overloaded_transpose_ptrConstLMatrix3d(a):
    returnValue = libpanda._inPVZN3p_eQ(a.this)
    import Mat3D
    returnObject = Mat3D.Mat3D(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def __overloaded_transpose_ptrConstLMatrix3f(a):
    returnValue = libpanda._inPVZN3N4ee(a.this)
    import Mat3
    returnObject = Mat3.Mat3(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def __overloaded_transpose_ptrConstLMatrix4d(a):
    returnValue = libpanda._inPVZN3n_ss(a.this)
    import Mat4D
    returnObject = Mat4D.Mat4D(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def __overloaded_transpose_ptrConstLMatrix4f(a):
    returnValue = libpanda._inPVZN3L4s6(a.this)
    import Mat4
    returnObject = Mat4.Mat4(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def __overloaded_invert_ptrConstLMatrix3d(a):
    returnValue = libpanda._inPVZN39Gem(a.this)
    import Mat3D
    returnObject = Mat3D.Mat3D(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def __overloaded_invert_ptrConstLMatrix3f(a):
    returnValue = libpanda._inPVZN3Ngym(a.this)
    import Mat3
    returnObject = Mat3.Mat3(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def __overloaded_invert_ptrConstLMatrix4d(a):
    returnValue = libpanda._inPVZN3YJfW(a.this)
    import Mat4D
    returnObject = Mat4D.Mat4D(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def __overloaded_invert_ptrConstLMatrix4f(a):
    returnValue = libpanda._inPVZN3orzW(a.this)
    import Mat4
    returnObject = Mat4.Mat4(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def __overloaded_invert_ptrConstLQuaterniond(a):
    returnValue = libpanda._inPVZN3G8wm(a.this)
    import QuatD
    returnObject = QuatD.QuatD(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def __overloaded_invert_ptrConstLQuaternionf(a):
    returnValue = libpanda._inPVZN3qBx0(a.this)
    import Quat
    returnObject = Quat.Quat(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def __overloaded___mul___ptrConstLMatrix3d_ptrConstLQuaterniond(m, q):
    returnValue = libpanda._inPVZN3DzjX(m.this, q.this)
    import Mat3D
    returnObject = Mat3D.Mat3D(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def __overloaded___mul___ptrConstLMatrix3f_ptrConstLQuaternionf(m, q):
    returnValue = libpanda._inPVZN3kolH(m.this, q.this)
    import Mat3
    returnObject = Mat3.Mat3(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def __overloaded___mul___ptrConstLMatrix4d_ptrConstLQuaterniond(m, q):
    returnValue = libpanda._inPVZN3Rsje(m.this, q.this)
    import Mat4D
    returnObject = Mat4D.Mat4D(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def __overloaded___mul___ptrConstLMatrix4f_ptrConstLQuaternionf(m, q):
    returnValue = libpanda._inPVZN3qplO(m.this, q.this)
    import Mat4
    returnObject = Mat4.Mat4(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def __overloaded___mul___ptrConstLPoint2d_ptrConstLMatrix3d(v, m):
    returnValue = libpanda._inPVZN3yfKI(v.this, m.this)
    import Point2D
    returnObject = Point2D.Point2D(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def __overloaded___mul___ptrConstLPoint2f_ptrConstLMatrix3f(v, m):
    returnValue = libpanda._inPVZN3SCRW(v.this, m.this)
    import Point2
    returnObject = Point2.Point2(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def __overloaded___mul___ptrConstLPoint3d_ptrConstLMatrix4d(v, m):
    returnValue = libpanda._inPVZN3mWZA(v.this, m.this)
    import Point3D
    returnObject = Point3D.Point3D(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def __overloaded___mul___ptrConstLPoint3f_ptrConstLMatrix4f(v, m):
    returnValue = libpanda._inPVZN3eNeO(v.this, m.this)
    import Point3
    returnObject = Point3.Point3(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def __overloaded___mul___ptrConstLVecBase3d_ptrConstLMatrix3d(v, m):
    returnValue = libpanda._inPVZN36f4W(v.this, m.this)
    import VBase3D
    returnObject = VBase3D.VBase3D(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def __overloaded___mul___ptrConstLVecBase3f_ptrConstLMatrix3f(v, m):
    returnValue = libpanda._inPVZN3ZSml(v.this, m.this)
    import VBase3
    returnObject = VBase3.VBase3(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def __overloaded___mul___ptrConstLVecBase4d_ptrConstLMatrix4d(v, m):
    returnValue = libpanda._inPVZN3HpH4(v.this, m.this)
    import VBase4D
    returnObject = VBase4D.VBase4D(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def __overloaded___mul___ptrConstLVecBase4f_ptrConstLMatrix4f(v, m):
    returnValue = libpanda._inPVZN3lt1G(v.this, m.this)
    import VBase4
    returnObject = VBase4.VBase4(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def __overloaded___mul___ptrConstLVector2d_ptrConstLMatrix3d(v, m):
    returnValue = libpanda._inPVZN3QlWf(v.this, m.this)
    import Vec2D
    returnObject = Vec2D.Vec2D(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def __overloaded___mul___ptrConstLVector2f_ptrConstLMatrix3f(v, m):
    returnValue = libpanda._inPVZN3fZ0h(v.this, m.this)
    import Vec2
    returnObject = Vec2.Vec2(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def __overloaded___mul___ptrConstLVector3d_ptrConstLMatrix4d(v, m):
    returnValue = libpanda._inPVZN3wbZm(v.this, m.this)
    import Vec3D
    returnObject = Vec3D.Vec3D(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def __overloaded___mul___ptrConstLVector3f_ptrConstLMatrix4f(v, m):
    returnValue = libpanda._inPVZN37_2o(v.this, m.this)
    import Vec3
    returnObject = Vec3.Vec3(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def __overloaded_genericWriteDatagram_ptrDatagram_ptrConstLMatrix3d(dest, value):
    returnValue = libpanda._inPVZN3J63D(dest.this, value.this)
    return returnValue


def __overloaded_genericWriteDatagram_ptrDatagram_ptrConstLMatrix3f(dest, value):
    returnValue = libpanda._inPVZN3Qo4D(dest.this, value.this)
    return returnValue


def __overloaded_genericWriteDatagram_ptrDatagram_ptrConstLMatrix4d(dest, value):
    returnValue = libpanda._inPVZN3b53K(dest.this, value.this)
    return returnValue


def __overloaded_genericWriteDatagram_ptrDatagram_ptrConstLMatrix4f(dest, value):
    returnValue = libpanda._inPVZN3Cr4K(dest.this, value.this)
    return returnValue


def __overloaded_genericReadDatagram_ptrLMatrix3d_ptrDatagramIterator(result, source):
    returnValue = libpanda._inPVZN3G74L(result.this, source.this)
    return returnValue


def __overloaded_genericReadDatagram_ptrLMatrix3f_ptrDatagramIterator(result, source):
    returnValue = libpanda._inPVZN3GpUO(result.this, source.this)
    return returnValue


def __overloaded_genericReadDatagram_ptrLMatrix4d_ptrDatagramIterator(result, source):
    returnValue = libpanda._inPVZN30f6L(result.this, source.this)
    return returnValue


def __overloaded_genericReadDatagram_ptrLMatrix4f_ptrDatagramIterator(result, source):
    returnValue = libpanda._inPVZN30NWO(result.this, source.this)
    return returnValue


def __overloaded_composeMatrix_ptrLMatrix3d_ptrConstLVecBase3d_ptrConstLVecBase3d___enum__CoordinateSystem(mat, scale, hpr, cs):
    returnValue = libpanda._inPVZN3yVzC(mat.this, scale.this, hpr.this, cs)
    return returnValue


def __overloaded_composeMatrix_ptrLMatrix3d_ptrConstLVecBase3d_ptrConstLVecBase3d(mat, scale, hpr):
    returnValue = libpanda._inPVZN3hQb3(mat.this, scale.this, hpr.this)
    return returnValue


def __overloaded_composeMatrix_ptrLMatrix3d_ptrConstLVecBase3d_ptrConstLVecBase3d_ptrConstLVecBase3d___enum__CoordinateSystem(mat, scale, shear, hpr, cs):
    returnValue = libpanda._inPVZN33KHb(mat.this, scale.this, shear.this, hpr.this, cs)
    return returnValue


def __overloaded_composeMatrix_ptrLMatrix3d_ptrConstLVecBase3d_ptrConstLVecBase3d_ptrConstLVecBase3d(mat, scale, shear, hpr):
    returnValue = libpanda._inPVZN3RK2_(mat.this, scale.this, shear.this, hpr.this)
    return returnValue


def __overloaded_composeMatrix_ptrLMatrix3f_ptrConstLVecBase3f_ptrConstLVecBase3f___enum__CoordinateSystem(mat, scale, hpr, cs):
    returnValue = libpanda._inPVZN34aBn(mat.this, scale.this, hpr.this, cs)
    return returnValue


def __overloaded_composeMatrix_ptrLMatrix3f_ptrConstLVecBase3f_ptrConstLVecBase3f(mat, scale, hpr):
    returnValue = libpanda._inPVZN36xpb(mat.this, scale.this, hpr.this)
    return returnValue


def __overloaded_composeMatrix_ptrLMatrix3f_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f___enum__CoordinateSystem(mat, scale, shear, hpr, cs):
    returnValue = libpanda._inPVZN3s_WG(mat.this, scale.this, shear.this, hpr.this, cs)
    return returnValue


def __overloaded_composeMatrix_ptrLMatrix3f_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f(mat, scale, shear, hpr):
    returnValue = libpanda._inPVZN3k7Er(mat.this, scale.this, shear.this, hpr.this)
    return returnValue


def __overloaded_composeMatrix_ptrLMatrix4d_ptrConstLVecBase3d_ptrConstLVecBase3d_ptrConstLVecBase3d___enum__CoordinateSystem(mat, scale, hpr, translate, cs):
    returnValue = libpanda._inPVZN38KjT(mat.this, scale.this, hpr.this, translate.this, cs)
    return returnValue


def __overloaded_composeMatrix_ptrLMatrix4d_ptrConstLVecBase3d_ptrConstLVecBase3d_ptrConstLVecBase3d(mat, scale, hpr, translate):
    returnValue = libpanda._inPVZN3UKS4(mat.this, scale.this, hpr.this, translate.this)
    return returnValue


def __overloaded_composeMatrix_ptrLMatrix4d_ptrConstLVecBase3d_ptrConstLVecBase3d_ptrConstLVecBase3d_ptrConstLVecBase3d___enum__CoordinateSystem(mat, scale, shear, hpr, translate, cs):
    returnValue = libpanda._inPVZN3oQjw(mat.this, scale.this, shear.this, hpr.this, translate.this, cs)
    return returnValue


def __overloaded_composeMatrix_ptrLMatrix4d_ptrConstLVecBase3d_ptrConstLVecBase3d_ptrConstLVecBase3d_ptrConstLVecBase3d(mat, scale, shear, hpr, translate):
    returnValue = libpanda._inPVZN39vLl(mat.this, scale.this, shear.this, hpr.this, translate.this)
    return returnValue


def __overloaded_composeMatrix_ptrLMatrix4f_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f___enum__CoordinateSystem(mat, scale, hpr, translate, cs):
    returnValue = libpanda._inPVZN3Q_y_(mat.this, scale.this, hpr.this, translate.this, cs)
    return returnValue


def __overloaded_composeMatrix_ptrLMatrix4f_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f(mat, scale, hpr, translate):
    returnValue = libpanda._inPVZN377gj(mat.this, scale.this, hpr.this, translate.this)
    return returnValue


def __overloaded_composeMatrix_ptrLMatrix4f_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f___enum__CoordinateSystem(mat, scale, shear, hpr, translate, cs):
    returnValue = libpanda._inPVZN31X_c(mat.this, scale.this, shear.this, hpr.this, translate.this, cs)
    return returnValue


def __overloaded_composeMatrix_ptrLMatrix4f_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f(mat, scale, shear, hpr, translate):
    returnValue = libpanda._inPVZN3CknR(mat.this, scale.this, shear.this, hpr.this, translate.this)
    return returnValue


def __overloaded_decomposeMatrix_ptrConstLMatrix3d_ptrLVecBase3d_ptrLVecBase3d___enum__CoordinateSystem(mat, scale, hpr, cs):
    returnValue = libpanda._inPVZN3rGAD(mat.this, scale.this, hpr.this, cs)
    return returnValue


def __overloaded_decomposeMatrix_ptrConstLMatrix3d_ptrLVecBase3d_ptrLVecBase3d(mat, scale, hpr):
    returnValue = libpanda._inPVZN3VxX2(mat.this, scale.this, hpr.this)
    return returnValue


def __overloaded_decomposeMatrix_ptrConstLMatrix3d_ptrLVecBase3d_ptrLVecBase3d_ptrLVecBase3d___enum__CoordinateSystem(mat, scale, shear, hpr, cs):
    returnValue = libpanda._inPVZN3wk1_(mat.this, scale.this, shear.this, hpr.this, cs)
    return returnValue


def __overloaded_decomposeMatrix_ptrConstLMatrix3d_ptrLVecBase3d_ptrLVecBase3d_ptrLVecBase3d(mat, scale, shear, hpr):
    returnValue = libpanda._inPVZN3syts(mat.this, scale.this, shear.this, hpr.this)
    return returnValue


def __overloaded_decomposeMatrix_ptrConstLMatrix3f_ptrLVecBase3f_ptrLVecBase3f___enum__CoordinateSystem(mat, scale, hpr, cs):
    returnValue = libpanda._inPVZN3KI_s(mat.this, scale.this, hpr.this, cs)
    return returnValue


def __overloaded_decomposeMatrix_ptrConstLMatrix3f_ptrLVecBase3f_ptrLVecBase3f(mat, scale, hpr):
    returnValue = libpanda._inPVZN3zJVg(mat.this, scale.this, hpr.this)
    return returnValue


def __overloaded_decomposeMatrix_ptrConstLMatrix3f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f___enum__CoordinateSystem(mat, scale, shear, hpr, cs):
    returnValue = libpanda._inPVZN3b5Pi(mat.this, scale.this, shear.this, hpr.this, cs)
    return returnValue


def __overloaded_decomposeMatrix_ptrConstLMatrix3f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f(mat, scale, shear, hpr):
    returnValue = libpanda._inPVZN3FoHP(mat.this, scale.this, shear.this, hpr.this)
    return returnValue


def __overloaded_decomposeMatrix_ptrConstLMatrix4d_ptrLVecBase3d_ptrLVecBase3d_ptrLVecBase3d___enum__CoordinateSystem(mat, scale, hpr, translate, cs):
    returnValue = libpanda._inPVZN37y0_(mat.this, scale.this, hpr.this, translate.this, cs)
    return returnValue


def __overloaded_decomposeMatrix_ptrConstLMatrix4d_ptrLVecBase3d_ptrLVecBase3d_ptrLVecBase3d(mat, scale, hpr, translate):
    returnValue = libpanda._inPVZN31gus(mat.this, scale.this, hpr.this, translate.this)
    return returnValue


def __overloaded_decomposeMatrix_ptrConstLMatrix4d_ptrLVecBase3d_ptrLVecBase3d_ptrLVecBase3d_ptrLVecBase3d___enum__CoordinateSystem(mat, scale, shear, hpr, translate, cs):
    returnValue = libpanda._inPVZN3Fy__(mat.this, scale.this, shear.this, hpr.this, translate.this, cs)
    return returnValue


def __overloaded_decomposeMatrix_ptrConstLMatrix4d_ptrLVecBase3d_ptrLVecBase3d_ptrLVecBase3d_ptrLVecBase3d(mat, scale, shear, hpr, translate):
    returnValue = libpanda._inPVZN3ioSK(mat.this, scale.this, shear.this, hpr.this, translate.this)
    return returnValue


def __overloaded_decomposeMatrix_ptrConstLMatrix4f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f___enum__CoordinateSystem(mat, scale, hpr, translate, cs):
    returnValue = libpanda._inPVZN3QLRi(mat.this, scale.this, hpr.this, translate.this, cs)
    return returnValue


def __overloaded_decomposeMatrix_ptrConstLMatrix4f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f(mat, scale, hpr, translate):
    returnValue = libpanda._inPVZN3cmIP(mat.this, scale.this, hpr.this, translate.this)
    return returnValue


def __overloaded_decomposeMatrix_ptrConstLMatrix4f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f___enum__CoordinateSystem(mat, scale, shear, hpr, translate, cs):
    returnValue = libpanda._inPVZN3t1gv(mat.this, scale.this, shear.this, hpr.this, translate.this, cs)
    return returnValue


def __overloaded_decomposeMatrix_ptrConstLMatrix4f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f(mat, scale, shear, hpr, translate):
    returnValue = libpanda._inPVZN3Jlz6(mat.this, scale.this, shear.this, hpr.this, translate.this)
    return returnValue


def __overloaded_composeMatrixOldHpr_ptrLMatrix3d_ptrConstLVecBase3d_ptrConstLVecBase3d_ptrConstLVecBase3d___enum__CoordinateSystem(mat, scale, shear, hpr, cs):
    returnValue = libpanda._inPVZN35kiD(mat.this, scale.this, shear.this, hpr.this, cs)
    return returnValue


def __overloaded_composeMatrixOldHpr_ptrLMatrix3d_ptrConstLVecBase3d_ptrConstLVecBase3d_ptrConstLVecBase3d(mat, scale, shear, hpr):
    returnValue = libpanda._inPVZN3TMeM(mat.this, scale.this, shear.this, hpr.this)
    return returnValue


def __overloaded_composeMatrixOldHpr_ptrLMatrix3f_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f___enum__CoordinateSystem(mat, scale, shear, hpr, cs):
    returnValue = libpanda._inPVZN3URso(mat.this, scale.this, shear.this, hpr.this, cs)
    return returnValue


def __overloaded_composeMatrixOldHpr_ptrLMatrix3f_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f(mat, scale, shear, hpr):
    returnValue = libpanda._inPVZN3_Rpx(mat.this, scale.this, shear.this, hpr.this)
    return returnValue


def __overloaded_composeMatrixOldHpr_ptrLMatrix4d_ptrConstLVecBase3d_ptrConstLVecBase3d_ptrConstLVecBase3d_ptrConstLVecBase3d___enum__CoordinateSystem(mat, scale, shear, hpr, translate, cs):
    returnValue = libpanda._inPVZN3aU0J(mat.this, scale.this, shear.this, hpr.this, translate.this, cs)
    return returnValue


def __overloaded_composeMatrixOldHpr_ptrLMatrix4d_ptrConstLVecBase3d_ptrConstLVecBase3d_ptrConstLVecBase3d_ptrConstLVecBase3d(mat, scale, shear, hpr, translate):
    returnValue = libpanda._inPVZN3_LGV(mat.this, scale.this, shear.this, hpr.this, translate.this)
    return returnValue


def __overloaded_composeMatrixOldHpr_ptrLMatrix4f_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f___enum__CoordinateSystem(mat, scale, shear, hpr, translate, cs):
    returnValue = libpanda._inPVZN3Xr_e(mat.this, scale.this, shear.this, hpr.this, translate.this, cs)
    return returnValue


def __overloaded_composeMatrixOldHpr_ptrLMatrix4f_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f(mat, scale, shear, hpr, translate):
    returnValue = libpanda._inPVZN3gMRq(mat.this, scale.this, shear.this, hpr.this, translate.this)
    return returnValue


def __overloaded_decomposeMatrixOldHpr_ptrConstLMatrix3d_ptrLVecBase3d_ptrLVecBase3d_ptrLVecBase3d___enum__CoordinateSystem(mat, scale, shear, hpr, cs):
    returnValue = libpanda._inPVZN3tC1N(mat.this, scale.this, shear.this, hpr.this, cs)
    return returnValue


def __overloaded_decomposeMatrixOldHpr_ptrConstLMatrix3d_ptrLVecBase3d_ptrLVecBase3d_ptrLVecBase3d(mat, scale, shear, hpr):
    returnValue = libpanda._inPVZN3z5DH(mat.this, scale.this, shear.this, hpr.this)
    return returnValue


def __overloaded_decomposeMatrixOldHpr_ptrConstLMatrix3f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f___enum__CoordinateSystem(mat, scale, shear, hpr, cs):
    returnValue = libpanda._inPVZN3POdX(mat.this, scale.this, shear.this, hpr.this, cs)
    return returnValue


def __overloaded_decomposeMatrixOldHpr_ptrConstLMatrix3f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f(mat, scale, shear, hpr):
    returnValue = libpanda._inPVZN3RWrQ(mat.this, scale.this, shear.this, hpr.this)
    return returnValue


def __overloaded_decomposeMatrixOldHpr_ptrConstLMatrix4d_ptrLVecBase3d_ptrLVecBase3d_ptrLVecBase3d_ptrLVecBase3d___enum__CoordinateSystem(mat, scale, shear, hpr, translate, cs):
    returnValue = libpanda._inPVZN3vhAZ(mat.this, scale.this, shear.this, hpr.this, translate.this, cs)
    return returnValue


def __overloaded_decomposeMatrixOldHpr_ptrConstLMatrix4d_ptrLVecBase3d_ptrLVecBase3d_ptrLVecBase3d_ptrLVecBase3d(mat, scale, shear, hpr, translate):
    returnValue = libpanda._inPVZN3PJWn(mat.this, scale.this, shear.this, hpr.this, translate.this)
    return returnValue


def __overloaded_decomposeMatrixOldHpr_ptrConstLMatrix4f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f___enum__CoordinateSystem(mat, scale, shear, hpr, translate, cs):
    returnValue = libpanda._inPVZN3ST9i(mat.this, scale.this, shear.this, hpr.this, translate.this, cs)
    return returnValue


def __overloaded_decomposeMatrixOldHpr_ptrConstLMatrix4f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f(mat, scale, shear, hpr, translate):
    returnValue = libpanda._inPVZN395Tx(mat.this, scale.this, shear.this, hpr.this, translate.this)
    return returnValue


def __overloaded_composeMatrixNewHpr_ptrLMatrix3d_ptrConstLVecBase3d_ptrConstLVecBase3d_ptrConstLVecBase3d___enum__CoordinateSystem(mat, scale, shear, hpr, cs):
    returnValue = libpanda._inPVZN32yX5(mat.this, scale.this, shear.this, hpr.this, cs)
    return returnValue


def __overloaded_composeMatrixNewHpr_ptrLMatrix3d_ptrConstLVecBase3d_ptrConstLVecBase3d_ptrConstLVecBase3d(mat, scale, shear, hpr):
    returnValue = libpanda._inPVZN3ZHTC(mat.this, scale.this, shear.this, hpr.this)
    return returnValue


def __overloaded_composeMatrixNewHpr_ptrLMatrix3f_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f___enum__CoordinateSystem(mat, scale, shear, hpr, cs):
    returnValue = libpanda._inPVZN3SFhe(mat.this, scale.this, shear.this, hpr.this, cs)
    return returnValue


def __overloaded_composeMatrixNewHpr_ptrLMatrix3f_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f(mat, scale, shear, hpr):
    returnValue = libpanda._inPVZN31Zen(mat.this, scale.this, shear.this, hpr.this)
    return returnValue


def __overloaded_composeMatrixNewHpr_ptrLMatrix4d_ptrConstLVecBase3d_ptrConstLVecBase3d_ptrConstLVecBase3d_ptrConstLVecBase3d___enum__CoordinateSystem(mat, scale, shear, hpr, translate, cs):
    returnValue = libpanda._inPVZN3XOp_(mat.this, scale.this, shear.this, hpr.this, translate.this, cs)
    return returnValue


def __overloaded_composeMatrixNewHpr_ptrLMatrix4d_ptrConstLVecBase3d_ptrConstLVecBase3d_ptrConstLVecBase3d_ptrConstLVecBase3d(mat, scale, shear, hpr, translate):
    returnValue = libpanda._inPVZN3IA7K(mat.this, scale.this, shear.this, hpr.this, translate.this)
    return returnValue


def __overloaded_composeMatrixNewHpr_ptrLMatrix4f_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f___enum__CoordinateSystem(mat, scale, shear, hpr, translate, cs):
    returnValue = libpanda._inPVZN3R3yU(mat.this, scale.this, shear.this, hpr.this, translate.this, cs)
    return returnValue


def __overloaded_composeMatrixNewHpr_ptrLMatrix4f_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f(mat, scale, shear, hpr, translate):
    returnValue = libpanda._inPVZN3KHGg(mat.this, scale.this, shear.this, hpr.this, translate.this)
    return returnValue


def __overloaded_decomposeMatrixNewHpr_ptrConstLMatrix3d_ptrLVecBase3d_ptrLVecBase3d_ptrLVecBase3d___enum__CoordinateSystem(mat, scale, shear, hpr, cs):
    returnValue = libpanda._inPVZN30nyg(mat.this, scale.this, shear.this, hpr.this, cs)
    return returnValue


def __overloaded_decomposeMatrixNewHpr_ptrConstLMatrix3d_ptrLVecBase3d_ptrLVecBase3d_ptrLVecBase3d(mat, scale, shear, hpr):
    returnValue = libpanda._inPVZN3WfBa(mat.this, scale.this, shear.this, hpr.this)
    return returnValue


def __overloaded_decomposeMatrixNewHpr_ptrConstLMatrix3f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f___enum__CoordinateSystem(mat, scale, shear, hpr, cs):
    returnValue = libpanda._inPVZN3Suaq(mat.this, scale.this, shear.this, hpr.this, cs)
    return returnValue


def __overloaded_decomposeMatrixNewHpr_ptrConstLMatrix3f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f(mat, scale, shear, hpr):
    returnValue = libpanda._inPVZN37noj(mat.this, scale.this, shear.this, hpr.this)
    return returnValue


def __overloaded_decomposeMatrixNewHpr_ptrConstLMatrix4d_ptrLVecBase3d_ptrLVecBase3d_ptrLVecBase3d_ptrLVecBase3d___enum__CoordinateSystem(mat, scale, shear, hpr, translate, cs):
    returnValue = libpanda._inPVZN3Bw_r(mat.this, scale.this, shear.this, hpr.this, translate.this, cs)
    return returnValue


def __overloaded_decomposeMatrixNewHpr_ptrConstLMatrix4d_ptrLVecBase3d_ptrLVecBase3d_ptrLVecBase3d_ptrLVecBase3d(mat, scale, shear, hpr, translate):
    returnValue = libpanda._inPVZN31_T6(mat.this, scale.this, shear.this, hpr.this, translate.this)
    return returnValue


def __overloaded_decomposeMatrixNewHpr_ptrConstLMatrix4f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f___enum__CoordinateSystem(mat, scale, shear, hpr, translate, cs):
    returnValue = libpanda._inPVZN33x61(mat.this, scale.this, shear.this, hpr.this, translate.this, cs)
    return returnValue


def __overloaded_decomposeMatrixNewHpr_ptrConstLMatrix4f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f(mat, scale, shear, hpr, translate):
    returnValue = libpanda._inPVZN3GpPE(mat.this, scale.this, shear.this, hpr.this, translate.this)
    return returnValue


def __overloaded_oldToNewHpr_ptrConstLVecBase3d(oldHpr):
    returnValue = libpanda._inPVZN32peC(oldHpr.this)
    import VBase3D
    returnObject = VBase3D.VBase3D(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def __overloaded_oldToNewHpr_ptrConstLVecBase3f(oldHpr):
    returnValue = libpanda._inPVZN3I0gC(oldHpr.this)
    import VBase3
    returnObject = VBase3.VBase3(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def __overloaded_newToOldHpr_ptrConstLVecBase3d(newHpr):
    returnValue = libpanda._inPVZN3Pgfc(newHpr.this)
    import VBase3D
    returnObject = VBase3D.VBase3D(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def __overloaded_newToOldHpr_ptrConstLVecBase3f(newHpr):
    returnValue = libpanda._inPVZN3ZEhc(newHpr.this)
    import VBase3
    returnObject = VBase3.VBase3(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def __overloaded_autoBind_ptrPandaNode_ptrAnimControlCollection_int(rootNode, controls, hierarchyMatchFlags):
    returnValue = libpanda._inPn9gMknU_(rootNode.this, controls.this, hierarchyMatchFlags)
    return returnValue


def __overloaded_autoBind_ptrPandaNode_ptrAnimControlCollection(rootNode, controls):
    returnValue = libpanda._inPn9gMP30i(rootNode.this, controls.this)
    return returnValue

HCCUT = 1
HCFREE = 2
HCG1 = 3
HCSMOOTH = 4
PCTHPR = 2
PCTNONE = 0
PCTT = 3
PCTXYZ = 1
