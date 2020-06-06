# File: l (Python 2.2)

import types
import libpanda
import DSearchPath
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
import PandaNode
import AnimControlCollection

def deg2Rad(*_args):
    numArgs = len(_args)
    if numArgs == 1:
        if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
            return __overloaded_deg2Rad_float(_args[0])
        elif isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
            return __overloaded_deg2Rad_double(_args[0])
        else:
            raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <types.FloatType> '
    else:
        raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


def rad2Deg(*_args):
    numArgs = len(_args)
    if numArgs == 1:
        if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
            return __overloaded_rad2Deg_float(_args[0])
        elif isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
            return __overloaded_rad2Deg_double(_args[0])
        else:
            raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <types.FloatType> '
    else:
        raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


def lookAt(*_args):
    numArgs = len(_args)
    if numArgs == 2:
        import QuatD
        import Quat
        import Mat4D
        import Mat4
        import Mat3D
        import Mat3
        if isinstance(_args[0], QuatD.QuatD):
            import Vec3D
            if isinstance(_args[1], Vec3D.Vec3D):
                return __overloaded_lookAt_ptrLQuaterniond_ptrConstLVector3d(_args[0], _args[1])
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Vec3D.Vec3D> '
        elif isinstance(_args[0], Quat.Quat):
            import Vec3
            if isinstance(_args[1], Vec3.Vec3):
                return __overloaded_lookAt_ptrLQuaternionf_ptrConstLVector3f(_args[0], _args[1])
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Vec3.Vec3> '
        elif isinstance(_args[0], Mat4D.Mat4D):
            import Vec3D
            if isinstance(_args[1], Vec3D.Vec3D):
                return __overloaded_lookAt_ptrLMatrix4d_ptrConstLVector3d(_args[0], _args[1])
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Vec3D.Vec3D> '
        elif isinstance(_args[0], Mat4.Mat4):
            import Vec3
            if isinstance(_args[1], Vec3.Vec3):
                return __overloaded_lookAt_ptrLMatrix4f_ptrConstLVector3f(_args[0], _args[1])
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Vec3.Vec3> '
        elif isinstance(_args[0], Mat3D.Mat3D):
            import Vec3D
            if isinstance(_args[1], Vec3D.Vec3D):
                return __overloaded_lookAt_ptrLMatrix3d_ptrConstLVector3d(_args[0], _args[1])
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Vec3D.Vec3D> '
        elif isinstance(_args[0], Mat3.Mat3):
            import Vec3
            if isinstance(_args[1], Vec3.Vec3):
                return __overloaded_lookAt_ptrLMatrix3f_ptrConstLVector3f(_args[0], _args[1])
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Vec3.Vec3> '
        else:
            raise TypeError, 'Invalid argument 0, expected one of: <QuatD.QuatD> <Quat.Quat> <Mat4D.Mat4D> <Mat4.Mat4> <Mat3D.Mat3D> <Mat3.Mat3> '
    elif numArgs == 3:
        import QuatD
        import Quat
        import Mat4D
        import Mat4
        import Mat3D
        import Mat3
        if isinstance(_args[0], QuatD.QuatD):
            import Vec3D
            if isinstance(_args[1], Vec3D.Vec3D):
                import Vec3D
                if isinstance(_args[2], types.IntType):
                    return __overloaded_lookAt_ptrLQuaterniond_ptrConstLVector3d___enum__CoordinateSystem(_args[0], _args[1], _args[2])
                elif isinstance(_args[2], Vec3D.Vec3D):
                    return __overloaded_lookAt_ptrLQuaterniond_ptrConstLVector3d_ptrConstLVector3d(_args[0], _args[1], _args[2])
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> <Vec3D.Vec3D> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Vec3D.Vec3D> '
        elif isinstance(_args[0], Quat.Quat):
            import Vec3
            if isinstance(_args[1], Vec3.Vec3):
                import Vec3
                if isinstance(_args[2], types.IntType):
                    return __overloaded_lookAt_ptrLQuaternionf_ptrConstLVector3f___enum__CoordinateSystem(_args[0], _args[1], _args[2])
                elif isinstance(_args[2], Vec3.Vec3):
                    return __overloaded_lookAt_ptrLQuaternionf_ptrConstLVector3f_ptrConstLVector3f(_args[0], _args[1], _args[2])
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> <Vec3.Vec3> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Vec3.Vec3> '
        elif isinstance(_args[0], Mat4D.Mat4D):
            import Vec3D
            if isinstance(_args[1], Vec3D.Vec3D):
                import Vec3D
                if isinstance(_args[2], types.IntType):
                    return __overloaded_lookAt_ptrLMatrix4d_ptrConstLVector3d___enum__CoordinateSystem(_args[0], _args[1], _args[2])
                elif isinstance(_args[2], Vec3D.Vec3D):
                    return __overloaded_lookAt_ptrLMatrix4d_ptrConstLVector3d_ptrConstLVector3d(_args[0], _args[1], _args[2])
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> <Vec3D.Vec3D> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Vec3D.Vec3D> '
        elif isinstance(_args[0], Mat4.Mat4):
            import Vec3
            if isinstance(_args[1], Vec3.Vec3):
                import Vec3
                if isinstance(_args[2], types.IntType):
                    return __overloaded_lookAt_ptrLMatrix4f_ptrConstLVector3f___enum__CoordinateSystem(_args[0], _args[1], _args[2])
                elif isinstance(_args[2], Vec3.Vec3):
                    return __overloaded_lookAt_ptrLMatrix4f_ptrConstLVector3f_ptrConstLVector3f(_args[0], _args[1], _args[2])
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> <Vec3.Vec3> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Vec3.Vec3> '
        elif isinstance(_args[0], Mat3D.Mat3D):
            import Vec3D
            if isinstance(_args[1], Vec3D.Vec3D):
                import Vec3D
                if isinstance(_args[2], types.IntType):
                    return __overloaded_lookAt_ptrLMatrix3d_ptrConstLVector3d___enum__CoordinateSystem(_args[0], _args[1], _args[2])
                elif isinstance(_args[2], Vec3D.Vec3D):
                    return __overloaded_lookAt_ptrLMatrix3d_ptrConstLVector3d_ptrConstLVector3d(_args[0], _args[1], _args[2])
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> <Vec3D.Vec3D> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Vec3D.Vec3D> '
        elif isinstance(_args[0], Mat3.Mat3):
            import Vec3
            if isinstance(_args[1], Vec3.Vec3):
                import Vec3
                if isinstance(_args[2], types.IntType):
                    return __overloaded_lookAt_ptrLMatrix3f_ptrConstLVector3f___enum__CoordinateSystem(_args[0], _args[1], _args[2])
                elif isinstance(_args[2], Vec3.Vec3):
                    return __overloaded_lookAt_ptrLMatrix3f_ptrConstLVector3f_ptrConstLVector3f(_args[0], _args[1], _args[2])
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> <Vec3.Vec3> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Vec3.Vec3> '
        else:
            raise TypeError, 'Invalid argument 0, expected one of: <QuatD.QuatD> <Quat.Quat> <Mat4D.Mat4D> <Mat4.Mat4> <Mat3D.Mat3D> <Mat3.Mat3> '
    elif numArgs == 4:
        import QuatD
        import Quat
        import Mat4D
        import Mat4
        import Mat3D
        import Mat3
        if isinstance(_args[0], QuatD.QuatD):
            import Vec3D
            if isinstance(_args[1], Vec3D.Vec3D):
                import Vec3D
                if isinstance(_args[2], Vec3D.Vec3D):
                    if isinstance(_args[3], types.IntType):
                        return __overloaded_lookAt_ptrLQuaterniond_ptrConstLVector3d_ptrConstLVector3d___enum__CoordinateSystem(_args[0], _args[1], _args[2], _args[3])
                    else:
                        raise TypeError, 'Invalid argument 3, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <Vec3D.Vec3D> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Vec3D.Vec3D> '
        elif isinstance(_args[0], Quat.Quat):
            import Vec3
            if isinstance(_args[1], Vec3.Vec3):
                import Vec3
                if isinstance(_args[2], Vec3.Vec3):
                    if isinstance(_args[3], types.IntType):
                        return __overloaded_lookAt_ptrLQuaternionf_ptrConstLVector3f_ptrConstLVector3f___enum__CoordinateSystem(_args[0], _args[1], _args[2], _args[3])
                    else:
                        raise TypeError, 'Invalid argument 3, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <Vec3.Vec3> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Vec3.Vec3> '
        elif isinstance(_args[0], Mat4D.Mat4D):
            import Vec3D
            if isinstance(_args[1], Vec3D.Vec3D):
                import Vec3D
                if isinstance(_args[2], Vec3D.Vec3D):
                    if isinstance(_args[3], types.IntType):
                        return __overloaded_lookAt_ptrLMatrix4d_ptrConstLVector3d_ptrConstLVector3d___enum__CoordinateSystem(_args[0], _args[1], _args[2], _args[3])
                    else:
                        raise TypeError, 'Invalid argument 3, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <Vec3D.Vec3D> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Vec3D.Vec3D> '
        elif isinstance(_args[0], Mat4.Mat4):
            import Vec3
            if isinstance(_args[1], Vec3.Vec3):
                import Vec3
                if isinstance(_args[2], Vec3.Vec3):
                    if isinstance(_args[3], types.IntType):
                        return __overloaded_lookAt_ptrLMatrix4f_ptrConstLVector3f_ptrConstLVector3f___enum__CoordinateSystem(_args[0], _args[1], _args[2], _args[3])
                    else:
                        raise TypeError, 'Invalid argument 3, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <Vec3.Vec3> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Vec3.Vec3> '
        elif isinstance(_args[0], Mat3D.Mat3D):
            import Vec3D
            if isinstance(_args[1], Vec3D.Vec3D):
                import Vec3D
                if isinstance(_args[2], Vec3D.Vec3D):
                    if isinstance(_args[3], types.IntType):
                        return __overloaded_lookAt_ptrLMatrix3d_ptrConstLVector3d_ptrConstLVector3d___enum__CoordinateSystem(_args[0], _args[1], _args[2], _args[3])
                    else:
                        raise TypeError, 'Invalid argument 3, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <Vec3D.Vec3D> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Vec3D.Vec3D> '
        elif isinstance(_args[0], Mat3.Mat3):
            import Vec3
            if isinstance(_args[1], Vec3.Vec3):
                import Vec3
                if isinstance(_args[2], Vec3.Vec3):
                    if isinstance(_args[3], types.IntType):
                        return __overloaded_lookAt_ptrLMatrix3f_ptrConstLVector3f_ptrConstLVector3f___enum__CoordinateSystem(_args[0], _args[1], _args[2], _args[3])
                    else:
                        raise TypeError, 'Invalid argument 3, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <Vec3.Vec3> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Vec3.Vec3> '
        else:
            raise TypeError, 'Invalid argument 0, expected one of: <QuatD.QuatD> <Quat.Quat> <Mat4D.Mat4D> <Mat4.Mat4> <Mat3D.Mat3D> <Mat3.Mat3> '
    else:
        raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 4 '


