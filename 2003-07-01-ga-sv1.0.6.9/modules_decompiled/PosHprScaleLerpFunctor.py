# File: P (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import LerpFunctor

class PosHprScaleLerpFunctor(LerpFunctor.LerpFunctor, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _PosHprScaleLerpFunctor__overloaded_constructor_ptrNodePath_ptrLPoint3f_ptrLPoint3f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f(self, np, pstart, pend, hstart, hend, sstart, send):
        self.this = libpanda._inPkJyoP4RJ(np.this, pstart.this, pend.this, hstart.this, hend.this, sstart.this, send.this)
        self.userManagesMemory = 1

    
    def _PosHprScaleLerpFunctor__overloaded_constructor_ptrNodePath_ptrLPoint3f_ptrLPoint3f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f_ptrNodePath(self, np, pstart, pend, hstart, hend, sstart, send, wrt):
        self.this = libpanda._inPkJyosRMm(np.this, pstart.this, pend.this, hstart.this, hend.this, sstart.this, send.this, wrt.this)
        self.userManagesMemory = 1

    
    def _PosHprScaleLerpFunctor__overloaded_constructor_ptrNodePath_float_float_float_float_float_float_float_float_float_float_float_float_float_float_float_float_float_float(self, np, psx, psy, psz, pex, pey, pez, hsx, hsy, hsz, hex, hey, hez, ssx, ssy, ssz, sex, sey, sez):
        self.this = libpanda._inPkJyohyws(np.this, psx, psy, psz, pex, pey, pez, hsx, hsy, hsz, hex, hey, hez, ssx, ssy, ssz, sex, sey, sez)
        self.userManagesMemory = 1

    
    def _PosHprScaleLerpFunctor__overloaded_constructor_ptrNodePath_float_float_float_float_float_float_float_float_float_float_float_float_float_float_float_float_float_float_ptrNodePath(self, np, psx, psy, psz, pex, pey, pez, hsx, hsy, hsz, hex, hey, hez, ssx, ssy, ssz, sex, sey, sez, wrt):
        self.this = libpanda._inPkJyoOFig(np.this, psx, psy, psz, pex, pey, pez, hsx, hsy, hsz, hex, hey, hez, ssx, ssy, ssz, sex, sey, sez, wrt.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClassType():
        returnValue = libpanda._inPkJyoKG7x()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def takeShortest(self):
        returnValue = libpanda._inPkJyo8q_U(self.this)
        return returnValue

    
    def takeLongest(self):
        returnValue = libpanda._inPkJyoEgah(self.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 7:
            import NodePath
            if isinstance(_args[0], NodePath.NodePath):
                import Point3
                if isinstance(_args[1], Point3.Point3):
                    import Point3
                    if isinstance(_args[2], Point3.Point3):
                        import VBase3
                        if isinstance(_args[3], VBase3.VBase3):
                            import VBase3
                            if isinstance(_args[4], VBase3.VBase3):
                                import VBase3
                                if isinstance(_args[5], VBase3.VBase3):
                                    import VBase3
                                    if isinstance(_args[6], VBase3.VBase3):
                                        return self._PosHprScaleLerpFunctor__overloaded_constructor_ptrNodePath_ptrLPoint3f_ptrLPoint3f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f(_args[0], _args[1], _args[2], _args[3], _args[4], _args[5], _args[6])
                                    else:
                                        raise TypeError, 'Invalid argument 6, expected one of: <VBase3.VBase3> '
                                else:
                                    raise TypeError, 'Invalid argument 5, expected one of: <VBase3.VBase3> '
                            else:
                                raise TypeError, 'Invalid argument 4, expected one of: <VBase3.VBase3> '
                        else:
                            raise TypeError, 'Invalid argument 3, expected one of: <VBase3.VBase3> '
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <Point3.Point3> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <Point3.Point3> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath.NodePath> '
        elif numArgs == 8:
            import NodePath
            if isinstance(_args[0], NodePath.NodePath):
                import Point3
                if isinstance(_args[1], Point3.Point3):
                    import Point3
                    if isinstance(_args[2], Point3.Point3):
                        import VBase3
                        if isinstance(_args[3], VBase3.VBase3):
                            import VBase3
                            if isinstance(_args[4], VBase3.VBase3):
                                import VBase3
                                if isinstance(_args[5], VBase3.VBase3):
                                    import VBase3
                                    if isinstance(_args[6], VBase3.VBase3):
                                        import NodePath
                                        if isinstance(_args[7], NodePath.NodePath):
                                            return self._PosHprScaleLerpFunctor__overloaded_constructor_ptrNodePath_ptrLPoint3f_ptrLPoint3f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f_ptrNodePath(_args[0], _args[1], _args[2], _args[3], _args[4], _args[5], _args[6], _args[7])
                                        else:
                                            raise TypeError, 'Invalid argument 7, expected one of: <NodePath.NodePath> '
                                    else:
                                        raise TypeError, 'Invalid argument 6, expected one of: <VBase3.VBase3> '
                                else:
                                    raise TypeError, 'Invalid argument 5, expected one of: <VBase3.VBase3> '
                            else:
                                raise TypeError, 'Invalid argument 4, expected one of: <VBase3.VBase3> '
                        else:
                            raise TypeError, 'Invalid argument 3, expected one of: <VBase3.VBase3> '
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <Point3.Point3> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <Point3.Point3> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath.NodePath> '
        elif numArgs == 19:
            import NodePath
            if isinstance(_args[0], NodePath.NodePath):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                            if isinstance(_args[4], types.FloatType) or isinstance(_args[4], types.IntType):
                                if isinstance(_args[5], types.FloatType) or isinstance(_args[5], types.IntType):
                                    if isinstance(_args[6], types.FloatType) or isinstance(_args[6], types.IntType):
                                        if isinstance(_args[7], types.FloatType) or isinstance(_args[7], types.IntType):
                                            if isinstance(_args[8], types.FloatType) or isinstance(_args[8], types.IntType):
                                                if isinstance(_args[9], types.FloatType) or isinstance(_args[9], types.IntType):
                                                    if isinstance(_args[10], types.FloatType) or isinstance(_args[10], types.IntType):
                                                        if isinstance(_args[11], types.FloatType) or isinstance(_args[11], types.IntType):
                                                            if isinstance(_args[12], types.FloatType) or isinstance(_args[12], types.IntType):
                                                                if isinstance(_args[13], types.FloatType) or isinstance(_args[13], types.IntType):
                                                                    if isinstance(_args[14], types.FloatType) or isinstance(_args[14], types.IntType):
                                                                        if isinstance(_args[15], types.FloatType) or isinstance(_args[15], types.IntType):
                                                                            if isinstance(_args[16], types.FloatType) or isinstance(_args[16], types.IntType):
                                                                                if isinstance(_args[17], types.FloatType) or isinstance(_args[17], types.IntType):
                                                                                    if isinstance(_args[18], types.FloatType) or isinstance(_args[18], types.IntType):
                                                                                        return self._PosHprScaleLerpFunctor__overloaded_constructor_ptrNodePath_float_float_float_float_float_float_float_float_float_float_float_float_float_float_float_float_float_float(_args[0], _args[1], _args[2], _args[3], _args[4], _args[5], _args[6], _args[7], _args[8], _args[9], _args[10], _args[11], _args[12], _args[13], _args[14], _args[15], _args[16], _args[17], _args[18])
                                                                                    else:
                                                                                        raise TypeError, 'Invalid argument 18, expected one of: <types.FloatType> '
                                                                                else:
                                                                                    raise TypeError, 'Invalid argument 17, expected one of: <types.FloatType> '
                                                                            else:
                                                                                raise TypeError, 'Invalid argument 16, expected one of: <types.FloatType> '
                                                                        else:
                                                                            raise TypeError, 'Invalid argument 15, expected one of: <types.FloatType> '
                                                                    else:
                                                                        raise TypeError, 'Invalid argument 14, expected one of: <types.FloatType> '
                                                                else:
                                                                    raise TypeError, 'Invalid argument 13, expected one of: <types.FloatType> '
                                                            else:
                                                                raise TypeError, 'Invalid argument 12, expected one of: <types.FloatType> '
                                                        else:
                                                            raise TypeError, 'Invalid argument 11, expected one of: <types.FloatType> '
                                                    else:
                                                        raise TypeError, 'Invalid argument 10, expected one of: <types.FloatType> '
                                                else:
                                                    raise TypeError, 'Invalid argument 9, expected one of: <types.FloatType> '
                                            else:
                                                raise TypeError, 'Invalid argument 8, expected one of: <types.FloatType> '
                                        else:
                                            raise TypeError, 'Invalid argument 7, expected one of: <types.FloatType> '
                                    else:
                                        raise TypeError, 'Invalid argument 6, expected one of: <types.FloatType> '
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
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath.NodePath> '
        elif numArgs == 20:
            import NodePath
            if isinstance(_args[0], NodePath.NodePath):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                            if isinstance(_args[4], types.FloatType) or isinstance(_args[4], types.IntType):
                                if isinstance(_args[5], types.FloatType) or isinstance(_args[5], types.IntType):
                                    if isinstance(_args[6], types.FloatType) or isinstance(_args[6], types.IntType):
                                        if isinstance(_args[7], types.FloatType) or isinstance(_args[7], types.IntType):
                                            if isinstance(_args[8], types.FloatType) or isinstance(_args[8], types.IntType):
                                                if isinstance(_args[9], types.FloatType) or isinstance(_args[9], types.IntType):
                                                    if isinstance(_args[10], types.FloatType) or isinstance(_args[10], types.IntType):
                                                        if isinstance(_args[11], types.FloatType) or isinstance(_args[11], types.IntType):
                                                            if isinstance(_args[12], types.FloatType) or isinstance(_args[12], types.IntType):
                                                                if isinstance(_args[13], types.FloatType) or isinstance(_args[13], types.IntType):
                                                                    if isinstance(_args[14], types.FloatType) or isinstance(_args[14], types.IntType):
                                                                        if isinstance(_args[15], types.FloatType) or isinstance(_args[15], types.IntType):
                                                                            if isinstance(_args[16], types.FloatType) or isinstance(_args[16], types.IntType):
                                                                                if isinstance(_args[17], types.FloatType) or isinstance(_args[17], types.IntType):
                                                                                    if isinstance(_args[18], types.FloatType) or isinstance(_args[18], types.IntType):
                                                                                        import NodePath
                                                                                        if isinstance(_args[19], NodePath.NodePath):
                                                                                            return self._PosHprScaleLerpFunctor__overloaded_constructor_ptrNodePath_float_float_float_float_float_float_float_float_float_float_float_float_float_float_float_float_float_float_ptrNodePath(_args[0], _args[1], _args[2], _args[3], _args[4], _args[5], _args[6], _args[7], _args[8], _args[9], _args[10], _args[11], _args[12], _args[13], _args[14], _args[15], _args[16], _args[17], _args[18], _args[19])
                                                                                        else:
                                                                                            raise TypeError, 'Invalid argument 19, expected one of: <NodePath.NodePath> '
                                                                                    else:
                                                                                        raise TypeError, 'Invalid argument 18, expected one of: <types.FloatType> '
                                                                                else:
                                                                                    raise TypeError, 'Invalid argument 17, expected one of: <types.FloatType> '
                                                                            else:
                                                                                raise TypeError, 'Invalid argument 16, expected one of: <types.FloatType> '
                                                                        else:
                                                                            raise TypeError, 'Invalid argument 15, expected one of: <types.FloatType> '
                                                                    else:
                                                                        raise TypeError, 'Invalid argument 14, expected one of: <types.FloatType> '
                                                                else:
                                                                    raise TypeError, 'Invalid argument 13, expected one of: <types.FloatType> '
                                                            else:
                                                                raise TypeError, 'Invalid argument 12, expected one of: <types.FloatType> '
                                                        else:
                                                            raise TypeError, 'Invalid argument 11, expected one of: <types.FloatType> '
                                                    else:
                                                        raise TypeError, 'Invalid argument 10, expected one of: <types.FloatType> '
                                                else:
                                                    raise TypeError, 'Invalid argument 9, expected one of: <types.FloatType> '
                                            else:
                                                raise TypeError, 'Invalid argument 8, expected one of: <types.FloatType> '
                                        else:
                                            raise TypeError, 'Invalid argument 7, expected one of: <types.FloatType> '
                                    else:
                                        raise TypeError, 'Invalid argument 6, expected one of: <types.FloatType> '
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
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath.NodePath> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 7 8 19 20 '


