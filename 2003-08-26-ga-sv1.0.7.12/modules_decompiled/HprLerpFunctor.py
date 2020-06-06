# File: H (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import SimpleLerpFunctorLVecBase3f

class HprLerpFunctor(SimpleLerpFunctorLVecBase3f.SimpleLerpFunctorLVecBase3f, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def _HprLerpFunctor__overloaded_constructor_ptrNodePath_ptrLVecBase3f_ptrLVecBase3f(self, np, start, end):
        self.this = libpanda._inPkJyopTQ4(np.this, start.this, end.this)
        self.userManagesMemory = 1

    
    def _HprLerpFunctor__overloaded_constructor_ptrNodePath_ptrLVecBase3f_ptrLVecBase3f_ptrNodePath(self, np, start, end, wrt):
        self.this = libpanda._inPkJyoyiY5(np.this, start.this, end.this, wrt.this)
        self.userManagesMemory = 1

    
    def _HprLerpFunctor__overloaded_constructor_ptrNodePath_float_float_float_float_float_float(self, np, sx, sy, sz, ex, ey, ez):
        self.this = libpanda._inPkJyor6ke(np.this, sx, sy, sz, ex, ey, ez)
        self.userManagesMemory = 1

    
    def _HprLerpFunctor__overloaded_constructor_ptrNodePath_float_float_float_float_float_float_ptrNodePath(self, np, sx, sy, sz, ex, ey, ez, wrt):
        self.this = libpanda._inPkJyobDib(np.this, sx, sy, sz, ex, ey, ez, wrt.this)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClassType():
        returnValue = libpanda._inPkJyoiuir()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def takeShortest(self):
        returnValue = libpanda._inPkJyoO8qB(self.this)
        return returnValue

    
    def takeLongest(self):
        returnValue = libpanda._inPkJyo8PLx(self.this)
        return returnValue

    
    def constructor(self, *_args):
        numArgs = len(_args)
        if numArgs == 3:
            import NodePath
            if isinstance(_args[0], NodePath.NodePath):
                import VBase3
                if isinstance(_args[1], VBase3.VBase3):
                    import VBase3
                    if isinstance(_args[2], VBase3.VBase3):
                        return self._HprLerpFunctor__overloaded_constructor_ptrNodePath_ptrLVecBase3f_ptrLVecBase3f(_args[0], _args[1], _args[2])
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <VBase3.VBase3> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath.NodePath> '
        elif numArgs == 4:
            import NodePath
            if isinstance(_args[0], NodePath.NodePath):
                import VBase3
                if isinstance(_args[1], VBase3.VBase3):
                    import VBase3
                    if isinstance(_args[2], VBase3.VBase3):
                        import NodePath
                        if isinstance(_args[3], NodePath.NodePath):
                            return self._HprLerpFunctor__overloaded_constructor_ptrNodePath_ptrLVecBase3f_ptrLVecBase3f_ptrNodePath(_args[0], _args[1], _args[2], _args[3])
                        else:
                            raise TypeError, 'Invalid argument 3, expected one of: <NodePath.NodePath> '
                    else:
                        raise TypeError, 'Invalid argument 2, expected one of: <VBase3.VBase3> '
                else:
                    raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <NodePath.NodePath> '
        elif numArgs == 7:
            import NodePath
            if isinstance(_args[0], NodePath.NodePath):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                            if isinstance(_args[4], types.FloatType) or isinstance(_args[4], types.IntType):
                                if isinstance(_args[5], types.FloatType) or isinstance(_args[5], types.IntType):
                                    if isinstance(_args[6], types.FloatType) or isinstance(_args[6], types.IntType):
                                        return self._HprLerpFunctor__overloaded_constructor_ptrNodePath_float_float_float_float_float_float(_args[0], _args[1], _args[2], _args[3], _args[4], _args[5], _args[6])
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
        elif numArgs == 8:
            import NodePath
            if isinstance(_args[0], NodePath.NodePath):
                if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                    if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                        if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                            if isinstance(_args[4], types.FloatType) or isinstance(_args[4], types.IntType):
                                if isinstance(_args[5], types.FloatType) or isinstance(_args[5], types.IntType):
                                    if isinstance(_args[6], types.FloatType) or isinstance(_args[6], types.IntType):
                                        import NodePath
                                        if isinstance(_args[7], NodePath.NodePath):
                                            return self._HprLerpFunctor__overloaded_constructor_ptrNodePath_float_float_float_float_float_float_ptrNodePath(_args[0], _args[1], _args[2], _args[3], _args[4], _args[5], _args[6], _args[7])
                                        else:
                                            raise TypeError, 'Invalid argument 7, expected one of: <NodePath.NodePath> '
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
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 3 4 7 8 '