def headsUp(*_args):
    numArgs = len(_args)
    if numArgs == 2:
        import QuatD
        import Quat
        import Mat4D
        import Mat4
        import Mat3D
        import Mat3
        if isinstance(_args[0], QuatD.QuatD):
            import Vec3D
            if isinstance(_args[1], Vec3D.Vec3D):
                return __overloaded_headsUp_ptrLQuaterniond_ptrConstLVector3d(_args[0], _args[1])
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Vec3D.Vec3D> '
        elif isinstance(_args[0], Quat.Quat):
            import Vec3
            if isinstance(_args[1], Vec3.Vec3):
                return __overloaded_headsUp_ptrLQuaternionf_ptrConstLVector3f(_args[0], _args[1])
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Vec3.Vec3> '
        elif isinstance(_args[0], Mat4D.Mat4D):
            import Vec3D
            if isinstance(_args[1], Vec3D.Vec3D):
                return __overloaded_headsUp_ptrLMatrix4d_ptrConstLVector3d(_args[0], _args[1])
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Vec3D.Vec3D> '
        elif isinstance(_args[0], Mat4.Mat4):
            import Vec3
            if isinstance(_args[1], Vec3.Vec3):
                return __overloaded_headsUp_ptrLMatrix4f_ptrConstLVector3f(_args[0], _args[1])
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Vec3.Vec3> '
        elif isinstance(_args[0], Mat3D.Mat3D):
            import Vec3D
            if isinstance(_args[1], Vec3D.Vec3D):
                return __overloaded_headsUp_ptrLMatrix3d_ptrConstLVector3d(_args[0], _args[1])
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Vec3D.Vec3D> '
        elif isinstance(_args[0], Mat3.Mat3):
            import Vec3
            if isinstance(_args[1], Vec3.Vec3):
                return __overloaded_headsUp_ptrLMatrix3f_ptrConstLVector3f(_args[0], _args[1])
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Vec3.Vec3> '
        else:
            raise TypeError, 'Invalid argument 0, expected one of: <QuatD.QuatD> <Quat.Quat> <Mat4D.Mat4D> <Mat4.Mat4> <Mat3D.Mat3D> <Mat3.Mat3> '
    elif numArgs == 3:
        import QuatD
        import Quat
        import Mat4D
        import Mat4
        import Mat3D
        import Mat3
        if isinstance(_args[0], QuatD.QuatD):
            import Vec3D
            if isinstance(_args[1], Vec3D.Vec3D):
                import Vec3D
                if isinstance(_args[2], types.IntType):
                    return __overloaded_headsUp_ptrLQuaterniond_ptrConstLVector3d___enum__CoordinateSystem(_args[0], _args[1], _args[2])
                elif isinstance(_args[2], Vec3D.Vec3D):
                    return __overloaded_headsUp_ptrLQuaterniond_ptrConstLVector3d_ptrConstLVector3d(_args[0], _args[1], _args[2])
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> <Vec3D.Vec3D> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Vec3D.Vec3D> '
        elif isinstance(_args[0], Quat.Quat):
            import Vec3
            if isinstance(_args[1], Vec3.Vec3):
                import Vec3
                if isinstance(_args[2], types.IntType):
                    return __overloaded_headsUp_ptrLQuaternionf_ptrConstLVector3f___enum__CoordinateSystem(_args[0], _args[1], _args[2])
                elif isinstance(_args[2], Vec3.Vec3):
                    return __overloaded_headsUp_ptrLQuaternionf_ptrConstLVector3f_ptrConstLVector3f(_args[0], _args[1], _args[2])
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> <Vec3.Vec3> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Vec3.Vec3> '
        elif isinstance(_args[0], Mat4D.Mat4D):
            import Vec3D
            if isinstance(_args[1], Vec3D.Vec3D):
                import Vec3D
                if isinstance(_args[2], types.IntType):
                    return __overloaded_headsUp_ptrLMatrix4d_ptrConstLVector3d___enum__CoordinateSystem(_args[0], _args[1], _args[2])
                elif isinstance(_args[2], Vec3D.Vec3D):
                    return __overloaded_headsUp_ptrLMatrix4d_ptrConstLVector3d_ptrConstLVector3d(_args[0], _args[1], _args[2])
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> <Vec3D.Vec3D> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Vec3D.Vec3D> '
        elif isinstance(_args[0], Mat4.Mat4):
            import Vec3
            if isinstance(_args[1], Vec3.Vec3):
                import Vec3
                if isinstance(_args[2], types.IntType):
                    return __overloaded_headsUp_ptrLMatrix4f_ptrConstLVector3f___enum__CoordinateSystem(_args[0], _args[1], _args[2])
                elif isinstance(_args[2], Vec3.Vec3):
                    return __overloaded_headsUp_ptrLMatrix4f_ptrConstLVector3f_ptrConstLVector3f(_args[0], _args[1], _args[2])
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> <Vec3.Vec3> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Vec3.Vec3> '
        elif isinstance(_args[0], Mat3D.Mat3D):
            import Vec3D
            if isinstance(_args[1], Vec3D.Vec3D):
                import Vec3D
                if isinstance(_args[2], types.IntType):
                    return __overloaded_headsUp_ptrLMatrix3d_ptrConstLVector3d___enum__CoordinateSystem(_args[0], _args[1], _args[2])
                elif isinstance(_args[2], Vec3D.Vec3D):
                    return __overloaded_headsUp_ptrLMatrix3d_ptrConstLVector3d_ptrConstLVector3d(_args[0], _args[1], _args[2])
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> <Vec3D.Vec3D> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Vec3D.Vec3D> '
        elif isinstance(_args[0], Mat3.Mat3):
            import Vec3
            if isinstance(_args[1], Vec3.Vec3):
                import Vec3
                if isinstance(_args[2], types.IntType):
                    return __overloaded_headsUp_ptrLMatrix3f_ptrConstLVector3f___enum__CoordinateSystem(_args[0], _args[1], _args[2])
                elif isinstance(_args[2], Vec3.Vec3):
                    return __overloaded_headsUp_ptrLMatrix3f_ptrConstLVector3f_ptrConstLVector3f(_args[0], _args[1], _args[2])
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> <Vec3.Vec3> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Vec3.Vec3> '
        else:
            raise TypeError, 'Invalid argument 0, expected one of: <QuatD.QuatD> <Quat.Quat> <Mat4D.Mat4D> <Mat4.Mat4> <Mat3D.Mat3D> <Mat3.Mat3> '
    elif numArgs == 4:
        import QuatD
        import Quat
        import Mat4D
        import Mat4
        import Mat3D
        import Mat3
        if isinstance(_args[0], QuatD.QuatD):
            import Vec3D
            if isinstance(_args[1], Vec3D.Vec3D):
                import Vec3D
                if isinstance(_args[2], Vec3D.Vec3D):
                    if isinstance(_args[3], types.IntType):
                        return __overloaded_headsUp_ptrLQuaterniond_ptrConstLVector3d_ptrConstLVector3d___enum__CoordinateSystem(_args[0], _args[1], _args[2], _args[3])
                    else:
                        raise TypeError, 'Invalid argument 3, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <Vec3D.Vec3D> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Vec3D.Vec3D> '
        elif isinstance(_args[0], Quat.Quat):
            import Vec3
            if isinstance(_args[1], Vec3.Vec3):
                import Vec3
                if isinstance(_args[2], Vec3.Vec3):
                    if isinstance(_args[3], types.IntType):
                        return __overloaded_headsUp_ptrLQuaternionf_ptrConstLVector3f_ptrConstLVector3f___enum__CoordinateSystem(_args[0], _args[1], _args[2], _args[3])
                    else:
                        raise TypeError, 'Invalid argument 3, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <Vec3.Vec3> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Vec3.Vec3> '
        elif isinstance(_args[0], Mat4D.Mat4D):
            import Vec3D
            if isinstance(_args[1], Vec3D.Vec3D):
                import Vec3D
                if isinstance(_args[2], Vec3D.Vec3D):
                    if isinstance(_args[3], types.IntType):
                        return __overloaded_headsUp_ptrLMatrix4d_ptrConstLVector3d_ptrConstLVector3d___enum__CoordinateSystem(_args[0], _args[1], _args[2], _args[3])
                    else:
                        raise TypeError, 'Invalid argument 3, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <Vec3D.Vec3D> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Vec3D.Vec3D> '
        elif isinstance(_args[0], Mat4.Mat4):
            import Vec3
            if isinstance(_args[1], Vec3.Vec3):
                import Vec3
                if isinstance(_args[2], Vec3.Vec3):
                    if isinstance(_args[3], types.IntType):
                        return __overloaded_headsUp_ptrLMatrix4f_ptrConstLVector3f_ptrConstLVector3f___enum__CoordinateSystem(_args[0], _args[1], _args[2], _args[3])
                    else:
                        raise TypeError, 'Invalid argument 3, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <Vec3.Vec3> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Vec3.Vec3> '
        elif isinstance(_args[0], Mat3D.Mat3D):
            import Vec3D
            if isinstance(_args[1], Vec3D.Vec3D):
                import Vec3D
                if isinstance(_args[2], Vec3D.Vec3D):
                    if isinstance(_args[3], types.IntType):
                        return __overloaded_headsUp_ptrLMatrix3d_ptrConstLVector3d_ptrConstLVector3d___enum__CoordinateSystem(_args[0], _args[1], _args[2], _args[3])
                    else:
                        raise TypeError, 'Invalid argument 3, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <Vec3D.Vec3D> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Vec3D.Vec3D> '
        elif isinstance(_args[0], Mat3.Mat3):
            import Vec3
            if isinstance(_args[1], Vec3.Vec3):
                import Vec3
                if isinstance(_args[2], Vec3.Vec3):
                    if isinstance(_args[3], types.IntType):
                        return __overloaded_headsUp_ptrLMatrix3f_ptrConstLVector3f_ptrConstLVector3f___enum__CoordinateSystem(_args[0], _args[1], _args[2], _args[3])
                    else:
                        raise TypeError, 'Invalid argument 3, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <Vec3.Vec3> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Vec3.Vec3> '
        else:
            raise TypeError, 'Invalid argument 0, expected one of: <QuatD.QuatD> <Quat.Quat> <Mat4D.Mat4D> <Mat4.Mat4> <Mat3D.Mat3D> <Mat3.Mat3> '
    else:
        raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 4 '


def rotateTo(*_args):
    numArgs = len(_args)
    if numArgs == 3:
        import Mat4D
        import Mat4
        import Mat3D
        import Mat3
        if isinstance(_args[0], Mat4D.Mat4D):
            import Vec3D
            if isinstance(_args[1], Vec3D.Vec3D):
                import Vec3D
                if isinstance(_args[2], Vec3D.Vec3D):
                    return __overloaded_rotateTo_ptrLMatrix4d_ptrConstLVector3d_ptrConstLVector3d(_args[0], _args[1], _args[2])
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <Vec3D.Vec3D> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Vec3D.Vec3D> '
        elif isinstance(_args[0], Mat4.Mat4):
            import Vec3
            if isinstance(_args[1], Vec3.Vec3):
                import Vec3
                if isinstance(_args[2], Vec3.Vec3):
                    return __overloaded_rotateTo_ptrLMatrix4f_ptrConstLVector3f_ptrConstLVector3f(_args[0], _args[1], _args[2])
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <Vec3.Vec3> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Vec3.Vec3> '
        elif isinstance(_args[0], Mat3D.Mat3D):
            import Vec3D
            if isinstance(_args[1], Vec3D.Vec3D):
                import Vec3D
                if isinstance(_args[2], Vec3D.Vec3D):
                    return __overloaded_rotateTo_ptrLMatrix3d_ptrConstLVector3d_ptrConstLVector3d(_args[0], _args[1], _args[2])
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <Vec3D.Vec3D> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Vec3D.Vec3D> '
        elif isinstance(_args[0], Mat3.Mat3):
            import Vec3
            if isinstance(_args[1], Vec3.Vec3):
                import Vec3
                if isinstance(_args[2], Vec3.Vec3):
                    return __overloaded_rotateTo_ptrLMatrix3f_ptrConstLVector3f_ptrConstLVector3f(_args[0], _args[1], _args[2])
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <Vec3.Vec3> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Vec3.Vec3> '
        else:
            raise TypeError, 'Invalid argument 0, expected one of: <Mat4D.Mat4D> <Mat4.Mat4> <Mat3D.Mat3D> <Mat3.Mat3> '
    else:
        raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 3 '


def autoBind(*_args):
    numArgs = len(_args)
    if numArgs == 2:
        import PandaNode
        if isinstance(_args[0], PandaNode.PandaNode):
            import AnimControlCollection
            if isinstance(_args[1], AnimControlCollection.AnimControlCollection):
                return __overloaded_autoBind_ptrPandaNode_ptrAnimControlCollection(_args[0], _args[1])
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <AnimControlCollection.AnimControlCollection> '
        else:
            raise TypeError, 'Invalid argument 0, expected one of: <PandaNode.PandaNode> '
    elif numArgs == 3:
        import PandaNode
        if isinstance(_args[0], PandaNode.PandaNode):
            import AnimControlCollection
            if isinstance(_args[1], AnimControlCollection.AnimControlCollection):
                if isinstance(_args[2], types.IntType):
                    return __overloaded_autoBind_ptrPandaNode_ptrAnimControlCollection_int(_args[0], _args[1], _args[2])
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <AnimControlCollection.AnimControlCollection> '
        else:
            raise TypeError, 'Invalid argument 0, expected one of: <PandaNode.PandaNode> '
    else:
        raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '


def composeMatrix(*_args):
    numArgs = len(_args)
    if numArgs == 3:
        import Mat3D
        import Mat3
        if isinstance(_args[0], Mat3D.Mat3D):
            import VBase3D
            if isinstance(_args[1], VBase3D.VBase3D):
                import VBase3D
                if isinstance(_args[2], VBase3D.VBase3D):
                    return __overloaded_composeMatrix_ptrLMatrix3d_ptrConstLVecBase3d_ptrConstLVecBase3d(_args[0], _args[1], _args[2])
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <VBase3D.VBase3D> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <VBase3D.VBase3D> '
        elif isinstance(_args[0], Mat3.Mat3):
            import VBase3
            if isinstance(_args[1], VBase3.VBase3):
                import VBase3
                if isinstance(_args[2], VBase3.VBase3):
                    return __overloaded_composeMatrix_ptrLMatrix3f_ptrConstLVecBase3f_ptrConstLVecBase3f(_args[0], _args[1], _args[2])
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <VBase3.VBase3> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
        else:
            raise TypeError, 'Invalid argument 0, expected one of: <Mat3D.Mat3D> <Mat3.Mat3> '
    elif numArgs == 4:
        import Mat4D
        import Mat4
        import Mat3D
        import Mat3
        if isinstance(_args[0], Mat4D.Mat4D):
            import VBase3D
            if isinstance(_args[1], VBase3D.VBase3D):
                import VBase3D
                if isinstance(_args[2], VBase3D.VBase3D):
                    import VBase3D
                    if isinstance(_args[3], VBase3D.VBase3D):
                        return __overloaded_composeMatrix_ptrLMatrix4d_ptrConstLVecBase3d_ptrConstLVecBase3d_ptrConstLVecBase3d(_args[0], _args[1], _args[2], _args[3])
                    else:
                        raise TypeError, 'Invalid argument 3, expected one of: <VBase3D.VBase3D> '
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <VBase3D.VBase3D> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <VBase3D.VBase3D> '
        elif isinstance(_args[0], Mat4.Mat4):
            import VBase3
            if isinstance(_args[1], VBase3.VBase3):
                import VBase3
                if isinstance(_args[2], VBase3.VBase3):
                    import VBase3
                    if isinstance(_args[3], VBase3.VBase3):
                        return __overloaded_composeMatrix_ptrLMatrix4f_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f(_args[0], _args[1], _args[2], _args[3])
                    else:
                        raise TypeError, 'Invalid argument 3, expected one of: <VBase3.VBase3> '
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <VBase3.VBase3> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
        elif isinstance(_args[0], Mat3D.Mat3D):
            import VBase3D
            if isinstance(_args[1], VBase3D.VBase3D):
                import VBase3D
                if isinstance(_args[2], VBase3D.VBase3D):
                    if isinstance(_args[3], types.IntType):
                        return __overloaded_composeMatrix_ptrLMatrix3d_ptrConstLVecBase3d_ptrConstLVecBase3d___enum__CoordinateSystem(_args[0], _args[1], _args[2], _args[3])
                    else:
                        raise TypeError, 'Invalid argument 3, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <VBase3D.VBase3D> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <VBase3D.VBase3D> '
        elif isinstance(_args[0], Mat3.Mat3):
            import VBase3
            if isinstance(_args[1], VBase3.VBase3):
                import VBase3
                if isinstance(_args[2], VBase3.VBase3):
                    if isinstance(_args[3], types.IntType):
                        return __overloaded_composeMatrix_ptrLMatrix3f_ptrConstLVecBase3f_ptrConstLVecBase3f___enum__CoordinateSystem(_args[0], _args[1], _args[2], _args[3])
                    else:
                        raise TypeError, 'Invalid argument 3, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <VBase3.VBase3> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
        else:
            raise TypeError, 'Invalid argument 0, expected one of: <Mat4D.Mat4D> <Mat4.Mat4> <Mat3D.Mat3D> <Mat3.Mat3> '
    elif numArgs == 5:
        import Mat4D
        import Mat4
        if isinstance(_args[0], Mat4D.Mat4D):
            import VBase3D
            if isinstance(_args[1], VBase3D.VBase3D):
                import VBase3D
                if isinstance(_args[2], VBase3D.VBase3D):
                    import VBase3D
                    if isinstance(_args[3], VBase3D.VBase3D):
                        if isinstance(_args[4], types.IntType):
                            return __overloaded_composeMatrix_ptrLMatrix4d_ptrConstLVecBase3d_ptrConstLVecBase3d_ptrConstLVecBase3d___enum__CoordinateSystem(_args[0], _args[1], _args[2], _args[3], _args[4])
                        else:
                            raise TypeError, 'Invalid argument 4, expected one of: <types.IntType> '
                    else:
                        raise TypeError, 'Invalid argument 3, expected one of: <VBase3D.VBase3D> '
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <VBase3D.VBase3D> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <VBase3D.VBase3D> '
        elif isinstance(_args[0], Mat4.Mat4):
            import VBase3
            if isinstance(_args[1], VBase3.VBase3):
                import VBase3
                if isinstance(_args[2], VBase3.VBase3):
                    import VBase3
                    if isinstance(_args[3], VBase3.VBase3):
                        if isinstance(_args[4], types.IntType):
                            return __overloaded_composeMatrix_ptrLMatrix4f_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f___enum__CoordinateSystem(_args[0], _args[1], _args[2], _args[3], _args[4])
                        else:
                            raise TypeError, 'Invalid argument 4, expected one of: <types.IntType> '
                    else:
                        raise TypeError, 'Invalid argument 3, expected one of: <VBase3.VBase3> '
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <VBase3.VBase3> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
        else:
            raise TypeError, 'Invalid argument 0, expected one of: <Mat4D.Mat4D> <Mat4.Mat4> '
    else:
        raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 3 4 5 '


def decomposeMatrix(*_args):
    numArgs = len(_args)
    if numArgs == 3:
        import Mat3D
        import Mat3
        if isinstance(_args[0], Mat3D.Mat3D):
            import VBase3D
            if isinstance(_args[1], VBase3D.VBase3D):
                import VBase3D
                if isinstance(_args[2], VBase3D.VBase3D):
                    return __overloaded_decomposeMatrix_ptrConstLMatrix3d_ptrLVecBase3d_ptrLVecBase3d(_args[0], _args[1], _args[2])
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <VBase3D.VBase3D> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <VBase3D.VBase3D> '
        elif isinstance(_args[0], Mat3.Mat3):
            import VBase3
            if isinstance(_args[1], VBase3.VBase3):
                import VBase3
                if isinstance(_args[2], VBase3.VBase3):
                    return __overloaded_decomposeMatrix_ptrConstLMatrix3f_ptrLVecBase3f_ptrLVecBase3f(_args[0], _args[1], _args[2])
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <VBase3.VBase3> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
        else:
            raise TypeError, 'Invalid argument 0, expected one of: <Mat3D.Mat3D> <Mat3.Mat3> '
    elif numArgs == 4:
        import Mat4D
        import Mat4
        import Mat3D
        import Mat3
        if isinstance(_args[0], Mat4D.Mat4D):
            import VBase3D
            if isinstance(_args[1], VBase3D.VBase3D):
                import VBase3D
                if isinstance(_args[2], VBase3D.VBase3D):
                    import VBase3D
                    if isinstance(_args[3], VBase3D.VBase3D):
                        return __overloaded_decomposeMatrix_ptrConstLMatrix4d_ptrLVecBase3d_ptrLVecBase3d_ptrLVecBase3d(_args[0], _args[1], _args[2], _args[3])
                    else:
                        raise TypeError, 'Invalid argument 3, expected one of: <VBase3D.VBase3D> '
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <VBase3D.VBase3D> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <VBase3D.VBase3D> '
        elif isinstance(_args[0], Mat4.Mat4):
            import VBase3
            if isinstance(_args[1], VBase3.VBase3):
                import VBase3
                if isinstance(_args[2], VBase3.VBase3):
                    import VBase3
                    if isinstance(_args[3], VBase3.VBase3):
                        return __overloaded_decomposeMatrix_ptrConstLMatrix4f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f(_args[0], _args[1], _args[2], _args[3])
                    else:
                        raise TypeError, 'Invalid argument 3, expected one of: <VBase3.VBase3> '
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <VBase3.VBase3> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
        elif isinstance(_args[0], Mat3D.Mat3D):
            import VBase3D
            if isinstance(_args[1], VBase3D.VBase3D):
                import VBase3D
                if isinstance(_args[2], VBase3D.VBase3D):
                    if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                        return __overloaded_decomposeMatrix_ptrConstLMatrix3d_ptrLVecBase3d_ptrLVecBase3d_double(_args[0], _args[1], _args[2], _args[3])
                    elif isinstance(_args[3], types.IntType):
                        return __overloaded_decomposeMatrix_ptrConstLMatrix3d_ptrLVecBase3d_ptrLVecBase3d___enum__CoordinateSystem(_args[0], _args[1], _args[2], _args[3])
                    else:
                        raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <VBase3D.VBase3D> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <VBase3D.VBase3D> '
        elif isinstance(_args[0], Mat3.Mat3):
            import VBase3
            if isinstance(_args[1], VBase3.VBase3):
                import VBase3
                if isinstance(_args[2], VBase3.VBase3):
                    if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                        return __overloaded_decomposeMatrix_ptrConstLMatrix3f_ptrLVecBase3f_ptrLVecBase3f_float(_args[0], _args[1], _args[2], _args[3])
                    elif isinstance(_args[3], types.IntType):
                        return __overloaded_decomposeMatrix_ptrConstLMatrix3f_ptrLVecBase3f_ptrLVecBase3f___enum__CoordinateSystem(_args[0], _args[1], _args[2], _args[3])
                    else:
                        raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <VBase3.VBase3> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
        else:
            raise TypeError, 'Invalid argument 0, expected one of: <Mat4D.Mat4D> <Mat4.Mat4> <Mat3D.Mat3D> <Mat3.Mat3> '
    elif numArgs == 5:
        import Mat4D
        import Mat4
        import Mat3D
        import Mat3
        if isinstance(_args[0], Mat4D.Mat4D):
            import VBase3D
            if isinstance(_args[1], VBase3D.VBase3D):
                import VBase3D
                if isinstance(_args[2], VBase3D.VBase3D):
                    import VBase3D
                    if isinstance(_args[3], VBase3D.VBase3D):
                        if isinstance(_args[4], types.FloatType) or isinstance(_args[4], types.IntType):
                            return __overloaded_decomposeMatrix_ptrConstLMatrix4d_ptrLVecBase3d_ptrLVecBase3d_ptrLVecBase3d_double(_args[0], _args[1], _args[2], _args[3], _args[4])
                        elif isinstance(_args[4], types.IntType):
                            return __overloaded_decomposeMatrix_ptrConstLMatrix4d_ptrLVecBase3d_ptrLVecBase3d_ptrLVecBase3d___enum__CoordinateSystem(_args[0], _args[1], _args[2], _args[3], _args[4])
                        else:
                            raise TypeError, 'Invalid argument 4, expected one of: <types.FloatType> <types.IntType> '
                    else:
                        raise TypeError, 'Invalid argument 3, expected one of: <VBase3D.VBase3D> '
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <VBase3D.VBase3D> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <VBase3D.VBase3D> '
        elif isinstance(_args[0], Mat4.Mat4):
            import VBase3
            if isinstance(_args[1], VBase3.VBase3):
                import VBase3
                if isinstance(_args[2], VBase3.VBase3):
                    import VBase3
                    if isinstance(_args[3], VBase3.VBase3):
                        if isinstance(_args[4], types.FloatType) or isinstance(_args[4], types.IntType):
                            return __overloaded_decomposeMatrix_ptrConstLMatrix4f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f_float(_args[0], _args[1], _args[2], _args[3], _args[4])
                        elif isinstance(_args[4], types.IntType):
                            return __overloaded_decomposeMatrix_ptrConstLMatrix4f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f___enum__CoordinateSystem(_args[0], _args[1], _args[2], _args[3], _args[4])
                        else:
                            raise TypeError, 'Invalid argument 4, expected one of: <types.FloatType> <types.IntType> '
                    else:
                        raise TypeError, 'Invalid argument 3, expected one of: <VBase3.VBase3> '
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <VBase3.VBase3> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
        elif isinstance(_args[0], Mat3D.Mat3D):
            import VBase3D
            if isinstance(_args[1], VBase3D.VBase3D):
                import VBase3D
                if isinstance(_args[2], VBase3D.VBase3D):
                    if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                        if isinstance(_args[4], types.IntType):
                            return __overloaded_decomposeMatrix_ptrConstLMatrix3d_ptrLVecBase3d_ptrLVecBase3d_double___enum__CoordinateSystem(_args[0], _args[1], _args[2], _args[3], _args[4])
                        else:
                            raise TypeError, 'Invalid argument 4, expected one of: <types.IntType> '
                    else:
                        raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <VBase3D.VBase3D> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <VBase3D.VBase3D> '
        elif isinstance(_args[0], Mat3.Mat3):
            import VBase3
            if isinstance(_args[1], VBase3.VBase3):
                import VBase3
                if isinstance(_args[2], VBase3.VBase3):
                    if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                        if isinstance(_args[4], types.IntType):
                            return __overloaded_decomposeMatrix_ptrConstLMatrix3f_ptrLVecBase3f_ptrLVecBase3f_float___enum__CoordinateSystem(_args[0], _args[1], _args[2], _args[3], _args[4])
                        else:
                            raise TypeError, 'Invalid argument 4, expected one of: <types.IntType> '
                    else:
                        raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <VBase3.VBase3> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
        else:
            raise TypeError, 'Invalid argument 0, expected one of: <Mat4D.Mat4D> <Mat4.Mat4> <Mat3D.Mat3D> <Mat3.Mat3> '
    elif numArgs == 6:
        import Mat4D
        import Mat4
        if isinstance(_args[0], Mat4D.Mat4D):
            import VBase3D
            if isinstance(_args[1], VBase3D.VBase3D):
                import VBase3D
                if isinstance(_args[2], VBase3D.VBase3D):
                    import VBase3D
                    if isinstance(_args[3], VBase3D.VBase3D):
                        if isinstance(_args[4], types.FloatType) or isinstance(_args[4], types.IntType):
                            if isinstance(_args[5], types.IntType):
                                return __overloaded_decomposeMatrix_ptrConstLMatrix4d_ptrLVecBase3d_ptrLVecBase3d_ptrLVecBase3d_double___enum__CoordinateSystem(_args[0], _args[1], _args[2], _args[3], _args[4], _args[5])
                            else:
                                raise TypeError, 'Invalid argument 5, expected one of: <types.IntType> '
                        else:
                            raise TypeError, 'Invalid argument 4, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 3, expected one of: <VBase3D.VBase3D> '
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <VBase3D.VBase3D> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <VBase3D.VBase3D> '
        elif isinstance(_args[0], Mat4.Mat4):
            import VBase3
            if isinstance(_args[1], VBase3.VBase3):
                import VBase3
                if isinstance(_args[2], VBase3.VBase3):
                    import VBase3
                    if isinstance(_args[3], VBase3.VBase3):
                        if isinstance(_args[4], types.FloatType) or isinstance(_args[4], types.IntType):
                            if isinstance(_args[5], types.IntType):
                                return __overloaded_decomposeMatrix_ptrConstLMatrix4f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f_float___enum__CoordinateSystem(_args[0], _args[1], _args[2], _args[3], _args[4], _args[5])
                            else:
                                raise TypeError, 'Invalid argument 5, expected one of: <types.IntType> '
                        else:
                            raise TypeError, 'Invalid argument 4, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 3, expected one of: <VBase3.VBase3> '
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <VBase3.VBase3> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
        else:
            raise TypeError, 'Invalid argument 0, expected one of: <Mat4D.Mat4D> <Mat4.Mat4> '
    else:
        raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 3 4 5 6 '


def __mul__(*_args):
    numArgs = len(_args)
    if numArgs == 2:
        import Vec3D
        import Vec3
        import Vec2D
        import Vec2
        import VBase4D
        import VBase4
        import VBase3D
        import VBase3
        import Point3D
        import Point3
        import Point2D
        import Point2
        import Mat4D
        import Mat4
        import Mat3D
        import Mat3
        if isinstance(_args[0], Vec3D.Vec3D):
            import Mat4D
            if isinstance(_args[1], Mat4D.Mat4D):
                return __overloaded___mul___ptrConstLVector3d_ptrConstLMatrix4d(_args[0], _args[1])
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Mat4D.Mat4D> '
        elif isinstance(_args[0], Vec3.Vec3):
            import Mat4
            if isinstance(_args[1], Mat4.Mat4):
                return __overloaded___mul___ptrConstLVector3f_ptrConstLMatrix4f(_args[0], _args[1])
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Mat4.Mat4> '
        elif isinstance(_args[0], Vec2D.Vec2D):
            import Mat3D
            if isinstance(_args[1], Mat3D.Mat3D):
                return __overloaded___mul___ptrConstLVector2d_ptrConstLMatrix3d(_args[0], _args[1])
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Mat3D.Mat3D> '
        elif isinstance(_args[0], Vec2.Vec2):
            import Mat3
            if isinstance(_args[1], Mat3.Mat3):
                return __overloaded___mul___ptrConstLVector2f_ptrConstLMatrix3f(_args[0], _args[1])
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Mat3.Mat3> '
        elif isinstance(_args[0], VBase4D.VBase4D):
            import Mat4D
            if isinstance(_args[1], Mat4D.Mat4D):
                return __overloaded___mul___ptrConstLVecBase4d_ptrConstLMatrix4d(_args[0], _args[1])
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Mat4D.Mat4D> '
        elif isinstance(_args[0], VBase4.VBase4):
            import Mat4
            if isinstance(_args[1], Mat4.Mat4):
                return __overloaded___mul___ptrConstLVecBase4f_ptrConstLMatrix4f(_args[0], _args[1])
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Mat4.Mat4> '
        elif isinstance(_args[0], VBase3D.VBase3D):
            import Mat3D
            if isinstance(_args[1], Mat3D.Mat3D):
                return __overloaded___mul___ptrConstLVecBase3d_ptrConstLMatrix3d(_args[0], _args[1])
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Mat3D.Mat3D> '
        elif isinstance(_args[0], VBase3.VBase3):
            import Mat3
            if isinstance(_args[1], Mat3.Mat3):
                return __overloaded___mul___ptrConstLVecBase3f_ptrConstLMatrix3f(_args[0], _args[1])
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Mat3.Mat3> '
        elif isinstance(_args[0], Point3D.Point3D):
            import Mat4D
            if isinstance(_args[1], Mat4D.Mat4D):
                return __overloaded___mul___ptrConstLPoint3d_ptrConstLMatrix4d(_args[0], _args[1])
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Mat4D.Mat4D> '
        elif isinstance(_args[0], Point3.Point3):
            import Mat4
            if isinstance(_args[1], Mat4.Mat4):
                return __overloaded___mul___ptrConstLPoint3f_ptrConstLMatrix4f(_args[0], _args[1])
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Mat4.Mat4> '
        elif isinstance(_args[0], Point2D.Point2D):
            import Mat3D
            if isinstance(_args[1], Mat3D.Mat3D):
                return __overloaded___mul___ptrConstLPoint2d_ptrConstLMatrix3d(_args[0], _args[1])
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Mat3D.Mat3D> '
        elif isinstance(_args[0], Point2.Point2):
            import Mat3
            if isinstance(_args[1], Mat3.Mat3):
                return __overloaded___mul___ptrConstLPoint2f_ptrConstLMatrix3f(_args[0], _args[1])
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Mat3.Mat3> '
        elif isinstance(_args[0], Mat4D.Mat4D):
            import QuatD
            if isinstance(_args[1], QuatD.QuatD):
                return __overloaded___mul___ptrConstLMatrix4d_ptrConstLQuaterniond(_args[0], _args[1])
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <QuatD.QuatD> '
        elif isinstance(_args[0], Mat4.Mat4):
            import Quat
            if isinstance(_args[1], Quat.Quat):
                return __overloaded___mul___ptrConstLMatrix4f_ptrConstLQuaternionf(_args[0], _args[1])
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Quat.Quat> '
        elif isinstance(_args[0], Mat3D.Mat3D):
            import QuatD
            if isinstance(_args[1], QuatD.QuatD):
                return __overloaded___mul___ptrConstLMatrix3d_ptrConstLQuaterniond(_args[0], _args[1])
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <QuatD.QuatD> '
        elif isinstance(_args[0], Mat3.Mat3):
            import Quat
            if isinstance(_args[1], Quat.Quat):
                return __overloaded___mul___ptrConstLMatrix3f_ptrConstLQuaternionf(_args[0], _args[1])
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Quat.Quat> '
        else:
            raise TypeError, 'Invalid argument 0, expected one of: <Vec3D.Vec3D> <Vec3.Vec3> <Vec2D.Vec2D> <Vec2.Vec2> <VBase4D.VBase4D> <VBase4.VBase4> <VBase3D.VBase3D> <VBase3.VBase3> <Point3D.Point3D> <Point3.Point3> <Point2D.Point2D> <Point2.Point2> <Mat4D.Mat4D> <Mat4.Mat4> <Mat3D.Mat3D> <Mat3.Mat3> '
    else:
        raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 '


def getModelPath():
    returnValue = libpanda._inPelbo36dg()
    import DSearchPath
    returnObject = DSearchPath.DSearchPath(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    return returnObject


def getTexturePath():
    returnValue = libpanda._inPelboXgtZ()
    import DSearchPath
    returnObject = DSearchPath.DSearchPath(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    return returnObject


def getSoundPath():
    returnValue = libpanda._inPelbo08uu()
    import DSearchPath
    returnObject = DSearchPath.DSearchPath(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    return returnObject


def __overloaded_headsUp_ptrLMatrix3d_ptrConstLVector3d___enum__CoordinateSystem(mat, fwd, cs):
    returnValue = libpanda._inPSkjP9Yd4(mat.this, fwd.this, cs)
    return returnValue


def __overloaded_headsUp_ptrLMatrix3d_ptrConstLVector3d_ptrConstLVector3d___enum__CoordinateSystem(mat, fwd, up, cs):
    returnValue = libpanda._inPSkjPljSo(mat.this, fwd.this, up.this, cs)
    return returnValue


def __overloaded_headsUp_ptrLMatrix3d_ptrConstLVector3d_ptrConstLVector3d(mat, fwd, up):
    returnValue = libpanda._inPSkjPu5m2(mat.this, fwd.this, up.this)
    return returnValue


def __overloaded_headsUp_ptrLMatrix3d_ptrConstLVector3d(mat, fwd):
    returnValue = libpanda._inPSkjPSJmh(mat.this, fwd.this)
    return returnValue


def __overloaded_headsUp_ptrLMatrix3f_ptrConstLVector3f___enum__CoordinateSystem(mat, fwd, cs):
    returnValue = libpanda._inPSkjP4qVz(mat.this, fwd.this, cs)
    return returnValue


def __overloaded_headsUp_ptrLMatrix3f_ptrConstLVector3f_ptrConstLVector3f___enum__CoordinateSystem(mat, fwd, up, cs):
    returnValue = libpanda._inPSkjPstmb(mat.this, fwd.this, up.this, cs)
    return returnValue


def __overloaded_headsUp_ptrLMatrix3f_ptrConstLVector3f_ptrConstLVector3f(mat, fwd, up):
    returnValue = libpanda._inPSkjP4P9p(mat.this, fwd.this, up.this)
    return returnValue


def __overloaded_headsUp_ptrLMatrix3f_ptrConstLVector3f(mat, fwd):
    returnValue = libpanda._inPSkjPucec(mat.this, fwd.this)
    return returnValue


def __overloaded_headsUp_ptrLMatrix4d_ptrConstLVector3d___enum__CoordinateSystem(mat, fwd, cs):
    returnValue = libpanda._inPSkjP90V9(mat.this, fwd.this, cs)
    return returnValue


def __overloaded_headsUp_ptrLMatrix4d_ptrConstLVector3d_ptrConstLVector3d___enum__CoordinateSystem(mat, fwd, up, cs):
    returnValue = libpanda._inPSkjPl_Kt(mat.this, fwd.this, up.this, cs)
    return returnValue


def __overloaded_headsUp_ptrLMatrix4d_ptrConstLVector3d_ptrConstLVector3d(mat, fwd, up):
    returnValue = libpanda._inPSkjPudh7(mat.this, fwd.this, up.this)
    return returnValue


def __overloaded_headsUp_ptrLMatrix4d_ptrConstLVector3d(mat, fwd):
    returnValue = libpanda._inPSkjPStem(mat.this, fwd.this)
    return returnValue


def __overloaded_headsUp_ptrLMatrix4f_ptrConstLVector3f___enum__CoordinateSystem(mat, fwd, cs):
    returnValue = libpanda._inPSkjP4GM4(mat.this, fwd.this, cs)
    return returnValue


def __overloaded_headsUp_ptrLMatrix4f_ptrConstLVector3f_ptrConstLVector3f___enum__CoordinateSystem(mat, fwd, up, cs):
    returnValue = libpanda._inPSkjPrJfg(mat.this, fwd.this, up.this, cs)
    return returnValue


def __overloaded_headsUp_ptrLMatrix4f_ptrConstLVector3f_ptrConstLVector3f(mat, fwd, up):
    returnValue = libpanda._inPSkjP4j1u(mat.this, fwd.this, up.this)
    return returnValue


def __overloaded_headsUp_ptrLMatrix4f_ptrConstLVector3f(mat, fwd):
    returnValue = libpanda._inPSkjPpwWh(mat.this, fwd.this)
    return returnValue


def __overloaded_headsUp_ptrLQuaterniond_ptrConstLVector3d___enum__CoordinateSystem(quat, fwd, cs):
    returnValue = libpanda._inPSkjPQxQm(quat.this, fwd.this, cs)
    return returnValue


def __overloaded_headsUp_ptrLQuaterniond_ptrConstLVector3d_ptrConstLVector3d___enum__CoordinateSystem(quat, fwd, up, cs):
    returnValue = libpanda._inPSkjPc9Wi(quat.this, fwd.this, up.this, cs)
    return returnValue


def __overloaded_headsUp_ptrLQuaterniond_ptrConstLVector3d_ptrConstLVector3d(quat, fwd, up):
    returnValue = libpanda._inPSkjPhZq8(quat.this, fwd.this, up.this)
    return returnValue


def __overloaded_headsUp_ptrLQuaterniond_ptrConstLVector3d(quat, fwd):
    returnValue = libpanda._inPSkjP0Jjx(quat.this, fwd.this)
    return returnValue


def __overloaded_headsUp_ptrLQuaternionf_ptrConstLVector3f___enum__CoordinateSystem(quat, fwd, cs):
    returnValue = libpanda._inPSkjPRh3W(quat.this, fwd.this, cs)
    return returnValue


def __overloaded_headsUp_ptrLQuaternionf_ptrConstLVector3f_ptrConstLVector3f___enum__CoordinateSystem(quat, fwd, up, cs):
    returnValue = libpanda._inPSkjPjnkT(quat.this, fwd.this, up.this, cs)
    return returnValue


def __overloaded_headsUp_ptrLQuaternionf_ptrConstLVector3f_ptrConstLVector3f(quat, fwd, up):
    returnValue = libpanda._inPSkjPGl5t(quat.this, fwd.this, up.this)
    return returnValue


def __overloaded_headsUp_ptrLQuaternionf_ptrConstLVector3f(quat, fwd):
    returnValue = libpanda._inPSkjPyYKi(quat.this, fwd.this)
    return returnValue


def __overloaded_lookAt_ptrLMatrix3d_ptrConstLVector3d___enum__CoordinateSystem(mat, fwd, cs):
    returnValue = libpanda._inPSkjP3iJ6(mat.this, fwd.this, cs)
    return returnValue


def __overloaded_lookAt_ptrLMatrix3d_ptrConstLVector3d_ptrConstLVector3d___enum__CoordinateSystem(mat, fwd, up, cs):
    returnValue = libpanda._inPSkjPf3n7(mat.this, fwd.this, up.this, cs)
    return returnValue


def __overloaded_lookAt_ptrLMatrix3d_ptrConstLVector3d_ptrConstLVector3d(mat, fwd, up):
    returnValue = libpanda._inPSkjPbQHg(mat.this, fwd.this, up.this)
    return returnValue


def __overloaded_lookAt_ptrLMatrix3d_ptrConstLVector3d(mat, fwd):
    returnValue = libpanda._inPSkjPgTgt(mat.this, fwd.this)
    return returnValue


def __overloaded_lookAt_ptrLMatrix3f_ptrConstLVector3f___enum__CoordinateSystem(mat, fwd, cs):
    returnValue = libpanda._inPSkjPTR_D(mat.this, fwd.this, cs)
    return returnValue


def __overloaded_lookAt_ptrLMatrix3f_ptrConstLVector3f_ptrConstLVector3f___enum__CoordinateSystem(mat, fwd, up, cs):
    returnValue = libpanda._inPSkjPzsOP(mat.this, fwd.this, up.this, cs)
    return returnValue


def __overloaded_lookAt_ptrLMatrix3f_ptrConstLVector3f_ptrConstLVector3f(mat, fwd, up):
    returnValue = libpanda._inPSkjP34uz(mat.this, fwd.this, up.this)
    return returnValue


def __overloaded_lookAt_ptrLMatrix3f_ptrConstLVector3f(mat, fwd):
    returnValue = libpanda._inPSkjPMDW3(mat.this, fwd.this)
    return returnValue


def __overloaded_lookAt_ptrLMatrix4d_ptrConstLVector3d___enum__CoordinateSystem(mat, fwd, cs):
    returnValue = libpanda._inPSkjP_RT6(mat.this, fwd.this, cs)
    return returnValue


def __overloaded_lookAt_ptrLMatrix4d_ptrConstLVector3d_ptrConstLVector3d___enum__CoordinateSystem(mat, fwd, up, cs):
    returnValue = libpanda._inPSkjPXkx7(mat.this, fwd.this, up.this, cs)
    return returnValue


def __overloaded_lookAt_ptrLMatrix4d_ptrConstLVector3d_ptrConstLVector3d(mat, fwd, up):
    returnValue = libpanda._inPSkjPThRg(mat.this, fwd.this, up.this)
    return returnValue


def __overloaded_lookAt_ptrLMatrix4d_ptrConstLVector3d(mat, fwd):
    returnValue = libpanda._inPSkjPoCqt(mat.this, fwd.this)
    return returnValue


def __overloaded_lookAt_ptrLMatrix4f_ptrConstLVector3f___enum__CoordinateSystem(mat, fwd, cs):
    returnValue = libpanda._inPSkjPbAJE(mat.this, fwd.this, cs)
    return returnValue


def __overloaded_lookAt_ptrLMatrix4f_ptrConstLVector3f_ptrConstLVector3f___enum__CoordinateSystem(mat, fwd, up, cs):
    returnValue = libpanda._inPSkjPLcXP(mat.this, fwd.this, up.this, cs)
    return returnValue


def __overloaded_lookAt_ptrLMatrix4f_ptrConstLVector3f_ptrConstLVector3f(mat, fwd, up):
    returnValue = libpanda._inPSkjPPJ3z(mat.this, fwd.this, up.this)
    return returnValue


def __overloaded_lookAt_ptrLMatrix4f_ptrConstLVector3f(mat, fwd):
    returnValue = libpanda._inPSkjP0yf3(mat.this, fwd.this)
    return returnValue


def __overloaded_lookAt_ptrLQuaterniond_ptrConstLVector3d___enum__CoordinateSystem(quat, fwd, cs):
    returnValue = libpanda._inPSkjPcgkh(quat.this, fwd.this, cs)
    return returnValue


def __overloaded_lookAt_ptrLQuaterniond_ptrConstLVector3d_ptrConstLVector3d___enum__CoordinateSystem(quat, fwd, up, cs):
    returnValue = libpanda._inPSkjPr4at(quat.this, fwd.this, up.this, cs)
    return returnValue


def __overloaded_lookAt_ptrLQuaterniond_ptrConstLVector3d_ptrConstLVector3d(quat, fwd, up):
    returnValue = libpanda._inPSkjP6OSa(quat.this, fwd.this, up.this)
    return returnValue


def __overloaded_lookAt_ptrLQuaterniond_ptrConstLVector3d(quat, fwd):
    returnValue = libpanda._inPSkjPmF_T(quat.this, fwd.this)
    return returnValue


def __overloaded_lookAt_ptrLQuaternionf_ptrConstLVector3f___enum__CoordinateSystem(quat, fwd, cs):
    returnValue = libpanda._inPSkjPMvHl(quat.this, fwd.this, cs)
    return returnValue


def __overloaded_lookAt_ptrLQuaternionf_ptrConstLVector3f_ptrConstLVector3f___enum__CoordinateSystem(quat, fwd, up, cs):
    returnValue = libpanda._inPSkjP8f8w(quat.this, fwd.this, up.this, cs)
    return returnValue


def __overloaded_lookAt_ptrLQuaternionf_ptrConstLVector3f_ptrConstLVector3f(quat, fwd, up):
    returnValue = libpanda._inPSkjPxh1d(quat.this, fwd.this, up.this)
    return returnValue


def __overloaded_lookAt_ptrLQuaternionf_ptrConstLVector3f(quat, fwd):
    returnValue = libpanda._inPSkjPGIgX(quat.this, fwd.this)
    return returnValue


def __overloaded_rotateTo_ptrLMatrix3d_ptrConstLVector3d_ptrConstLVector3d(mat, a, b):
    returnValue = libpanda._inPSkjPzzF6(mat.this, a.this, b.this)
    return returnValue


def __overloaded_rotateTo_ptrLMatrix3f_ptrConstLVector3f_ptrConstLVector3f(mat, a, b):
    returnValue = libpanda._inPSkjP5uMk(mat.this, a.this, b.this)
    return returnValue


def __overloaded_rotateTo_ptrLMatrix4d_ptrConstLVector3d_ptrConstLVector3d(mat, a, b):
    returnValue = libpanda._inPSkjPxzTW(mat.this, a.this, b.this)
    return returnValue


def __overloaded_rotateTo_ptrLMatrix4f_ptrConstLVector3f_ptrConstLVector3f(mat, a, b):
    returnValue = libpanda._inPSkjP_uaA(mat.this, a.this, b.this)
    return returnValue


def __overloaded_deg2Rad_double(f):
    returnValue = libpanda._inPUZN3ZTo4(f)
    return returnValue


def __overloaded_deg2Rad_float(f):
    returnValue = libpanda._inPUZN3RKCI(f)
    return returnValue


def __overloaded_rad2Deg_double(f):
    returnValue = libpanda._inPUZN3jpRs(f)
    return returnValue


def __overloaded_rad2Deg_float(f):
    returnValue = libpanda._inPUZN3Pbq7(f)
    return returnValue


def __overloaded___mul___ptrConstLMatrix3d_ptrConstLQuaterniond(m, q):
    returnValue = libpanda._inPUZN3DzjX(m.this, q.this)
    import Mat3D
    returnObject = Mat3D.Mat3D(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def __overloaded___mul___ptrConstLMatrix3f_ptrConstLQuaternionf(m, q):
    returnValue = libpanda._inPUZN3kolH(m.this, q.this)
    import Mat3
    returnObject = Mat3.Mat3(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def __overloaded___mul___ptrConstLMatrix4d_ptrConstLQuaterniond(m, q):
    returnValue = libpanda._inPUZN3Rsje(m.this, q.this)
    import Mat4D
    returnObject = Mat4D.Mat4D(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def __overloaded___mul___ptrConstLMatrix4f_ptrConstLQuaternionf(m, q):
    returnValue = libpanda._inPUZN3qplO(m.this, q.this)
    import Mat4
    returnObject = Mat4.Mat4(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def __overloaded___mul___ptrConstLPoint2d_ptrConstLMatrix3d(v, m):
    returnValue = libpanda._inPUZN3yfKI(v.this, m.this)
    import Point2D
    returnObject = Point2D.Point2D(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def __overloaded___mul___ptrConstLPoint2f_ptrConstLMatrix3f(v, m):
    returnValue = libpanda._inPUZN3SCRW(v.this, m.this)
    import Point2
    returnObject = Point2.Point2(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def __overloaded___mul___ptrConstLPoint3d_ptrConstLMatrix4d(v, m):
    returnValue = libpanda._inPUZN3mWZA(v.this, m.this)
    import Point3D
    returnObject = Point3D.Point3D(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def __overloaded___mul___ptrConstLPoint3f_ptrConstLMatrix4f(v, m):
    returnValue = libpanda._inPUZN3eNeO(v.this, m.this)
    import Point3
    returnObject = Point3.Point3(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def __overloaded___mul___ptrConstLVecBase3d_ptrConstLMatrix3d(v, m):
    returnValue = libpanda._inPUZN36f4W(v.this, m.this)
    import VBase3D
    returnObject = VBase3D.VBase3D(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def __overloaded___mul___ptrConstLVecBase3f_ptrConstLMatrix3f(v, m):
    returnValue = libpanda._inPUZN3YSml(v.this, m.this)
    import VBase3
    returnObject = VBase3.VBase3(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def __overloaded___mul___ptrConstLVecBase4d_ptrConstLMatrix4d(v, m):
    returnValue = libpanda._inPUZN3EpH4(v.this, m.this)
    import VBase4D
    returnObject = VBase4D.VBase4D(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def __overloaded___mul___ptrConstLVecBase4f_ptrConstLMatrix4f(v, m):
    returnValue = libpanda._inPUZN3lt1G(v.this, m.this)
    import VBase4
    returnObject = VBase4.VBase4(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def __overloaded___mul___ptrConstLVector2d_ptrConstLMatrix3d(v, m):
    returnValue = libpanda._inPUZN3QlWf(v.this, m.this)
    import Vec2D
    returnObject = Vec2D.Vec2D(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def __overloaded___mul___ptrConstLVector2f_ptrConstLMatrix3f(v, m):
    returnValue = libpanda._inPUZN3eZ0h(v.this, m.this)
    import Vec2
    returnObject = Vec2.Vec2(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def __overloaded___mul___ptrConstLVector3d_ptrConstLMatrix4d(v, m):
    returnValue = libpanda._inPUZN3xbZm(v.this, m.this)
    import Vec3D
    returnObject = Vec3D.Vec3D(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def __overloaded___mul___ptrConstLVector3f_ptrConstLMatrix4f(v, m):
    returnValue = libpanda._inPUZN36_2o(v.this, m.this)
    import Vec3
    returnObject = Vec3.Vec3(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def __overloaded_composeMatrix_ptrLMatrix3d_ptrConstLVecBase3d_ptrConstLVecBase3d___enum__CoordinateSystem(mat, scale, hpr, cs):
    returnValue = libpanda._inPUZN3yVzC(mat.this, scale.this, hpr.this, cs)
    return returnValue


def __overloaded_composeMatrix_ptrLMatrix3d_ptrConstLVecBase3d_ptrConstLVecBase3d(mat, scale, hpr):
    returnValue = libpanda._inPUZN3gQb3(mat.this, scale.this, hpr.this)
    return returnValue


def __overloaded_composeMatrix_ptrLMatrix3f_ptrConstLVecBase3f_ptrConstLVecBase3f___enum__CoordinateSystem(mat, scale, hpr, cs):
    returnValue = libpanda._inPUZN37aBn(mat.this, scale.this, hpr.this, cs)
    return returnValue


def __overloaded_composeMatrix_ptrLMatrix3f_ptrConstLVecBase3f_ptrConstLVecBase3f(mat, scale, hpr):
    returnValue = libpanda._inPUZN36xpb(mat.this, scale.this, hpr.this)
    return returnValue


def __overloaded_composeMatrix_ptrLMatrix4d_ptrConstLVecBase3d_ptrConstLVecBase3d_ptrConstLVecBase3d___enum__CoordinateSystem(mat, scale, hpr, translate, cs):
    returnValue = libpanda._inPUZN38KjT(mat.this, scale.this, hpr.this, translate.this, cs)
    return returnValue


def __overloaded_composeMatrix_ptrLMatrix4d_ptrConstLVecBase3d_ptrConstLVecBase3d_ptrConstLVecBase3d(mat, scale, hpr, translate):
    returnValue = libpanda._inPUZN3XKS4(mat.this, scale.this, hpr.this, translate.this)
    return returnValue


def __overloaded_composeMatrix_ptrLMatrix4f_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f___enum__CoordinateSystem(mat, scale, hpr, translate, cs):
    returnValue = libpanda._inPUZN3R_y_(mat.this, scale.this, hpr.this, translate.this, cs)
    return returnValue


def __overloaded_composeMatrix_ptrLMatrix4f_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f(mat, scale, hpr, translate):
    returnValue = libpanda._inPUZN367gj(mat.this, scale.this, hpr.this, translate.this)
    return returnValue


def __overloaded_decomposeMatrix_ptrConstLMatrix3d_ptrLVecBase3d_ptrLVecBase3d___enum__CoordinateSystem(mat, scale, hpr, cs):
    returnValue = libpanda._inPUZN3rGAD(mat.this, scale.this, hpr.this, cs)
    return returnValue


def __overloaded_decomposeMatrix_ptrConstLMatrix3d_ptrLVecBase3d_ptrLVecBase3d(mat, scale, hpr):
    returnValue = libpanda._inPUZN3SxX2(mat.this, scale.this, hpr.this)
    return returnValue


def __overloaded_decomposeMatrix_ptrConstLMatrix3d_ptrLVecBase3d_ptrLVecBase3d_double___enum__CoordinateSystem(mat, scale, hpr, roll, cs):
    returnValue = libpanda._inPUZN3QW8r(mat.this, scale.this, hpr.this, roll, cs)
    return returnValue


def __overloaded_decomposeMatrix_ptrConstLMatrix3d_ptrLVecBase3d_ptrLVecBase3d_double(mat, scale, hpr, roll):
    returnValue = libpanda._inPUZN3RXrQ(mat.this, scale.this, hpr.this, roll)
    return returnValue


def __overloaded_decomposeMatrix_ptrConstLMatrix3f_ptrLVecBase3f_ptrLVecBase3f___enum__CoordinateSystem(mat, scale, hpr, cs):
    returnValue = libpanda._inPUZN3NI_s(mat.this, scale.this, hpr.this, cs)
    return returnValue


def __overloaded_decomposeMatrix_ptrConstLMatrix3f_ptrLVecBase3f_ptrLVecBase3f(mat, scale, hpr):
    returnValue = libpanda._inPUZN3wJVg(mat.this, scale.this, hpr.this)
    return returnValue


def __overloaded_decomposeMatrix_ptrConstLMatrix3f_ptrLVecBase3f_ptrLVecBase3f_float___enum__CoordinateSystem(mat, scale, hpr, roll, cs):
    returnValue = libpanda._inPUZN3s0v6(mat.this, scale.this, hpr.this, roll, cs)
    return returnValue


def __overloaded_decomposeMatrix_ptrConstLMatrix3f_ptrLVecBase3f_ptrLVecBase3f_float(mat, scale, hpr, roll):
    returnValue = libpanda._inPUZN3l67B(mat.this, scale.this, hpr.this, roll)
    return returnValue


def __overloaded_decomposeMatrix_ptrConstLMatrix4d_ptrLVecBase3d_ptrLVecBase3d_ptrLVecBase3d___enum__CoordinateSystem(mat, scale, hpr, translate, cs):
    returnValue = libpanda._inPUZN36y0_(mat.this, scale.this, hpr.this, translate.this, cs)
    return returnValue


def __overloaded_decomposeMatrix_ptrConstLMatrix4d_ptrLVecBase3d_ptrLVecBase3d_ptrLVecBase3d(mat, scale, hpr, translate):
    returnValue = libpanda._inPUZN32gus(mat.this, scale.this, hpr.this, translate.this)
    return returnValue


def __overloaded_decomposeMatrix_ptrConstLMatrix4d_ptrLVecBase3d_ptrLVecBase3d_ptrLVecBase3d_double___enum__CoordinateSystem(mat, scale, hpr, translate, roll, cs):
    returnValue = libpanda._inPUZN3zIDK(mat.this, scale.this, hpr.this, translate.this, roll, cs)
    return returnValue


def __overloaded_decomposeMatrix_ptrConstLMatrix4d_ptrLVecBase3d_ptrLVecBase3d_ptrLVecBase3d_double(mat, scale, hpr, translate, roll):
    returnValue = libpanda._inPUZN3SKSD(mat.this, scale.this, hpr.this, translate.this, roll)
    return returnValue


def __overloaded_decomposeMatrix_ptrConstLMatrix4f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f___enum__CoordinateSystem(mat, scale, hpr, translate, cs):
    returnValue = libpanda._inPUZN3TLRi(mat.this, scale.this, hpr.this, translate.this, cs)
    return returnValue


def __overloaded_decomposeMatrix_ptrConstLMatrix4f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f(mat, scale, hpr, translate):
    returnValue = libpanda._inPUZN3cmIP(mat.this, scale.this, hpr.this, translate.this)
    return returnValue


def __overloaded_decomposeMatrix_ptrConstLMatrix4f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f_float___enum__CoordinateSystem(mat, scale, hpr, translate, roll, cs):
    returnValue = libpanda._inPUZN3y3rF(mat.this, scale.this, hpr.this, translate.this, roll, cs)
    return returnValue


def __overloaded_decomposeMatrix_ptrConstLMatrix4f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f_float(mat, scale, hpr, translate, roll):
    returnValue = libpanda._inPUZN3d3hX(mat.this, scale.this, hpr.this, translate.this, roll)
    return returnValue


def __overloaded_autoBind_ptrPandaNode_ptrAnimControlCollection_int(rootNode, controls, hierarchyMatchFlags):
    returnValue = libpanda._inPn9gMlnU_(rootNode.this, controls.this, hierarchyMatchFlags)
    return returnValue


def __overloaded_autoBind_ptrPandaNode_ptrAnimControlCollection(rootNode, controls):
    returnValue = libpanda._inPn9gMI30i(rootNode.this, controls.this)
    return returnValue

HCCUT = 1
HCFREE = 2
HCG1 = 3
HCSMOOTH = 4
PCTHPR = 2
PCTNONE = 0
PCTT = 3
PCTXYZ = 1
